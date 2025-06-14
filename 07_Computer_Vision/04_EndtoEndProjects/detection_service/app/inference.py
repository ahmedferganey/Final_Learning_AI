from ultralytics import YOLO
import cv2
import numpy as np

class InferenceEngine:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, image_bytes):
        np_arr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        results = self.model(image, conf=0.3)[0]

        detections = []
        for box in results.boxes:
            label = results.names[int(box.cls)]
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
            detections.append({
                "label": label,
                "box": [x1, y1, x2, y2],
                "conf": float(box.conf)
            })
        return detections
