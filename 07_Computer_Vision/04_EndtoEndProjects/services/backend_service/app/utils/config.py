import os
from dotenv import load_dotenv

 # Works locally and safely inside Docker when env_file is used
load_dotenv()

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_USER = os.getenv('RABBITMQ_USER')
RABBITMQ_PASS = os.getenv('RABBITMQ_PASS')
RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT', 5672))
RABBITMQ_EXCHANGE = os.getenv('RABBITMQ_EXCHANGE')
RABBITMQ_STREAMING_FRAME_QUEUE = os.getenv('RABBITMQ_STREAMING_FRAME_QUEUE')

