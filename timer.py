import time
import tkinter as tk
from tkinter import StringVar, IntVar
from datetime import datetime
from threading import Thread
import pygame  # For cross-platform audio playback

# Initialize pygame mixer for sound
pygame.mixer.init()

# Creating a window
window = tk.Tk()
window.geometry('600x600')
window.title('Artemis')

head = tk.Label(window, text="Countdown Clock and Timer", font=('Calibri', 15))
head.pack(pady=20)

tk.Label(window, text="Enter time in HH:MM:SS", font=('bold', 12)).pack(pady=5)

hour = StringVar()
minute = StringVar()
second = StringVar()

tk.Entry(window, textvariable=hour, width=10).pack()
tk.Entry(window, textvariable=minute, width=10).pack()
tk.Entry(window, textvariable=second, width=10).pack()

play_sound = IntVar()
tk.Checkbutton(window, text='Check for Music', variable=play_sound).pack(pady=10)

def countdown():
    try:
        h = int(hour.get() or 0)
        m = int(minute.get() or 0)
        s = int(second.get() or 0)
        total_seconds = h * 3600 + m * 60 + s

        def run_timer():
            nonlocal total_seconds
            while total_seconds > 0:
                mins, secs = divmod(total_seconds, 60)
                time_display = f"{mins:02d}:{secs:02d}"
                timer_label.config(text=time_display)
                window.update()
                time.sleep(1)
                total_seconds -= 1

            timer_label.config(text="Time-Up", font=('bold', 20))
            notify_timer_end()

        timer_thread = Thread(target=run_timer)
        timer_thread.start()

    except ValueError:
        timer_label.config(text="Invalid Input", font=('bold', 12))

def notify_timer_end():
    if play_sound.get():
        pygame.mixer.music.load("spidgetfinners.mp3")  # Replace with your sound file
        pygame.mixer.music.play()

timer_label = tk.Label(window, text="", font=('Calibri', 20))
timer_label.pack(pady=20)

tk.Button(window, text="Set Countdown", command=countdown, bg='yellow').pack(pady=10)

def update_time():
    now = datetime.now().strftime("%H:%M:%S")
    current_time_label.config(text=f"Current Time: {now}")
    window.after(1000, update_time)

current_time_label = tk.Label(window, text="", font=('Calibri', 12))
current_time_label.pack(pady=20)
update_time()

window.mainloop()