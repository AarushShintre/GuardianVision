import cv2
import numpy as np
import pandas as pd

# Read the CSV file
data = pd.read_csv(r'C:\Users\gangliagurdian\Downloads\GaurdianPose\220CLIP.csv', skiprows=3)

# Read the input video
input_video = cv2.VideoCapture(r'C:\Users\gangliagurdian\Downloads\GaurdianPose\view1_labeled.avi')

# Check if video opened successfully
if not input_video.isOpened():
    print("Error: Could not open input video")
    exit()

# Get video properties
frame_width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(input_video.get(cv2.CAP_PROP_FPS))

# Create video writer with absolute path
output_path = r'C:\Users\gangliagurdian\Downloads\GaurdianPose\output_tracking_bbox.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

if not out.isOpened():
    print("Error: Could not create output video writer")
    exit()

def draw_bbox(frame, points, sus=False):
    if not points:
        return
        
    points = np.array(points)
    
    # Get min/max coordinates
    x_min = np.min(points[:, 0])
    y_min = np.min(points[:, 1])
    x_max = np.max(points[:, 0])
    y_max = np.max(points[:, 1])
    
    # Add padding
    padding = 10
    x_min = max(0, x_min - padding)
    y_min = max(0, y_min - padding)
    x_max = min(frame_width, x_max + padding)
    y_max = min(frame_height, y_max + padding)
    
    # Set color based on sus parameter
    color = (0, 0, 255) if sus else (0, 255, 0)
    
    # Draw bounding box
    cv2.rectangle(frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), color, 2)
    cv2.putText(frame, 'Person', (int(x_min), int(y_min)-10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

print(f"Processing {len(data)} frames")

# Process frames
for frame_idx in range(len(data)):
    ret, frame = input_video.read()
    if not ret:
        break
    
    # Get all points for current frame
    frame_data = data.iloc[frame_idx]
    points = []
    
    # Extract valid points
    try:
        for i in range(0, len(frame_data)-2, 3):
            x = int(float(frame_data[i]))
            y = int(float(frame_data[i+1]))
            likelihood = float(frame_data[i+2])
            
            if likelihood > 0.8:
                points.append((x, y))
                # Draw blue points
                cv2.circle(frame, (x, y), 4, (255, 0, 0), -1)
    except (ValueError, IndexError) as e:
        print(f"Error processing point at frame {frame_idx}, index {i}: {str(e)}")
        continue
    
    # Draw bounding box if we have points
    if points:
        draw_bbox(frame, points, sus=True)  # Set sus=False for green box
    
    # Write frame
    out.write(frame)

# Release resources
input_video.release()
out.release()
print("Video processing completed successfully")