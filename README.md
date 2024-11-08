<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="description"
        content="Assessing the Gap for MLLMs to Achieve Streaming Video Understanding">
  <meta name="keywords" content="StreamingBench">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title> StreamingBench</title>



  <link rel="icon" href="./static/images/StreamingBench.png">

  <link href="https://fonts.googleapis.com/css?family=Google+Sans|Noto+Sans|Castoro" rel="stylesheet">

  <link rel="stylesheet" href="./static/css/bulma.min.css">
  <link rel="stylesheet" href="./static/css/bulma-carousel.min.css">
  <link rel="stylesheet" href="./static/css/bulma-slider.min.css">
  <link rel="stylesheet" href="./static/css/fontawesome.all.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css">
  <link rel="stylesheet" href="./static/css/index.css">
  <link rel="stylesheet" href="./static/css/leaderboard.css">

  <!-- <link href="https://unpkg.com/tabulator-tables@5.5.2/dist/css/tabulator_bulma.min.css" rel="stylesheet">
  <script type="text/javascript" src="https://unpkg.com/tabulator-tables@5.5.2/dist/js/tabulator.min.js"></script> -->
  <script type="text/javascript" src="static/js/sort-table.js" defer></script>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script defer src="./static/js/fontawesome.all.min.js"></script>
  <script src="./static/js/bulma-carousel.min.js"></script>
  <script src="./static/js/bulma-slider.min.js"></script>
  <script src="./static/js/explorer-index.js"></script>
  <script src="./static/js/question_card.js"></script>

  <script src="./static/js/leaderboard_testmini.js"></script>  
  <script src="./data/results/output_folders.js" defer></script>
  <script src="./data/results/model_scores.js" defer></script>

  <script src="./visualizer/data/data_public.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
<!-- 
<nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>
  <div class="navbar-menu">
    <div class="navbar-start" style="flex-grow: 1; justify-content: center;">
      <div class="navbar-item has-dropdown is-hoverable">
        <div class="navbar-dropdown">
          <a class="navbar-item" href=" ">
            <b>StreamingBench (V2)</b> <p style="font-size:18px; display: inline; margin-left: 5px;">🔥</p>
          </a>
          <a class="navbar-item" href=" ">
            <b>StreamingBench (V3)</b> <p style="font-size:18px; display: inline; margin-left: 5px;">🔥</p>
          </a>
        </div>
      </div>
    </div>

  </div>
</nav> -->


<section class="hero">
  <div class="hero-body">
    <div class="container is-max-desktop">
      <div class="columns is-centered">
        <div class="column has-text-centered">
          <h1 class="title is-1 publication-title is-bold">
            <img src="./static/images/StreamingBench.png" style="width:2em;vertical-align: middle" alt="Logo"/>
            <span class="StreamingBench" style="font-family: 'CustomFont', sans-serif;">StreamingBench</span>
            </h1>
          <h2 class="subtitle is-3 publication-subtitle">
            Assessing the Gap for MLLMs to Achieve Streaming Video Understanding
            <!-- <br> -->
            <!-- with GPT-4V, Bard, and Other Large Multimodal Models -->
          </h2>
          <div class="is-size-5 publication-authors">
            <span class="author-block">
              <a href="https://openreview.net/profile?id=~Junming_Lin1">Junming Lin</a><sup style="color:#ed4b82;">2</sup>,</span>
            <span class="author-block">
              <a href="https://openreview.net/profile?id=~Zheng_Fang14">Zheng Fang</a><sup style="color:#6fbf73;">1</sup>,</span>
            <span class="author-block">
              <a href="https://openreview.net/profile?id=~Chi_Chen1">Chi Chen</a><sup style="color:#6fbf73">1</sup>,
            </span>
            <span class="author-block">
              <a href="https://openreview.net/profile?id=~Zihao_Wan2">Zihao Wan</a><sup style="color:#6fbf73;">1</sup>,
            </span>
            <span class="author-block">
              <a href="https://openreview.net/profile?id=~Fuwen_Luo1">Fuwen Luo</a><sup style="color:#6fbf73">1</sup>,
            </span>
        
            <span class="author-block">
              <a href="https://openreview.net/profile?id=~Peng_Li2">Peng Li</a><sup style="color:#6fbf73">1</sup>,
            </span>
            <span class="author-block">
              <a href="https://openreview.net/profile?id=~Yang_Liu19">Yang Liu</a><sup style="color:#6fbf73">1</sup>,
            </span>
            <span class="author-block">
              <a href="https://openreview.net/profile?id=~Maosong_Sun1">Maosong Sun</a><sup style="color:#6fbf73;">1</sup>,
            </span>
          </div>

          <div class="is-size-5 publication-authors">
            <span class="author-block"><sup style="color:#6fbf73;">1</sup>Tsinghua University</span><br>
            <span class="author-block"><sup style="color:#ed4b82">2</sup>Beijing University of Posts and Telecommunications</span><br>
          </div>

          <div class="column has-text-centered">
            <div class="publication-links">
              <!-- PDF Link. -->
              <span class="link-block">
                <a href="https://arxiv.org/abs/2411.03628"
                   class="external-link button is-normal is-rounded is-dark">
                  <span class="icon">
                      <i class="ai ai-arxiv"></i>
                  </span>
                  <span>arXiv</span>
                </a>
              </span>
              <!-- Code Link. -->
              <span class="link-block">
                <a href="https://github.com/THUNLP-MT/StreamingBench"
                   class="external-link button is-normal is-rounded is-dark">
                  <span class="icon">
                      <i class="fab fa-github"></i>
                  </span>
                  <span>Code</span>
                  </a>
              </span>
              <!-- Dataset Link. -->
              <span class="link-block">
                <a href="https://huggingface.co/datasets/mjuicem/StreamingBench"
                   class="external-link button is-normal is-rounded is-dark">
                  <span class="icon">
                      <!-- <i class="far fa-images"></i> -->
                      <p style="font-size:18px">📊</p>
                  </span>
                  <span>Dataset</span>
                </a>
              </span> 
              <!-- Leaderboard Link. -->
              <span class="link-block">
                <a href="#leaderboard"
                   class="external-link button is-normal is-rounded is-dark">
                  <span class="icon">
                      <p style="font-size:18px">🏆</p>
                  </span>
                  <span>Leaderboard</span>
                </a>
              </span>

            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- <section class="hero teaser">
  <div class="container is-max-desktop">
    <div class="content has-text-centered">
      <img src="static/images/tease_scores_gpt4v.png" alt="geometric reasoning" width="99%"/>
      <p> Accuracy scores of one leading LLM (i.e., PoT GPT-4), four primary LMMs, random chance, and human performance our proposed 
      <img src="static/images/mathvista.png" style="width:1.0em;vertical-align: middle" alt="Logo"/>
      <span class="mathvista">MathVista</span>
      across mathematical reasoning and visual context types. PoT refers to program-of-thought prompting, and PoT GPT-4 is a textual LLM augmented with the caption and OCR text. GPT-4V is manually evaluated via the playground chatbot.
      </p>
    </div>
  </div>
</section> -->


<section class="section">
  <div class="container" style="margin-top: -150px; margin-bottom: -100px;">
    <div class="columns is-centered m-6">
      <div class="column is-full has-text-centered content">
        <div id="results-carousel" class="carousel results-carousel">
          <div class="box m-5">
            <div class="content has-text-centered">
              <video autoplay loop muted playsinline width="100%">
                <source src="static/images/sv.mp4" type="video/mp4">
                Your browser does not support the video tag.
              </video>
              </p>
            </div>
          </div>
          <div class="box m-5">
            <div class="content has-text-centered">
              <img src="static/images/question_sample_2.png" alt="geometric reasoning" width="84%"/>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
</section>


<section class="section">
  <div class="container" style="margin-bottom: 2vh;">
    <!-- Abstract. -->
    <div class="columns is-centered has-text-centered">
      <div class="column is-four-fifths">
        <h2 class="title is-3">Introduction</h2>
        <div class="content has-text-justified">
          <p>
            The rapid development of Multimodal Large Language Models (MLLMs) has expanded their capabilities from image comprehension to video understanding. However, most of these MLLMs focus primarily on offline video comprehension, necessitating extensive processing of all video frames before any queries can be made. This presents a significant gap compared to the human ability to watch, listen, think, and respond to streaming inputs in real time, highlighting the limitations of current MLLMs. In this paper, we introduce <strong>StreamingBench</strong>, the first comprehensive benchmark designed to evaluate the streaming video understanding capabilities of MLLMs.
            StreamingBench assesses three core aspects of streaming video understanding:
<strong>real-time visual understanding</strong>, <strong>omni-source understanding</strong>, and <strong>contextual understanding</strong>.
            The benchmark consists of 18 tasks, featuring 900 videos and 4,500 human-curated QA pairs. Each video features five questions presented at different time points to simulate a continuous streaming scenario. We conduct experiments on StreamingBench with 13 open-source and proprietary MLLMs and find that even the most advanced proprietary MLLMs like Gemini 1.5 Pro and GPT-4o perform significantly below human-level streaming video understanding capabilities. We hope our work can facilitate further advancements for MLLMs, empowering them to approach human-level video comprehension and interaction in more realistic scenarios.
          </p>
        </div>
      </div>
    </div>
    <!--/ Abstract. -->
</div>
</section>

<audio controls style="display: block; margin: 0 auto; width: 40%;">
  <source src="StreamingBench.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>
<p style="text-align: center; font-style: italic;">* This audio was generated by NoteBookLM</p>


<section class="section">
  <div class="container">
    
    <div class="columns is-centered">
      <div class="column is-full has-text-centered content">

        <h2 class="title is-3" id="leaderboard">Leaderboard</h2>
        <div class="content">

          <div class="table-container" id="tablePage1">
            <table class="js-sort-table" id="results" style="margin-left: auto; margin-right: auto;">
              <thead>
                <tr>
                  <th rowspan="1" class="no-sort" style="vertical-align: middle; width: 50px;" data-js-sort-colNum="none"><strong>Rank</strong></th>
                  <th rowspan="1" class="no-sort" style="vertical-align: middle; width: 180px;" data-js-sort-colNum="none"><strong>Model</strong></th>
                  <th rowspan="1" class="no-sort" style="vertical-align: middle; width: 50px;" data-js-sort-colNum="none"><strong>LLM <br>Params</strong></th>
                  <th rowspan="1" class="no-sort" style="vertical-align: middle; width: 100px;" data-js-sort-colNum="none"><strong>Frames</strong></th>
                  <th rowspan="1" class="no-sort" style="vertical-align: middle; width: 110px;" data-js-sort-colNum="none"><strong>Date</strong></th>
                  <th rowspan="1" class="no-sort" style="vertical-align: middle; width: 110px;" data-js-sort-colNum="none"><strong>Overall (%)</strong></th>
                  <th rowspan="1" class="no-sort" style="vertical-align: middle; width: 110px;" data-js-sort-colNum="none"><strong>Real-Time Visual Understanding (%)</strong></th>
                  <th rowspan="1" class="no-sort" style="vertical-align: middle; width: 110px;" data-js-sort-colNum="none"><strong>Omni-Source Understanding (%)</strong></th>
                  <th rowspan="1" class="no-sort" style="vertical-align: middle; width: 110px;" data-js-sort-colNum="none"><strong>Contextual Understanding (%)</strong></th>


                </tr>
              </thead>
              <tbody>

                <tr>
                  <td style="vertical-align: middle;">
                    <span class="icon" style="color: gold;">
                      <i class="fas fa-medal"></i>
                    </span>
                  </td>
                  <td style="text-align: left; padding: 2px 10px;">
                    <b class="">
                      <a href="https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf" class="ext-link" style="font-size: 16px; margin-left: 5px;">Gemini 1.5 Pro</a>
                      <p style="font-size: 12px; margin-left: 5px; color: #858383;">Google</p>
                    </b>
                  </td>
                  <td style="vertical-align: middle;">- </td>
                  <td style="vertical-align: middle;">Video</td>
                  <td style="vertical-align: middle;">2024-06-15</td>
                  <td style="vertical-align: middle;"><b class="">66.91</b></td>
                  <td style="vertical-align: middle;">75.69</td>
                  <td style="vertical-align: middle;">60.22</td>
                  <td style="vertical-align: middle;">47.86</td>
                                
                </tr>
                <tr>
                  <td style="vertical-align: middle;"></td>
                  <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://huggingface.co/spaces/Qwen/Qwen2-VL" class="ext-link" style="font-size: 16px; margin-left: 5px;">Qwen2-VL
                    <p style="font-size: 12px; margin-left: 5px; color: #858383;">Alibaba</p>
                  </a></b></td>
                  <td style="vertical-align: middle;">7B </td>
                  <td style="vertical-align: middle;">768 </td>
                  <td style="vertical-align: middle;">2024-08-19</td>
                  <td style="vertical-align: middle;"><b class="">54.14</b></td>
                  <td style="vertical-align: middle;">69.04</td>
                  <td style="vertical-align: middle;">34.90</td>
                  <td style="vertical-align: middle;">31.66</td>
                </tr>
                <tr>
                  <td style="vertical-align: middle;">
                    <span class="icon" style="color: silver;">
                      <i class="fas fa-medal"></i>
                    </span>
                  </td>
                  <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://openai.com/index/hello-gpt-4o/" class="ext-link" style="font-size: 16px; margin-left: 5px;">GPT-4o
                    <p style="font-size: 12px; margin-left: 5px; color: #858383;">OpenAI</p>
                  </a></b></td>
                  <td style="vertical-align: middle;">- </td>
                  <td style="vertical-align: middle;">32</td>
                  <td style="vertical-align: middle;">2024-06-15</td>
                  <td style="vertical-align: middle;"><b class="">60.15</b></td>
                  <td style="vertical-align: middle;">73.28</td>
                  <td style="vertical-align: middle;">44.50</td>
                  <td style="vertical-align: middle;">38.70</td>
                </tr>
                <tr>
                  <td style="vertical-align: middle;"></td>
                  <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://huggingface.co/lmms-lab/LLaVA-NeXT-Video-72B-Qwen2" class="ext-link" style="font-size: 16px; margin-left: 5px;">LLaVA-NeXT-Video
                    <p style="font-size: 12px; margin-left: 5px; color: #858383;">Bytedance & NTU S-Lab</p>
                  </a></b></td>
                  <td style="vertical-align: middle;">32B</td>
                  <td style="vertical-align: middle;">64 </td>
                  <td style="vertical-align: middle;">2024-05-10</td>
                  <td style="vertical-align: middle;"><strong>52.77</strong></td>
                  <td style="vertical-align: middle;">66.96</td>
                  <td style="vertical-align: middle;">34.90</td>
                  <td style="vertical-align: middle;">30.79</td>
                </tr>
                <tr>
                  <td style="vertical-align: middle;"></td>
                  <td style="text-align: left; padding: 2px 10px;">
                    <b class="">
                      <a href="https://arxiv.org/pdf/2408.03326" class="ext-link" style="font-size: 16px; margin-left: 5px;">LLaVA-OneVision</a>
                      <p style="font-size: 12px; margin-left: 5px; color: #858383;">Bytedance & NTU S-Lab</p>
                    </b>
                  </td>
                  <td style="vertical-align: middle;">7B </td>
                  <td style="vertical-align: middle;">32 </td>
                  <td style="vertical-align: middle;">2024-08-08</td>
                  <td style="vertical-align: middle;"><b class="">56.36</b></td>
                  <td style="vertical-align: middle;">71.12</td>
                  <td style="vertical-align: middle;">38.40</td>
                  <td style="vertical-align: middle;">32.74</td>
                </tr>
                <tr>
                  <td style="vertical-align: middle;"></td>
                  <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/DAMO-NLP-SG/VideoLLaMA2" class="ext-link" style="font-size: 16px; margin-left: 5px;">VideoLLaMA 2
                    <p style="font-size: 12px; margin-left: 5px; color: #858383;">Alibaba</p>
                  </a></b></td>
                  <td style="vertical-align: middle;">7B</td>
                  <td style="vertical-align: middle;">32 </td>
                  <td style="vertical-align: middle;">2024-08-29</td>
                  <td style="vertical-align: middle;"><strong>40.40</strong></td>
                  <td style="vertical-align: middle;">49.52</td>
                  <td style="vertical-align: middle;">32.40</td>
                  <td style="vertical-align: middle;">21.93</td>
                </tr>
                <tr>
                  <td style="vertical-align: middle;"></td>
                  <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/NVlabs/VILA" class="ext-link" style="font-size: 16px; margin-left: 5px;">VILA-1.5
                    <p style="font-size: 12px; margin-left: 5px; color: #858383;">NVIDIA & MIT</p>
                  </a> </b></td>
                  <td style="vertical-align: middle;">8B </td>
                  <td style="vertical-align: middle;">14 </td>
                  <td style="vertical-align: middle;">2024-07-21</td>
                  <td style="vertical-align: middle;"><b class="">43.20</b></td>
                  <td style="vertical-align: middle;">52.32</td>
                  <td style="vertical-align: middle;">33.10</td>
                  <td style="vertical-align: middle;">27.35</td>
                </tr>
                <tr>
                  <td style="vertical-align: middle;"></td>
                  <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/OpenBMB/MiniCPM-V" class="ext-link" style="font-size: 16px; margin-left: 5px;">MiniCPM-V 2.6
                    <p style="font-size: 12px; margin-left: 5px; color: #858383;">OpenBMB</p>
                  </a> </b></td>
                  <td style="vertical-align: middle;">8B </td>
                  <td style="vertical-align: middle;">64 </td>
                  <td style="vertical-align: middle;">2024-08-12</td>
                  <td style="vertical-align: middle;"><b class="">53.85</b></td>
                  <td style="vertical-align: middle;">67.44</td>
                  <td style="vertical-align: middle;">35.00</td>
                  <td style="vertical-align: middle;">34.97</td>
                </tr>
                <tr>
                  <td style="vertical-align: middle;">
                    <span class="icon" style="color: #cd7f32;">
                      <i class="fas fa-medal"></i>
                    </span>
                  </td>
                  <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://www.anthropic.com/news/claude-3-5-sonnet" class="ext-link" style="font-size: 16px; margin-left: 5px;">Claude 3.5 Sonnet
                    <p style="font-size: 12px; margin-left: 5px; color: #858383;">Anthropic</p>
                  </a></b></td>
                  <td style="vertical-align: middle;">- </td>
                  <td style="vertical-align: middle;">20 </td>
                  <td style="vertical-align: middle;">2024-07-30</td>
                  <td style="vertical-align: middle;"><strong>57.68</strong></td>
                  <td style="vertical-align: middle;">72.44</td>
                  <td style="vertical-align: middle;">36.80</td>
                  <td style="vertical-align: middle;">37.70</td>
                </tr>
                <tr>
                  <td style="vertical-align: middle;"></td>
                  <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/OpenGVLab/InternVL" class="ext-link" style="font-size: 16px; margin-left: 5px;">InternVL2
                    <p style="font-size: 12px; margin-left: 5px; color: #858383;">Shanghai AI Lab</p>
                  </a></b></td>
                  <td style="vertical-align: middle;">8B</td>
                  <td style="vertical-align: middle;">16 </td>
                  <td style="vertical-align: middle;">2024-07-18</td>
                  <td style="vertical-align: middle;"><strong>51.40</strong></td>
                  <td style="vertical-align: middle;">63.72</td>
                  <td style="vertical-align: middle;">35.80</td>
                  <td style="vertical-align: middle;">32.42</td>
                </tr>
                <tr>
                  <td style="vertical-align: middle;"></td>
                  <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/KangarooGroup/Kangaroo" class="ext-link" style="font-size: 16px; margin-left: 5px;">Kangaroo
                    <p style="font-size: 12px; margin-left: 5px; color: #858383;">Meituan & UCAS</p>
                  </a></b></td>
                  <td style="vertical-align: middle;">8B</td>
                  <td style="vertical-align: middle;">64 </td>
                  <td style="vertical-align: middle;">2024-07-23</td>
                  <td style="vertical-align: middle;"><strong>51.10</strong></td>
                  <td style="vertical-align: middle;">64.60</td>
                  <td style="vertical-align: middle;">34.20</td>
                  <td style="vertical-align: middle;">30.06</td>
                </tr>
            
                <tr>
                  <td style="vertical-align: middle;"></td>
                  <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/QQ-MM/Video-CCAM" class="ext-link" style="font-size: 16px; margin-left: 5px;">Video-CCAM
                    <p style="font-size: 12px; margin-left: 5px; color: #858383;">QQMM</p>
                  </a></b></td>
                  <td style="vertical-align: middle;">14B</td>
                  <td style="vertical-align: middle;">96 </td>
                  <td style="vertical-align: middle;">2024-07-16</td>
                  <td style="vertical-align: middle;"><strong>42.53</strong></td>
                  <td style="vertical-align: middle;">53.96</td>
                  <td style="vertical-align: middle;">29.70</td>
                  <td style="vertical-align: middle;">22.88</td>
                </tr>
                <tr>
                  <td style="vertical-align: middle;"></td>
                  <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/EvolvingLMMs-Lab/LongVA" class="ext-link" style="font-size: 16px; margin-left: 5px;">LongVA
                    <p style="font-size: 12px; margin-left: 5px; color: #858383;">NTU S-Lab</p>
                  </a></b></td>
                  <td style="vertical-align: middle;">7B</td>
                  <td style="vertical-align: middle;">128 </td>
                  <td style="vertical-align: middle;">2024-06-25</td>
                  <td style="vertical-align: middle;"><strong>48.66</strong></td>
                  <td style="vertical-align: middle;">59.96</td>
                  <td style="vertical-align: middle;">35.40</td>
                  <td style="vertical-align: middle;">29.95</td>
                </tr>
            </tbody>                                                   
          </table> 
        </div>

        <div class="table-container" id="tablePage2" style="display: none;">
          <table class="js-sort-table" id="results2" style="margin-left: auto; margin-right: auto;">
            <thead>
              <tr>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 50px;" data-js-sort-colNum="none"><strong>Rank</strong></th>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 180px;" data-js-sort-colNum="none"><strong>Model</strong></th>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 50px;" data-js-sort-colNum="none"><strong>LLM <br>Params</strong></th>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 100px;" data-js-sort-colNum="none"><strong>Frames</strong></th>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 110px;" data-js-sort-colNum="none"><strong>Date</strong></th>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 110px;" data-js-sort-colNum="none"><strong>Overall (%)</strong></th>
                <th colspan="10" class="no-sort" style="vertical-align: middle; width: 110px;" data-js-sort-colNum="none"><strong>Real-Time Visual Understanding (%)</strong></th>
              </tr>
              <tr>
                <th data-js-sort-colNum="6"><strong>OP</strong></th>
                <th data-js-sort-colNum="7"><strong>CR</strong></th>
                <th data-js-sort-colNum="8"><strong>CS</strong></th>
                <th data-js-sort-colNum="9"><strong>ATP</strong></th>
                <th data-js-sort-colNum="10"><strong>EU</strong></th>
                <th data-js-sort-colNum="11"><strong>TR</strong></th>
                <th data-js-sort-colNum="12"><strong>PR</strong></th>
                <th data-js-sort-colNum="13"><strong>SU</strong></th>
                <th data-js-sort-colNum="14"><strong>ACP</strong></th>
                <th data-js-sort-colNum="15"><strong>CT</strong></th>
              </tr>
            </thead>
            <tbody>

              <tr>
                <td style="vertical-align: middle;">
                  <span class="icon" style="color: gold;">
                    <i class="fas fa-medal"></i>
                  </span>
                </td>
                <td style="text-align: left; padding: 2px 10px;">
                  <b class="">
                    <a href="https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf" class="ext-link" style="font-size: 16px; margin-left: 5px;">Gemini 1.5 Pro</a>
                    <p style="font-size: 12px; margin-left: 5px; color: #858383;">Google</p>
                  </b>
                </td>
                <td style="vertical-align: middle;">- </td>
                <td style="vertical-align: middle;">1 fps</td>
                <td style="vertical-align: middle;">2024-06-15</td>
                <td style="vertical-align: middle;"><b class="">75.69</b></td>
                <td style="vertical-align: middle;">79.02</td>
                <td style="vertical-align: middle;">80.47</td>
                <td style="vertical-align: middle;">83.54</td>
                <td style="vertical-align: middle;">79.67</td>
                <td style="vertical-align: middle;">80.00</td>
                <td style="vertical-align: middle;">84.74</td>
                <td style="vertical-align: middle;">77.78</td>
                <td style="vertical-align: middle;">64.23</td>
                <td style="vertical-align: middle;">71.95</td>
                <td style="vertical-align: middle;">48.70</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://huggingface.co/spaces/Qwen/Qwen2-VL" class="ext-link" style="font-size: 16px; margin-left: 5px;">Qwen2-VL
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Alibaba</p>
                </a></b></td>
                <td style="vertical-align: middle;">7B </td>
                <td style="vertical-align: middle;">0.2-1 fps </td>
                <td style="vertical-align: middle;">2024-08-19</td>
                <td style="vertical-align: middle;"><b class="">69.04</b></td>
                <td style="vertical-align: middle;">75.20</td>
                <td style="vertical-align: middle;">82.81</td>
                <td style="vertical-align: middle;">73.19</td>
                <td style="vertical-align: middle;">77.45</td>
                <td style="vertical-align: middle;">68.32</td>
                <td style="vertical-align: middle;">71.03</td>
                <td style="vertical-align: middle;">72.22</td>
                <td style="vertical-align: middle;">61.19</td>
                <td style="vertical-align: middle;">61.47</td>
                <td style="vertical-align: middle;">46.11</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;">
                  <span class="icon" style="color: silver;">
                    <i class="fas fa-medal"></i>
                  </span>
                </td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://openai.com/index/hello-gpt-4o/" class="ext-link" style="font-size: 16px; margin-left: 5px;">GPT-4o
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">OpenAI</p>
                </a></b></td>
                <td style="vertical-align: middle;">- </td>
                <td style="vertical-align: middle;">64</td>
                <td style="vertical-align: middle;">2024-06-15</td>
                <td style="vertical-align: middle;"><b class="">73.28</b></td>
                <td style="vertical-align: middle;">77.11</td>
                <td style="vertical-align: middle;">80.47</td>
                <td style="vertical-align: middle;">83.91</td>
                <td style="vertical-align: middle;">76.47</td>
                <td style="vertical-align: middle;">70.19</td>
                <td style="vertical-align: middle;">83.80</td>
                <td style="vertical-align: middle;">66.67</td>
                <td style="vertical-align: middle;">62.19</td>
                <td style="vertical-align: middle;">69.12</td>
                <td style="vertical-align: middle;">49.22</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="" class="ext-link" style="font-size: 16px; margin-left: 5px;">LLaVA-NeXT-Video
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Bytedance & NTU S-Lab</p>
                </a></b></td>
                <td style="vertical-align: middle;">32B</td>
                <td style="vertical-align: middle;">64 </td>
                <td style="vertical-align: middle;">2024-05-10</td>
                <td style="vertical-align: middle;"><strong>66.96</strong></td>
                <td style="vertical-align: middle;">78.20</td>
                <td style="vertical-align: middle;">70.31</td>
                <td style="vertical-align: middle;">73.82</td>
                <td style="vertical-align: middle;">76.80</td>
                <td style="vertical-align: middle;">63.35</td>
                <td style="vertical-align: middle;">69.78</td>
                <td style="vertical-align: middle;">57.41</td>
                <td style="vertical-align: middle;">56.10</td>
                <td style="vertical-align: middle;">64.31</td>
                <td style="vertical-align: middle;">38.86</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;">
                  <b class="">
                    <a href="https://arxiv.org/pdf/2408.03326" class="ext-link" style="font-size: 16px; margin-left: 5px;">LLaVA-OneVision</a>
                    <p style="font-size: 12px; margin-left: 5px; color: #858383;">Bytedance & NTU S-Lab</p>
                  </b>
                </td>
                <td style="vertical-align: middle;">7B </td>
                <td style="vertical-align: middle;">32 </td>
                <td style="vertical-align: middle;">2024-08-08</td>
                <td style="vertical-align: middle;"><b class="">71.12</b></td>
                <td style="vertical-align: middle;">80.38</td>
                <td style="vertical-align: middle;">74.22</td>
                <td style="vertical-align: middle;">76.03</td>
                <td style="vertical-align: middle;">80.72</td>
                <td style="vertical-align: middle;">72.67</td>
                <td style="vertical-align: middle;">71.65</td>
                <td style="vertical-align: middle;">67.59</td>
                <td style="vertical-align: middle;">65.45</td>
                <td style="vertical-align: middle;">65.72</td>
                <td style="vertical-align: middle;">45.08</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/DAMO-NLP-SG/VideoLLaMA2" class="ext-link" style="font-size: 16px; margin-left: 5px;">VideoLLaMA 2
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Alibaba</p>
                </a></b></td>
                <td style="vertical-align: middle;">7B</td>
                <td style="vertical-align: middle;">32 </td>
                <td style="vertical-align: middle;">2024-08-29</td>
                <td style="vertical-align: middle;"><strong>49.52</strong></td>
                <td style="vertical-align: middle;">55.86</td>
                <td style="vertical-align: middle;">55.47</td>
                <td style="vertical-align: middle;">57.41</td>
                <td style="vertical-align: middle;">58.17</td>
                <td style="vertical-align: middle;">52.80</td>
                <td style="vertical-align: middle;">43.61</td>
                <td style="vertical-align: middle;">39.81</td>
                <td style="vertical-align: middle;">42.68</td>
                <td style="vertical-align: middle;">45.61</td>
                <td style="vertical-align: middle;">35.23</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/NVlabs/VILA" class="ext-link" style="font-size: 16px; margin-left: 5px;">VILA-1.5
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">NVIDIA & MIT</p>
                </a> </b></td>
                <td style="vertical-align: middle;">8B </td>
                <td style="vertical-align: middle;">14 </td>
                <td style="vertical-align: middle;">2024-07-21</td>
                <td style="vertical-align: middle;"><b class="">52.32</b></td>
                <td style="vertical-align: middle;">53.68</td>
                <td style="vertical-align: middle;">49.22</td>
                <td style="vertical-align: middle;">70.98</td>
                <td style="vertical-align: middle;">56.86</td>
                <td style="vertical-align: middle;">53.42</td>
                <td style="vertical-align: middle;">53.89</td>
                <td style="vertical-align: middle;">54.63</td>
                <td style="vertical-align: middle;">48.78</td>
                <td style="vertical-align: middle;">50.14</td>
                <td style="vertical-align: middle;">17.62</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/OpenBMB/MiniCPM-V" class="ext-link" style="font-size: 16px; margin-left: 5px;">MiniCPM-V 2.6
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">OpenBMB</p>
                </a> </b></td>
                <td style="vertical-align: middle;">8B </td>
                <td style="vertical-align: middle;">32 </td>
                <td style="vertical-align: middle;">2024-08-12</td>
                <td style="vertical-align: middle;"><b class="">67.44</b></td>
                <td style="vertical-align: middle;">71.93</td>
                <td style="vertical-align: middle;">71.09</td>
                <td style="vertical-align: middle;">77.92</td>
                <td style="vertical-align: middle;">75.82</td>
                <td style="vertical-align: middle;">64.60</td>
                <td style="vertical-align: middle;">65.73</td>
                <td style="vertical-align: middle;">70.37</td>
                <td style="vertical-align: middle;">56.10</td>
                <td style="vertical-align: middle;">62.32</td>
                <td style="vertical-align: middle;">53.37</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;">
                  <span class="icon" style="color: #cd7f32;">
                    <i class="fas fa-medal"></i>
                  </span>
                </td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://www.anthropic.com/news/claude-3-5-sonnet" class="ext-link" style="font-size: 16px; margin-left: 5px;">Claude 3.5 Sonnet
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Anthropic</p>
                </a></b></td>
                <td style="vertical-align: middle;">- </td>
                <td style="vertical-align: middle;">20 </td>
                <td style="vertical-align: middle;">2024-07-30</td>
                <td style="vertical-align: middle;"><strong>72.44</strong></td>
                <td style="vertical-align: middle;">80.49</td>
                <td style="vertical-align: middle;">77.34</td>
                <td style="vertical-align: middle;">82.02</td>
                <td style="vertical-align: middle;">81.73</td>
                <td style="vertical-align: middle;">72.33</td>
                <td style="vertical-align: middle;">75.39</td>
                <td style="vertical-align: middle;">61.11</td>
                <td style="vertical-align: middle;">61.79</td>
                <td style="vertical-align: middle;">69.32</td>
                <td style="vertical-align: middle;">43.09</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/OpenGVLab/InternVL" class="ext-link" style="font-size: 16px; margin-left: 5px;">InternVL2
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Shanghai AI Lab</p>
                </a></b></td>
                <td style="vertical-align: middle;">8B</td>
                <td style="vertical-align: middle;">16 </td>
                <td style="vertical-align: middle;">2024-07-18</td>
                <td style="vertical-align: middle;"><strong>63.72</strong></td>
                <td style="vertical-align: middle;">68.12</td>
                <td style="vertical-align: middle;">60.94</td>
                <td style="vertical-align: middle;">69.40</td>
                <td style="vertical-align: middle;">77.12</td>
                <td style="vertical-align: middle;">67.70</td>
                <td style="vertical-align: middle;">62.93</td>
                <td style="vertical-align: middle;">59.26</td>
                <td style="vertical-align: middle;">53.25</td>
                <td style="vertical-align: middle;">54.96</td>
                <td style="vertical-align: middle;">56.48</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/KangarooGroup/Kangaroo" class="ext-link" style="font-size: 16px; margin-left: 5px;">Kangaroo
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Meituan & UCAS</p>
                </a></b></td>
                <td style="vertical-align: middle;">7B</td>
                <td style="vertical-align: middle;">64 </td>
                <td style="vertical-align: middle;">2024-07-23</td>
                <td style="vertical-align: middle;"><strong>64.60</strong></td>
                <td style="vertical-align: middle;">71.12</td>
                <td style="vertical-align: middle;">84.38</td>
                <td style="vertical-align: middle;">70.66</td>
                <td style="vertical-align: middle;">73.20</td>
                <td style="vertical-align: middle;">67.08</td>
                <td style="vertical-align: middle;">61.68</td>
                <td style="vertical-align: middle;">56.48</td>
                <td style="vertical-align: middle;">55.69</td>
                <td style="vertical-align: middle;">62.04</td>
                <td style="vertical-align: middle;">38.86</td>
              </tr>
          
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/QQ-MM/Video-CCAM" class="ext-link" style="font-size: 16px; margin-left: 5px;">Video-CCAM
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">QQMM</p>
                </a></b></td>
                <td style="vertical-align: middle;">14B</td>
                <td style="vertical-align: middle;">96 </td>
                <td style="vertical-align: middle;">2024-07-16</td>
                <td style="vertical-align: middle;"><strong>53.96</strong></td>
                <td style="vertical-align: middle;">56.40</td>
                <td style="vertical-align: middle;">57.81</td>
                <td style="vertical-align: middle;">65.30</td>
                <td style="vertical-align: middle;">62.75</td>
                <td style="vertical-align: middle;">64.60</td>
                <td style="vertical-align: middle;">51.40</td>
                <td style="vertical-align: middle;">42.59</td>
                <td style="vertical-align: middle;">47.97</td>
                <td style="vertical-align: middle;">49.58</td>
                <td style="vertical-align: middle;">31.61</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/EvolvingLMMs-Lab/LongVA" class="ext-link" style="font-size: 16px; margin-left: 5px;">LongVA
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">NTU S-Lab</p>
                </a></b></td>
                <td style="vertical-align: middle;">7B</td>
                <td style="vertical-align: middle;">128 </td>
                <td style="vertical-align: middle;">2024-06-25</td>
                <td style="vertical-align: middle;"><strong>59.96</strong></td>
                <td style="vertical-align: middle;">70.03</td>
                <td style="vertical-align: middle;">63.28</td>
                <td style="vertical-align: middle;">61.20</td>
                <td style="vertical-align: middle;">70.92</td>
                <td style="vertical-align: middle;">62.73</td>
                <td style="vertical-align: middle;">59.50</td>
                <td style="vertical-align: middle;">61.11</td>
                <td style="vertical-align: middle;">53.66</td>
                <td style="vertical-align: middle;">54.67</td>
                <td style="vertical-align: middle;">34.72</td>
              </tr>
          </tbody>                                                   
        </table> 
        </div>

        <div class="table-container" id="tablePage3" style="display: none;">
          <table class="js-sort-table" id="results3" style="margin-left: auto; margin-right: auto;">
            <thead>
              <tr>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 50px;" data-js-sort-colNum="none"><strong>Rank</strong></th>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 180px;" data-js-sort-colNum="none"><strong>Model</strong></th>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 50px;" data-js-sort-colNum="none"><strong>LLM <br>Params</strong></th>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 100px;" data-js-sort-colNum="none"><strong>Frames</strong></th>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 110px;" data-js-sort-colNum="none"><strong>Date</strong></th>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 110px;" data-js-sort-colNum="none"><strong>Overall (%)</strong></th>
                <th colspan="4" class="no-sort" style="vertical-align: middle; width: 110px;" data-js-sort-colNum="none"><strong>Omni-Source Understanding (%)</strong></th>
              </tr>
              <tr>
                <th data-js-sort-colNum="7"><strong>ER</strong></th>
                <th data-js-sort-colNum="8"><strong>SCU</strong></th>
                <th data-js-sort-colNum="9"><strong>SD</strong></th>
                <th data-js-sort-colNum="10"><strong>MA</strong></th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="vertical-align: middle;">
                  <span class="icon" style="color: gold;">
                    <i class="fas fa-medal"></i>
                  </span>
                </td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf" class="ext-link" style="font-size: 16px; margin-left: 5px;">Gemini 1.5 Pro
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Google</p>
                </a></b></td>
                <td style="vertical-align: middle;">-</td>
                <td style="vertical-align: middle;">1 fps</td>
                <td style="vertical-align: middle;">2024-06-15</td>
                <td style="vertical-align: middle;"><strong>60.22</strong></td>
                <td style="vertical-align: middle;">46.80</td>
                <td style="vertical-align: middle;">39.60</td>
                <td style="vertical-align: middle;">74.90</td>
                <td style="vertical-align: middle;">80.00</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://huggingface.co/spaces/Qwen/Qwen2-VL" class="ext-link" style="font-size: 16px; margin-left: 5px;">Qwen2-VL
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Alibaba</p>
                </a></b></td>
                <td style="vertical-align: middle;">7B</td>
                <td style="vertical-align: middle;">0.2-1 fps</td>
                <td style="vertical-align: middle;">2024-07-16</td>
                <td style="vertical-align: middle;"><strong>34.90</strong></td>
                <td style="vertical-align: middle;">41.20</td>
                <td style="vertical-align: middle;">22.00</td>
                <td style="vertical-align: middle;">32.80</td>
                <td style="vertical-align: middle;">43.60</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/OpenBMB/MiniCPM" class="ext-link" style="font-size: 16px; margin-left: 5px;">MiniCPM-V 2.6
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">OpenBMB</p>
                </a></b></td>
                <td style="vertical-align: middle;">8B</td>
                <td style="vertical-align: middle;">32</td>
                <td style="vertical-align: middle;">2024-08-12</td>
                <td style="vertical-align: middle;"><strong>35.00</strong></td>
                <td style="vertical-align: middle;">40.80</td>
                <td style="vertical-align: middle;">24.00</td>
                <td style="vertical-align: middle;">34.00</td>
                <td style="vertical-align: middle;">41.20</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/haotian-liu/LLaVA" class="ext-link" style="font-size: 16px; margin-left: 5px;">LLaVA-NeXT-Video
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">UW & Microsoft</p>
                </a></b></td>
                <td style="vertical-align: middle;">32B</td>
                <td style="vertical-align: middle;">64</td>
                <td style="vertical-align: middle;">2024-05-10</td>
                <td style="vertical-align: middle;"><strong>34.90</strong></td>
                <td style="vertical-align: middle;">37.69</td>
                <td style="vertical-align: middle;">24.80</td>
                <td style="vertical-align: middle;">34.40</td>
                <td style="vertical-align: middle;">42.80</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/OpenGVLab/InternVL" class="ext-link" style="font-size: 16px; margin-left: 5px;">InternVL-V2
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Shanghai AI Lab</p>
                </a></b></td>
                <td style="vertical-align: middle;">8B</td>
                <td style="vertical-align: middle;">16</td>
                <td style="vertical-align: middle;">2024-07-18</td>
                <td style="vertical-align: middle;"><strong>35.80</strong></td>
                <td style="vertical-align: middle;">37.60</td>
                <td style="vertical-align: middle;">26.40</td>
                <td style="vertical-align: middle;">37.20</td>
                <td style="vertical-align: middle;">42.00</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/KangarooGroup/Kangaroo" class="ext-link" style="font-size: 16px; margin-left: 5px;">Kangaroo
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Meituan & UCAS</p>
                </a></b></td>
                <td style="vertical-align: middle;">7B</td>
                <td style="vertical-align: middle;">64</td>
                <td style="vertical-align: middle;">2024-07-23</td>
                <td style="vertical-align: middle;"><strong>34.20</strong></td>
                <td style="vertical-align: middle;">37.60</td>
                <td style="vertical-align: middle;">31.20</td>
                <td style="vertical-align: middle;">28.80</td>
                <td style="vertical-align: middle;">39.20</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/EvolvingLMMs-Lab/LongVA" class="ext-link" style="font-size: 16px; margin-left: 5px;">LongVA
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">NTU S-Lab</p>
                </a></b></td>
                <td style="vertical-align: middle;">7B</td>
                <td style="vertical-align: middle;">128</td>
                <td style="vertical-align: middle;">2024-06-25</td>
                <td style="vertical-align: middle;"><strong>35.40</strong></td>
                <td style="vertical-align: middle;">39.60</td>
                <td style="vertical-align: middle;">32.40</td>
                <td style="vertical-align: middle;">28.00</td>
                <td style="vertical-align: middle;">41.60</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/VILA-Lab/VILA-1.5" class="ext-link" style="font-size: 16px; margin-left: 5px;">VILA-1.5
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">VILA Lab</p>
                </a></b></td>
                <td style="vertical-align: middle;">8B</td>
                <td style="vertical-align: middle;">14</td>
                <td style="vertical-align: middle;">2024-07-21</td>
                <td style="vertical-align: middle;"><strong>33.10</strong></td>
                <td style="vertical-align: middle;">41.60</td>
                <td style="vertical-align: middle;">26.40</td>
                <td style="vertical-align: middle;">28.40</td>
                <td style="vertical-align: middle;">36.00</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/QQ-MM/Video-CCAM" class="ext-link" style="font-size: 16px; margin-left: 5px;">Video-CCAM
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">QQMM</p>
                </a></b></td>
                <td style="vertical-align: middle;">14B</td>
                <td style="vertical-align: middle;">96</td>
                <td style="vertical-align: middle;">2024-07-16</td>
                <td style="vertical-align: middle;"><strong>29.70</strong></td>
                <td style="vertical-align: middle;">33.60</td>
                <td style="vertical-align: middle;">22.00</td>
                <td style="vertical-align: middle;">28.40</td>
                <td style="vertical-align: middle;">34.80</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/DAMO-NLP-SG/Video-LLaMA" class="ext-link" style="font-size: 16px; margin-left: 5px;">Video-LLaMA2
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">DAMO NLP</p>
                </a></b></td>
                <td style="vertical-align: middle;">7B</td>
                <td style="vertical-align: middle;">32</td>
                <td style="vertical-align: middle;">2024-08-29</td>
                <td style="vertical-align: middle;"><strong>32.40</strong></td>
                <td style="vertical-align: middle;">30.40</td>
                <td style="vertical-align: middle;">32.40</td>
                <td style="vertical-align: middle;">30.40</td>
                <td style="vertical-align: middle;">36.00</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;">
                  <span class="icon" style="color: #cd7f32;">
                    <i class="fas fa-medal"></i>
                  </span>
                </td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="#" class="ext-link" style="font-size: 16px; margin-left: 5px;">LLaVA-OneVision
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Microsoft</p>
                </a></b></td>
                <td style="vertical-align: middle;">7B</td>
                <td style="vertical-align: middle;">32</td>
                <td style="vertical-align: middle;">2024-08-08</td>
                <td style="vertical-align: middle;"><strong>38.40</strong></td>
                <td style="vertical-align: middle;">40.80</td>
                <td style="vertical-align: middle;">37.20</td>
                <td style="vertical-align: middle;">33.60</td>
                <td style="vertical-align: middle;">44.80</td>
              </tr>
              <tr>
、
                <td style="vertical-align: middle;">
                  <span class="icon" style="color: silver;">
                    <i class="fas fa-medal"></i>
                  </span>
                </td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="#" class="ext-link" style="font-size: 16px; margin-left: 5px;">GPT-4o
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">OpenAI</p>
                </a></b></td>
                <td style="vertical-align: middle;">-</td>
                <td style="vertical-align: middle;">64</td>
                <td style="vertical-align: middle;">2024-06-15</td>
                <td style="vertical-align: middle;"><strong>44.50</strong></td>
                <td style="vertical-align: middle;">41.20</td>
                <td style="vertical-align: middle;">37.20</td>
                <td style="vertical-align: middle;">43.60</td>
                <td style="vertical-align: middle;">56.00</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="#" class="ext-link" style="font-size: 16px; margin-left: 5px;">Claude 3.5 Sonnet
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Anthropic</p>
                </a></b></td>
                <td style="vertical-align: middle;">-</td>
                <td style="vertical-align: middle;">20</td>
                <td style="vertical-align: middle;">2024-07-30</td>
                <td style="vertical-align: middle;"><strong>36.80</strong></td>
                <td style="vertical-align: middle;">31.60</td>
                <td style="vertical-align: middle;">34.00</td>
                <td style="vertical-align: middle;">32.80</td>
                <td style="vertical-align: middle;">48.80</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="table-container" id="tablePage4" style="display: none;">
          <table class="js-sort-table" id="results4" style="margin-left: auto; margin-right: auto;">
            <thead>
              <tr>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 50px;" data-js-sort-colNum="none"><strong>Rank</strong></th>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 180px;" data-js-sort-colNum="none"><strong>Model</strong></th>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 50px;" data-js-sort-colNum="none"><strong>LLM <br>Params</strong></th>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 100px;" data-js-sort-colNum="none"><strong>Frames</strong></th>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 110px;" data-js-sort-colNum="none"><strong>Date</strong></th>
                <th rowspan="2" class="no-sort" style="vertical-align: middle; width: 110px;" data-js-sort-colNum="none"><strong>Overall (%)</strong></th>
                <th colspan="4" class="no-sort" style="vertical-align: middle; width: 110px;" data-js-sort-colNum="none"><strong>Contextual Understanding (%)</strong></th>
              </tr>
              <tr>
                <th data-js-sort-colNum="7"><strong>MCU</strong></th>
                <th data-js-sort-colNum="8"><strong>ACU</strong></th>
                <th data-js-sort-colNum="9"><strong>SQA</strong></th>
                <th data-js-sort-colNum="10"><strong>PO</strong></th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="vertical-align: middle;">
                  <span class="icon" style="color: gold;">
                    <i class="fas fa-medal"></i>
                  </span>
                </td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf" class="ext-link" style="font-size: 16px; margin-left: 5px;">Gemini 1.5 pro
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Google</p>
                </a></b></td>
                <td style="vertical-align: middle;">-</td>
                <td style="vertical-align: middle;">1 fps</td>
                <td style="vertical-align: middle;">2024-06-15</td>
                <td style="vertical-align: middle;"><strong>47.86</strong></td>
                <td style="vertical-align: middle;">40.73</td>
                <td style="vertical-align: middle;">51.41</td>
                <td style="vertical-align: middle;">54.80</td>
                <td style="vertical-align: middle;">31.37</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;">
                  <span class="icon" style="color: silver;">

                    <i class="fas fa-medal"></i>
                  </span>
                </td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="#" class="ext-link" style="font-size: 16px; margin-left: 5px;">GPT-4o
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">OpenAI</p>
                </a></b></td>
                <td style="vertical-align: middle;">-</td>
                <td style="vertical-align: middle;">64</td>
                <td style="vertical-align: middle;">2024-06-25</td>
                <td style="vertical-align: middle;"><strong>38.70</strong></td>
                <td style="vertical-align: middle;">38.40</td>
                <td style="vertical-align: middle;">41.20</td>
                <td style="vertical-align: middle;">32.80</td>
                <td style="vertical-align: middle;">56.86</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;">
                  <span class="icon" style="color: #cd7f32;">
                    <i class="fas fa-medal"></i>
                  </span>
                </td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="#" class="ext-link" style="font-size: 16px; margin-left: 5px;">Claude 3.5 Sonnet
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Anthropic</p>
                </a></b></td>
                <td style="vertical-align: middle;">-</td>
                <td style="vertical-align: middle;">20</td>
                <td style="vertical-align: middle;">2024-07-30</td>
                <td style="vertical-align: middle;"><strong>37.70</strong></td>
                <td style="vertical-align: middle;">34.80</td>
                <td style="vertical-align: middle;">38.40</td>
                <td style="vertical-align: middle;">34.40</td>
                <td style="vertical-align: middle;">64.71</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="#" class="ext-link" style="font-size: 16px; margin-left: 5px;">LLaVA-OneVision
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Microsoft</p>
                </a></b></td>
                <td style="vertical-align: middle;">7B</td>
                <td style="vertical-align: middle;">32</td>
                <td style="vertical-align: middle;">2024-08-08</td>
                <td style="vertical-align: middle;"><strong>32.74</strong></td>
                <td style="vertical-align: middle;">36.00</td>
                <td style="vertical-align: middle;">35.60</td>
                <td style="vertical-align: middle;">27.27</td>
                <td style="vertical-align: middle;">29.55</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://huggingface.co/spaces/Qwen/Qwen2-VL" class="ext-link" style="font-size: 16px; margin-left: 5px;">Qwen2-VL
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Alibaba</p>
                </a></b></td>
                <td style="vertical-align: middle;">7B</td>
                <td style="vertical-align: middle;">0.2-1 fps</td>
                <td style="vertical-align: middle;">2024-08-19</td>
                <td style="vertical-align: middle;"><strong>31.66</strong></td>
                <td style="vertical-align: middle;">26.00</td>
                <td style="vertical-align: middle;">31.20</td>
                <td style="vertical-align: middle;">39.60</td>
                <td style="vertical-align: middle;">22.73</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/OpenBMB/MiniCPM" class="ext-link" style="font-size: 16px; margin-left: 5px;">MiniCPM-V 2.6
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">OpenBMB</p>
                </a></b></td>
                <td style="vertical-align: middle;">8B</td>
                <td style="vertical-align: middle;">32</td>
                <td style="vertical-align: middle;">2024-06-25</td>
                <td style="vertical-align: middle;"><strong>34.97</strong></td>
                <td style="vertical-align: middle;">31.60</td>
                <td style="vertical-align: middle;">34.00</td>
                <td style="vertical-align: middle;">41.92</td>
                <td style="vertical-align: middle;">22.22</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/haotian-liu/LLaVA" class="ext-link" style="font-size: 16px; margin-left: 5px;">LLaVA-NeXT-Video
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">UW & Microsoft</p>
                </a></b></td>
                <td style="vertical-align: middle;">32B</td>
                <td style="vertical-align: middle;">64</td>
                <td style="vertical-align: middle;">2024-05-10</td>
                <td style="vertical-align: middle;"><strong>30.79</strong></td>
                <td style="vertical-align: middle;">30.40</td>
                <td style="vertical-align: middle;">29.20</td>
                <td style="vertical-align: middle;">35.35</td>
                <td style="vertical-align: middle;">18.18</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/OpenGVLab/InternVL" class="ext-link" style="font-size: 16px; margin-left: 5px;">InternVL-V2
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Shanghai AI Lab</p>
                </a></b></td>
                <td style="vertical-align: middle;">8B</td>
                <td style="vertical-align: middle;">16</td>
                <td style="vertical-align: middle;">2024-07-18</td>
                <td style="vertical-align: middle;"><strong>32.42</strong></td>
                <td style="vertical-align: middle;">31.20</td>
                <td style="vertical-align: middle;">32.00</td>
                <td style="vertical-align: middle;">32.32</td>
                <td style="vertical-align: middle;">40.91</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/KangarooGroup/Kangaroo" class="ext-link" style="font-size: 16px; margin-left: 5px;">Kangaroo
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">Meituan & UCAS</p>
                </a></b></td>
                <td style="vertical-align: middle;">7B</td>
                <td style="vertical-align: middle;">64</td>
                <td style="vertical-align: middle;">2024-07-23</td>
                <td style="vertical-align: middle;"><strong>30.06</strong></td>
                <td style="vertical-align: middle;">26.40</td>
                <td style="vertical-align: middle;">32.80</td>
                <td style="vertical-align: middle;">33.84</td>
                <td style="vertical-align: middle;">16.00</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/EvolvingLMMs-Lab/LongVA" class="ext-link" style="font-size: 16px; margin-left: 5px;">LongVA
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">NTU S-Lab</p>
                </a></b></td>
                <td style="vertical-align: middle;">7B</td>
                <td style="vertical-align: middle;">128</td>
                <td style="vertical-align: middle;">2024-06-25</td>
                <td style="vertical-align: middle;"><strong>29.95</strong></td>
                <td style="vertical-align: middle;">29.60</td>
                <td style="vertical-align: middle;">32.80</td>
                <td style="vertical-align: middle;">30.30</td>
                <td style="vertical-align: middle;">15.91</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/VILA-Lab/VILA-1.5" class="ext-link" style="font-size: 16px; margin-left: 5px;">VILA-1.5
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">VILA Lab</p>
                </a></b></td>
                <td style="vertical-align: middle;">8B</td>
                <td style="vertical-align: middle;">14</td>
                <td style="vertical-align: middle;">2024-07-21</td>
                <td style="vertical-align: middle;"><strong>27.35</strong></td>
                <td style="vertical-align: middle;">34.00</td>
                <td style="vertical-align: middle;">26.80</td>
                <td style="vertical-align: middle;">23.23</td>
                <td style="vertical-align: middle;">17.65</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/QQ-MM/Video-CCAM" class="ext-link" style="font-size: 16px; margin-left: 5px;">Video-CCAM
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">QQMM</p>
                </a></b></td>
                <td style="vertical-align: middle;">14B</td>
                <td style="vertical-align: middle;">96</td>
                <td style="vertical-align: middle;">2024-07-16</td>
                <td style="vertical-align: middle;"><strong>22.88</strong></td>
                <td style="vertical-align: middle;">24.40</td>
                <td style="vertical-align: middle;">27.60</td>
                <td style="vertical-align: middle;">16.67</td>
                <td style="vertical-align: middle;">22.73</td>
              </tr>
              <tr>
                <td style="vertical-align: middle;"></td>
                <td style="text-align: left; padding: 2px 10px;"><b class=""><a href="https://github.com/DAMO-NLP-SG/Video-LLaMA" class="ext-link" style="font-size: 16px; margin-left: 5px;">Video-LLaMA2
                  <p style="font-size: 12px; margin-left: 5px; color: #858383;">DAMO NLP</p>
                </a></b></td>
                <td style="vertical-align: middle;">7B</td>
                <td style="vertical-align: middle;">32</td>
                <td style="vertical-align: middle;">2024-08-29</td>
                <td style="vertical-align: middle;"><strong>21.93</strong></td>
                <td style="vertical-align: middle;">26.80</td>
                <td style="vertical-align: middle;">24.80</td>
                <td style="vertical-align: middle;">18.67</td>
                <td style="vertical-align: middle;">0</td>
              </tr>
            </tbody>
          </table>
        </div>

        <nav class="pagination is-centered" role="navigation" aria-label="pagination">
          <a class="pagination-previous" id="prevPage">Previous Page</a>
          <a class="pagination-next" id="nextPage">Next Page</a>
          <ul class="pagination-list" id="paginationList">
          </ul>
        </nav>

        </div>

      </div>
    </div>

  </div>
</section>

<!-- <section class="section">
  <div class="container" style="margin-bottom: 2vh;">
    <div class="columns is-centered has-text-centered">
      <div class="column is-four-fifths">
        <h2 class="title is-3">Introduction</h2>
        <div class="content has-text-justified">
          <p> -->



<section class="section">
  <div class="container">
    <div class="columns is-centered m-6">
      <div class="column is-max-desktop has-text-centered">
        <h2 class="title is-3" id="visualization">Visualization</h2>
        <iframe src="https://sbvisualizer-github-io.vercel.app/" style="width: 100%;min-height: 100vh; border-radius: 20px;"></iframe>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <h2 class="title is-3" style="text-align: center;">Data Statistics</h2>
  <div class="container">
    <div id="charts-carousel" class="carousel">
      <!-- Answer Distribution Chart -->
      <div class="box m-5 chart-container" style="background: linear-gradient(135deg, #ffffff, #f8f9fa); border-radius: 20px; box-shadow: 0 15px 35px rgba(50,115,220,0.1); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"
           onmouseover="this.style.transform='translateY(-5px)'" 
           onmouseout="this.style.transform='translateY(0)'">
        <div class="columns is-centered">
          <div class="column is-half">
            <div class="chart-wrapper" style="padding: 25px;">
              <canvas id="answerDistChart" style="max-width: 100%; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1));"></canvas>
            </div>
          </div>
          <div class="column is-half">
            <table class="table is-fullwidth is-hoverable" style="background: transparent; margin-top: 25px; border-radius: 10px; overflow: hidden;">
              <thead>
                <tr>
                  <th style="border-bottom: 3px solid #3273dc; color: #363636; font-weight: 600;">Option</th>
                  <th style="border-bottom: 3px solid #3273dc; color: #363636; font-weight: 600;">Count</th>
                  <th style="border-bottom: 3px solid #3273dc; color: #363636; font-weight: 600;">Percentage</th>
                </tr>
              </thead>
              <tbody id="answerDistTable" style="font-size: 0.95rem;">
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Video Category Chart -->
      <div class="box m-5 chart-container" style="background: linear-gradient(135deg, #ffffff, #f8f9fa); border-radius: 20px; box-shadow: 0 15px 35px rgba(50,115,220,0.1); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);" 
           onmouseover="this.style.transform='translateY(-5px)'" 
           onmouseout="this.style.transform='translateY(0)'">
        <div class="columns is-centered">
          <div class="column is-half">
            <div class="chart-wrapper" style="padding: 25px;">
              <canvas id="videoCategoryChart" style="max-width: 100%; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1));"></canvas>
            </div>
          </div>
          <div class="column is-half">
            <table class="table is-fullwidth is-hoverable" style="background: transparent; margin-top: 25px; border-radius: 10px; overflow: hidden;">
              <thead>
                <tr>
                  <th style="border-bottom: 3px solid #3273dc; color: #363636; font-weight: 600;">Category</th>
                  <th style="border-bottom: 3px solid #3273dc; color: #363636; font-weight: 600;">Count</th>
                  <th style="border-bottom: 3px solid #3273dc; color: #363636; font-weight: 600;">Percentage</th>
                </tr>
              </thead>
              <tbody id="videoCategoryTable" style="font-size: 0.95rem;">
                <!-- Dynamic table content -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Task Distribution Chart -->
      <div class="box m-5 chart-container" style="background: linear-gradient(135deg, #ffffff, #f8f9fa); border-radius: 20px; box-shadow: 0 15px 35px rgba(50,115,220,0.1); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"
           onmouseover="this.style.transform='translateY(-5px)'" 
           onmouseout="this.style.transform='translateY(0)'">
        <div class="chart-wrapper" style="padding: 25px;">
          <canvas id="taskChart" width="800" height="400" style="max-width: 100%; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1));"></canvas>
        </div>
      </div>

      <!-- Query Count Chart -->
      <div class="box m-5 chart-container" style="background: linear-gradient(135deg, #ffffff, #f8f9fa); border-radius: 20px; box-shadow: 0 15px 35px rgba(50,115,220,0.1); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"
           onmouseover="this.style.transform='translateY(-5px)'" 
           onmouseout="this.style.transform='translateY(0)'">
        <div class="chart-wrapper" style="padding: 25px;">
          <canvas id="queryCountChart" style="max-width: 100%; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1));"></canvas>
        </div>
      </div>

      <!-- Temporal Clues Chart -->
      <div class="box m-5 chart-container" style="background: linear-gradient(135deg, #ffffff, #f8f9fa); border-radius: 20px; box-shadow: 0 15px 35px rgba(50,115,220,0.1); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"
           onmouseover="this.style.transform='translateY(-5px)'" 
           onmouseout="this.style.transform='translateY(0)'">
        <div class="chart-wrapper" style="padding: 25px;">
          <canvas id="temporalCluesChart" style="max-width: 100%; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1));"></canvas>
        </div>
      </div>
      
      <div class="box m-5 chart-container" style="background: linear-gradient(135deg, #ffffff, #f8f9fa); border-radius: 20px; box-shadow: 0 15px 35px rgba(50,115,220,0.1); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"
           onmouseover="this.style.transform='translateY(-5px)'" 
           onmouseout="this.style.transform='translateY(0)'">
        <div class="content has-text-centered">
          <img src="static/images/Temporal_Clue.png" alt="arithmetic reasoning" 
               style="width: 70%; border-radius: 15px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); transition: all 0.3s ease;"
               onmouseover="this.style.transform='scale(1.02)'" 
               onmouseout="this.style.transform='scale(1)'"/>
          <p> </p>
        </div>
      </div>

      <!-- Question Length Distribution -->
      <div class="box m-5 chart-container" style="background: linear-gradient(135deg, #ffffff, #f8f9fa); border-radius: 20px; box-shadow: 0 15px 35px rgba(50,115,220,0.1); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"
     onmouseover="this.style.transform='translateY(-5px)'" 
     onmouseout="this.style.transform='translateY(0)'">
  <div class="content has-text-centered">
    <h3 class="title is-4">Question Length Distribution</h3>
    <canvas id="questionLengthChart"></canvas>
    <p style="margin-top: 20px;">
      Minimum length: 4 words<br>
      Maximum length: 34 words<br>
      Average length: 11.57 words
    </p>
  </div>
</div>

<div class="box m-5 chart-container" style="background: linear-gradient(135deg, #ffffff, #f8f9fa); border-radius: 20px; box-shadow: 0 15px 35px rgba(50,115,220,0.1); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"
onmouseover="this.style.transform='translateY(-5px)'" 
onmouseout="this.style.transform='translateY(0)'">
<div class="content has-text-centered">
<h3 class="title is-4">Options Length Distribution</h3>
<canvas id="optionsLengthChart"></canvas>
</div>
</div>
      
    </div>
  </div>
   
</section>

<script>

const questionLengthCtx = document.getElementById('questionLengthChart').getContext('2d');
new Chart(questionLengthCtx, {
  type: 'bar',
  data: {
    labels: ['(0, 5]', '(5, 10]', '(10, 15]', '(15, 20]', '(20, 25]', '(25, 30]', '(30, 35]'],
    datasets: [{
      label: 'Question Count',
      data: [297, 1677, 1526, 538, 168, 27, 17],
      backgroundColor: function(context) {
        const gradient = context.chart.ctx.createLinearGradient(0, 0, 0, 400);
        gradient.addColorStop(0, 'rgba(54, 162, 235, 0.9)');
        gradient.addColorStop(1, 'rgba(54, 162, 235, 0.4)');
        return gradient;
      },
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 2,
      borderRadius: 8,
      barPercentage: 0.8,
    }]
  },
  options: {
    responsive: true,
    animation: {
      duration: 2000,
      easing: 'easeInOutQuart'
    },
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Count',
          font: { size: 14, weight: 'bold' }
        }
      },
      x: {
        title: {
          display: true,
          text: 'Word Count',
          font: { size: 14, weight: 'bold' }
        }
      }
    },
    plugins: {
      legend: {
        display: false
      },
      tooltip: {
        backgroundColor: 'rgba(255, 255, 255, 0.9)',
        titleColor: '#000',
        bodyColor: '#000',
        borderColor: 'rgba(54, 162, 235, 0.8)',
        borderWidth: 1,
        padding: 10
      }
    }
  }
});
// Answer Distribution Chart
const answerDistCtx = document.getElementById('answerDistChart').getContext('2d');
const answerData = [
  { option: 'A', count: 1064, percentage: 25.0 },
  { option: 'B', count: 1059, percentage: 24.9 },
  { option: 'C', count: 1062, percentage: 25.0 },
  { option: 'D', count: 1065, percentage: 25.1 }
];

new Chart(answerDistCtx, {
  type: 'doughnut',
  data: {
    labels: answerData.map(item => item.option),
    datasets: [{
      data: answerData.map(item => item.percentage),
      backgroundColor: [
        'rgba(255, 99, 132, 0.8)',
        'rgba(54, 162, 235, 0.8)',
        'rgba(255, 206, 86, 0.8)',
        'rgba(75, 192, 192, 0.8)'
      ],
      borderColor: 'white',
      borderWidth: 2,
      hoverOffset: 15
    }]
  },
  options: {
    responsive: true,
    cutout: '60%',
    animation: {
      animateRotate: true,
      animateScale: true
    },
    plugins: {
      legend: {
        position: 'right',
        labels: {
          font: {
            size: 12
          },
          padding: 15
        }
      },
      title: {
        display: true,
        text: 'Answer Distribution',
        font: {
          size: 18,
          weight: 'bold'
        },
        padding: 20
      },
      tooltip: {
        backgroundColor: 'rgba(255, 255, 255, 0.9)',
        titleColor: '#000',
        bodyColor: '#000',
        borderColor: 'rgba(0, 0, 0, 0.1)',
        borderWidth: 1,
        padding: 10
      }
    }
  }
});

const optionsLengthCtx = document.getElementById('optionsLengthChart').getContext('2d');
new Chart(optionsLengthCtx, {
  type: 'bar',
  data: {
    labels: ['0', '1', '2', '3', '4', '5', '6-10', '11-20', '21-30', '31-50', '>50'],
    datasets: [{
      label: 'Options Count',
      data: [2, 306, 2973, 1296, 1605, 992, 2997, 3643, 1439, 747, 250],
      backgroundColor: function(context) {
        const gradient = context.chart.ctx.createLinearGradient(0, 0, 0, 400);
        gradient.addColorStop(0, 'rgba(75, 192, 192, 0.9)');
        gradient.addColorStop(1, 'rgba(75, 192, 192, 0.4)');
        return gradient;
      },
      borderColor: 'rgba(75, 192, 192, 1)',
      borderWidth: 2,
      borderRadius: 8,
      barPercentage: 0.8,
    }]
  },
  options: {
    responsive: true,
    animation: {
      duration: 2000,
      easing: 'easeInOutQuart'
    },
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Count',
          font: { size: 14, weight: 'bold' }
        }
      },
      x: {
        title: {
          display: true,
          text: 'Word Count',
          font: { size: 14, weight: 'bold' }
        }
      }
    },
    plugins: {
      legend: {
        display: false
      },
      tooltip: {
        backgroundColor: 'rgba(255, 255, 255, 0.9)',
        titleColor: '#000',
        bodyColor: '#000',
        borderColor: 'rgba(75, 192, 192, 0.8)',
        borderWidth: 1,
        padding: 10
      }
    }
  }
});

// Fill Answer Distribution table
const answerTableBody = document.getElementById('answerDistTable');
answerData.forEach(item => {
  const row = answerTableBody.insertRow();
  row.style.transition = 'all 0.3s ease';
  row.onmouseover = function() {
    this.style.backgroundColor = 'rgba(54, 162, 235, 0.1)';
    this.style.transform = 'scale(1.02)';
  };
  row.onmouseout = function() {
    this.style.backgroundColor = '';
    this.style.transform = 'scale(1)';
  };
  
  const cells = [
    item.option,
    item.count,
    item.percentage.toFixed(1) + '%'
  ];
  
  cells.forEach(text => {
    const cell = row.insertCell();
    cell.textContent = text;
    cell.style.padding = '12px';
  });
});

// Add total row
const totalAnswerRow = answerTableBody.insertRow();
totalAnswerRow.style.fontWeight = 'bold';
totalAnswerRow.style.backgroundColor = 'rgba(54, 162, 235, 0.1)';
['Total', '4250', '100%'].forEach(text => {
  const cell = totalAnswerRow.insertCell();
  cell.textContent = text;
  cell.style.padding = '12px';
});

// Query Count Chart
const queryCountCtx = document.getElementById('queryCountChart').getContext('2d');
new Chart(queryCountCtx, {
  type: 'bar',
  data: {
    labels: ['[0-60)', '[60-120)', '[120-180)', '[180-240)', '[240-300)', '[300-340)', '[340-420)', '[420-480)', '[480-540)', '[540-600)', '≥600'],
    datasets: [{
      label: 'Query Count',
      data: [909, 521, 674, 498, 441, 358, 296, 192, 265, 136, 210],
      backgroundColor: function(context) {
        const gradient = context.chart.ctx.createLinearGradient(0, 0, 0, 400);
        gradient.addColorStop(0, 'rgba(54, 162, 235, 0.9)');
        gradient.addColorStop(1, 'rgba(54, 162, 235, 0.4)');
        return gradient;
      },
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 2,
      borderRadius: 8,
      barPercentage: 0.8,
    }]
  },
  options: {
    responsive: true,
    animation: {
      duration: 2000,
      easing: 'easeInOutQuart'
    },
    interaction: {
      mode: 'index',
      intersect: false,
    },
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Query Count',
          font: {
            size: 14,
            weight: 'bold'
          }
        },
        grid: {
          color: 'rgba(0, 0, 0, 0.1)',
          drawBorder: false
        }
      },
      x: {
        title: {
          display: true,
          text: 'Time Range (seconds)',
          font: {
            size: 14,
            weight: 'bold'
          }
        },
        grid: {
          display: false
        }
      }
    },
    plugins: {
      title: {
        display: true,
        text: 'Query Count Distribution',
        font: {
          size: 18,
          weight: 'bold'
        },
        padding: 20
      },
      legend: {
        display: false
      },
      tooltip: {
        backgroundColor: 'rgba(255, 255, 255, 0.9)',
        titleColor: '#000',
        bodyColor: '#000',
        borderColor: 'rgba(54, 162, 235, 0.8)',
        borderWidth: 1,
        padding: 10,
        displayColors: false,
        callbacks: {
          label: function(context) {
            return `Count: ${context.parsed.y}`;
          }
        }
      }
    }
  }
});

// Video Category Chart
const videoCategoryCtx = document.getElementById('videoCategoryChart').getContext('2d');
const videoCategoryData = [
  { category: 'Education', count: 182, percentage: 20.22, subCategories: ['Online Tutorial', 'Science', 'Art', 'Handcraft', 'Lecture'] },
  { category: 'Life Record', count: 293, percentage: 32.56, subCategories: ['Daily Life', 'Travel', 'Vlog', 'Cooking', 'Working'] },
  { category: 'Competition', count: 185, percentage: 20.56, subCategories: ['Car Match', 'Boxing', 'Snooker', 'Basketball', 'Football'] },
  { category: 'Video Games', count: 43, percentage: 4.78, subCategories: ['Sandbox', 'Open-World'] },
  { category: 'Documentary', count: 37, percentage: 4.11, subCategories: ['Nature', 'Science', 'Culture', 'Kids'] },
  { category: 'Animation & Movie', count: 33, percentage: 3.67, subCategories: ['Animated Movie', 'Car Crash'] },
  { category: 'Unusual Event', count: 39, percentage: 4.33, subCategories: ['Magic Show', 'Prank', 'Unexpected Situation'] },
  { category: 'TV Show', count: 88, percentage: 9.78, subCategories: ['TV Series', 'News', 'Talk Show', 'Celebration Show'] }
];

new Chart(videoCategoryCtx, {
  type: 'doughnut',
  data: {
    labels: videoCategoryData.map(item => item.category),
    datasets: [{
      data: videoCategoryData.map(item => item.percentage),
      backgroundColor: [
        'rgba(255, 99, 132, 0.8)',
        'rgba(54, 162, 235, 0.8)', 
        'rgba(255, 206, 86, 0.8)',
        'rgba(75, 192, 192, 0.8)',
        'rgba(153, 102, 255, 0.8)',
        'rgba(255, 159, 64, 0.8)',
        'rgba(199, 199, 199, 0.8)',
        'rgba(83, 102, 255, 0.8)'
      ],
      borderColor: 'white',
      borderWidth: 2,
      hoverOffset: 15
    }]
  },
  options: {
    responsive: true,
    cutout: '60%',
    animation: {
      animateRotate: true,
      animateScale: true
    },
    plugins: {
      legend: {
        position: 'right',
        labels: {
          font: {
            size: 12
          },
          padding: 15,
          generateLabels: function(chart) {
            const data = chart.data;
            return data.labels.map((label, i) => ({
              text: `${label} (${data.datasets[0].data[i]}%)`,
              fillStyle: data.datasets[0].backgroundColor[i],
              strokeStyle: data.datasets[0].borderColor,
              lineWidth: data.datasets[0].borderWidth,
              hidden: isNaN(data.datasets[0].data[i]),
              index: i
            }));
          }
        }
      },
      title: {
        display: true,
        text: 'Video Category Distribution',
        font: {
          size: 18,
          weight: 'bold'
        },
        padding: 20
      },
      tooltip: {
        backgroundColor: 'rgba(255, 255, 255, 0.9)',
        titleColor: '#000',
        bodyColor: '#000',
        borderColor: 'rgba(0, 0, 0, 0.1)',
        borderWidth: 1,
        padding: 10,
        callbacks: {
          label: function(context) {
            const label = context.label || '';
            const value = context.formattedValue;
            const dataItem = videoCategoryData[context.dataIndex];
            const subCategories = dataItem.subCategories.join(', ');
            return [
              `${label}: ${value}%`,
              `Count: ${dataItem.count}`,
              `Sub-categories: ${subCategories}`
            ];
          }
        }
      }
    }
  }
});

// Fill the table with hover effects
const tableBody = document.getElementById('videoCategoryTable');

// Add Video Category data with enhanced styling
const categoryData = [
  { category: 'Education', count: 182, percentage: 20.22 },
  { category: 'Life Record', count: 293, percentage: 32.56 },
  { category: 'Competition', count: 185, percentage: 20.56 },
  { category: 'Video Games', count: 43, percentage: 4.78 },
  { category: 'Documentary', count: 37, percentage: 4.11 },
  { category: 'Animation & Movie', count: 33, percentage: 3.67 },
  { category: 'Unusual Event', count: 39, percentage: 4.33 },
  { category: 'TV Show', count: 88, percentage: 9.78 }
];

categoryData.forEach(item => {
  const row = tableBody.insertRow();
  row.style.transition = 'all 0.3s ease';
  row.onmouseover = function() {
    this.style.backgroundColor = 'rgba(54, 162, 235, 0.1)';
    this.style.transform = 'scale(1.02)';
  };
  row.onmouseout = function() {
    this.style.backgroundColor = '';
    this.style.transform = 'scale(1)';
  };
  
  const cells = [
    item.category,
    item.count,
    item.percentage.toFixed(2) + '%'
  ];
  
  cells.forEach(text => {
    const cell = row.insertCell();
    cell.textContent = text;
    cell.style.padding = '12px';
  });
});

// Add total row with special styling
const totalRow = tableBody.insertRow();
totalRow.style.fontWeight = 'bold';
totalRow.style.backgroundColor = 'rgba(54, 162, 235, 0.1)';
['Total', '900', '100%'].forEach(text => {
  const cell = totalRow.insertCell();
  cell.textContent = text;
  cell.style.padding = '12px';
});

// Add Video Perspective data
const perspectiveData = [
  { perspective: 'EgoCentric', count: 303, percentage: 33.67 },
  { perspective: 'Three-person', count: 597, percentage: 66.33 }
];

perspectiveData.forEach(item => {
  const row = tableBody.insertRow();
  row.style.transition = 'all 0.3s ease';
  row.onmouseover = function() {
    this.style.backgroundColor = 'rgba(75, 192, 192, 0.1)';
    this.style.transform = 'scale(1.02)';
  };
  row.onmouseout = function() {
    this.style.backgroundColor = '';
    this.style.transform = 'scale(1)';
  };
  
  const cells = [
    item.perspective,
    item.count,
    item.percentage.toFixed(2) + '%'
  ];
  
  cells.forEach(text => {
    const cell = row.insertCell();
    cell.textContent = text;
    cell.style.padding = '12px';
  });
});

// Temporal Clues Chart with enhanced 3D effects
const temporalCluesCtx = document.getElementById('temporalCluesChart').getContext('2d');
new Chart(temporalCluesCtx, {
  type: 'bar',
  data: {
    labels: ['Prior Clues', 'Concurrent Clues', 'Subsequent Clues'],
    datasets: [
      {
        label: 'Single Clue',
        data: [1658, 2592, 259],
        backgroundColor: function(context) {
          const gradient = context.chart.ctx.createLinearGradient(0, 0, 0, 400);
          gradient.addColorStop(0, 'rgba(255, 159, 64, 0.9)');
          gradient.addColorStop(1, 'rgba(255, 159, 64, 0.4)');
          return gradient;
        },
        borderColor: 'rgba(255, 159, 64, 1)',
        borderWidth: 2,
        borderRadius: 8,
      },
      {
        label: 'Multiple Clues',
        data: [1446, 1314, 75],
        backgroundColor: function(context) {
          const gradient = context.chart.ctx.createLinearGradient(0, 0, 0, 400);
          gradient.addColorStop(0, 'rgba(255, 99, 132, 0.9)');
          gradient.addColorStop(1, 'rgba(255, 99, 132, 0.4)');
          return gradient;
        },
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 2,
        borderRadius: 8,
      },
      {
        label: 'All',
        data: [212, 1278, 175],
        backgroundColor: function(context) {
          const gradient = context.chart.ctx.createLinearGradient(0, 0, 0, 400);
          gradient.addColorStop(0, 'rgba(54, 162, 235, 0.9)');
          gradient.addColorStop(1, 'rgba(54, 162, 235, 0.4)');
          return gradient;
        },
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 2,
        borderRadius: 8,
      }
    ]
  },
  options: {
    responsive: true,
    animation: {
      duration: 2000,
      easing: 'easeInOutQuart'
    },
    interaction: {
      mode: 'index',
      intersect: false,
    },
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Query Count',
          font: {
            size: 14,
            weight: 'bold'
          }
        },
        grid: {
          color: 'rgba(0, 0, 0, 0.1)',
          drawBorder: false
        }
      },
      x: {
        title: {
          display: true,
          text: 'Temporal Clues',
          font: {
            size: 14,
            weight: 'bold'
          }
        },
        grid: {
          display: false
        }
      }
    },
    plugins: {
      title: {
        display: true,
        text: 'Temporal Clues Distribution',
        font: {
          size: 18,
          weight: 'bold'
        },
        padding: 20
      },
      legend: {
        position: 'top',
        labels: {
          font: {
            size: 12
          },
          padding: 15
        }
      },
      tooltip: {
        backgroundColor: 'rgba(255, 255, 255, 0.9)',
        titleColor: '#000',
        bodyColor: '#000',
        borderColor: 'rgba(0, 0, 0, 0.1)',
        borderWidth: 1,
        padding: 10
      }
    }
  }
});

const ctx = document.getElementById('taskChart').getContext('2d');

const data = {
  labels: [
    null,
    'Object Perception', 'Attribute Perception', 'Action Perception', 'Event Understanding', 'Spatial Understanding', 'Text-Rich Understanding', 'Clips Summarization', 'Causal Reasoning', 'Prospective Reasoning', 'Counting',
    null,
    'Proactive Output', 'Anomaly Context Understanding', 'Misleading Context Understanding', 'Sequential Question Answering',
    null,
    'Emotion Recognition', 'Multimodal Alignment', 'Scene Understanding', 'Source Discrimination'
  ],
  datasets: [{
    label: 'Task Count',
    data: [
      null,
      367, 306, 353, 161, 246, 321, 317, 128, 108, 194,
      null,
      250, 250, 250, 250,
      null,
      250, 250, 250, 250
    ],
    backgroundColor: function(context) {
      const index = context.dataIndex;
      const chart = context.chart;
      const {ctx, chartArea} = chart;
      if (!chartArea) {
        return null;
      }
      if ([12, 13, 14, 15, 16].includes(index)) {
        // For 'Active Output' group - use red gradient
        const gradient = ctx.createLinearGradient(0, chartArea.bottom, 0, chartArea.top);
        gradient.addColorStop(0, 'rgba(255, 99, 132, 0.4)');
        gradient.addColorStop(1, 'rgba(255, 99, 132, 0.9)');
        return gradient;
      } else if ([17, 18, 19, 20, 21].includes(index)) {
        // For 'Emotion Recognition' group - use green gradient
        const gradient = ctx.createLinearGradient(0, chartArea.bottom, 0, chartArea.top);
        gradient.addColorStop(0, 'rgba(75, 192, 192, 0.4)');
        gradient.addColorStop(1, 'rgba(75, 192, 192, 0.9)');
        return gradient;
      } else {
        // Default - blue gradient
        const gradient = ctx.createLinearGradient(0, chartArea.bottom, 0, chartArea.top);
        gradient.addColorStop(0, 'rgba(54, 162, 235, 0.4)');
        gradient.addColorStop(1, 'rgba(54, 162, 235, 0.9)');
        return gradient;
      }
    },
    borderColor: function(context) {
      const index = context.dataIndex;
      if ([12, 13, 14, 15, 16].includes(index)) {
        return 'rgba(255, 99, 132, 1)'; // Red border
      } else if ([17, 18, 19, 20, 21].includes(index)) {
        return 'rgba(75, 192, 192, 1)'; // Green border
      } else {
        return 'rgba(54, 162, 235, 1)'; // Blue border
      }
    },
    borderWidth: 2,
    borderRadius: 8,
    barPercentage: 0.8,
  }]
};

const config = {
  type: 'bar',
  data: data,
  options: {
    responsive: true,
    animation: {
      duration: 2000,
      easing: 'easeInOutQuart'
    },
    interaction: {
      mode: 'index',
      intersect: false,
    },
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Task Count',
          font: {
            size: 14,
            weight: 'bold'
          }
        },
        grid: {
          color: 'rgba(0, 0, 0, 0.1)',
          drawBorder: false
        }
      },
      x: {
        title: {
          display: true,
          text: 'Task Categories',
          font: {
            size: 14,
            weight: 'bold'
          }
        },
        grid: {
          display: false
        }
      }
    },
    plugins: {
      title: {
        display: true,
        text: 'Task Distribution',
        font: {
          size: 18,
          weight: 'bold'
        },
        padding: 20
      },
      legend: {
        display: false
      },
      tooltip: {
        backgroundColor: 'rgba(255, 255, 255, 0.9)',
        titleColor: '#000',
        bodyColor: '#000',
        borderColor: 'rgba(0, 0, 0, 0.1)',
        borderWidth: 1,
        padding: 10
      }
    }
  },
};

new Chart(ctx, config);

// Initialize carousel with enhanced navigation
bulmaCarousel.attach('#charts-carousel', {
  slidesToScroll: 1,
  slidesToShow: 1,
  infinite: true,
  autoplay: false,
  navigation: true,
  navigationKeys: true,
  navigationSwipe: true,
  pagination: true
});



</script>


<!-- RESULTS SECTION
<section class="hero is-light is-small">
  <div class="hero-body has-text-centered">
    <h1 class="title is-1 mathvista">Experiment Results</h1>
  </div>
</section> -->

<!-- <section class="section">
  <div class="container">

    <div class="columns is-centered m-6">
      <div class="column is-full has-text-centered content">
        <h2 class="title is-3">Results on Existing Foundation Models</h2>
        <div id="results-carousel" class="carousel results-carousel">
          <div class="box m-5">
            <div class="content has-text-centered">
              <img src="static/images/results-figures/score_leaderboard_gpt4v.png" alt="grade-lv" width="60%"/>
              <p>Accuracy scores of primary baselines on the testmini subset (1,000 examples) of <img src="static/images/mathvista.png" style="width:1.0em;vertical-align: middle" alt="Logo"/>
                <span class="mathvista">MathVista</span>. 
                <br>
                Both CoT GPT-4 and PoT GPT-4 are augmented with Bard captions and OCR text.</p>
            </div>
          </div>
          <div class="box m-5">
            <div class="content has-text-centered">
              <img src="static/images/results-figures/bard_error.png" alt="grade-lv" width="70%"/>
              <p>
                Error analysis of Bard results: (a) presents errors in answers and explanations; <br>
                (b) delves into the details of wrong explanations. <br>
                Notations: "Answer" is "Ans.", "Explanation" is "Exp.", "Partially Correct" is "Partial", <br>
                and "Not applicable" refers to unanswerable or indeterminate cases.</p>
            </div>
          </div>
          <div class="box m-5">
            <div class="content has-text-centered">
              <img src="static/images/results-figures/grade-lv.png" alt="grade-lv" width="90%"/>
              <p>Average accuracy scores across different grade levels for leading foundation models</p>
            </div>
          </div>
          <div class="box m-5">
            <div class="content has-text-centered">
              <img src="static/images/results-figures/contexts.png" alt="contexts" width="90%"/>
              <p>Accuracy scores of leading baselines across various visual contexts</p>
            </div>
          </div>
          <div class="box m-5">
            <div class="content has-text-centered">
              <img src="static/images/results-figures/ablation.png" alt="geometric reasoning" width="90%"/>
              <p>Average accuracy scores of LLM baselines under various visual inputs</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section> -->


<!-- @PAN TODO: bibtex -->
<section class="section" id="BibTeX">
  <div class="container is-max-desktop content">
    <h2 class="title is-3 has-text-centered">Citation</h2>
    <pre><code>
      @article{lin2024streaming,
        title={StreamingBench: Assessing the Gap for MLLMs to Achieve Streaming Video Understanding},
        author={Junming Lin and Zheng Fang and Chi Chen and Zihao Wan and Fuwen Luo and Peng Li and Yang Liu and Maosong Sun},
        journal={arXiv preprint arXiv:2411.03628},
        year={2024}
      }
    </code></pre>
  </div>
</section>


<footer class="footer">
  <!-- <div class="container"> -->
    <div class="content has-text-centered">
    </div>
    <div class="columns is-centered">
      <div class="column is-8">
        <div class="content">
          <p>
            This website is adapted from <a href="https://mathvista.github.io/">MathVista</a> and <a href="https://video-mme.github.io/home_page.html">Video-MME</a>, licensed under a <a rel="license"
                                                href="http://creativecommons.org/licenses/by-sa/4.0/">Creative
            Commons Attribution-ShareAlike 4.0 International License</a>.
          </p>
        </div>
      </div>
    </div>
  <!-- </div> -->
</footer>

</body>
</html>
