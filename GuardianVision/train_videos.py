import os
import random
from collections import defaultdict

def train_videos(get_bounding_boxes_func, categories, dataset_path):
    output = defaultdict(dict)
    for rootdirs, files in os.walk(dataset_path):
        current_category = os.path.basename(root)
        if current_category in categories:
            video_files = [f for f in files if f.endswith('.mp4')]

            num_videos_to_select = min(10, len(video_files))

            selected_videos = random.sample(video_files, num_videos_to_select)

            for video in selected_videos:
                video_path = os.path.join(root, video_file)
                bounding_boxes_output = get_bounding_boxes_func(video_path)
                output[current_category][video_file] = get_bounding_boxes_func(video_path)
    return output
