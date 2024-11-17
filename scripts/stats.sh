cd ../src/data

# python count.py --model "<model_name>" --task "<real/omini/sqa/proactive>" --src "<output_file>"

python count.py --model "MiniCPM-V" --task "real" --src "real_output_MiniCPM-V.json"
python count.py --model "MiniCPM-V" --task "omini" --src "omini_output_MiniCPM-V.json"
python count.py --model "MiniCPM-V" --task "sqa" --src "sqa_output_MiniCPM-V.json"
python count.py --model "MiniCPM-V" --task "proactive" --src "proactive_output_MiniCPM-V.json"