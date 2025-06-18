import cv2
import base64
import logging

def encode_frame(frame):
    try:
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 85]  # Optional: better compression
        _, buffer = cv2.imencode('.jpg', frame, encode_param)
        return base64.b64encode(buffer).decode('utf-8')
    except Exception as e:
        logging.warning(f"[utils] Encoding failed: {e}")
        return None

