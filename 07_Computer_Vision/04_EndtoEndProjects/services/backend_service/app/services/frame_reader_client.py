# app/services/frame_reader_client.py
import aio_pika
from app.core import rabbitmq, config
from app.streaming.manager import StreamManager

class FrameReaderClient:
    def __init__(self):
        self.connection = None
        self.channel = None
        
    async def consume_frames(self, camera_id: str):
        self.connection = await rabbitmq.get_rabbitmq_connection()
        self.channel = await self.connection.channel()
        await self.channel.set_qos(prefetch_count=10)
        
        queue = await self.channel.declare_queue(
            config.settings.RABBITMQ_STREAMING_FRAME_QUEUE,
            durable=True
        )
        
        async for message in queue:
            async with message.process():
                frame = message.body
                await StreamManager.broadcast(camera_id, frame)# Service: frame_reader_client
