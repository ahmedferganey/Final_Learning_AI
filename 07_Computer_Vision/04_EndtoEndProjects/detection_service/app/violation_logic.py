def check_violation(detections, roi_zones):
    hands = [d for d in detections if d['label'] == 'hand']
    scoopers = [d for d in detections if d['label'] == 'scooper']
    violations = []

    for roi in roi_zones:
        rx1, ry1, rx2, ry2 = roi
        hand_in_roi = any(
            rx1 < box[0] < rx2 and ry1 < box[1] < ry2
            for d in hands for box in [d['box']]
        )
        scooper_present = any(
            rx1 < box[0] < rx2 and ry1 < box[1] < ry2
            for d in scoopers for box in [d['box']]
        )

        if hand_in_roi and not scooper_present:
            violations.append({"roi": roi, "violation": True})
    return violations
