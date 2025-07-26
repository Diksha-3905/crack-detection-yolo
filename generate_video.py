import cv2
import os
import random

# Use correct relative folder paths based on your actual folder names
pos_folder = 'Positive'
neg_folder = 'Negative'
video_name = 'deformation_sim_video.mp4'

# Collect sample images
images = []
for f in os.listdir(pos_folder)[:30]:  # first 30 cracked
    images.append(os.path.join(pos_folder, f))
for f in os.listdir(neg_folder)[:30]:  # first 30 uncracked
    images.append(os.path.join(neg_folder, f))

# Shuffle for realistic stream
random.shuffle(images)

# Video config
frame = cv2.imread(images[0])
height, width, _ = frame.shape
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), 5, (width, height))

# Write images to video
for img in images:
    frame = cv2.imread(img)
    video.write(frame)

video.release()
print("✅ Video created:", video_name)
