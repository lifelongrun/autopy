import tkinter as tk
import pyautogui
import time
import threading

def countdown(t, n):
    while t > 0:
        label.config(text=f"拍摄状态：正在拍摄第{n}张照片，剩余时间：{t}秒")
        root.update()
        time.sleep(1)
        t -= 1

def update_label():
    n = 1
    while n <= 10:
        pyautogui.click(coords["click"])
        countdown(int(t1), n)
        n += 1
    label.config(text="------it's done------")

# Tkinter setup
root = tk.Tk()
root.title("Photo Status")

# Define coordinates and time interval
coords = {"click": (2011, 197)}
t1 = 5.5

label = tk.Label(root, text="------it starts------")
label.pack()

# Start the process in a separate thread
thread = threading.Thread(target=update_label)
thread.start()

root.mainloop()
