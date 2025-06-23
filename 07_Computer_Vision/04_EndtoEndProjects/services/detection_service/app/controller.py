# controller.py
import json
import base64
import numpy as np
from datetime import datetime
import cv2

class FrameProcessor:
    def __init__(self, detector, violation_service, repo, streamer):
        self.detector = detector
        self.violation_service = violation_service
        self.repo = repo
        self.streamer = streamer

    def decode_frame(self, base64_str):
        return cv2.imdecode(np.frombuffer(base64.b64decode(base64_str), np.uint8), cv2.IMREAD_COLOR)

    def save_frame_to_disk(self, frame, source, frame_id):
        filename = f"{source}_frame{frame_id}_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.jpg"
        path = os.path.join("/app/videos/violations", filename)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        cv2.imwrite(path, frame)
        return path

    def process(self, ch, method, properties, body):
        data = json.loads(body)
        frame = self.decode_frame(data['frame_data'])
        detections = self.detector.detect(frame)
        violation, boxes = self.violation_service.check_violation(detections, frame, data['frame_id'])
        frame_path = self.save_frame_to_disk(frame, data['source'], data['frame_id']) if violation else None

        if violation:
            self.repo.save_violation(
                frame_id=data['frame_id'],
                source=data['source'],
                bounding_boxes=boxes,
                labels=[b['label'] for b in boxes],
                timestamp=data['timestamp'],
                frame_path=frame_path
            )
        self.streamer.send(data['frame_id'], data['source'], detections, violation, frame)
        ch.basic_ack(delivery_tag=method.delivery_tag)


