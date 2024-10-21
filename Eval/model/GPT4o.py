from model.modelclass import Model
from utils.video_execution import video_to_images
from openai import OpenAI
import time
import base64
import os
FRAME_NUM = 48

# client = OpenAI(
#     api_key='sk-PMuFYQfYEay4oBglBeA8EcB121A9414dBf90Ab4591918c7d',
#     base_url='https://yeysai.com/v1/'
# )

client = OpenAI(
    api_key='sk-UOArhyzuKw4Xaiga3e40F22502B44a6c93CaAaC336A3A1F1',
    base_url='http://15.204.101.64:4000/v1/'
)

# os.environ['OPENAI_API_KEY'] = GPT_API_KEY
# os.environ['OPENAI_BASE_URL'] = GPT_BASE_URL
# model_openai = openai.OpenAI()

class GPT4o(Model):
    def __init__(self):
        """
        Initialize the model
        """
        pass

    def Run(self, file, inp, timestamp):
        return GPT4o_Run(file, inp, timestamp)
    
    def name(self):
        return "GPT4o"

def get_response(query, model_type):
    response = ''
    try:
        if model_type == 'GPT4O':

            response = client.chat.completions.create(
                model = 'gpt-4o',
                messages = [
                    {
                        'role': 'user',
                        'content': query
                }]
            )
            response = response.choices[0].message.content
    except Exception as e:
        print(e)
        time.sleep(5)
    return response

def GPT4o_Run(file, inp, timestamp):
    # extract frame num from file's name '...output_{frame_num}.mp4'
    if file.endswith('.mp4'):
        frame_num = timestamp
        if frame_num > FRAME_NUM:
            frame_num = FRAME_NUM

        base64Frames = video_to_images(file, frame_num, timestamp)
        print("Encode finished!")

        model_input = [
            {"type": "text", "text": inp},
            *map(
                lambda x: {"type": "image_url", "image_url": {"url": f"data:image/jpg;base64,{x}"}},
                base64Frames,
            )
        ]
    elif file.endswith('.jpg'):
        with open(file, "rb") as image_file:
            x = base64.b64encode(image_file.read()).decode("utf-8")
        model_input = [
            {"type": "text", "text": inp},
            {"type": "image_url", "image_url": {"url": f"data:image/jpg;base64,{x}"}}
        ]
    else:
        model_input = [
            {"type": "text", "text": inp}
        ]
        for img in os.listdir(file):
            with open(os.path.join(file, img), "rb") as image_file:
                x = base64.b64encode(image_file.read()).decode("utf-8")
                model_input.append({"type": "image_url", "image_url": {"url": f"data:image/jpg;base64,{x}"}})
    # for x in base64Frames:
    #     model_input.append({'type': 'image_url', 'image_url': {'url': f'data:image/jpg;base64,{x}'}})

    # model_input.append({'type': 'text', 'text': inp})

    # for i in range(frame_num):
    #     model_input.append({'type': 'image_url', 'image_url': {'url': f'https://raw.githubusercontent.com/resi1ience/gpt_upload_two/main/{video_name}_{file_name}/frame_{i}.jpg'}})
    # print(model_input)
    response = get_response(model_input, 'GPT4O')

    print(response)

    return response

# prompt = """You are an advanced video question-answering AI assistant. You have been provided with the video and a multiple-choice question related to the video. Your task is to carefully analyze the video and provide the best answer to question, choosing from the four options provided. Respond with only the letter (A, B, C, or D) of the correct option.

# Question: What did the person do just now?

# Options:
# A. Presented a respiratory mask from various angles.
# B. Directed a heat tool at a canvas.
# C. Disassembled the resin kit.
# D. Held and examined two round items.
# """
# # GPT4o_Run("/data1/private/fz/streaming/gpt_upload/0814/sample_428_83", prompt)
# GPT4o_Run("/data1/private/fz/streaming/Eval/data/videos/sample_62_143/output.mp4", prompt)