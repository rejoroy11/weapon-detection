# weapon-detection
Real-time weapon detection using YOLO &amp;OpenCV
# Weapon Detection 🔫

A real-time computer vision project for detecting weapons using YOLO and OpenCV.

## Technologies

- Python
- YOLO
- OpenCV
- Ultralytics

## Features

- Real-time camera detection
- Object detection using YOLO
- Confidence-based detection
- Live bounding boxes

## Installation

```bash
pip install -r requirements.txt
## Detection Classes

The model can detect:

- 🔪 Knife
- 🔫 Handgun
- 💣 Grenade
- 😷 Medicinal Mask
- 😷 Theft Mask

## Example Result

The system successfully detected a knife with 82% confidence in testing.

## Pipeline

Image → YOLO26 → Object Detection → Bounding Box → Confidence Score
