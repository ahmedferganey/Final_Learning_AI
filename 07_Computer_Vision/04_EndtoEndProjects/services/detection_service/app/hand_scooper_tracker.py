# Updated hand_scooper_tracker.py using Deep SORT
import cv2
import numpy as np
from deep_sort_realtime.deepsort_tracker import DeepSort

class HandScooperTracker:
    def __init__(self):
        self.tracker = DeepSort(max_age=30)

    def update(self, detections, frame_idx):
        # Convert detections to DeepSort format
        converted = []
        for d in detections:
            if not d.get("bbox") or len(d["bbox"]) != 4:
                continue
            x1, y1, x2, y2 = d["bbox"]
            w, h = x2 - x1, y2 - y1
            confidence = d.get("confidence", 0.9)
            label = d.get("label", "")
            converted.append(([x1, y1, w, h], confidence, label, None))

        outputs = self.tracker.update_tracks(converted, frame=np.zeros((720, 1280, 3), dtype=np.uint8))

        hands = [d for d in detections if any(label in d["label"].lower() for label in ["hand", "bare_hand"])]
        scoopers = [d for d in detections if any(label in d["label"].lower() for label in ["scooper", "glove", "spoon"])]

        tracked = []
        for track in outputs:
            if not track.is_confirmed():
                continue
            track_id = track.track_id
            ltrb = track.to_ltrb()
            x1, y1, x2, y2 = map(int, ltrb)
            label = track.get_det_class()
            if not label:
                print(f"[WARNING] Skipping track {track_id} with missing label.")
                continue
            if "hand" not in label.lower():
                continue
            
            bbox = [x1, y1, x2, y2]
            has_scooper = any(self._iou(bbox, s["bbox"]) > 0.1 for s in scoopers)

            tracked.append({
                "id": track_id,
                "type": "hand",
                "bbox": bbox,
                "has_scooper": has_scooper
            })

        return tracked

    def _iou(self, boxA, boxB):
        xA = max(boxA[0], boxB[0])
        yA = max(boxA[1], boxB[1])
        xB = min(boxA[2], boxB[2])
        yB = min(boxA[3], boxB[3])
        interArea = max(0, xB - xA) * max(0, yB - yA)
        boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
        boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
        return interArea / float(boxAArea + boxBArea - interArea + 1e-6)
