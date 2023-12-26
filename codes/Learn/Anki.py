import time
import pyautogui

'''
中断程序：
way1: 回到此界面，快捷键ctrl+F2: 退出/
way2: 将光标不断移回至屏幕右下角：退出/

'''
n = 1

try:
    while True:
        # 点击"Show"按钮
        pyautogui.click(x=1924, y=1484)  # 替换成实际的按钮坐标

        # 等待1秒
        time.sleep(2)

        # 点击"Hard"按钮
        pyautogui.click(x=1845, y=1484)  # 替换成实际的按钮坐标

        # 等待1秒
        time.sleep(2)

        print(f"Loop: This one is the {n}th word")
        n += 1
except KeyboardInterrupt:
    pass
