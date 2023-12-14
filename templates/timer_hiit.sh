#!/bin/bash

# デフォルト値の設定
FOCUS_INTERVAL=${1:-20}
BREAK_INTERVAL=${2:-10}
BLOCK_ITER=${3:-4}
BLOCK_BREAK_INTERVAL=${4:-60}
EPOCH=${5:-2}


# Pythonスクリプトに引数を渡す
/path/to/python \
/path/to/StudyTools/src/pomodoro_service.py \
--focus_sec "$FOCUS_INTERVAL" \
--break_sec "$BREAK_INTERVAL" \
--block_break_sec "$BLOCK_BREAK_INTERVAL" \
--block_iter "$BLOCK_ITER" \
--epoch "$EPOCH"