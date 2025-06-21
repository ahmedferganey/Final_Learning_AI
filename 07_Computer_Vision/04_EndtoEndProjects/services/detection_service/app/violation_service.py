# violation_service.py
from shapely.geometry import box as shapely_box, Polygon
from typing import List, Dict

class ViolationService:
    PROTEIN_LABELS = {"protein", "meat", "ingredient"}
    SCOOPER_LABELS = {"scooper", "spoon", "glove"}
    HAND_LABELS = {"hand", "bare_hand", "uncovered_hand"}

    # Default zones (same as old logic)
    DEFAULT_ZONES_OF_INTEREST = {
        "protein_zone": [
            [60, 200, 200, 720],   # Vertical tray zone (left side)
            [220, 260, 400, 400]   # Front counter area near pizza
        ]
    }

    def __init__(self, roi_zones: Dict[str, List[List[int]]] = None):
        self.roi_zones = roi_zones or self.DEFAULT_ZONES_OF_INTEREST
        self.roi_polygons = self.get_rois_polygons(self.roi_zones)

    def bbox_to_polygon(self, bbox: List[int]) -> Polygon:
        """Convert a bounding box to a Shapely polygon."""
        return shapely_box(*bbox)

    def get_rois_polygons(self, zones: Dict[str, List[List[int]]]) -> List[Polygon]:
        """Convert zone bboxes into shapely polygons."""
        return [self.bbox_to_polygon(bbox) for zone in zones.values() for bbox in zone]

    def check_violation(self, detections: List[Dict]) -> (bool, List[Dict]):
        scooper_present = any(
            det.get('label', '').lower() in self.SCOOPER_LABELS for det in detections
        )

        hand_detections = []
        for det in detections:
            label = det.get('label', '').lower()
            bbox = det.get('bbox', [])

            if not bbox or len(bbox) != 4:
                continue  # Skip malformed bbox

            if any(hand_label in label for hand_label in self.HAND_LABELS):
                hand_detections.append({"label": label, "bbox": bbox})

        if not hand_detections:
            print("[VIOLATION] No hand detected — no violation.")
            return False, []

        for hand in hand_detections:
            hand_poly = self.bbox_to_polygon(hand["bbox"])
            for roi in self.roi_polygons:
                if hand_poly.intersects(roi):
                    if not scooper_present:
                        print(f"[VIOLATION] Hand entered ROI without scooper: {hand}")
                        return True, [hand]
                    else:
                        print(f"[SAFE] Hand entered ROI but scooper is present.")
                        return False, []

        print("[SAFE] Hands detected but none in ROI.")
        return False, []

