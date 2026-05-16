# Drone Detection System

A **real-time drone detection** web app built with **Streamlit** and **YOLOv8**. Detects and tracks drones through a live camera feed or uploaded video.

## Features

- Live camera drone detection using a custom YOLOv8 model (`best-300e.pt`)
- Video file upload and frame-by-frame detection
- Real-time bounding boxes with tracking IDs
- Streamlit multi-page UI

## Prerequisites

```bash
pip install -r requirements.txt
```

Requirements include: `streamlit`, `ultralytics`, `opencv-python`

## Usage

```bash
streamlit run main.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

## Pages

| Page | Description |
|------|-------------|
| Home (`main.py`) | Navigation hub |
| Live Camera | Real-time detection via webcam |
| Upload Video | Detection on uploaded video files |

## Model

`best-300e.pt` — YOLOv8 model trained for 300 epochs on a drone detection dataset.

## Project Structure

```
Drone-Detection-System/
├── main.py            # Streamlit entry point
├── pages/             # Multi-page app pages
│   └── Live.py        # Live camera detection
├── best-300e.pt       # Trained YOLOv8 weights
├── yolo/              # YOLO utilities
└── requirements.txt
```
