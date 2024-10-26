# This file contains the main pipeline for processing educational videos through caption generation and question generation
# Author: Junming Lin
# Date: 2024-10-26
# Copyright (c) THUNLP, Tsinghua University. All rights reserved.
# See LICENSE file in the project root for license information.

import argparse
from captions.dense_captions import generate_dense_captions
from captions.sparse_captions import generate_sparse_captions
from questions.give_questions import run_give_questions
from prompt.prompt import PROMPT_DENSE_CAPTIONS, PROMPT_GENERAL_CAPTIONS, DIRECT_PROMPT_STR, DIRECT_PROMPT_NOT_STR
from config import VIDEO_CONFIG, PATH_CONFIG

def process_video(sample_dir, modes):
    """Process a single video through caption and question generation pipeline
    
    This function takes a video file and processes it through different modes including
    dense caption generation, sparse caption generation and question generation.
    The modes cannot include both dense and sparse captioning simultaneously.
    
    Args:
        sample_dir (str): Name of the sample_dir to process
        modes (list): List of processing modes to run ('dense', 'sparse', 'questions')
    
    Raises:
        ValueError: If both 'dense' and 'sparse' modes are specified
    """
    video_path = f"{PATH_CONFIG['VIDEO_DIR']}/{sample_dir}"

    if 'dense' in modes and 'sparse' in modes:
        raise ValueError("'dense' and 'sparse' modes cannot be used simultaneously")

    if 'dense' in modes:
        print("\nGenerating dense captions...")
        generate_dense_captions(
            video_path=video_path,
            prompt=PROMPT_DENSE_CAPTIONS
        )
    
    if 'sparse' in modes:
        print("\nGenerating sparse captions...")
        generate_sparse_captions(
            video_path=video_path,
            prompt=PROMPT_GENERAL_CAPTIONS,
            clip_length=VIDEO_CONFIG['CLIP_LENGTH'],
            interval=VIDEO_CONFIG['INTERVAL']
        )
    
    if 'questions' in modes:
        print("\nGenerating questions...")
        run_give_questions(
            videos_path=video_path,
            captions_per_group=VIDEO_CONFIG['CAPTIONS_PER_GROUP'],
            prompt_str=DIRECT_PROMPT_STR,
            prompt_not_str=DIRECT_PROMPT_NOT_STR
        )

def main():
    """Main entry point for the video processing pipeline
    
    Parses command line arguments to get video name and processing modes,
    then runs the processing pipeline on the specified video.
    """
    parser = argparse.ArgumentParser(description='Video Processing Pipeline')
    parser.add_argument('--sample_dir', required=True, help='Name of the video to process')
    parser.add_argument('--mode', nargs='+', 
                        choices=['dense', 'sparse', 'questions'],
                        default=['dense','questions'],
                        help='Processing modes (can specify multiple)')
    
    args = parser.parse_args()
    process_video(args.sample_dir, args.mode)

if __name__ == "__main__":
    main()