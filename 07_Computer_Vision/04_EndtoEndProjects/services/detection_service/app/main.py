## main.py

import os
import json
import pika
import base64
import numpy as np
import cv2
import logging
from dotenv import load_dotenv
from datetime import datetime
from config import RABBITMQ_HOST, RABBITMQ_QUEUE
from object_detector import detect_objects
from violation_logic import check_violation
from db import save_violation_record
from stream_sender import send_to_streaming_service

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# Load environment variables
load_dotenv(dotenv_path="/app/.env")

# RabbitMQ setup
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
channel.basic_qos(prefetch_count=1)

# Save directory
FRAME_SAVE_DIR = "/app/videos/violations"
os.makedirs(FRAME_SAVE_DIR, exist_ok=True)

def decode_frame(base64_str):
    image_bytes = base64.b64decode(base64_str)
    np_arr = np.frombuffer(image_bytes, np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

def save_frame_to_disk(frame, source, frame_id):
    filename = f"{source}_frame{frame_id}_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.jpg"
    path = os.path.join(FRAME_SAVE_DIR, filename)
    cv2.imwrite(path, frame)
    return path

def process_frame(ch, method, properties, body):
    try:
        frame_data = json.loads(body)
        frame_id = frame_data['frame_id']
        source = frame_data['source']
        timestamp = frame_data['timestamp']
        frame = decode_frame(frame_data['frame_data'])

        detections = detect_objects(frame)
        violation, violation_boxes = check_violation(detections)

        if violation:
            frame_path = save_frame_to_disk(frame, source, frame_id)

            save_violation_record(
                frame_id=frame_id,
                source=source,
                bounding_boxes=violation_boxes,
                labels=[d['label'] for d in violation_boxes],
                timestamp=timestamp,
                frame_path=frame_path
            )

        send_to_streaming_service(
            frame_id=frame_id,
            source=source,
            bounding_boxes=detections,
            violation=violation,
	    frame=frame
        )

        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        logging.error(f"❌ Error processing frame: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)


