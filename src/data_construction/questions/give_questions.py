# This file contains functions for generating questions from video captions using GPT-4o
# Author: Junming Lin
# Date: 2024-10-26
# Copyright (c) THUNLP, Tsinghua University. All rights reserved.
# See LICENSE file in the project root for license information.

import base64
import time, tqdm, re, os, json
from openai import OpenAI
from config import API_CONFIG

client = OpenAI(
    api_key=API_CONFIG['OPENAI_API_KEY'], 
    base_url=API_CONFIG['OPENAI_BASE_URL']
)

def get_response(prompt):
    """Get response from GPT-4 model with retry mechanism
    
    Args:
        prompt (str): Input prompt for the model
        
    Returns:
        str: Model's response text
    """
    for _ in range(20):
        try:
            response = client.chat.completions.create(
                model='gpt-4o',
                messages=[{
                    'role': 'user',
                    'content': prompt,
                }],
                max_tokens=1200,
            ).choices[0].message.content
            break
        except:
            time.sleep(5)
            continue
    return response


def encode_image(image_path):
    """Encode image file to base64 string
    
    Args:
        image_path (str): Path to image file
        
    Returns:
        str: Base64 encoded image string
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def get_captions(caption_raw, captions_per_group):
    """Process raw captions and group them
    
    Args:
        caption_raw (dict): Raw caption data
        captions_per_group (int): Number of captions per group
        
    Returns:
        list: Processed and grouped captions with timestamps
    """
    result = []
    caption_processed = []
    time_marks = []

    for item in caption_raw['captions']:
        if item.strip(): 
            caption_processed.append(re.sub('\n+', ' ', item))

    filtered_captions = [caption for caption in caption_processed if caption.count('[') > 1]
    for item in filtered_captions:
        matches = re.search(r'\[(\d:\d\d:\d\d) - (\d:\d\d:\d\d)\]', item)
        if matches:
            time_marks.append((matches[1], matches[2]))

    for i in tqdm.tqdm(range(0, len(filtered_captions), captions_per_group)):
        st, ed = time_marks[i][0], time_marks[min(i, len(time_marks) - 1)][1]
        result.append({
            'time': f'[{st} - {ed}]',
            'captions': '\n'.join(filtered_captions[i:i + captions_per_group])
        })

    for i in result:
        print(i)
    return result


def get_qa(questions_raw):
    """Parse raw question text into structured format
    
    Args:
        questions_raw (str): Raw question text
        
    Returns:
        list: Structured question data with options and answers
    """
    questions = []
    blocks = questions_raw.strip().split('\n\n')
    for block in blocks:
        lines = block.strip().split('\n')
        question_data = {}
        options = []
        for line in lines:
            if line.startswith("Task Type: ") or line.startswith("**Task Type: "):
                cleaned_line = line.replace("**", "").strip()
                question_data['task_type'] = cleaned_line[len("Task Type: "):].strip()
            elif line.startswith("Question: ") or line.startswith("**Question: "):
                cleaned_line = line.replace("**", "").strip()
                question_data['question'] = cleaned_line[len("Question: "):].strip()
            elif line.startswith("Time Stamp: ")or line.startswith("**Time Stamp: "):
                cleaned_line = line.replace("**", "").strip()
                question_data['time_stamp'] = cleaned_line[len("Time Stamp: "):].strip()
            elif line.startswith("A. ") or line.startswith("**A. "):
                cleaned_line = line.replace("**", "").strip()
                options.append(cleaned_line[len("A. "):].strip())
            elif line.startswith("B. ") or line.startswith("**B. "):
                cleaned_line = line.replace("**", "").strip()
                options.append(cleaned_line[len("B. "):].strip())
            elif line.startswith("C. ") or line.startswith("**C. "):
                cleaned_line = line.replace("**", "").strip()
                options.append(cleaned_line[len("C. "):].strip())
            elif line.startswith("D. ") or line.startswith("**D. "):
                cleaned_line = line.replace("**", "").strip()
                options.append(cleaned_line[len("D. "):].strip())
            elif line.startswith("Answer: ") or line.startswith("**Answer: "):
                cleaned_line = line.replace("**", "").strip()
                question_data['answer'] = cleaned_line[len("Answer: "):].strip()
        if 'task_type' in question_data and 'question' in question_data and 'time_stamp' in question_data and len(options) == 4:
            question_data['options'] = options
            questions.append(question_data)
    return questions


def get_questions(result, prompt_str, prompt_not_str):
    """Generate questions from caption groups
    
    Args:
        result (list): Grouped captions
        prompt_str (str): Initial prompt template
        prompt_not_str (str): Follow-up prompt template
        
    Returns:
        list: Generated questions for each caption group
    """
    previous_questions = list()
    output = []
    for i in tqdm.tqdm(range(len(result))):
        if i == 0:
            model_input = prompt_str
        else:
            model_input = prompt_not_str
        model_input += '\n' + result[i]['captions'] + '\n'
        model_output = get_response(model_input)
        print(model_output)
        question = get_qa(model_output)
        print(question)
        result[i]['questions'] = question
        previous_questions.extend(result[i]['questions'])
        output.append(result[i])
    return output


def run_give_questions(videos_path, captions_per_group, prompt_str, prompt_not_str):
    """Main function to generate questions from video captions
    
    Args:
        videos_path (str): Path to video directory
        captions_per_group (int): Number of captions to group together
        prompt_str (str): Initial prompt template
        prompt_not_str (str): Follow-up prompt template
    """
    # Determine input and output filenames based on the caption file type
    caption_files = ['captions.json', 'dense_captions.json']
    for caption_file in caption_files:
        if os.path.exists(os.path.join(videos_path, caption_file)):
            output_file = 'questions.json' if caption_file == 'captions.json' else 'dense_questions.json'
            
            with open(os.path.join(videos_path, caption_file), 'r') as fp:
                captions = json.load(fp)
            
            flat_questions = []
            print(f'\nGenerating questions and answers from {caption_file}:')
            groups = get_captions(captions[0], captions_per_group)
            questions = get_questions(groups, prompt_str, prompt_not_str)
            flat_questions.extend(questions)
            
            with open(os.path.join(videos_path, output_file), 'w') as fp:
                json.dump(flat_questions, fp, indent=4, ensure_ascii=False)
