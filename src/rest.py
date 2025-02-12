# notification_schedule.py
import os
import time
import argparse
from datetime import datetime, timedelta
from playsound import playsound  # Required if playsound is not installed

from constants import HIIT_FOCUS_SEC, HIIT_BREAK_SEC, HIIT_BROCK_SEC, HIIT_BLOCK_ITER, HIIT_EPOCH

# Function to play the specified sound
def play_sound(sound_name):
    print(f"Notification sound for {sound_name} played at {datetime.now().strftime('%H:%M:%S')}.")
    sound_path = os.path.join(os.path.dirname(__file__), 'sounds', f"{sound_name}.mp3")
    playsound(sound_path)

def alarm(rest_sec: int):
    current_time = datetime.now()
    play_sound('break_start')
    time.sleep(rest_sec)
    play_sound('interval_end')

def main():
    parser = argparse.ArgumentParser(description="Set the schedule for rest.")
    parser.add_argument("--rest_sec", type=int, default=240, help="Seconds to take a rest (default: 240 sec)")

    args = parser.parse_args()
    alarm(args.rest_sec)

if __name__ == '__main__':
    main()
