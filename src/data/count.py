import json
import csv
from collections import defaultdict

MODEL = 'GPT4o'
task = ""
src = ""

# Load the JSON file
with open(src, 'r') as file:
    data = json.load(file)

# Initialize counters
stats = defaultdict(lambda: defaultdict(int))

# Process each entry in the JSON data
total = 0

if task == "context":
    for ques in data:
        for entry in ques:
            # if ques.index(entry) == 0:
            #     continue
            for question in entry["questions"]:
                task_type = question["task_type"]
                if MODEL not in question or not question.get(MODEL, None):
                    continue
                model_answer = question.get(MODEL, None)[0]
                correct_answer = question["answer"]

                if model_answer:
                    total += 1
                    stats[task_type]["total"] += 1
                    if correct_answer == model_answer:
                        stats[task_type]["correct"] += 1
elif task == "active":
    for entry in data:
        for question in entry["questions"]:
            if MODEL not in question:
                continue
            ground_truth_timestamp = question["ground_truth_time_stamp"]
            ground_truth_time = sum(int(x) * 60 ** i for i, x in enumerate(reversed(ground_truth_timestamp.split(":"))))

            task_type = question["task_type"]
            model_answer = question.get(MODEL, None)
            history = model_answer["dialog_history"]
            last_time = history[-1]["time"]

            if model_answer:
                total += 1
                for gap in [0, 1, 2, 3, 4, 5]:
                    stats[f'{task_type}_{gap}']["total"] += 1
                    if abs(last_time - ground_truth_time) <= gap:
                        stats[f'{task_type}_{gap}']["correct"] += 1
else:
    for entry in data:
        for question in entry["questions"]:
            task_type = question["task_type"]
            if MODEL not in question:
                continue
            model_answer = question.get(MODEL, None)[0]
            correct_answer = question["answer"]

            if model_answer:
                total += 1
                stats[task_type]["total"] += 1
                stats["total"]["total"] += 1
                if model_answer == correct_answer:
                    stats[task_type]["correct"] += 1
                    stats["total"]["correct"] += 1

# Calculate accuracy for each task_type
for task_type, counts in stats.items():
    counts["accuracy"] = counts["correct"] / counts["total"] if counts["total"] > 0 else 0

# Save results as a JSON file
with open(f'{MODEL}_stats.json', 'w') as json_file:
    json.dump(stats, json_file, indent=4)

# Save results as a CSV file
with open(f'{MODEL}_stats.csv', 'w', newline='') as csv_file:
    fieldnames = ["task_type", "total", "correct", "accuracy"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    for task_type, counts in stats.items():
        writer.writerow({
            "task_type": task_type,
            "total": counts["total"],
            "correct": counts["correct"],
            "accuracy": counts["accuracy"]
        })

print(f"{total} items have been statisticed")
