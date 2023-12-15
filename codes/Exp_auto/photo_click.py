import pyautogui
import time
import keyboard

# 定义坐标（控制窗口大小为1/2屏幕，位于屏幕右侧位置）
coords = {
    "click": (2011, 197),
}

t1 = 5.5 # 间隔时间
n = 1 # 点击数量
print(f"------it starts------")
while n <= 10:
    pyautogui.click(coords["click"])
    print(f"拍摄状态：已拍摄第{n}张照片")
    time.sleep(t1)
    n += 1
print(f"------it's done------")