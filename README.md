- [StudyTools](#studytools)
  - [Abstract](#abstract)
  - [Setup](#setup)
  - [ツール](#ツール)
    - [ポモドーロタイマー](#ポモドーロタイマー)
      - [機能](#機能)
    - [使い方](#使い方)


# StudyTools
## Abstract
自分が普段勉強するのに利用しているツールをまとめています。
## Setup
1. このリポジトリをクローンします。
2. pythonをインストールしておきます。
3. `pip install -r requirements.txt`で必要なモジュールをインストールします。python環境を汚したくないので、仮想環境を作っておくことをおすすめします。
## ツール
### ポモドーロタイマー
#### 機能
一定の時間の間、作業開始のアラームと休憩開始のアラーム音を交互に鳴らします。
### 使い方
1. `shells/pomodoro_timer_template.sh`を編集して`pomodoro_timer.sh`として保存します(保存場所はどこでも良いです)。
  - `/path/to/python`はpythonのパスに書き換えます(venv使う場合は`/path/to/StudyTools/`+`venv/bin/python`になります)。
  - `/path/to/pomodoro_service.py`は`pomodoro_service.py`のパスに書き換えます。
  - ブロック時間、集中時間、休憩時間を分単位で設定します。今回は90, 13, 3にしていますがお好きな時間に変更してください。
2. `pomodoro_timer.sh`を実行します。

もしくはsrc/pomodoro_service.pyを直接実行しても同じです。デフォルト値はsrc/constants.pyに書いているので適当に変更してください。