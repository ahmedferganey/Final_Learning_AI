## rabbitmq_consumer.py



# app/rabbitmq_consumer.py
import pika
from config import RABBITMQ_HOST, RABBITMQ_QUEUE
from main import process_frame

def start_rabbitmq_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(
        queue=RABBITMQ_QUEUE,
        on_message_callback=process_frame
    )

    print(f"[RabbitMQ] ✅ Connected to {RABBITMQ_QUEUE}. Waiting for frames...")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("[RabbitMQ] 🛑 Stopped by user.")
        channel.stop_consuming()
    finally:
        connection.close()

if __name__ == '__main__':
    start_rabbitmq_consumer()

