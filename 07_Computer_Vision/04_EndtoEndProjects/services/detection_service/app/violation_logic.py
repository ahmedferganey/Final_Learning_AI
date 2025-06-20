## violation_logic.py


# app/violation_logic.py
from shapely.geometry import box as shapely_box, Polygon
from typing import List, Tuple, Dict

# Define labels
PROTEIN_LABELS = {"protein", "meat", "ingredient"}
SCOOPER_LABELS = {"scooper", "spoon", "glove"}
HAND_LABELS = {"hand", "bare_hand", "uncovered_hand"}


# Default Zones of Interest for ingredient area
# Format: [x1, y1, x2, y2] — you can customize or load per camera
ZONES_OF_INTEREST = {
    "protein_zone": [
        [60, 200, 200, 720],   # Vertical tray zone (left side)
        [220, 260, 400, 400]   # Front counter area near pizza
    ]
}

def bbox_to_polygon(bbox: List[int]) -> Polygon:
    """Convert bounding box list to a Shapely polygon."""
    return shapely_box(*bbox)


def get_rois_polygons(zones: Dict[str, List[List[int]]]) -> List[Polygon]:
    """Convert all ROIs from zone dictionary to Shapely polygons."""
    return [bbox_to_polygon(bbox) for box_list in zones.values() for bbox in box_list]




def check_violation(
    detections: List[Dict],
    roi_zones: Dict[str, List[List[int]]] = ZONES_OF_INTEREST
) -> Tuple[bool, List[Dict]]:
    """
    Check for violations:
    - If a hand intersects with ROI and no scooper is detected → violation

    Returns:
        Tuple of (bool: violation_detected, List[Dict]: violating_detections)
    """

    roi_polygons = get_rois_polygons(roi_zones)
    if not roi_polygons:
        print("[WARNING] No ROI zones configured.")
        return False, []

    scooper_present = False
    hand_detections = []

    # First pass: check for scooper and collect hands
    for det in detections:
        label = det.get("label", "").lower()
        bbox = det.get("bbox", [])

        if not bbox or len(bbox) != 4:
            continue  # Skip invalid bbox

        if label in SCOOPER_LABELS:
            scooper_present = True
        elif any(hand_label in label for hand_label in HAND_LABELS):
            hand_detections.append({"label": label, "bbox": bbox})

    # If no hands, nothing to check
    if not hand_detections:
        return False, []

    # Second pass: check each hand against all ROIs
    for hand in hand_detections:
        hand_poly = bbox_to_polygon(hand["bbox"])
        for roi in roi_polygons:
            if hand_poly.intersects(roi):
                if not scooper_present:
                    print(f"[VIOLATION] Hand entered ROI without scooper: {hand}")
                    return True, [hand]
                else:
                    print(f"[SAFE] Hand in ROI but scooper is present.")
                    return False, []

    return False, []
