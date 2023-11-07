# notification_schedule.py
import os
import time
import argparse
from datetime import datetime, timedelta
from playsound import playsound  # Required if playsound is not installed

from constants import FOCUS_MIN, BREAK_MIN, BROCK_MIN

# Function to play the specified sound
def play_sound(sound_name):
    print(f"Notification sound for {sound_name} played at {datetime.now().strftime('%H:%M:%S')}.")
    sound_path = os.path.join(os.path.dirname(__file__), 'sounds', f"{sound_name}.mp3")
    playsound(sound_path)

# Function to set scheduled notifications
def set_schedule(start_time, block_min, focus_min, break_min):
    # Set the schedule for the specified start time
    current_time = start_time
    repeat_count = block_min // (focus_min + break_min)  # Repeat for the number of times that fits into one set
    last_focus_time = block_min % (focus_min + break_min)  # The last focus time will be shorter
    
    yield current_time, 'focus_start'
    for i in range(repeat_count):  # Repeat sets of A and B notifications five times
        current_time += timedelta(minutes=focus_min)
        yield current_time, 'break_start'
        current_time += timedelta(minutes=break_min)
        yield current_time, 'focus_start'
    current_time += timedelta(minutes=last_focus_time)
    yield current_time, 'interval_end'

def main():
    parser = argparse.ArgumentParser(description="Set the schedule for notifications.")
    parser.add_argument("--block_min", type=int, default=BROCK_MIN, help=f"Minutes to continue the repeat (default: {BROCK_MIN} min)")
    parser.add_argument("--focus_min", type=int, default=FOCUS_MIN, help=f"Minutes until the first notification (default: {FOCUS_MIN} min)")
    parser.add_argument("--break_min", type=int, default=BREAK_MIN, help=f"Minutes until the second notification (default: {BREAK_MIN} min)")
    args = parser.parse_args()

    # Use the current time as the start time
    start_time = datetime.now()

    # Set the schedule
    schedule = set_schedule(start_time, args.block_min, args.focus_min, args.break_min)

    # Execute notifications according to the schedule
    for notify_time, sound in schedule:
        while datetime.now() < notify_time:
            time.sleep(1)  # Check every second
        play_sound(sound)

if __name__ == '__main__':
    main()