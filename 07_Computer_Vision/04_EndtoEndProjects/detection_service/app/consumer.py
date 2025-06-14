import pika, json, os, threading
from fastapi import FastAPI
from app.inference import InferenceEngine
from app.violation_logic import check_violation
import cv2
import time
from app.config import *

app = FastAPI()
inference = InferenceEngine(MODEL_PATH)

OUTPUT_PATH = os.getenv("OUTPUT_PATH", "/processed_frames")
os.makedirs(OUTPUT_PATH, exist_ok=True)

def consume_frames():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
            channel = connection.channel()
            channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)

            def callback(ch, method, properties, body):
                detections = inference.detect(body)
                violations = check_violation(detections, ROI_ZONES)

                timestamp = int(time.time() * 1000)
                frame_file = os.path.join(OUTPUT_PATH, f"{timestamp}.jpg")
                with open(frame_file, "wb") as fp:
                    fp.write(body)

                metadata = {
                    "timestamp": timestamp,
                    "detections": detections,
                    "violations": violations,
                    "latest_frame": os.path.basename(frame_file),
                }

                with open(os.path.join(OUTPUT_PATH, "metadata.json"), "w") as fp:
                    json.dump(metadata, fp)

            print("✅ Detection service listening for frames...")
            channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)
            channel.start_consuming()

        except pika.exceptions.AMQPConnectionError:
            print("🔁 Waiting for RabbitMQ to be ready...")
            time.sleep(5)

@app.on_event("startup")
def startup_event():
    thread = threading.Thread(target=consume_frames)
    thread.start()

