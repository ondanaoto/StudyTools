#!/bin/bash

# デフォルト値の設定
BLOCK_INTERVAL=${1:-90}
FOCUS_INTERVAL=${2:-13}
BREAK_INTERVAL=${3:-3}

# Pythonスクリプトに引数を渡す
/path/to/python \
/path/to/StudyTools/src/pomodoro_service.py \
--block_min "$BLOCK_INTERVAL" \
--focus_min "$FOCUS_INTERVAL" \
--break_min "$BREAK_INTERVAL" 