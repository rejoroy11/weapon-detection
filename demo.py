from ultralytics import YOLO
from pathlib import Path

MODEL_PATH = "yolo26n_detection_best.pt"

model = YOLO(MODEL_PATH)

image_path = input("Enter image path: ")

results = model(image_path, conf=0.25)

for result in results:
    if len(result.boxes) == 0:
        print("No weapons detected.")
        continue

    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = model.names[class_id]

        print(
            f"Detected: {class_name} | "
            f"Confidence: {confidence:.2f}"
        )

    result.save("output")
