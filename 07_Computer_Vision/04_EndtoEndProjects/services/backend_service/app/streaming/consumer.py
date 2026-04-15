# consumer.py
import aio_pika
from app.core.config import settings
from app.streaming.manager import stream_manager

async def consume_frames():
    connection = await aio_pika.connect_robust(
        host=settings.RABBITMQ_HOST,
        port=settings.RABBITMQ_PORT,
        login=settings.RABBITMQ_USER,
        password=settings.RABBITMQ_PASS
    )
    channel = await connection.channel()
    await channel.set_qos(prefetch_count=10)

    exchange = await channel.declare_exchange(
        settings.RABBITMQ_EXCHANGE,
        aio_pika.ExchangeType.FANOUT,
        durable=True
    )

    queue = await channel.declare_queue(exclusive=True)
    await queue.bind(exchange)

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                frame = message.body
                await stream_manager.broadcast("main_camera", frame)

