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

# Function to set scheduled notifications
def set_schedule(start_time, focus_sec, break_sec, block_break_sec, block_iter, epoch):
    # Set the schedule for the specified start time
    current_time = start_time  # Repeat for the number of times that fits into one set
    
    for epoch_cnt in range(epoch):
        for block_cnt in range(block_iter):  # Repeat sets of A and B notifications five times
            yield current_time, 'focus_start'
            current_time += timedelta(seconds=focus_sec)
            
            if block_cnt == block_iter-1:
                break
            yield current_time, 'break_start'
            current_time += timedelta(seconds=break_sec)
            
        if epoch_cnt == epoch-1:
            break
        yield current_time, 'block_break_start'
        current_time += timedelta(seconds=block_break_sec)
        
    yield current_time, 'interval_end'

def main():
    parser = argparse.ArgumentParser(description="Set the schedule for notifications.")
    parser.add_argument("--focus_sec", type=int, default=HIIT_FOCUS_SEC, help=f"Seconds until the first notification (default: {HIIT_FOCUS_SEC} sec)")
    parser.add_argument("--break_sec", type=int, default=HIIT_BREAK_SEC, help=f"Seconds until the second notification (default: {HIIT_BREAK_SEC} sec)")
    parser.add_argument("--block_break_sec", type=int, default=HIIT_BROCK_SEC, help=f"Seconds until the second notification (default: {HIIT_BROCK_SEC} sec)")
    parser.add_argument("--block_iter", type=int, default=HIIT_BLOCK_ITER, help=f"Number of block iterations (default: {HIIT_BLOCK_ITER})")
    parser.add_argument("--epoch", type=int, default=HIIT_EPOCH, help=f"Number of epochs (default: {HIIT_EPOCH})")
    
    args = parser.parse_args()

    # Use the current time as the start time
    start_time = datetime.now()

    # Set the schedule
    schedule = set_schedule(
        start_time=start_time, 
        focus_sec=args.focus_sec, 
        break_sec=args.break_sec,
        block_break_sec=args.block_break_sec,
        block_iter=args.block_iter,
        epoch=args.epoch
        )

    # Execute notifications according to the schedule
    for notify_time, sound in schedule:
        while datetime.now() < notify_time:
            time.sleep(1)  # Check every second
        play_sound(sound)

if __name__ == '__main__':
    main()