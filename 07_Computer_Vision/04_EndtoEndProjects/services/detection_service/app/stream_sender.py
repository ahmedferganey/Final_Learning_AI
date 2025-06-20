## stream_sender.py


# app/stream_sender.py
import os
import json
import pika
import base64
import cv2
from dotenv import load_dotenv

load_dotenv(dotenv_path="/app/.env")

# RabbitMQ settings for streaming
STREAM_QUEUE = os.getenv("STREAM_QUEUE", "annotated_frames")
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")

connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue=STREAM_QUEUE, durable=True)

def send_to_streaming_service(frame_id, source, bounding_boxes, violation, frame):
    # Draw bounding boxes on frame
    for box in bounding_boxes:
        x1, y1, x2, y2 = box["bbox"]
        label = box["label"]
        color = (0, 0, 255) if violation else (0, 255, 0)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    _, jpeg = cv2.imencode('.jpg', frame)
    encoded = base64.b64encode(jpeg.tobytes()).decode('utf-8')

    message = json.dumps({
        "frame_id": frame_id,
        "source": source,
        "violation": violation,
        "frame": encoded
    })

    channel.basic_publish(
        exchange='',
        routing_key=STREAM_QUEUE,
        body=message
    )

    print(f"[STREAM] ✅ Published annotated frame {frame_id} to {STREAM_QUEUE}")




