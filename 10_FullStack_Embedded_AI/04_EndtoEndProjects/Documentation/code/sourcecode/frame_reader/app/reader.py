import cv2
import pika
import time
import base64
import logging
from config import (
    CAMERA_URL,
    RABBITMQ_HOST,
    RABBITMQ_USER,
    RABBITMQ_PASS,
    RABBITMQ_QUEUE,
    RABBITMQ_EXCHANGE,
    RABBITMQ_ROUTING_KEY,
)
from utils import encode_frame

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')

# Establish connection and setup the RabbitMQ channel
def setup_rabbitmq(retries=10, delay=3):
    for i in range(retries):
        try:
            credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials))
            channel = connection.channel()

            channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type='direct', durable=True)
            channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
            channel.queue_bind(exchange=RABBITMQ_EXCHANGE, queue=RABBITMQ_QUEUE, routing_key=RABBITMQ_ROUTING_KEY)

            logging.info(f"✅ Connected to RabbitMQ at {RABBITMQ_HOST}")
            return connection, channel

        except pika.exceptions.AMQPConnectionError:
            logging.warning(f"⏳ Connection attempt {i+1}/{retries} failed. Retrying in {delay}s...")
            time.sleep(delay)

    raise pika.exceptions.AMQPConnectionError("❌ Failed to connect to RabbitMQ after several attempts.")

# Capture and publish frames from video source
def read_and_publish_frames():
    cap = cv2.VideoCapture(CAMERA_URL)
    if not cap.isOpened():
        logging.error(f"❌ Failed to open camera or video source: {CAMERA_URL}")
        return

    connection, channel = setup_rabbitmq()

    try:
        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                logging.info("📴 End of video stream or error occurred.")
                break

            encoded = encode_frame(frame)
            if not encoded:
                logging.warning("⚠️ Frame encoding failed, skipping.")
                continue

            channel.basic_publish(
                exchange=RABBITMQ_EXCHANGE,
                routing_key=RABBITMQ_ROUTING_KEY,
                body=encoded,
                properties=pika.BasicProperties(delivery_mode=2)  # Make message persistent
            )

            frame_count += 1
            if frame_count % 30 == 0:
                logging.info(f"📤 Published {frame_count} frames...")

            time.sleep(0.03)  # ~30 FPS

    except Exception as e:
        logging.exception("❌ Error occurred while publishing frames.")
    finally:
        cap.release()
        connection.close()
        logging.info("🔒 Released video and RabbitMQ resources.")

if __name__ == "__main__":
    read_and_publish_frames()

