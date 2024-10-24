# StreamingBench: Assessing the Gap for MLLMs to Achieve Streaming Video Understanding

<p align="center">
    <img src="./images/icon.png" width="100%" height="100%">
</p>

<font size=7><div align='center'>[[🍎 Project Page](https://streamingbench.github.io/)] [[📖 arXiv Paper](https://arxiv.org/pdf/ICLR_2025)] [[📊 Dataset](https://huggingface.co/datasets/mjuicem/StreamingBench)][[🏆 Leaderboard](https://streamingbench.github.io/home_page.html#leaderboard)]</div></font>

**StreamingBench** evaluates **Multimodal Large Language Models (MLLMs)** in real-time, streaming video understanding tasks. 🌟

---

## 👀 StreamingBench Overview

As MLLMs continue to advance, they remain largely focused on offline video comprehension, where all frames are pre-loaded before making queries. However, this is far from the human ability to process and respond to video streams in real-time, capturing the dynamic nature of multimedia content. To bridge this gap, **StreamingBench** introduces the first comprehensive benchmark for streaming video understanding in MLLMs.

StreamingBench evaluates MLLMs across three core aspects:
- **Real-time Visual Understanding**: Can the model process and respond to visual changes in real-time?
- **Omni-source Understanding**: Does the model integrate visual and audio inputs synchronously as seen in live environments?
- **Contextual Understanding**: Can the model maintain continuity in its responses based on historical interactions within the video?

StreamingBench comprises **900 videos** across diverse categories with **4,300 human-annotated QA pairs**. Each video includes five questions presented at different timestamps to simulate continuous interactions during streaming scenarios.

<p align="center">
    <img src="./asset/sta.jpg" width="100%" height="100%">
</p>

---

## 📐 Dataset Examples

<p align="center">
    <img src="./asset/Highlights-2.png" width="100%" height="100%">
</p>

<div align='center'>
<details>
<summary>Click to expand more examples</summary>
<p align="center">
    <img src="./asset/Highlights-1.png" width="100%" height="100%">
    <img src="./asset/Highlights-3.png" width="100%" height="100%">
    <img src="./asset/Highlights-4.png" width="100%" height="100%">
</p>
</details>
</div>

---

## 🔍 Dataset

**License**:
