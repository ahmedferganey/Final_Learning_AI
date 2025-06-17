import os
import base64
import cv2
import numpy as np
import torch
import torch.serialization
import torch.nn.modules.container
from torch.serialization import add_safe_globals

from ultralytics import YOLO
from ultralytics.nn.tasks import DetectionModel

# Allowlist standard classes
torch.serialization.add_safe_globals([
    torch.nn.modules.container.Sequential,
])
add_safe_globals([DetectionModel])

# Load model path from environment
MODEL_PATH = os.getenv("MODEL_PATH", "/app/models/yolo12m-v2.pt")

# Load model with weights_only=False workaround
model_obj = torch.load(MODEL_PATH, map_location='cpu', weights_only=False)

# Allowlist any custom class from the loaded model
conv_class = type(model_obj['model'].model[0])  # Usually first layer is Conv
torch.serialization.add_safe_globals([conv_class])

# Now safely load with YOLO
model = YOLO(MODEL_PATH)


def run_inference(encoded_image):
    """Run YOLO inference on a base64-encoded image and return results."""
    try:
        # Decode the base64 image to OpenCV format
        img_data = base64.b64decode(encoded_image)
        np_arr = np.frombuffer(img_data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if frame is None:
            raise ValueError("Failed to decode image.")

        # Run the model on the image
        results = model(frame)[0]

        # Parse results
        detections = []
        for box, cls in zip(results.boxes.xyxy, results.boxes.cls):
            x1, y1, x2, y2 = map(int, box.tolist())
            label = results.names[int(cls)]
            detections.append({"label": label, "box": [x1, y1, x2, y2]})

        return frame, detections

    except Exception as e:
        print(f"❌ Inference error: {e}")
        return None, []

