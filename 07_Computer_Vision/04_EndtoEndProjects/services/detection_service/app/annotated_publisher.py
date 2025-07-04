import pika
import json
import base64
import cv2
from io import BytesIO

class AnnotatedFramePublisher:
    def __init__(self, config):
        self.config = config
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=config.RABBITMQ_HOST)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=config.ANNOTATED_FRAME_QUEUE, durable=True)

    def publish(self, frame_id, source, detections, is_violation, frame):
        try:
            # Encode frame to base64
            _, buffer = cv2.imencode('.jpg', frame)
            frame_b64 = base64.b64encode(buffer).decode('utf-8')

            message = {
                "frame_id": frame_id,
                "source": source,
                "detections": detections,
                "is_violation": is_violation,
                "frame_data": frame_b64,
            }

            self.channel.basic_publish(
                exchange='',
                routing_key=self.config.ANNOTATED_FRAME_QUEUE,
                body=json.dumps(message),
                properties=pika.BasicProperties(
                    delivery_mode=2  # Make message persistent
                )
            )
            print(f"[PUBLISH] ✅ Published annotated frame {frame_id}")
        except Exception as e:
            print(f"[PUBLISH] ❌ Failed to publish annotated frame: {e}")

