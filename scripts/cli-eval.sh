# export HF_ENDPOINT="https://hf-mirror.com"
# export HUGGINGFACE_HUB_CACHE="/yeesuanAI05/thumt/wzh/huggingface_cache"
# export HF_HOME="/yeesuanAI05/thumt/wzh/huggingface_cache"
# export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128
# export DECORD_EOF_RETRY_MAX=20480
cd ../src
EVAL_MODEL="GPT4o"

Devices=0
DATA_FILE="./data/questions_1.json"
OUTPUT_FILE="./data/active_output_GPT4o.json"
BENCHMARK="StreamingActive"

# source /yeesuanAI05/miniconda3/etc/profile.d/conda.sh # enable conda change

if [ "$EVAL_MODEL" = "MiniCPM-V" ]; then
    conda activate MiniCPM-V
    CUDA_VISIBLE_DEVICES=$Devices python eval.py --model_name $EVAL_MODEL --benchmark_name $BENCHMARK --data_file $DATA_FILE --output_file $OUTPUT_FILE

if [ "$EVAL_MODEL" = "GPT4o" ]; then
    python eval.py --model_name $EVAL_MODEL --benchmark_name $BENCHMARK --data_file $DATA_FILE --output_file $OUTPUT_FILE
