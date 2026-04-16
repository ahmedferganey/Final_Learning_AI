import pika
import json
import base64
import logging
import signal
import sys
from app.utils.video_buffer import VideoBuffer
from app.config import Config

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

config = Config()


connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue=config.ANNOTATED_FRAME_QUEUE, durable=True)

buffer = VideoBuffer()



# Graceful shutdown handling
def shutdown_handler(sig, frame):
    logging.info("🔌 Shutting down gracefully...")
    try:
        if channel.is_open:
            channel.close()
        if connection.is_open:
            connection.close()
    except Exception as e:
        logging.error(f"❌ Error during shutdown: {e}")
    sys.exit(0)
    
    

signal.signal(signal.SIGINT, shutdown_handler)
signal.signal(signal.SIGTERM, shutdown_handler)
    

# Message callback
def callback(ch, method, properties, body):
    try:
        message = json.loads(body)
        logging.debug(f"📨 Full message received: {message}")

        if 'frame_data' not in message:
            logging.warning("⚠️ Received message without 'frame_data' key.")
            ch.basic_ack(delivery_tag=method.delivery_tag)
            return

        frame_data_b64 = message['frame_data']
        is_violation = message.get("is_violation", False)

        # Just validate the base64 (no need to decode/store it)
        try:
            base64.b64decode(frame_data_b64)
        except Exception as decode_err:
            logging.error(f"❌ Invalid base64 frame: {decode_err}")
            ch.basic_ack(delivery_tag=method.delivery_tag)
            return

        logging.info(f"✅ Frame received (len={len(frame_data_b64)} base64 chars) | Violation: {is_violation}")

        # Store base64 frame directly
        buffer.add_frame(frame_data_b64, is_violation)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        logging.exception("❌ Unexpected error while processing message")

      
# Start consuming
channel.basic_consume(queue=config.ANNOTATED_FRAME_QUEUE, on_message_callback=callback)

logging.info("🚀 [RabbitMQ] Listening for frame queue frames...")
channel.start_consuming()
