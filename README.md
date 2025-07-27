Crack-Detection-YOLO
A YOLO-based system for detecting and segmenting cracks in images—powered by YOLO (vX) and optionally SAHI or instance segmentation tools.

🧠 Overview
Trains a crack detection model (YOLOv8/v7/v5) using annotated datasets.

Supports both object detection and segmentation for cracks.

Generates bounding boxes and segmentation masks for accurate localization.

Optional post-processing pipeline to measure crack length, width, and structure.

🚀 Features
Object Detection: YOLO detects cracks as bounding boxes or segmentation masks.

Segmentation Support: Enables pixel-wise delineation of crack boundaries.

Inference Options: Real-time detection via CLI or GUI.

Export Results: Export annotations, skeletal graph data, or DXF outputs.

Post‑processing: Length measurement, skeleton analysis, junction detection.

📁 Repository Structure
graphql
Copy
Edit
├── data/                   # Datasets and train/val/test splits
├── configs/                # YOLO config files (data.yaml, model.yaml)
├── models/                 # Pretrained weights, checkpoints
├── src/
│   ├── train.py
│   ├── detect.py
│   ├── segment.py
│   ├── postprocess.py
│   └── utils.py
├── results/                # Inference outputs (images, CSVs, masks)
├── requirements.txt
└── README.md
⚙️ Installation
bash
Copy
Edit
git clone https://github.com/Diksha-3905/crack-detection-yolo.git
cd crack-detection-yolo

# (Optional) Virtual environment
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
🎯 Training

python src/train.py \
  --data data/crack-data.yaml \
  --cfg models/yolov8-custom.yaml \
  --weights 'yolov8n.pt' \
  --epochs 50 \
  --imgsz 640
Training will output model weights (e.g. best.pt) in runs/train/....

🤖 Inference / Segmentation

python src/detect.py \
  --weights runs/train/.../weights/best.pt \
  --source path/to/images \
  --conf 0.25 \
  --save-img
For segmentation :

python src/segment.py \
  --weights runs/train/.../weights/best.pt \
  --source path/to/images \
  --save-mask
🔧 Post‑processing / Measurement

python src/postprocess.py \
  --input results/segmented/ \
  --output results/measurements.csv \
  --measure-length
Outputs include computed crack lengths and optionally skeletal graph data.

📊 Evaluation
Evaluate using standard metrics: Precision, Recall, mAP@0.5 (for detection); IoU, F1-score (for segmentation).

Example: mAP up to ~67–70% on road/pavement crack datasets using YOLOv5/Yolov8 
YouTube
+4
Roboflow
+4
GitHub
+4
GitHub
+2
GitHub
+2
Ultralytics Docs
+2
GitHub
+2
Syddansk Universitet
+2
GitHub
+2
arXiv
+10
arXiv
+10
GitHub
+10
GitHub
.

Related research benchmarks: YOLOv8 with stronger performance via segmentation and attention enhancements 
arXiv
arXiv
.

🧪 Example Dataset
You may leverage public crack segmentation datasets like [Ultralytics Crack‑Seg Dataset] (~4,000 annotated images) for training/testing. YAML format examples and training scripts are also available 
Ultralytics Docs
.

👤 Contributing
Contributions, feature requests, and bug reports are welcome:

Fork the repo

Create a feature or fix branch

Commit and push changes

Open a pull request with clear description

ℹ️ Cite this project
If you use this work in your research, please reference it accordingly:

arduino

@misc{crack_detection_yolo,
  title = {Crack Detection using YOLO},
  author = {Diksha-3905},
  year = {2025},
  url = {https://github.com/Diksha-3905/crack-detection-yolo}
}
