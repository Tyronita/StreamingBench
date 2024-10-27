import os
from moviepy.editor import VideoFileClip

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
    