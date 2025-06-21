## stream_sender.py


# app/stream_sender.py
# stream_service.py
import cv2
import json
import base64
import pika

class StreamService:
    def __init__(self, config):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.RABBITMQ_HOST))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=config.STREAM_QUEUE, durable=True)
        self.queue = config.STREAM_QUEUE

    def send(self, frame_id, source, bounding_boxes, violation, frame):
        for box in bounding_boxes:
            x1, y1, x2, y2 = box["bbox"]
            label = box["label"]
            color = (0, 0, 255) if violation else (0, 255, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        _, jpeg = cv2.imencode('.jpg', frame)
        encoded = base64.b64encode(jpeg.tobytes()).decode('utf-8')
        message = json.dumps({"frame_id": frame_id, "source": source, "violation": violation, "frame": encoded})
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=message)
        print(f"[STREAM] ✅ Published annotated frame {frame_id} to {self.queue}")





