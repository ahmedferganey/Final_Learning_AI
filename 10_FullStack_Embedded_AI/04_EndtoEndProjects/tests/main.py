import cv2

points = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"Clicked: ({x}, {y})")

video_path = "pizza.mp4"
cap = cv2.VideoCapture(video_path)

ret, frame = cap.read()
if ret:
    cv2.imshow("Click to mark ROI corners", frame)
    cv2.setMouseCallback("Click to mark ROI corners", click_event)

    print("🖱️ Click two corners (top-left and bottom-right)... then press any key.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if len(points) == 2:
        (x1, y1), (x2, y2) = points
        print(f"✅ ROI Bounding Box: [{x1}, {y1}, {x2}, {y2}]")
    else:
        print("❌ You must click two points!")
else:
    print("❌ Failed to load video.")

