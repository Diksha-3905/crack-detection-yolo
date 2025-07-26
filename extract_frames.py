import cv2
import os

video_path = 'deformation_sim_video.mp4'
output_folder = 'frames'
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imwrite(os.path.join(output_folder, f'frame_{count:03}.jpg'), frame)
    count += 1

cap.release()
print(f"✅ Extracted {count} frames into 'frames/' folder")
