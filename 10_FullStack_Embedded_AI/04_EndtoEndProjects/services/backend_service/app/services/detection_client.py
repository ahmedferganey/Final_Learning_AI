from app.schemas.detection import DetectionRequest, DetectionResponse

async def trigger_detection_job(request: DetectionRequest) -> DetectionResponse:
    # Simulate triggering external detection service
    # In production, send HTTP or publish to RabbitMQ
    dummy_result = DetectionResponse(
        video_id=request.video_id,
        results=[
            {
                "object_id": "obj_123",
                "label": "car",
                "confidence": 0.94,
                "bounding_box": {"x": 100, "y": 120, "width": 80, "height": 60}
            }
        ]
    )
    return dummy_result

