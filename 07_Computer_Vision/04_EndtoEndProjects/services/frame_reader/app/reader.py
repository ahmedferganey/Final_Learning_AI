#!/usr/bin/env python3
import cv2
import pika
import json
import base64
import time
import os
import logging
import sys
from datetime import datetime
from utils import encode_frame  # reuse from Version B

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class FrameReaderService:
    def __init__(self):
        self.video_source = os.getenv('CAMERA_URL', '/data/pizza.mp4')
        self.rabbitmq_url = os.getenv('RABBITMQ_URL')
        self.rabbitmq_host = os.getenv('RABBITMQ_HOST', 'rabbitmq')
        self.rabbitmq_user = os.getenv('RABBITMQ_USER', 'guest')
        self.rabbitmq_pass = os.getenv('RABBITMQ_PASS', 'guest')
        self.rabbitmq_queue = os.getenv('RABBITMQ_QUEUE', 'frame_queue')
        self.rabbitmq_exchange = os.getenv('RABBITMQ_EXCHANGE', 'video_exchange')
        self.rabbitmq_routing_key = os.getenv('RABBITMQ_ROUTING_KEY', 'video_frame')
        self.target_fps = float(os.getenv('TARGET_FPS', '10'))
        
        self.connection = None
        self.channel = None
        self.cap = None
        self.frame_count = 0
        self.total_frames = 0
        self.video_fps = 0

    def setup_rabbitmq(self):
        for i in range(10):
            try:
                if self.rabbitmq_url:
                    conn_params = pika.URLParameters(self.rabbitmq_url)
                else:
                    creds = pika.PlainCredentials(self.rabbitmq_user, self.rabbitmq_pass)
                    conn_params = pika.ConnectionParameters(host=self.rabbitmq_host, credentials=creds)

                self.connection = pika.BlockingConnection(conn_params)
                self.channel = self.connection.channel()
                self.channel.exchange_declare(exchange=self.rabbitmq_exchange, exchange_type='direct', durable=True)
                self.channel.queue_declare(queue=self.rabbitmq_queue, durable=True)
                self.channel.queue_bind(exchange=self.rabbitmq_exchange, queue=self.rabbitmq_queue, routing_key=self.rabbitmq_routing_key)
                logger.info(f"✅ Connected to RabbitMQ at {self.rabbitmq_host or self.rabbitmq_url}")
                return True
            except Exception as e:
                logger.warning(f"⏳ RabbitMQ connection failed: {e}, retrying...")
                time.sleep(5)
        return False

    def setup_video(self):
        if not os.path.exists(self.video_source):
            logger.error(f"❌ Video not found: {self.video_source}")
            return False

        self.cap = cv2.VideoCapture(self.video_source)
        if not self.cap.isOpened():
            logger.error("❌ Could not open video source")
            return False

        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.video_fps = self.cap.get(cv2.CAP_PROP_FPS)
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        logger.info(f"🎞️  Video loaded: {self.video_source}")
        logger.info(f"Frames: {self.total_frames}, FPS: {self.video_fps}, Resolution: {width}x{height}")
        return True

    def publish(self, frame_data, frame_number, width, height):
        try:
            message = {
                'frame_id': self.frame_count,
                'frame_number': frame_number,
                'timestamp': datetime.now().isoformat(),
                'frame_data': frame_data,
                'width': width,
                'height': height,
                'source': self.video_source,
                'total_frames': self.total_frames,
                'video_fps': self.video_fps
            }

            self.channel.basic_publish(
                exchange=self.rabbitmq_exchange,
                routing_key=self.rabbitmq_routing_key,
                body=json.dumps(message),
                properties=pika.BasicProperties(delivery_mode=2)
            )
            return True
        except Exception as e:
            logger.error(f"❌ Failed to publish frame: {e}")
            return False

    def run(self):
        if not self.setup_rabbitmq() or not self.setup_video():
            logger.error("❌ Initialization failed")
            return False

        frame_skip = max(1, int(self.video_fps / self.target_fps)) if self.video_fps else 1
        frame_number = 0

        while True:
            ret, frame = self.cap.read()
            if not ret:
                logger.info("📴 End of video")
                break

            frame_number += 1
            if frame_number % frame_skip != 0:
                continue

            h, w = frame.shape[:2]
            if w > 1280:
                scale = 1280 / w
                frame = cv2.resize(frame, (1280, int(h * scale)))

            encoded = encode_frame(frame)
            if encoded and self.publish(encoded, frame_number, frame.shape[1], frame.shape[0]):
                self.frame_count += 1

            if self.frame_count % 30 == 0:
                percent = (frame_number / self.total_frames) * 100
                logger.info(f"📤 Published {self.frame_count} frames ({percent:.1f}%)")

            time.sleep(0.03)

        self.cleanup()
        logger.info("✅ FrameReader finished")
        return True

    def cleanup(self):
        if self.cap:
            self.cap.release()
        if self.connection and not self.connection.is_closed:
            self.connection.close()
        logger.info("🔒 Cleaned up resources")

if __name__ == "__main__":
    service = FrameReaderService()
    success = service.run()
    sys.exit(0 if success else 1)

