import pika
import cv2
import base64
import json
import logging
from config import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_QUEUE,
    RABBITMQ_EXCHANGE,
    RABBITMQ_ROUTING_KEY,
)

class FramePublisher:
    def __init__(self):
        try:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT)
            )
            self.channel = self.connection.channel()
            self.channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type='direct', durable=True)
            self.channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
            self.channel.queue_bind(exchange=RABBITMQ_EXCHANGE, queue=RABBITMQ_QUEUE, routing_key=RABBITMQ_ROUTING_KEY)
        except Exception as e:
            logging.error(f"❌ Failed to connect to RabbitMQ: {e}")
            raise

    def publish_json(self, payload: dict):
        try:
            self.channel.basic_publish(
                exchange=RABBITMQ_EXCHANGE,
                routing_key=RABBITMQ_ROUTING_KEY,
                body=json.dumps(payload),
                properties=pika.BasicProperties(delivery_mode=2)
            )
            logging.info(f"✅ Published frame from {payload['source']} ID={payload['frame_id']}")
        except Exception as e:
            logging.error(f"❌ Failed to publish message: {e}")

