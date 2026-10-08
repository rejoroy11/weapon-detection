import cv2
from ultralytics import YOLO

model = YOLO("best.pt")

camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success:
        break

    results = model(frame, conf=0.5)
    output = results[0].plot()

    cv2.imshow("Weapon Detection", output)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()