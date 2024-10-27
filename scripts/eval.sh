cd ../src
EVAL_MODEL="<your_model_name>"

Devices=0
DATA_FILE="./data/questions_real.json"
OUTPUT_FILE="./data/active_output_GPT4o.json"

# Streaming for real-time visual understanding and omini-source understanding
# StreamingSQA for sequential question answering
# StreamingProactive for proactive output
BENCHMARK="Streaming"

# source /yeesuanAI05/miniconda3/etc/profile.d/conda.sh # enable conda change

if [ "$EVAL_MODEL" = "MiniCPM-V" ]; then
    conda activate MiniCPM-V
    CUDA_VISIBLE_DEVICES=$Devices python eval.py --model_name $EVAL_MODEL --benchmark_name $BENCHMARK --data_file $DATA_FILE --output_file $OUTPUT_FILE
