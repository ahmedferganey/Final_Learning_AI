# utils.py

import cv2
import base64
import logging

def encode_frame(frame, resize=(640, 480), grayscale=False, format='jpg', quality=85, max_bytes=512000):
    """
    Encodes a frame to base64 with optional resizing, grayscale, format selection,
    and maximum byte size constraint.

    Args:
        frame (np.ndarray): The image frame.
        resize (tuple): Resize target as (width, height), or None to keep original size.
        grayscale (bool): Convert to grayscale before encoding.
        format (str): 'jpg', 'png', or 'webp'.
        quality (int): Compression quality (for JPEG/WEBP).
        max_bytes (int): Max allowed byte size for the output.

    Returns:
        str: Base64 encoded frame, or None if encoding fails or too large.
    """
    try:
        if resize:
            frame = cv2.resize(frame, resize)

        if grayscale:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Encoding parameters
        encode_param = []
        ext = f'.{format.lower()}'
        if format.lower() in ['jpg', 'jpeg', 'webp']:
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        elif format.lower() == 'png':
            encode_param = [int(cv2.IMWRITE_PNG_COMPRESSION), 3]

        success, buffer = cv2.imencode(ext, frame, encode_param)
        if not success:
            raise ValueError("Frame encoding failed.")

        encoded = base64.b64encode(buffer).decode('utf-8')

        if len(encoded) > max_bytes:
            logging.warning(f"[utils] Encoded frame exceeds {max_bytes} bytes limit. Skipping.")
            return None

        return encoded

    except Exception as e:
        logging.warning(f"[utils] Encoding failed: {e}")
        return None

