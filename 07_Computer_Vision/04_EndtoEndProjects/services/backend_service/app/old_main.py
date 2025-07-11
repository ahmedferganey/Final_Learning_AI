# Import asyncio for asynchronous operations
import asyncio

# Import pika for connecting to RabbitMQ
import pika

# Import FastAPI for creating the web application
from fastapi import FastAPI, WebSocket

# Import middleware to handle Cross-Origin Resource Sharing (CORS)
from fastapi.middleware.cors import CORSMiddleware

# Import all variables (like RabbitMQ config) from config.py
from config import *

# Create an instance of the FastAPI application
app = FastAPI()

# Initialize a set to keep track of connected WebSocket clients
clients = set()

# Add middleware to allow connections from frontend apps (like React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; you can replace "*" with specific domains for security
    allow_credentials=True,  # Allow credentials (cookies, HTTP auth, etc.)
    allow_methods=["*"],     # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],     # Allow all headers
)

# Define the WebSocket endpoint that clients will connect to for real-time frame updates
@app.websocket("/ws/frames")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()      # Accept the WebSocket connection
    clients.add(websocket)        # Add client to the active set
    try:
        while True:
            await asyncio.sleep(1000)  # Keep the connection alive (this is just a placeholder)
    except Exception:
        pass                      # Ignore disconnection or any exception
    finally:
        clients.remove(websocket) # Remove the client if disconnected

# Asynchronously broadcast a frame to all connected WebSocket clients
async def broadcast_frame(frame_data):
    for ws in list(clients):         # Iterate over all active WebSocket connections
        try:
            await ws.send_bytes(frame_data)  # Send frame data as bytes
        except Exception:
            clients.remove(ws)       # If sending fails (e.g. client disconnected), remove from set

# Start a RabbitMQ consumer in a separate thread
def start_rabbitmq(loop):
    # Define callback for when a message is received from RabbitMQ
    def callback(ch, method, properties, body):
        # Run the broadcast coroutine in the main asyncio loop (thread-safe)
        asyncio.run_coroutine_threadsafe(broadcast_frame(body), loop)
        # Acknowledge the message so it won't be re-queued
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # Setup RabbitMQ connection with credentials
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    params = pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, credentials=credentials)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    # Declare the exchange (must match producer)
    channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type='fanout', durable=True)

    # Declare the queue that this service will consume from
    channel.queue_declare(queue=RABBITMQ_STREAMING_FRAME_QUEUE, durable=True)

    # Bind the queue to the exchange
    channel.queue_bind(exchange=RABBITMQ_EXCHANGE, queue=RABBITMQ_STREAMING_FRAME_QUEUE)

    # Start consuming from the queue and handle messages with callback
    channel.basic_consume(queue=RABBITMQ_STREAMING_FRAME_QUEUE, on_message_callback=callback)
    print("🟢 Streaming is consuming and broadcasting frames...")
    channel.start_consuming()  # Blocking call, runs in executor thread

# Start the consumer in a background thread when the FastAPI app starts
@app.on_event("startup")
def start_consumer():
    loop = asyncio.get_event_loop()  # Get the current event loop
    # Run the RabbitMQ consumer in a thread so it doesn't block the main event loop
    loop.run_in_executor(None, start_rabbitmq, loop)

