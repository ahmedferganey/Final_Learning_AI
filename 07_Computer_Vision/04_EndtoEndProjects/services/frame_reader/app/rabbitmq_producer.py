# rabbitmq_producer.py

import pika
import json
import time
import logging
from config import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_QUEUE,
    RABBITMQ_EXCHANGE,
    RABBITMQ_ROUTING_KEY,
)

class FramePublisher:
    def __init__(self, max_retries=5, retry_delay=2):
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self._connect()

    def _connect(self):
        retry_count = 0
        while retry_count < self.max_retries:
            try:
                logging.info("[RabbitMQ] Connecting...")
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(
                        host=RABBITMQ_HOST,
                        port=RABBITMQ_PORT,
                        heartbeat=60,  # heartbeat for connection health
                        blocked_connection_timeout=30
                    )
                )
                self.channel = self.connection.channel()
                self.channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type='direct', durable=True)
                self.channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
                self.channel.queue_bind(exchange=RABBITMQ_EXCHANGE, queue=RABBITMQ_QUEUE, routing_key=RABBITMQ_ROUTING_KEY)
                self.channel.confirm_delivery()  # ensure ACK confirmation
                logging.info("[RabbitMQ] ✅ Connected and confirmed delivery enabled.")
                return
            except Exception as e:
                retry_count += 1
                logging.error(f"[RabbitMQ] ❌ Connection failed: {e}. Retrying ({retry_count}/{self.max_retries})...")
                time.sleep(self.retry_delay * retry_count)

        raise ConnectionError("❌ Failed to connect to RabbitMQ after retries.")

    def publish_json(self, payload: dict):
        body = json.dumps(payload)
        for attempt in range(1, self.max_retries + 1):
            try:
                success = self.channel.basic_publish(
                    exchange=RABBITMQ_EXCHANGE,
                    routing_key=RABBITMQ_ROUTING_KEY,
                    body=body,
                    properties=pika.BasicProperties(delivery_mode=2)  # persistent message
                )
                if success:
                    logging.info(f"✅ Published frame from {payload['source']} ID={payload['frame_id']}")
                    return True
                else:
                    logging.warning(f"⚠️ Publish failed (no ACK) for frame {payload['frame_id']} (Attempt {attempt})")
            except pika.exceptions.AMQPError as e:
                logging.error(f"❌ AMQP error during publish: {e} (Attempt {attempt})")
                self._connect()  # attempt to reconnect
            except Exception as e:
                logging.error(f"❌ Unexpected error during publish: {e} (Attempt {attempt})")

            time.sleep(self.retry_delay * attempt)

        logging.error(f"❌ Final failure to publish frame {payload['frame_id']} after {self.max_retries} attempts.")
        return False


