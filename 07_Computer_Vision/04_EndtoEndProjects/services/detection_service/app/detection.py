# app/detection.py

import os
import cv2
from ultralytics import YOLO
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path="/app/.env")
MODEL_PATH = os.getenv("MODEL_PATH", "/app/models/yolo12m-v2.pt")


class YOLO12Detector:
    _model_instance = None  # Class-level lazy-loaded singleton

    def __init__(self, model_path=MODEL_PATH):
        if YOLO12Detector._model_instance is None:
            print(f"[DETECTION] 🚀 Loading YOLO model from {model_path}...")
            YOLO12Detector._model_instance = YOLO(model_path)
            print("[DETECTION] ✅ YOLO model loaded.")
        self.model = YOLO12Detector._model_instance

    def detect(self, frame):
        """
        Perform detection on a single frame.
        Returns list of dictionaries with label, confidence, and bounding box.
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.model(rgb_frame)  # Returns a list of Results
        detections = []

        for box in results[0].boxes:
            coords = box.xyxy.cpu().numpy().astype(int)[0]
            x1, y1, x2, y2 = coords.tolist()
            conf = float(box.conf.cpu().numpy()[0])
            cls_id = int(box.cls.cpu().numpy()[0])
            label = self.model.names[cls_id]

            detections.append({
                "label": label,
                "confidence": conf,
                "bbox": [x1, y1, x2, y2]
            })

        return detections

