# Enhanced violation_service.py
from shapely.geometry import box as shapely_box, Polygon
from typing import List, Dict
from .hand_classifier import HandActionClassifier
from .hand_scooper_tracker import HandScooperTracker

class ViolationService:
    PROTEIN_LABELS = {"protein", "meat", "ingredient"}
    SCOOPER_LABELS = {"scooper", "spoon", "glove"}
    HAND_LABELS = {"hand", "bare_hand", "uncovered_hand"}

    DEFAULT_ZONES_OF_INTEREST = {
        "protein_zone": [
            [319, 525, 389, 590]  # Actual protein area in the video
        ]
    }

    def __init__(self, roi_zones: Dict[str, List[List[int]]] = None):
        self.roi_zones = roi_zones or self.DEFAULT_ZONES_OF_INTEREST
        self.roi_polygons = self.get_rois_polygons(self.roi_zones)
        self.hand_action_classifier = HandActionClassifier()
        self.tracker = HandScooperTracker()

    def bbox_to_polygon(self, bbox: List[int]) -> Polygon:
        return shapely_box(*bbox)

    def get_rois_polygons(self, zones: Dict[str, List[List[int]]]) -> List[Polygon]:
        return [self.bbox_to_polygon(bbox) for zone in zones.values() for bbox in zone]

    def check_violation(self, detections: List[Dict], frame: any, frame_idx: int) -> (bool, List[Dict]):
        tracked_objects = self.tracker.update(detections, frame_idx)
        violations = []

        for obj in tracked_objects:
            if obj["type"] != "hand":
                continue

            hand_poly = self.bbox_to_polygon(obj["bbox"])
            in_roi = any(hand_poly.intersects(roi) for roi in self.roi_polygons)

            if not in_roi:
                continue

            # 🧠 Feed bounding box and frame to MediaPipe-based classifier
            self.hand_action_classifier.update(obj["id"], frame, obj["bbox"])

            scooper_nearby = obj.get("has_scooper", False)
            action = self.hand_action_classifier.classify(obj["id"])

            if action == "grabbing" and not scooper_nearby:
                print(f"[VIOLATION] Hand {obj['id']} grabbed from ROI without scooper.")
                violations.append(obj)

        return bool(violations), violations

