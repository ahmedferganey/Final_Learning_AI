import pika
from app.config import *
from app.inference import run_inference
from app.violation_logic import check_violation

def callback(ch, method, properties, body):
    try:
        frame, detections = run_inference(body.decode())
        check_violation(frame, detections)
        print("[INFO] Detection complete, message processed.")
    except Exception as e:
        print("[ERROR]", e)


def start_consuming():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE)
    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)
    print("[INFO] Waiting for messages...")
    channel.start_consuming()

