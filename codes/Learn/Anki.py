import time
import pyautogui


# ctrl+F2: 退出

# 等待Anki程序启动并获得焦点

pyautogui.click(x=1481, y=1568)  # 替换成Anki窗口的坐标
time.sleep(2)  # 可能需要根据Anki启动时间进行调整
pyautogui.click(x=920, y=735)  # 替换成Anki窗口中需要进入的卡牌组的坐标
time.sleep(1)
pyautogui.click(x=1447, y=597)  # 替换成Anki窗口中需要进入的卡牌组的坐标
time.sleep(1)
# 手动进入卡牌组，等待更新，点击“Study"按钮,进入到单词卡牌界面

try:
    while True:
        # 点击"Show"按钮
        pyautogui.click(x=1277, y=1151)  # 替换成实际的按钮坐标

        # 等待1秒
        time.sleep(1)

        # 点击"Hard"按钮
        pyautogui.click(x=1206, y=1250)  # 替换成实际的按钮坐标

        # 等待1秒
        time.sleep(1)
except KeyboardInterrupt:
    pass
