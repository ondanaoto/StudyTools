- [StudyTools](#studytools)
  - [Abstract](#abstract)
  - [Setup](#setup)
  - [ツール](#ツール)
    - [ポモドーロタイマー](#ポモドーロタイマー)
      - [機能](#機能)
      - [環境設定](#環境設定)
      - [使い方](#使い方)
    - [HIITタイマー](#hiitタイマー)
      - [機能](#機能-1)
      - [環境設定](#環境設定-1)
      - [使い方](#使い方-1)
  - [謝辞](#謝辞)


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
#### 環境設定
1. `templates/timer_pomodoro.sh`を編集して`pomodoro.sh`として保存します(保存場所はどこでも良いですが、`StudyTools/timer`ディレクトリはgitで追跡しないように設定しているのでここを推奨しています)。
   - `/path/to/python`はpythonのパスに書き換えます(venvを使う場合は`/path/to/StudyTools/`+`venv/bin/python`になります)。
   - `/path/to/pomodoro_service.py`は`pomodoro_service.py`のパスに書き換えます。
   - ブロック時間、集中時間、休憩時間を分単位で設定します。今回は90, 13, 3にしていますがお好きな時間に変更してください。
2. `pomodoro.sh`に実行権限を与えます。
  ```
  chmod +x /path/to/StudyTools/timer/pomodoro.sh
  ```
#### 使い方
`pomodoro.sh`を実行します。
```
/path/to/StudyTools/timer/pomodoro.sh
```
もしくはsrc/pomodoro_service.pyを直接実行しても同じです。デフォルト値はsrc/constants.pyに書いているので適当に変更してください。
### HIITタイマー
#### 機能
HIIT(High Intensity Interval Training)のタイマーです。トレーニング時間と休憩時間を交互に繰り返します。
#### 環境設定
1. `templates/timer_hiit.sh`を編集して`hiit.sh`として保存します(保存場所はどこでも良いですが、`StudyTools/timer`ディレクトリはgitで追跡しないように設定しているのでここを推奨しています)。
    - `/path/to/python`はpythonのパスに書き換えます(venvを使う場合は`/path/to/StudyTools/`+`venv/bin/python`になります)。
   - `/path/to/hiit_service.py`は`hiit_service.py`のパスに書き換えます。
   - トレーニング時間・休憩時間・セット間の休憩時間を秒単位で、セット内連続回数・セット数を整数で設定します。今回は20, 10, 60, 4, 2にしていますがお好きな時間に変更してください。
2. `hiit.sh`に実行権限を与えます。
  ```
  chmod +x /path/to/StudyTools/timer/hiit.sh
  ```
#### 使い方
`hiit.sh`を実行します。
```
/path/to/StudyTools/timer/hiit.sh
```
もしくはsrc/hiit_service.pyを直接実行しても同じです。デフォルト値はsrc/constants.pyに書いているので適当に変更してください。
## 謝辞
効果音は以下のサイトからお借りしています。ありがとうございます。

https://soundeffect-lab.info/sound/button/