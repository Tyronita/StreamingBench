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



Here’s a revised version of your markdown for clarity and better guidance:

## 🔮 Evaluation Pipeline

### Requirements

- Python 3.x
- moviepy

### Data Preparation

1. **Download Dataset**: Retrieve all necessary files from the [StreamingBench Dataset](https://huggingface.co/datasets/mjuicem/StreamingBench).
   
2. **Decompress Files**: Extract the downloaded files and organize them in the `./data` directory as follows:

   ```
   StreamingBench/
   ├── data/
   │   ├── real/               # Unzip Real Time Visual Understanding_*.zip into this folder
   │   ├── omini/              # Unzip other .zip files into this folder
   │   ├── sqa/                # Unzip Sequential Question Answering_*.zip into this folder
   │   └── proactive/          # Unzip Proactive Output_*.zip into this folder
   ```

3. **Preprocess Data**: Run the following command to preprocess the data:

   ```bash
   bash scripts/preprocess.sh
   ```

### Model Preparation

Prepare your own model for evaluation by following the instructions provided [here](./docs/model_guide.md). This guide will help you set up and configure your model to ensure it is ready for testing against the dataset.


## 📝 Citation
