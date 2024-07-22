import time
import pyautogui
import keyboard  # 需要安装 keyboard 库

'''
中断程序：
way1: 回到此界面，快捷键ctrl+F2: 退出/
way2: 将光标不断移回至屏幕右下角：退出/
'''


def exit_loop():
    if keyboard.is_pressed('esc'):  # 按下 'Esc' 键中断程序
        print("Process interrupted by user.")
        return True
    return False


n = 1

try:
    while n <= 49:
        if exit_loop():
            break

        # 进入deck界面后，出现卡片的正面，然后运行脚本将自动点击"Show Answer"按钮
        pyautogui.click(x=1280, y=1484)  # 替换成实际的按钮坐标

        # 等待
        time_pron = 2.75
        time.sleep(time_pron)

        if exit_loop():
            break

        # 点击"Hard"按钮
        pyautogui.click(x=1200, y=1484)  # 替换成实际的按钮坐标

        # 等待
        time_meaning = 2.75
        time.sleep(time_meaning)

        print(f"Loop: This one is the {n}th word")
        n += 1

    print(f"The total time of this deck cost you in 🤺{n * (time_pron + time_meaning) / 60} mins")
except KeyboardInterrupt:
    print("Error: The process is stopped")
    pass
