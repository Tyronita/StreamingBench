# StreamingBench: Assessing the Gap for MLLMs to Achieve Streaming Video Understanding

<div align="center">
  <img src="./figs/icon.png" width="100%" alt="StreamingBench Banner">

  <div style="margin: 30px 0">
    <a href="https://streamingbench.github.io/" style="margin: 0 10px">🏠 Project Page</a> |
    <a href="https://arxiv.org/pdf/ICLR_2025" style="margin: 0 10px">📄 arXiv Paper</a> |
    <a href="https://huggingface.co/datasets/mjuicem/StreamingBench" style="margin: 0 10px">📦 Dataset</a> |
    <a href="https://streamingbench.github.io/home_page.html#leaderboard" style="margin: 0 10px">🏅Leaderboard</a>
  </div>
</div>

**StreamingBench** evaluates **Multimodal Large Language Models (MLLMs)** in real-time, streaming video understanding tasks. 🌟

## 👀 StreamingBench Overview

As MLLMs continue to advance, they remain largely focused on offline video comprehension, where all frames are pre-loaded before making queries. However, this is far from the human ability to process and respond to video streams in real-time, capturing the dynamic nature of multimedia content. To bridge this gap, **StreamingBench** introduces the first comprehensive benchmark for streaming video understanding in MLLMs.

### Key Evaluation Aspects
- 🎯 **Real-time Visual Understanding**: Can the model process and respond to visual changes in real-time?
- 🔊 **Omni-source Understanding**: Does the model integrate visual and audio inputs synchronously as seen in live environments?
- 🎬 **Contextual Understanding**: Can the model maintain continuity in its responses based on historical interactions within the video?

### Dataset Statistics
- 📊 **900** diverse videos
- 📝 **4,500** human-annotated QA pairs
- ⏱️ Five questions per video at different timestamps
#### 🎬 Video Categories
<div align="center">
  <img src="./figs/StreamingBench_Video.png" width="80%" alt="Video Categories">
</div>

#### 🔍 Task Taxonomy
<div align="center">
  <img src="./figs/task_taxonomy.png" width="80%" alt="Task Taxonomy">
</div>

## 📐 Dataset Examples

<div align="center">
  <img src="./figs/example.gif" width="100%" alt="Dataset Example">
</div>

## 🔍 Dataset

**License**: [License information to be added]



## 🔮 Evaluation Pipeline





## ⚙️ Data Construction Pipeline

### Directory Structure
```
src/data_construction/
├── videos/                  # Input video files
│   ├── sample_1/
│   │   ├── video.mp4
│   │   ├── images/
│   │   ├── captions.json
│   │   └── questions.json
│   │   ...
├── run_pipeline.py         # Main pipeline script
├── config.py              # Configuration settings
├── captions/              # Caption generation modules
│   ├── dense_captions.py
│   └── sparse_captions.py
├── questions/            # Question generation module
│   └── give_questions.py
└── prompt/              # Prompt templates
    └── prompt.py
```

### Configure API settings in `config.py`:
```python
API_CONFIG = {
    'OPENAI_API_KEY': '',  # TODO: Add your OpenAI API key here
    'OPENAI_BASE_URL': '', # TODO: Add your OpenAI API base URL here
}
```

### Run the pipeline
```bash
python run_pipeline.py --sample_dir <sample_dir> --mode <processing_modes>
```
Available processing modes: 
- `dense`: Generate detailed captions for every segment of the video
- `sparse`: Generate captions for selected key segments only
- `questions`: Generate questions based on the captions

Example:
```bash
python run_pipeline.py --sample_dir sample_2 --mode dense questions
``` 

## 🖥️ Experimental Results


## 📝 Citation
