import pika
import cv2
import time
from config import *

# Setup RabbitMQ connection
credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
params = pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, credentials=credentials)
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Declare fanout exchange (broadcast)
channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type='fanout', durable=True)

# Read and publish video frames
cap = cv2.VideoCapture(VIDEO_PATH)
print(f"Reading video from: {VIDEO_PATH}")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    _, buffer = cv2.imencode('.jpg', frame)
    body = buffer.tobytes()

    # Publish to fanout exchange — all bound queues will receive it
    channel.basic_publish(
        exchange=RABBITMQ_EXCHANGE,
        routing_key='',  # ignored for fanout
        body=body,
        properties=pika.BasicProperties(delivery_mode=2)  # make message persistent
    )

    time.sleep(0.03)  # ~30 fps

cap.release()
connection.close()

