# This file contains functions for generating sparse captions from video frames using GPT-4o
# Author: Junming Lin
# Date: 2024-10-26
# Copyright (c) THUNLP, Tsinghua University. All rights reserved.
# See LICENSE file in the project root for license information.

import base64
import time
import cv2
import PIL.Image
import math
import datetime
import os
import json
import tqdm
import openai
from PIL import Image
from config import API_CONFIG

os.environ['OPENAI_API_KEY'] = API_CONFIG['OPENAI_API_KEY']
os.environ['OPENAI_BASE_URL'] = API_CONFIG['OPENAI_BASE_URL']
model_openai = openai.OpenAI()

def encode_image(image_path):
    """Encode image file to base64 string
    
    Args:
        image_path (str): Path to image file
        
    Returns:
        str: Base64 encoded image string
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
        
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
def get_response(model_input):
    """Get response from GPT-4 model with retry mechanism
    
    Args:
        model_input (dict): Input for the model including text and images
        
    Returns:
        str: Model's response text
    """
    response = ''
    for _ in range(20):
        try:
            response = model_openai.chat.completions.create(
                model='gpt-4o-2024-05-13',
                messages=[{
                    'role': 'user',
                    'content': model_input
                }],
                max_tokens=1000,
            ).choices[0].message.content
            break
        except:
            continue
    return response

def format_time(seconds):
    """Format seconds into HH-MM-SS string
    
    Args:
        seconds (float): Time in seconds
        
    Returns:
        str: Formatted time string in HH-MM-SS format
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours}_{minutes:02d}_{seconds:02d}".replace('_', '-')

def video_to_images(video_path):
    """Extract frames from video and save as images with timestamps
    
    Args:
        video_path (str): Path to video directory
    """
    video_file = os.path.join(video_path, 'video.mp4')
    if not os.path.exists(video_file):
        raise FileNotFoundError(f"Video file not found: {video_file}")
        
    images_folder = os.path.join(video_path, 'images')
    if not os.path.exists(images_folder):
        os.makedirs(images_folder)
        cap = cv2.VideoCapture(video_file)
        if not cap.isOpened():
            raise RuntimeError(f"Failed to open video file: {video_file}")
            
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = 0
        saved_count = 0
        current_time = 0.0
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        color = (255, 255, 255)
        thickness = 2
        position = (10, 50)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame_time = frame_count / fps
            if frame_time >= current_time:
                formatted_time = format_time(current_time)
                cv2.putText(frame, formatted_time.replace('-', ':'), position, font, font_scale, color, thickness,
                            cv2.LINE_AA)
                frame_name = os.path.join(images_folder, f'time_{formatted_time}.jpg')
                img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                img.save(frame_name)
                saved_count += 1
                current_time += 1.0
            frame_count += 1
        cap.release()
        print(f"Total saved frames: {saved_count}")
    else:
        print(f"Images folder already exists")

def get_captions_gpt4o(prompt, video_path, clip_length=20, interval=1):
    """Generate captions for video clips using GPT-4o
    
    Args:
        prompt (str): Prompt template for caption generation
        video_path (str): Path to video directory
        clip_length (int): Length of each video clip in seconds
        interval (int): Interval between frames in seconds
        
    Returns:
        list: Generated captions with timestamps
    """
    video_file = os.path.join(video_path, 'video.mp4')
    if not os.path.exists(video_file):
        raise FileNotFoundError(f"Video file not found: {video_file}")
        
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        raise RuntimeError(f"Failed to open video file: {video_file}")
        
    rate = cap.get(5)
    frame_num = cap.get(7)
    tot_time = int(frame_num / rate)
    model_outputs = list()
    start_times = []
    for m in range(tot_time // 60 + 1):
        base_time = m * 60
        start_times.append(base_time)
        start_times.append(base_time + 20)
        start_times.append(base_time + 40)
    start_times = [t for t in start_times if t < tot_time]
    if len(start_times) < 5:
        raise ValueError("The video is too short to generate 5 captions.")
    selected_times = [start_times[0]]
    step = (len(start_times) - 2) // 4
    for i in range(1, 4):
        selected_times.append(start_times[i * step + i])
    selected_times.append(start_times[-1])
    for i in tqdm.tqdm(range(0, len(start_times))):
        if start_times[i] in selected_times:
            time_prompt = 'Now, the time range corresponding the following video frames is:'
            time_prompt += f'[{datetime.timedelta(seconds=start_times[i])} - {datetime.timedelta(seconds=min(start_times[i] + clip_length, tot_time))}]' + '\n'
            model_input = [{'type': 'text', 'text': prompt + '\n' + time_prompt}]
            end_time = min(start_times[i] + clip_length, tot_time)
            for j in range(start_times[i], end_time, interval):
                cur_time = str(datetime.timedelta(seconds=j)).replace(':', '-')
                image_path = os.path.join(video_path, 'images', f'time_{cur_time}.jpg')
                if not os.path.exists(image_path):
                    raise FileNotFoundError(f"Image file not found: {image_path}")
                base64_image = encode_image(image_path)
                model_input.append({
                    'type': 'image_url',
                    'image_url': {'url': f"data:image/jpeg;base64,{base64_image}", 'detail': 'low'},
                })
            model_output = get_response(model_input)
            model_outputs.append(
                f'[{datetime.timedelta(seconds=start_times[i])} - {datetime.timedelta(seconds=min(start_times[i] + clip_length, tot_time))}] {model_output.strip()}')
        else:
            model_outputs.append(
                f'[{datetime.timedelta(seconds=start_times[i])} - {datetime.timedelta(seconds=min(start_times[i] + clip_length, tot_time))}]')
    return model_outputs

def generate_sparse_captions(video_path, prompt, clip_length=20, interval=1):
    """Generate sparse captions for a video
    
    Args:
        video_path (str): Path to video directory
        prompt (str): Prompt template for caption generation
        clip_length (int): Length of each video clip in seconds
        interval (int): Interval between frames in seconds
    """
    if not os.path.exists(os.path.join(video_path, 'captions.json')):
        captions = list()
        video_to_images(video_path)
        captions.append({'captions': get_captions_gpt4o(prompt, video_path, clip_length, interval), 'from': 'gpt4o'})
        with open(os.path.join(video_path, 'captions.json'), 'w') as fp:
            json.dump(captions, fp, indent=4, ensure_ascii=False)
    else:
        print('captions.json already exists.')

def video_duration(dir_name):
    """Calculate total duration of videos in directory
    
    Args:
        dir_name (str): Directory containing video files
        
    Returns:
        float: Total duration in seconds
    """
    sum_duration = 0
    for root, dirs, files in os.walk(dir_name, topdown=False):
        for filename in files:
            video_path = os.path.join(dir_name, filename)
            cap = cv2.VideoCapture(video_path)
            if cap.isOpened():
                rate = cap.get(5)
                frame_num = cap.get(7)
                duration = frame_num / rate
                sum_duration += duration
                cap.release()
    return sum_duration