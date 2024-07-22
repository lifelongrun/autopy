import time
import pyautogui
import keyboard
import threading
import tkinter as tk
from tkinter import messagebox
import json
import os

# 定义配置文件路径
config_file = "config.json"

# 默认配置
default_config = {
    "n": 50,
    "time_pron": 2.5,
    "time_meaning": 3
}

# 加载配置
def load_config():
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            return json.load(file)
    else:
        return default_config

# 保存配置
def save_config(config):
    with open(config_file, "w") as file:
        json.dump(config, file)

def exit_loop():
    if keyboard.is_pressed('esc'):
        log("Process interrupted by user.")
        return True
    return False

# 全局变量
pause = False
stop = False
click_thread = None

def start_clicking(n, time_pron, time_meaning):
    try:
        for i in range(1, n + 1):
            if stop:
                break
            while pause:
                time.sleep(0.1)

            if exit_loop():
                break

            pyautogui.click(x=1280, y=1484)
            time.sleep(time_pron)

            if stop:
                break
            while pause:
                time.sleep(0.1)

            if exit_loop():
                break

            pyautogui.click(x=1200, y=1484)
            time.sleep(time_meaning)

            log(f"Loop: This one is the {i}th word")

        log(f"The total time of this deck cost you in 🤺{n * (time_pron + time_meaning) / 60} mins")
    except KeyboardInterrupt:
        log("Error: The process is stopped")
        pass

def start_thread():
    global stop, click_thread
    stop = False
    try:
        n = int(n_var.get())
        time_pron = float(time_pron_var.get())
        time_meaning = float(time_meaning_var.get())

        # 保存当前配置
        current_config = {
            "n": n,
            "time_pron": time_pron,
            "time_meaning": time_meaning
        }
        save_config(current_config)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for all fields.")
        return

    log("Starting auto clicker...")
    click_thread = threading.Thread(target=start_clicking, args=(n, time_pron, time_meaning))
    click_thread.start()

def toggle_pause():
    global pause
    pause = not pause
    if pause:
        log("Paused")
    else:
        log("Resumed")

def stop_program():
    global stop
    stop = True
    if click_thread and click_thread.is_alive():
        click_thread.join()
    root.destroy()

def reset():
    global pause, stop, click_thread
    pause = False
    stop = True
    if click_thread and click_thread.is_alive():
        click_thread.join()
    log_text.config(state=tk.NORMAL)
    log_text.delete('1.0', tk.END)
    log_text.config(state=tk.DISABLED)
    n_var.set(str(config["n"]))
    time_pron_var.set(str(config["time_pron"]))
    time_meaning_var.set(str(config["time_meaning"]))
    log("Reset complete.")

def log(message):
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, message + "\n")
    log_text.config(state=tk.DISABLED)
    log_text.see(tk.END)

# 加载配置
config = load_config()

root = tk.Tk()
root.title("Auto Clicker")
root.geometry("400x500")

n_var = tk.StringVar(value=str(config["n"]))
time_pron_var = tk.StringVar(value=str(config["time_pron"]))
time_meaning_var = tk.StringVar(value=str(config["time_meaning"]))

tk.Label(root, text="Number of loops for total words (n):").pack(pady=5)
n_entry = tk.Entry(root, textvariable=n_var)
n_entry.pack(pady=5)

tk.Label(root, text="Time(s) for pronunciation (time_pron):").pack(pady=5)
time_pron_entry = tk.Entry(root, textvariable=time_pron_var)
time_pron_entry.pack(pady=5)

tk.Label(root, text="Time(s) for meaning (time_meaning):").pack(pady=5)
time_meaning_entry = tk.Entry(root, textvariable=time_meaning_var)
time_meaning_entry.pack(pady=5)

start_button = tk.Button(root, text="Start", command=start_thread)
start_button.pack(pady=20)

pause_button = tk.Button(root, text="Pause/Resume", command=toggle_pause)
pause_button.pack(pady=20)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(pady=20)

exit_button = tk.Button(root, text="Exit", command=stop_program)
exit_button.pack(pady=20)

log_text = tk.Text(root, state=tk.DISABLED, height=10)
log_text.pack(pady=10)

root.mainloop()