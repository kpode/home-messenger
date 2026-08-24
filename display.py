import tkinter as tk
import os
import platform
import subprocess

active_window = None
active_label = None
close_timer = None

def close_message():
    global active_window, active_label, close_timer

    if active_window is not None:
        active_window.destroy()

    active_window = None
    active_label = None
    close_timer = None


def show_message(root, sender, user_message):
    global active_window, active_label, close_timer

    play_alert()

    if active_window is None:
        active_window = tk.Toplevel(root)
        active_window.attributes("-fullscreen", True)
        active_window.configure(bg="black")

        active_label = tk.Label(
            active_window,
            text=f"NEW MESSAGE FROM {sender.upper()}:\n\n{user_message}",
            font=("Arial", 40, "bold"),
            bg="black",
            fg="white",
            wraplength=1000,
            justify="center"
        )

        active_label.pack(expand=True)

        active_window.bind(
            "<Escape>",
            lambda event: close_message()
        )

    else:
        active_label.config(text=user_message)

    if close_timer is not None:
        active_window.after_cancel(close_timer)

    close_timer = active_window.after(10000, close_message)

def play_alert():
    sound_path = os.path.join(
        os.path.dirname(__file__),
        "assets",
        "notification.mp3"
    )

    system = platform.system()

    if system == "Darwin":
        subprocess.Popen(["afplay", sound_path])

    elif system == "Linux":
        subprocess.Popen(["paplay", sound_path])

    elif system == "Windows":
        import winsound
        winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)