# This file contains configuration settings for the video processing application
# Author: Junming Lin
# Date: 2024-10-26
# Copyright (c) THUNLP, Tsinghua University. All rights reserved.
# See LICENSE file in the project root for license information.

import os

# Configuration for OpenAI API integration
# Contains API key, base URL and model name settings
# TODO: Fill in your OpenAI API key and base URL before running
API_CONFIG = {
    'OPENAI_API_KEY': '',  # TODO: Add your OpenAI API key here
    'OPENAI_BASE_URL': '', # TODO: Add your OpenAI API base URL here
    'MODEL_NAME': 'gpt-4o'
}

# Settings for video processing operations
# Defines clip length, processing interval and caption grouping
VIDEO_CONFIG = {
    'CLIP_LENGTH': 20,  # Duration of each video clip in seconds
    'INTERVAL': 1,      # Time interval between processing steps
    'CAPTIONS_PER_GROUP': 1  # Number of captions to group together
}

# Directory path configurations
# Specifies locations for input videos and processed outputs
PATH_CONFIG = {
    'VIDEO_DIR': os.path.join(os.path.dirname(__file__), 'videos'),
    'OUTPUT_DIR': os.path.join(os.path.dirname(__file__), 'videos')
}

# Subject matter configuration for content processing
SUBJECT = "Mathematics Teaching"

# Create necessary directories if they don't exist
for dir_path in PATH_CONFIG.values():
    os.makedirs(dir_path, exist_ok=True)