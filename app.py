import tkinter as tk
import threading
import queue

from shared import message_queue
from server import run_server
from display import show_message


def check_queue():
        try:
            new_message = message_queue.get_nowait()
            show_message(root, new_message)
        except queue.Empty:
            pass

        root.after(100, check_queue)


server_thread = threading.Thread(
        target=run_server,
        daemon=True
    )

server_thread.start()

root = tk.Tk()
root.withdraw()

check_queue()

root.mainloop()
