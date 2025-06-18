import pika
import time
import logging
from app.config import *
from app.inference import run_inference
from app.violation_logic import check_violation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def callback(ch, method, properties, body):
    try:
        frame, detections = run_inference(body.decode('utf-8'))
        if frame is not None and detections:
            check_violation(frame, detections)
        logger.info("📩 Frame processed.")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        logger.error(f"❌ Error processing frame: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

def start_consuming():
    for attempt in range(10):
        try:
            credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
            connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, credentials=credentials))
            channel = connection.channel()

            channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback)

            logger.info("✅ Connected to RabbitMQ. Waiting for frames...")
            channel.start_consuming()
            break

        except pika.exceptions.AMQPConnectionError as e:
            logger.warning(f"⏳ Retry {attempt+1}/10: RabbitMQ not ready. Waiting...")
            time.sleep(5)
        except Exception as e:
            logger.error(f"❌ Consumer fatal error: {e}")

