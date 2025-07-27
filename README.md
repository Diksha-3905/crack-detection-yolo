# Crack-Detection-YOLO

A YOLO-based system for detecting and segmenting cracks in images. Built with YOLO (v8/v7/v5) for accurate crack detection and measurement.

## 🧠 Overview

- Trains a YOLO model for crack detection and segmentation.
- Generates bounding boxes and masks for cracks.
- Includes optional post-processing for measuring crack length/width.

## 🚀 Features

- **Real-time Detection** using YOLO.
- **Segmentation Support** for pixel-level accuracy.
- **Measurement Tools** to analyze crack dimensions.
- **Export Options**: Save results with masks and CSVs.

## 📁 Repository Structure

```
├── data/                   # Dataset files and YAML configs
├── models/                 # Pretrained weights and checkpoints
├── src/                    # Training, detection, and postprocess scripts
│   ├── train.py
│   ├── detect.py
│   ├── segment.py
│   └── postprocess.py
├── results/                # Inference outputs
├── requirements.txt
└── README.md
```

## ⚙️ Installation

```bash
git clone https://github.com/Diksha-3905/crack-detection-yolo.git
cd crack-detection-yolo

# Optional: create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## 🎯 Training

```bash
python src/train.py \
  --data data/crack-data.yaml \
  --cfg models/yolov8-custom.yaml \
  --weights yolov8n.pt \
  --epochs 50 \
  --imgsz 640
```

## 🤖 Inference

```bash
python src/detect.py \
  --weights runs/train/.../weights/best.pt \
  --source path/to/images \
  --conf 0.25 \
  --save-img
```

## 🖌 Segmentation

```bash
python src/segment.py \
  --weights runs/train/.../weights/best.pt \
  --source path/to/images \
  --save-mask
```

## 📏 Post-Processing

```bash
python src/postprocess.py \
  --input results/segmented/ \
  --output results/measurements.csv \
  --measure-length
```

## 📊 Evaluation Metrics

- **Detection**: Precision, Recall, mAP@0.5
- **Segmentation**: IoU, F1-score

## 📂 Dataset

You can train with public crack datasets like:
- [Ultralytics Crack-Seg Dataset](https://docs.ultralytics.com/datasets/segment/crack-seg/)
- Custom annotated images in YOLO format.

## 👤 Contributing

1. Fork the repo
2. Create a branch
3. Commit your changes
4. Open a Pull Request

## 📜 Citation

```
@misc{crack_detection_yolo,
  title = {Crack Detection using YOLO},
  authors = {sarveshprjs, Diksha-3905},
  year = {2025},
  url = {https://github.com/Diksha-3905/crack-detection-yolo}
}
```
