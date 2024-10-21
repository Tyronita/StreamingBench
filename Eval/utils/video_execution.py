import os
from moviepy.editor import VideoFileClip
import cv2
import base64

def split_video(video_file, timestamp):
    """
    Split video into prefix part based on timestamp.
    video_file: path to video file
    timestamps: list of timestamps in the format "00:03:10"
    """
    timestamp = sum(int(x) * 60 ** i for i, x in enumerate(reversed(timestamp.split(":"))))

    video_name = os.path.splitext(os.path.basename(video_file))[0]
    output_dir = os.path.join(os.path.dirname(video_file), "tmp")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_file = os.path.join(output_dir, f"{video_name}_{timestamp}.mp4")

    if os.path.exists(output_file):
        print(f"Video file {output_file} already exists.")
        return output_file

    video = VideoFileClip(video_file)
    clip = video.subclip(0, timestamp)
    
    clip.write_videofile(output_file)
    clip.close()
    video.close()
    print(f"Video: {output_file} splitting completed.")
    return output_file

def video_to_images(video_path, frame_num, timestamp):
    video = cv2.VideoCapture(video_path)
    
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    max_frames_to_extract = min(frame_num, int(timestamp))

    img_list = []

    for i in range(max_frames_to_extract):
        # 均匀计算要提取的帧的位置
        frame_index = int(i * (total_frames / max_frames_to_extract))
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

        success, img = video.read()
        if not success:
            break

        _, buffer = cv2.imencode(".jpg", img)
        img_list.append(base64.b64encode(buffer).decode("utf-8"))
    
    video.release()
    print(len(img_list))
    return img_list
    