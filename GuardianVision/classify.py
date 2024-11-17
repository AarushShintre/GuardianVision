import torch
import cv2
import numpy as np
from typing import Dict, List, Tuple

class VideoProcessor:
    def __init__(self, model_path: str, num_keypoints: int = 28):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self.load_model(model_path)
        self.num_keypoints = num_keypoints
    
    def load_model(self, model_path: str) -> torch.nn.Module:
        """Load the PyTorch model"""
        try:
            model = torch.load(model_path, map_location=self.device)
            model.eval()
            return model
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")

    def process_frame(self, frame: np.ndarray) -> torch.Tensor:
        """Process a single frame"""
        # Convert frame to tensor and normalize
        frame_tensor = torch.from_numpy(frame).float()
        frame_tensor = frame_tensor.permute(2, 0, 1)  # HWC to CHW
        frame_tensor = frame_tensor / 255.0
        frame_tensor = frame_tensor.unsqueeze(0)  # Add batch dimension
        return frame_tensor.to(self.device)

    def get_keypoints(self, predictions: torch.Tensor) -> np.ndarray:
        """Extract keypoints from model predictions"""
        with torch.no_grad():
            # Assuming predictions shape is [batch, num_keypoints, height, width]
            keypoints = predictions.squeeze().cpu().numpy()
            # Ensure we don't exceed the number of keypoints
            keypoints = keypoints[:self.num_keypoints]
            return keypoints

    def process_video(self, video_path: str) -> List[np.ndarray]:
        """Process entire video and return keypoints"""
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError("Error: Could not open video file")

        keypoints_sequence = []
        frame_count = 0

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # Process frame
                frame_tensor = self.process_frame(frame)
                
                # Get model predictions
                with torch.no_grad():
                    predictions = self.model(frame_tensor)
                
                # Extract keypoints
                try:
                    frame_keypoints = self.get_keypoints(predictions)
                    keypoints_sequence.append(frame_keypoints)
                except IndexError as e:
                    print(f"Error processing point at frame {frame_count}: {str(e)}")
                    # Append None or placeholder for failed frames
                    keypoints_sequence.append(None)
                
                frame_count += 1

        except Exception as e:
            print(f"Error during video processing: {str(e)}")
        finally:
            cap.release()

        return keypoints_sequence

def main():
    # Configuration
    model_path = "path/to/your/model.pth"
    video_path = "path/to/your/video.mp4"
    
    try:
        # Initialize processor
        processor = VideoProcessor(model_path)
        
        # Process video
        print(f"Processing video: {video_path}")
        keypoints_sequence = processor.process_video(video_path)
        
        # Process results
        valid_frames = sum(1 for k in keypoints_sequence if k is not None)
        print(f"Successfully processed {valid_frames} out of {len(keypoints_sequence)} frames")
        
        # Optional: Save results
        output_path = "keypoints.npy"
        np.save(output_path, keypoints_sequence)
        print(f"Saved keypoints to {output_path}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()