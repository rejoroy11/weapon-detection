import cv2
from ultralytics import YOLO

MODEL_URL = "https://github.com/toNReverse/Weapon-and-Pose-Detection-YOLO26/releases/latest/download/yolo26n_detection_best.pt"

model = YOLO(MODEL_URL)

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open camera")
    exit()

while True:
    success, frame = camera.read()

    if not success:
        break

    results = model(frame, conf=0.25)
    output = results[0].plot()

    cv2.imshow("Weapon Detection", output)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()