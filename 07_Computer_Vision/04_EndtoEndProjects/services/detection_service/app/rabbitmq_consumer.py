## rabbitmq_consumer.py



# app/rabbitmq_consumer.py

# rabbitmq_consumer.py
import pika
from config import Config
from controller import FrameProcessor
from db_repository import ViolationRepository
from detection import YOLO12Detector as YOLODetector
from violation_service import ViolationService
from stream_service import StreamService

if __name__ == '__main__':
    config = Config()
    detector = YOLODetector(config.MODEL_PATH)
    violation_service = ViolationService({"protein_zone": [[60, 200, 200, 720], [220, 260, 400, 400]]})
    repo = ViolationRepository(config)
    streamer = StreamService(config)
    processor = FrameProcessor(detector, violation_service, repo, streamer)

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=config.RABBITMQ_QUEUE, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=config.RABBITMQ_QUEUE, on_message_callback=processor.process)

    print(f"[RabbitMQ] ✅ Waiting for frames on {config.RABBITMQ_QUEUE}...")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()

