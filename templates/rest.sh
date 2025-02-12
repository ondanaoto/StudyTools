#! /bin/bash

# デフォルト値の設定
BREAK_INTERVAL=${1:-240}

# Pythonスクリプトに引数を渡す
/path/to/python \
/path/to/StudyTools/src/rest.py \
--rest_sec "$BREAK_INTERVAL"
