
import cv2
import numpy as np
from deep_sort_realtime.deepsort_tracker import DeepSort


class HandScooperTracker:
    def __init__(self, use_appearance=True):
        """
        use_appearance: whether to use frame content for tracking (True enables embedder)
        """
        self.tracker = DeepSort(
            max_age=30,
            embedder=None if not use_appearance else "mobilenet",
            half=True,
            bgr=True
        )

    def update(self, detections, frame_idx, frame=None):
        """
        Track hands and associate them with scoopers.

        Args:
            detections: list of dicts with keys ["label", "confidence", "bbox"]
            frame_idx: int, current frame index
            frame: np.ndarray, actual frame image (required if use_appearance=True)

        Returns:
            List of tracked hands with scooper proximity flag.
        """
        if frame is None:
            # fallback dummy frame to satisfy DeepSort
            frame = np.zeros((720, 1280, 3), dtype=np.uint8)

        hands = [d for d in detections if self._is_hand(d["label"])]
        scoopers = [d for d in detections if self._is_scooper(d["label"])]

        # Prepare input for DeepSort
        converted = []
        for d in hands:
            if "bbox" not in d or len(d["bbox"]) != 4:
                continue
            x1, y1, x2, y2 = d["bbox"]
            w, h = x2 - x1, y2 - y1
            converted.append(([x1, y1, w, h], d.get("confidence", 0.9), d["label"], None))

        tracks = self.tracker.update_tracks(converted, frame=frame)
        tracked_hands = []

        for track in tracks:
            if not track.is_confirmed():
                continue

            track_id = track.track_id
            ltrb = track.to_ltrb()
            x1, y1, x2, y2 = map(int, ltrb)
            label = track.get_det_class()

            if label is None or not self._is_hand(label):
                continue

            bbox = [x1, y1, x2, y2]
            has_scooper = any(self._iou(bbox, s["bbox"]) > 0.1 for s in scoopers)

            tracked_hands.append({
                "id": track_id,
                "type": "hand",
                "bbox": bbox,
                "has_scooper": has_scooper
            })

        return tracked_hands

    def _iou(self, boxA, boxB):
        """Compute IoU between two bounding boxes."""
        xA = max(boxA[0], boxB[0])
        yA = max(boxA[1], boxB[1])
        xB = min(boxA[2], boxB[2])
        yB = min(boxA[3], boxB[3])

        interArea = max(0, xB - xA) * max(0, yB - yA)
        boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
        boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

        return interArea / float(boxAArea + boxBArea - interArea + 1e-6)

    def _is_hand(self, label: str) -> bool:
        return "hand" in label.lower()

    def _is_scooper(self, label: str) -> bool:
        return any(keyword in label.lower() for keyword in ["scooper", "spoon", "glove"])

