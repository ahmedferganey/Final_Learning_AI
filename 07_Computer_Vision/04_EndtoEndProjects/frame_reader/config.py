import os

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_QUEUE = os.getenv('RABBITMQ_QUEUE', 'frame_queue')
RABBITMQ_EXCHANGE = os.getenv('RABBITMQ_EXCHANGE', 'video_exchange')
RABBITMQ_ROUTING_KEY = os.getenv('RABBITMQ_ROUTING_KEY', 'video_frame')
VIDEO_SOURCE = os.getenv('VIDEO_SOURCE', 'pizza.mp4')
