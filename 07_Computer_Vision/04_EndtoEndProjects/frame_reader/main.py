# Importing OpenCV for video capture and frame processing
import cv2
# Importing pika library for interacting with RabbitMQ message broker
import pika
# Importing time module to control the frame publishing rate
import time
# Importing configuration variables (RabbitMQ host, queue name, and video source)
from config import (
    RABBITMQ_HOST,
    RABBITMQ_QUEUE,
    RABBITMQ_EXCHANGE,
    RABBITMQ_ROUTING_KEY,
    VIDEO_SOURCE
)

# Importing a utility function to encode frames before sending
from utils import encode_frame
import logging


# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')



# Function to establish connection and setup the RabbitMQ channel
def setup_rabbitmq(retries=10, delay=3):
    for i in range(retries):
        try:    
            # Create a blocking connection to RabbitMQ server
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
            # Create a channel on the connection to send messages
            channel = connection.channel()


            # Declare exchange with type (e.g., direct)
            channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type='direct', durable=True)

            # Declare queue with optional settings
            channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)


            # Bind queue to exchange with a routing key
            channel.queue_bind(exchange=RABBITMQ_EXCHANGE, queue=RABBITMQ_QUEUE, routing_key=RABBITMQ_ROUTING_KEY)

            logging.info(f"Connected to RabbitMQ at {RABBITMQ_HOST}")

            # Return the channel to be used for publishing
            return connection, channel
        except pika.exceptions.AMQPConnectionError as e:
            logging.warning(f"Connection failed (attempt {i+1}/{retries}), retrying in {delay}s...")
            time.sleep(delay)
    logging.error("Failed to connect to RabbitMQ after several attempts.")
    raise pika.exceptions.AMQPConnectionError("Could not connect to RabbitMQ")  


# Function to capture frames from video and publish them to RabbitMQ
def read_and_publish_frames():
    # Open the video source (file path or RTSP stream)
    cap = cv2.VideoCapture(VIDEO_SOURCE)
    if not cap.isOpened():
        logging.error(f"Failed to open video source: {VIDEO_SOURCE}")
        return
        
    # Setup RabbitMQ channel
    connection, channel = setup_rabbitmq()
    
    
    try:
        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                logging.info("End of video stream or error occurred.")
                break

            encoded = encode_frame(frame)
            if not encoded:
                logging.warning("Frame encoding failed, skipping frame.")
                continue

            # Publish the encoded frame
            channel.basic_publish(
                exchange=RABBITMQ_EXCHANGE,
                routing_key=RABBITMQ_ROUTING_KEY,
                body=encoded,
                properties=pika.BasicProperties(delivery_mode=2)  # Persistent
            )

            frame_count += 1
            if frame_count % 30 == 0:
                logging.info(f"Published {frame_count} frames...")

            time.sleep(0.03)  # Approx. 30 FPS

    except Exception as e:
        logging.exception("An error occurred while reading and publishing frames.")
    finally:
        cap.release()
        connection.close()
        logging.info("Resources released and RabbitMQ connection closed.")


# Main block to run the function if the script is executed directly
if __name__ == "__main__":
    read_and_publish_frames()
