import pika
import json
from app.utils.video_buffer import VideoBuffer
from app.config import Config

config = Config()

connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue=config.RABBITMQ_QUEUE, durable=True)

buffer = VideoBuffer()

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"[Debug] Frame received: {len(message['frame'])} bytes | Violation: {message['violation']}")
    buffer.add_frame(message["frame"], message["violation"])
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue=config.RABBITMQ_QUEUE, on_message_callback=callback)

print("[RabbitMQ] Listening for annotated frames...")
channel.start_consuming()

