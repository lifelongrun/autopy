import pyautogui
import time
import keyboard

# 定义坐标
coords = {
    "暂停采集": (173, 69),
    "水平轴设定位置": (1016, 425),
    "水平轴定位": (949, 355),
    "继续采集": (173, 69),
    "竖直轴设定位置": (1206, 426),
    "竖直轴定位": (1140, 352),
    "导出数据": (280, 70)
}

t1 = 4 # 定位时间
t2 = 60 # 采集时间
n = 8 # 文本框清空位数

# 竖直轴采集
A_n = -10  # axial初始值
R_n = -10 # lateral初始值
while A_n >= -400:
    # 设置步长
    if A_n > -50:
        step = -5
    elif A_n > -100:
        step = -10
    else:
        if A_n == -160:
            t2 = t2/2  # 后面位置采集时间减半
        step = -20
    print(f"暂停采集,竖直轴设定位置：{A_n}")
    pyautogui.click(coords["暂停采集"])
    # 竖直位置设定
    pyautogui.click(coords["竖直轴设定位置"])
    for _ in range(n):
        pyautogui.press('backspace')  # 从右向左清空文本框
    pyautogui.write(str(A_n), interval=0.25)
    # 竖直位置写入
    print(f"竖直轴定位：{A_n}，此时等待{t1}s")
    pyautogui.click(coords["竖直轴定位"])
    # time.sleep(t1)

    # ------水平采集------
    # 水平轴采集
    if R_n >= -70:
        pyautogui.click(coords["水平轴设定位置"])
        for _ in range(n):
            pyautogui.press('backspace')  # 从右向左清空文本框
        pyautogui.write(str(R_n), interval=0.25)
        print(f"水平轴定位：{R_n}，此时等待{t1}s")
        pyautogui.click(coords["水平轴定位"])
        # time.sleep(t1)
        if R_n == -70:
            print(f"------水平轴位置数据读取结束，现在开始读取剩余竖直轴位置数据！------")
    else:
        print("水平轴位置读取已结束！")
    # ------水平采集------
    time.sleep(t1)
    pyautogui.click(coords["竖直轴定位"])  # 取消定位
    if R_n >= -70:
        pyautogui.click(coords["水平轴定位"])  # 取消定位
        R_n -= 10  # 更新R_n,直到-80跳出本if条件语句
    pyautogui.click(coords["继续采集"])
    print(f"继续采集,倒计时{t2}s")
    time.sleep(t2)  # 数据采集停留时间
    print(f"{t2}倒计时结束！")
    A_n += step  # 更新A_n的值

print(f"------竖直轴与水平轴位置数据均读取结束，数据导出！------")
# 导出数据
pyautogui.click(coords["导出数据"])
