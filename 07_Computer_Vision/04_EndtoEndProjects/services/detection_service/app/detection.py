# app/detection.py

import os

# Disable GPU for MediaPipe compatibility
os.environ["MEDIAPIPE_DISABLE_GPU"] = "1"
import cv2
import numpy as np
from ultralytics import YOLO
from dotenv import load_dotenv
from typing import List, Dict


# Load environment variables
load_dotenv(dotenv_path="/app/.env")
MODEL_PATH = os.getenv("MODEL_PATH", "/app/models/yolo12m-v2.pt")


class YOLO12Detector:
    _model_instance = None  # Singleton model instance

    def __init__(self, model_path: str = MODEL_PATH):
        if YOLO12Detector._model_instance is None:
            print(f"[DETECTION] 🚀 Loading YOLO model from {model_path}...")
            try:
                YOLO12Detector._model_instance = YOLO(model_path)
                print("[DETECTION] ✅ YOLO model loaded.")
            except Exception as e:
                print(f"[DETECTION] ❌ Failed to load YOLO model: {e}")
                raise
        self.model = YOLO12Detector._model_instance

    def detect(self, frame: np.ndarray) -> List[Dict]:
        """
        Perform detection on a single frame.
        Returns list of dictionaries with label, confidence, and bounding box.
        """
        try:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.model(rgb_frame)

            detections = []
            if not results or not results[0].boxes:
                return detections

            for box in results[0].boxes:
                coords = box.xyxy.cpu().numpy().astype(int)[0]  # [x1, y1, x2, y2]
                conf = float(box.conf.cpu().numpy()[0])
                cls_id = int(box.cls.cpu().numpy()[0])
                label = self.model.names[cls_id]

                detections.append({
                    "label": label,
                    "confidence": round(conf, 4),
                    "bbox": coords.tolist()
                })

            return detections
        except Exception as e:
            print(f"[DETECTION] ❌ Detection failed: {e}")
            return []

