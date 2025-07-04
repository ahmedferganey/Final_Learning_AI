
import json
import os
import cv2
import base64
import numpy as np
from datetime import datetime


class FrameProcessor:
    def __init__(self, detector, violation_service, repo, publisher, debug=False):
        self.detector = detector
        self.violation_service = violation_service
        self.repo = repo
        self.publisher = publisher
        self.debug = debug

    def decode_frame(self, base64_str):
        try:
            decoded_bytes = base64.b64decode(base64_str)
            np_arr = np.frombuffer(decoded_bytes, dtype=np.uint8)
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            if frame is None:
                raise ValueError("cv2.imdecode returned None.")
            return frame
        except Exception as e:
            print(f"[DECODER] ❌ Failed to decode base64 frame: {e}")
            return None

    def save_frame_to_disk(self, frame, source, frame_id):
        try:
            timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
            filename = f"{source}_frame{frame_id}_{timestamp}.jpg"
            save_dir = "/app/videos/violations"
            os.makedirs(save_dir, exist_ok=True)
            path = os.path.join(save_dir, filename)
            cv2.imwrite(path, frame)
            return path
        except Exception as e:
            print(f"[SAVE] ❌ Failed to save frame: {e}")
            return None

    def process(self, ch, method, properties, body):
        try:
            data = json.loads(body)
            frame_id = data.get("frame_id")
            source = data.get("source", "unknown")
            timestamp = data.get("timestamp")
            base64_frame = data.get("frame_data")

            if not base64_frame:
                print(f"[PROCESS] ⚠️ Skipping frame {frame_id}: missing 'frame_data'")
                ch.basic_ack(delivery_tag=method.delivery_tag)
                return

            frame = self.decode_frame(base64_frame)
            if frame is None:
                ch.basic_ack(delivery_tag=method.delivery_tag)
                return

            detections = self.detector.detect(frame)
            is_violation, violating_objects = self.violation_service.check_violation(
                detections, frame, frame_id
            )

            frame_path = None
            if is_violation:
                frame_path = self.save_frame_to_disk(frame, source, frame_id)
                self.repo.save_violation(
                    frame_id=frame_id,
                    source=source,
                    bounding_boxes=violating_objects,
                    labels=[obj['label'] for obj in violating_objects],
                    timestamp=timestamp,
                    frame_path=frame_path,
                )

            self.publisher.publish(frame_id, source, detections, is_violation, frame)

        except Exception as e:
            print(f"[PROCESS] ❌ Unexpected error: {e}")
        finally:
            ch.basic_ack(delivery_tag=method.delivery_tag)

