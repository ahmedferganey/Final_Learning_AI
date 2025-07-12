async def handle_stream(websocket):
    await websocket.accept()
    await websocket.send_text("Streaming started")
