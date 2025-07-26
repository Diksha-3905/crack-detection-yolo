from ultralytics import YOLO

model = YOLO('best.pt')  # Make sure best.pt is in the same folder
results = model.predict(source='deformation_sim_video.mp4', save=True, conf=0.3)

print("✅ Detection complete. Output saved in 'runs/detect/predict/'")
