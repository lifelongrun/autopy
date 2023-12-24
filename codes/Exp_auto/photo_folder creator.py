import pyautogui
import time
import os

# 此代码说明
# 在进入到同级文件夹下的一个test文件夹中，再运行此代码（在若没有，则在同级文件夹中创建一个test文件夹）；

def create_unique_folder_name(base_path, folder_name):
    """
    如果存在同名文件夹，则生成一个唯一的文件夹名。
    """
    original_folder_name = folder_name
    count = 1
    while os.path.exists(os.path.join(base_path, folder_name)):
        folder_name = f"{original_folder_name}_{count}"
        count += 1
    return folder_name

# 假设文件浏览器已打开，且基本路径是已知的
 # 更改为实际的基本路径,防止文件夹重名
base_path = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm"
# 更改为期望的文件夹名
folder_name = 've3.5-eq0.6-H100-BBS-55-photo-below15mm'

# 生成唯一的文件夹名

unique_folder_name = create_unique_folder_name(base_path, folder_name)


# 模拟点击“浏览”按钮
# 假设浏览按钮的屏幕坐标为(100, 200)
pyautogui.click(2466, 665)

# 等待窗口反应
time.sleep(1)

# 模拟按键返回上一级文件夹
# 对于不同的操作系统，这个快捷键可能不同
pyautogui.hotkey('alt', 'up')

# 等待窗口反应
time.sleep(1)

# 模拟按键Ctrl+Shift+N创建新文件夹
pyautogui.hotkey('ctrl', 'shift', 'n')

# 等待新文件夹窗口打开
time.sleep(1)

# 输入新文件夹的名称，假设为“MyNewFolder”，然后按 Enter
pyautogui.write(unique_folder_name)
# time.sleep(0.5)
pyautogui.press('enter')

# 等待文件夹创建
time.sleep(1)

# 选中新创建的文件夹
# 这通常需要特定的逻辑来定位新文件夹，这里只是一个示例
pyautogui.press('down')

# 等待选中反应
time.sleep(1)

# 模拟点击“确认”按钮
# 假设确认按钮的屏幕坐标为(200, 300)
pyautogui.click(1636, 1243)
print(f"------it's done------\n folder: {folder_name} is created")