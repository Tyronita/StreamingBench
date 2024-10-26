# This file contains task descriptions and prompts for video understanding tasks
# Author: Junming Lin
# Date: 2024-10-26
# Copyright (c) THUNLP, Tsinghua University. All rights reserved.
# See LICENSE file in the project root for license information.

# Task descriptions for different video understanding capabilities
TASK_DESCRIPTION = [

    'Object Recognition: Detect and identify specific physical objects within a video. This includes recognizing logos, items, or other distinguishable elements present in the footage, such as cars, furniture, or branded products.',

	'Attribute Recognition: Identify and categorize the attributes of objects or individuals within a video, focusing on the properties and characteristics such as colors, shapes, sizes, textures, or other distinguishing features. This task involves describing the traits of objects or individuals rather than recognizing the objects or individuals themselves.',

	'Action Recognition: Identify and describe specific actions or movements performed by individuals in a video. This task focuses on detecting and understanding individual physical activities, such as walking, running, jumping, or waving, without necessarily considering the broader sequence or context of these actions.',

	'Event Understanding: Identify and understand a specific event or the sequence of events within a video. This task involves recognizing and describing a series of actions or occurrences that happen in a logical or meaningful order, focusing on the overall context and relationships between different actions or events to understand the narrative or progression in the video.',

	'Causal Reasoning: Analyze and determine the cause-and-effect relationships within a video. This task focuses on understanding why certain events happened by examining the context and sequence of prior actions, identifying the underlying reasons and factors that led to specific outcomes.',

	'Prospective Reasoning: Predict future actions or events in a video based on the current context. This task involves inferring what might happen next given the present information and observed patterns, focusing on anticipating upcoming occurrences rather than explaining past events.',

	'Spatial Understanding: Understand and describe the spatial relationships and locations within a video. This includes identifying and analyzing the positions and relative placements of objects, individuals, and places mentioned or shown in the footage. The task involves recognizing spatial arrangements, movements, and interactions within the environment, as well as understanding the geometry and topology of the scene to provide a comprehensive spatial context.',

    'Clips Summarize: Summarize the main content of specific clips within a video. This includes identifying key events and information presented in shorter segments of the footage.',

    'Text-Rich Understanding: Understand and interpret text-rich content within a video. This involves reading, comprehending, and explaining text information presented in the footage, such as subtitles, on-screen text, signs, or written materials.',

	'Counting: Determine and report the number of occurrences of a specific object or action within a video up to the current point in time. This task involves accurately tracking and quantifying the instances of the specified object or action as they appear in the video, considering various conditions such as movement, occlusions, and varying perspectives.'
]

# Prompt template for generating general video captions with timestamps
PROMPT_GENERAL_CAPTIONS = """
You are an AI assistant skilled in video comprehension, captioning, and adding timestamps. These are frames from a {20-second first-person perspective video with 1-second intervals between each frame}. Each image has a corresponding timestamp.

Follow these TWO STEPS:

STEP 1: Detailed Description
1. Describe the video in as much detail as possible, including features (shapes, sizes, colors, positions, orientations, etc.), actions, movements, relationships of people and objects, and backgrounds.
2. Only describe what is visible in the video. Do not include information you are unsure about.
3. Start the description naturally, without summaries.
4. Be objective and avoid subjective opinions or guesses.
5. Write naturally and fluently. Do not caption frame by frame.
6. Ensure proper grammar, especially for person and tense.

STEP 2: Add Timestamps
1. Add specific timestamps to different segments of the description based on the timestamps in the top left corner of the frames.
2. Do not modify the original description content.
3. Use the format [H:MM:SS - H:MM:SS] for ranges or [H:MM:SS] for single timestamps.
4. Ensure timestamps match the corresponding video frames.

Example format:
[H:MM:SS - H:MM:SS]: description segment; [H:MM:SS]: description segment; ...

Only output the captions with added timestamps. Do not include any other content. Carefully review the provided captions and video frames, then provide your response.
"""

# Prompt template for generating dense video captions with timestamps
PROMPT_DENSE_CAPTIONS = """
You are an AI assistant skilled in video comprehension, captioning, and adding timestamps. These are frames a full video with 1-second intervals between each frame. Each image has a corresponding timestamp.

Follow these TWO STEPS:

STEP 1: Detailed Description
1. Describe the video in as much detail as possible, including features (shapes, sizes, colors, positions, orientations, etc.), actions, movements, relationships of people and objects, and backgrounds.
2. Only describe what is visible in the video. Do not include information you are unsure about.
3. Start the description naturally, without summaries.
4. Be objective and avoid subjective opinions or guesses.
5. Write naturally and fluently. Do not caption frame by frame.
6. Ensure proper grammar, especially for person and tense.

STEP 2: Add Timestamps
1. Add specific timestamps to different segments of the description based on the timestamps in the top left corner of the frames.
2. Do not modify the original description content.
3. Use the format [H:MM:SS - H:MM:SS] for ranges or [H:MM:SS] for single timestamps.
4. Ensure timestamps match the corresponding video frames.

Example format:
[H:MM:SS - H:MM:SS]: description segment; [H:MM:SS]: description segment; ...

Only output the captions with added timestamps. Do not include any other content. Carefully review the provided captions and video frames, then provide your response.
"""

# Prompt template for generating questions from non-starting video segments
PROMPT_GIVE_QUESTIONS_NOT_STR = """
You are an AI assistant skilled at generating questions and answers. I have captions for a 20s video clips extracted from a original video, organized in chronological order with time marks like [0:01:00 - 0:01:20]. Since the clip is not from the beginning of the original video, the time marks do not start from 00:00:00. Please read the captions carefully and provide question-answer pairs based on the captions. Follow these instructions:

1. Ensure the questions and answers are highly relevant to the captions and DO NOT INCLUDE TOPICS NOT MENTIONED in the captions.
2. IGNORE CONTRADICTORY OR UNREASONABLE PARTS of the captions. Do not base questions on them.
3. Present questions as multiple-choice. Provide task type, questions, options, and answers. Each question should have 4 options with similar formats, and the wrong options should be deceptive.
4. Avoid questions specific to individual scenes or overly precise timing. Consider all scenes as a whole.
6. Pay attention to grammar. Avoid grammar mistakes, especially with person and tense.
7. Ensure questions are reasonable and challenging, requiring thoughtful consideration to answer correctly.
8. The question should not contain phrases like "In the beginning of the clips" or "at the beginning of the video" or "in the video" or "in this clips"; it can only include expressions of the present or recent past such as "just now" or "right now."
9. Please pay attention to the tense of the sentences.
10. Provide only one best question-answer pairs based on the caption.

Understand the following task descriptions:

""" + '\n'.join(TASK_DESCRIPTION) + """

Refer to the examples below and generate questions based on the given captions. Use the task types listed above.
The time_stamp in the following questions refers to the question 's timestamp. In the captions I provided, each segment has a corresponding timestamp. When providing the question, you should assign an appropriate question timestamp based on the time information in the captions. If the timestamps in the captions are given as a time range, only provide the end timestamp of that time range in the question, rather than the entire time range.

# Example Tasks:

# TODO {Few shots}

Please generate Q&A content in the following format:

Format:
Task Type: <task_type>
Question: <question>
Time Stamp: <time_stamp>
A. <option_A>
B. <option_B>
C. <option_C>
D. <option_D>
Answer: <answer>

Output only the questions and answers. Now, please carefully review the captions and output your questions and answers following the SAME FORMAT as the examples above.
"""

# Prompt template for generating questions from starting video segments
PROMPT_GIVE_QUESTIONS_STR = """
You are an AI assistant skilled at generating questions and answers. I have captions for a 20s video clips extracted from a original video, organized in chronological order with time marks like [00:00:00 - 00:00:20]. Since the clip is from the beginning of the original video, the time marks should start from 00:00:00. Please read the captions carefully and provide question-answer pairs based on the captions. Follow these instructions:

1. Ensure the questions and answers are highly relevant to the captions and DO NOT INCLUDE TOPICS NOT MENTIONED in the captions.
2. IGNORE CONTRADICTORY OR UNREASONABLE PARTS of the captions. Do not base questions on them.
3. Present questions as multiple-choice. Provide task type, questions, options, and answers. Each question should have 4 options with similar formats, and the wrong options should be deceptive.
4. Avoid questions specific to individual scenes or overly precise timing. Consider all scenes as a whole.
6. Pay attention to grammar. Avoid grammar mistakes, especially with person and tense.
7. Ensure questions are reasonable and challenging, requiring thoughtful consideration to answer correctly.
8. The question should not contain phrases like "In the beginning of the clips" or "at the beginning of the video" or "in the video" or "in this clips"; it can only include expressions of the present or recent past such as "just now" or "right now."
9. Please pay attention to the tense of the sentences.
10. Provide only one best question-answer pairs based on the caption.

Understand the following task descriptions:

""" + '\n'.join(TASK_DESCRIPTION) + """

Refer to the examples below and generate questions based on the given captions. Use the task types listed above. The time_stamp in the questions should refer to the question's timestamp, using the end timestamp of a time range. Do not include the task description in the output.

# Example Tasks:

# TODO {Few shots}


Please generate Q&A content in the following format:

Format:
Task Type: <task_type>
Question: <question>
Time Stamp: <time_stamp>
A. <option_A>
B. <option_B>
C. <option_C>
D. <option_D>
Answer: <answer>

Output only the questions and answers. Now, please carefully review the captions and output your questions and answers following the SAME FORMAT as the examples above.
"""

# Subject area for the video content
SUBJECT = "Mathematics Teaching"

# Direct prompt template for non-starting video segments
DIRECT_PROMPT_NOT_STR = f"""
You are an AI assistant skilled at generating questions and answers. I have a 20s video clips extracted from a {SUBJECT} video, organized in chronological order with time marks like [0:01:00 - 0:01:20]. Since the clip is not from the beginning of the original video, the time marks do not start from 00:00:00. Please read the video clips carefully and provide question-answer pairs based on the video clips. Follow these instructions:

1. Ensure the questions and answers are highly relevant to the video clips and DO NOT INCLUDE TOPICS NOT MENTIONED in the video clips.
2. Present questions as multiple-choice. Provide task type, questions, options, and answers. Each question should have 4 options with similar formats, and the wrong options should be deceptive.
3. Avoid questions specific to individual scenes or overly precise timing. Consider all scenes as a whole.
4. Pay attention to grammar. Avoid grammar mistakes, especially with person and tense.
5. Ensure questions are reasonable and challenging, requiring thoughtful consideration to answer correctly.
6. The question should not contain phrases like "In the beginning of the clips" or "in the video".
7. Don't use phrases like "at the beginning of the video" or "In this clips"
8. Please pay attention to the tense of the sentences. 
9. Provide only one best question-answer pairs based on the caption,(i.e. Prospective Reasoning)
10. Please pay attention to the logic before and after the formula derivation in the video. Pay attention to the mathematical formulas on the screen and the order and logic of the teacher's derivation of the formulas to generate high-quality Causal Reasoning and Prospective Reasoning tasks.
Understand the following task descriptions:

1. Prospective Reasoning: Predict future actions or events in a video based on the current context. This task involves inferring what might happen next given the present information and observed patterns, focusing on anticipating upcoming occurrences rather than explaining past events.

Refer to the examples below and generate questions based on the given video clips. Use the task types listed above.
The time_stamp in the following questions refers to the question 's timestamp. In the video clips I provided, each image has a corresponding timestamp. Each image has a corresponding white timestamp in the upper left corner. When providing the question, you should assign an appropriate question timestamp based on the time information in the image.

# Example Tasks:

<TIPS: The timestamp in the corresponding images are from 00:00:30 to 00:00:45>
Task Type: Prospective Reasoning
Question: What are you gonna do after that?
Time Stamp: 00:00:45
A. Multiply 12 by the number of numbers.
B. Divide 12 by the number of numbers.
C. Subtract the largest number from 12.
D. Add 12 to the number of numbers.
Answer: B

<TIPS: The timestamp in the corresponding images are from 00:00:30 to 00:00:45>
Task Type: Prospective Reasoning
Question: What might the speaker explain next?
Time Stamp: 00:00:45
A. Integrate with respect to x.
B. Integrate with respect to u.
C. Differentiate with respect to x.
D. Differentiate with respect to u.
Answer: B

<TIPS: The timestamp in the corresponding images are from 00:00:00 to 00:00:20>
Task Type: Prospective Reasoning
Question: What might the speaker discuss next?
Time Stamp: 00:00:16
A. Graphing on the Coordinate Plane.
B. Calculus functions.
C. Trigonometric ratios.
D. Differential equations.
Answer: A

<TIPS: The timestamp in the corresponding images are from 00:02:06 to 00:02:26>
Task Type: Prospective Reasoning
Question: What might the speaker explain next?
Time Stamp: 00:02:22
A. How to label the axes.
B. How to connect the plotted points.
C. How to identify coordinates.
D. How to scale the graph.
Answer: B

<TIPS: The timestamp in the corresponding images are from 00:04:12 to 00:04:32>
Task Type: Prospective Reasoning
Question: What might the speaker discuss next?
Time Stamp: 00:04:20
A. How to plot points on the axes.
B. The importance of the x-axis.
C. The significance of the y-axis.
D. What ordered pairs represent.
Answer: D

<TIPS: The timestamp in the corresponding images are from 00:06:18 to 00:06:38>
Task Type: Prospective Reasoning
Question: What might the speaker discuss next?
Time Stamp: 00:06:37
A. How to plot another point.
B. How to label the y-axis.
C. The importance of the y-intercept.
D. How to draw a quadratic curve.
Answer: A

<TIPS: The timestamp in the corresponding images are from 00:08:24 to 00:08:44>
Task Type: Prospective Reasoning
Question: What might the speaker discuss next?
Time Stamp: 00:08:31
A. How to plot a line graph.
B. The significance of the axes intersections.
C. How to differentiate the quadrants.
D. The concept of linear equations.
Answer: C

Please generate Q&A content in the following format:

Format:
Task Type: <task_type>
Question: <question>
Time Stamp: <time_stamp>
A. <option_A>
B. <option_B>
C. <option_C>
D. <option_D>
Answer: <answer>

Output only the questions and answers. Now, please carefully review the video clips and output your questions and answers following the SAME FORMAT as the examples above.
"""

# Direct prompt template for starting video segments
DIRECT_PROMPT_STR = f"""
You are an AI assistant skilled at generating questions and answers. I have a 20s video clips extracted from a {SUBJECT} video, organized in chronological order with time marks like [0:00:00 - 0:00:20]. The clip is from the beginning of the original video, the time marks start from 00:00:00. Please read the video clips carefully and provide question-answer pairs based on the video clips. Follow these instructions:

1. Ensure the questions and answers are highly relevant to the video clips and DO NOT INCLUDE TOPICS NOT MENTIONED in the video clips.
2. Present questions as multiple-choice. Provide task type, questions, options, and answers. Each question should have 4 options with similar formats, and the wrong options should be deceptive.
3. Avoid questions specific to individual scenes or overly precise timing. Consider all scenes as a whole.
4. Pay attention to grammar. Avoid grammar mistakes, especially with person and tense.
5. Ensure questions are reasonable and challenging, requiring thoughtful consideration to answer correctly.
6. The question should not contain phrases like "In the beginning of the clips" or "in the video".
7. Don't use phrases like "at the beginning of the video" or "In this clips"
8. Please pay attention to the tense of the sentences.
9. Provide only one best question-answer pairs based on the caption,(e.g. Prospective Reasoning)
10. Please pay attention to the logic before and after the formula derivation in the video. Pay attention to the mathematical formulas on the screen and the order and logic of the teacher's derivation of the formulas to generate high-quality Causal Reasoning and Prospective Reasoning tasks.
Understand the following task descriptions:

1. Prospective Reasoning: Predict future actions or events in a video based on the current context. This task involves inferring what might happen next given the present information and observed patterns, focusing on anticipating upcoming occurrences rather than explaining past events.

Refer to the examples below and generate questions based on the given video clips. Use the task types listed above.
The time_stamp in the following questions refers to the question 's timestamp. In the video clips I provided, each image has a corresponding timestamp. Each image has a corresponding white timestamp in the upper left corner. When providing the question, you should assign an appropriate question timestamp based on the time information in the image.

# Example Tasks:

<TIPS: The timestamp in the corresponding images are from 00:00:30 to 00:00:45>
Task Type: Prospective Reasoning
Question: What are you gonna do after that?
Time Stamp: 00:00:45
A. Multiply 12 by the number of numbers.
B. Divide 12 by the number of numbers.
C. Subtract the largest number from 12.
D. Add 12 to the number of numbers.
Answer: B

<TIPS: The timestamp in the corresponding images are from 00:00:30 to 00:00:45>
Task Type: Prospective Reasoning
Question: What might the speaker explain next?
Time Stamp: 00:00:45
A. Integrate with respect to x.
B. Integrate with respect to u.
C. Differentiate with respect to x.
D. Differentiate with respect to u.
Answer: B

<TIPS: The timestamp in the corresponding images are from 00:00:00 to 00:00:20>
Task Type: Prospective Reasoning
Question: What might the speaker discuss next?
Time Stamp: 00:00:16
A. Graphing on the Coordinate Plane.
B. Calculus functions.
C. Trigonometric ratios.
D. Differential equations.
Answer: A

<TIPS: The timestamp in the corresponding images are from 00:02:06 to 00:02:26>
Task Type: Prospective Reasoning
Question: What might the speaker explain next?
Time Stamp: 00:02:22
A. How to label the axes.
B. How to connect the plotted points.
C. How to identify coordinates.
D. How to scale the graph.
Answer: B

<TIPS: The timestamp in the corresponding images are from 00:04:12 to 00:04:32>
Task Type: Prospective Reasoning
Question: What might the speaker discuss next?
Time Stamp: 00:04:20
A. How to plot points on the axes.
B. The importance of the x-axis.
C. The significance of the y-axis.
D. What ordered pairs represent.
Answer: D

<TIPS: The timestamp in the corresponding images are from 00:06:18 to 00:06:38>
Task Type: Prospective Reasoning
Question: What might the speaker discuss next?
Time Stamp: 00:06:37
A. How to plot another point.
B. How to label the y-axis.
C. The importance of the y-intercept.
D. How to draw a quadratic curve.
Answer: A

<TIPS: The timestamp in the corresponding images are from 00:08:24 to 00:08:44>
Task Type: Prospective Reasoning
Question: What might the speaker discuss next?
Time Stamp: 00:08:31
A. How to plot a line graph.
B. The significance of the axes intersections.
C. How to differentiate the quadrants.
D. The concept of linear equations.
Answer: C

Please generate Q&A content in the following format:

Format:
Task Type: <task_type>
Question: <question>
Time Stamp: <time_stamp>
A. <option_A>
B. <option_B>
C. <option_C>
D. <option_D>
Answer: <answer>

Output only the questions and answers. Now, please carefully review the video clips and output your questions and answers following the SAME FORMAT as the examples above.
"""


TASK_DESCRIPTION = [

    'Object Recognition: Detect and identify specific physical objects within a video. This includes recognizing logos, items, or other distinguishable elements present in the footage, such as cars, furniture, or branded products.',

	'Attribute Recognition: Identify and categorize the attributes of objects or individuals within a video, focusing on the properties and characteristics such as colors, shapes, sizes, textures, or other distinguishing features. This task involves describing the traits of objects or individuals rather than recognizing the objects or individuals themselves.',

	'Action Recognition: Identify and describe specific actions or movements performed by individuals in a video. This task focuses on detecting and understanding individual physical activities, such as walking, running, jumping, or waving, without necessarily considering the broader sequence or context of these actions.',

	'Event Understanding: Identify and understand a specific event or the sequence of events within a video. This task involves recognizing and describing a series of actions or occurrences that happen in a logical or meaningful order, focusing on the overall context and relationships between different actions or events to understand the narrative or progression in the video.',

	'Causal Reasoning: Analyze and determine the cause-and-effect relationships within a video. This task focuses on understanding why certain events happened by examining the context and sequence of prior actions, identifying the underlying reasons and factors that led to specific outcomes.',

	'Prospective Reasoning: Predict future actions or events in a video based on the current context. This task involves inferring what might happen next given the present information and observed patterns, focusing on anticipating upcoming occurrences rather than explaining past events.',

	'Spatial Understanding: Understand and describe the spatial relationships and locations within a video. This includes identifying and analyzing the positions and relative placements of objects, individuals, and places mentioned or shown in the footage. The task involves recognizing spatial arrangements, movements, and interactions within the environment, as well as understanding the geometry and topology of the scene to provide a comprehensive spatial context.',

    'Clips Summarize: Summarize the main content of specific clips within a video. This includes identifying key events and information presented in shorter segments of the footage.',

    'Text-Rich Understanding: Understand and interpret text-rich content within a video. This involves reading, comprehending, and explaining text information presented in the footage, such as subtitles, on-screen text, signs, or written materials.',

	'Counting: Determine and report the number of occurrences of a specific object or action within a video up to the current point in time. This task involves accurately tracking and quantifying the instances of the specified object or action as they appear in the video, considering various conditions such as movement, occlusions, and varying perspectives.'
]