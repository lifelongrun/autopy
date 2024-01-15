import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

# 指定使用的字体，例如 SimHei 是一个包含中文字符的字体
plt.rcParams['font.sans-serif'] = ['SimHei']

def process_flame_image(image_path):
    # ------图像预处理
    # :param image_path: 图片路径
    # :return: 二值化后的图片
    if image_path is None:
        raise ValueError("Error: Binary image not found.")
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # 预处理A: 锐化图片
    height, width = image.shape[:2] # 获取图像的尺寸
    ksize = int(min(height, width) * 0.02) # 根据图像尺寸计算锐化核的大小
    if ksize % 2 == 0:
        ksize += 1
    print(f"Ksize: {ksize}")
    print(f"Image shape: {image.shape}")
    # 定义一个锐化的核
    sharpening_kernel = np.array([[-1, -1, -1],
                                  [-1, ksize/2, -1],
                                  [-1, -1, -1]])
    # image = cv2.filter2D(image, -1, sharpening_kernel) #深度为-1，表示输出图像与原图像有相同的深度
    # sharpened_image = image # 用于显示的锐化后的图像
    image_median_blur = cv2.medianBlur(image, 13) # 这里的窗口大小mXm要为奇数
    # 高斯处理
    # gaussian_blur = cv2.GaussianBlur(image, (ksize, ksize), 1)  #sigmaX=0,sigmaY=0，表示从ksize计算, sigma越大，图像越模糊
    # 应用二值化:OTSU算法
    _, binary_image = cv2.threshold(image_median_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # show
    # plt.imshow(binary_image, "gray")
    # plt.imshow(binary_image, cmap='gray')
    # plt.show()

    return binary_image

def find_fire_height(binary_image , binary_image_path, image_height_mm=500):
    # 传入参数: 二值化图像, 图像路径, 图像的实际高度（毫米）
    # 加载已经处理过的二值化图像

    if binary_image is None:
        raise ValueError("Error: Binary image not found.")
    top_row = find_top_row(binary_image) # 调用函数: 寻找火焰最顶部的像素

    if top_row is not None:
        # 计算火焰的实际高度
        pixel_to_mm_ratio = image_height_mm / binary_image.shape[0]
        flame_height_px = binary_image.shape[0] - top_row
        flame_height_mm = flame_height_px * pixel_to_mm_ratio

        # 标记火焰的长度并保存标记后的图像
        marked_image = mark_fire_height(binary_image.copy(), top_row) # 调用函数:标记出火焰的顶点位置
        # marked_image_path = 'mage-marker-01-11.jpg'
        # plt.imshow(marked_image)
        # plt.title("标记后的图片")
        # plt.axis('on')
        # plt.show()
        # cv2.imwrite(marked_image_path, marked_image)

        # 原图片名称
        original_image_basename = os.path.basename(binary_image_path)
        # 标记后的图片名称
        marked_image_basename = original_image_basename.replace(".jpg", "-marked.jpg")

        image_basename = os.path.dirname(binary_image_path)

        # os.path.join 仅用于生成路径字符串，并不涉及文件系统的实际操作。
        marked_image_path = os.path.join(image_basename, marked_image_basename) # 保存标记后的.jpg格式图像
        # 检查目录是否存在，如果不存在，则创建它
        if not os.path.exists(os.path.dirname(marked_image_path)):
            os.makedirs(os.path.dirname(marked_image_path))
        cv2.imwrite(marked_image_path, marked_image)

    else:
        print("Unable to find the flame in the image.")
        flame_height_mm = None
        marked_image_path = None

    return flame_height_mm, marked_image

def find_top_row(binary_image):
    #寻找火焰最顶部的像素
    non_zero_rows = np.where(binary_image.max(axis=1) > 0)[0]
    if non_zero_rows.any():
        return non_zero_rows[0]
    else:
        return None
# 标记出火焰的顶点位置
def mark_fire_height(image, top_row):
    cv2.line(image, (0, top_row), (image.shape[1], top_row), (255, 0, 0), 5)
    return image
def process_folder_and_get_statistics(folder_path, image_height_mm=500):
    # 处理文件夹中的.jpg文件并获取均值和标准差的函数
    # 参数:
    #   - folder_path: 文件夹路径
    #   - image_height_mm: 图像的实际高度（毫米）
    # 返回:
    #   - 均值和标准差的元组 (mean_height, std_deviation)
    # 获取.jpg文件列表
    jpg_files = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith('.jpg')]
    # 先收集创建dataframe所需的数据，然后再一次性赋值给DataFrame
    flame_heights = [] # 用于储存火焰高度
    indexes = [] # 用于储存对应的图像文件名
    # 遍历.jpg文件并获取火焰高度，然后将其添加到DataFrame中
    for jpg_file in jpg_files:
        binary_image = process_flame_image(jpg_file) # 调用函数:处理图像, 返回二值化图像

        if binary_image is not None:
            flame_height_mm, marked_image = find_fire_height(binary_image, jpg_file, image_height_mm) # 调用函数:计算火焰高度

            if flame_height_mm is not None:
                index = os.path.basename(jpg_file)
                indexes.append(index)
                flame_heights.append(flame_height_mm)
                # print(f"图像:{index}, 火焰高度: {flame_height_mm}mm")
    # 循环结束后，一次性创建 DataFrame
    df_flame_height = pd.DataFrame({'Flame Height (mm)': flame_heights}, index=indexes)

    # 计算均值和标准差
    mean_height = df_flame_height['Flame Height (mm)'].mean()
    std_deviation = df_flame_height['Flame Height (mm)'].std()
    # print(f"均值: {mean_height}mm, 标准差: {std_deviation}mm")
    # 创建一个新的 DataFrame 来存储统计数据
    stats_df = pd.DataFrame({'Flame Height (mm)': ['Mean', 'Standard Deviation'], 'Value': [mean_height, std_deviation]})

    # 将统计数据的 DataFrame 连接到原始 DataFrame 的底部
    df_combined = pd.concat([df_flame_height, stats_df], ignore_index=False)
    write_path = os.path.join(folder_path, "flame-height.csv")

    # 检查目录是否存在，如果不存在，则创建它
    if not os.path.exists(os.path.dirname(write_path)):
        os.makedirs(os.path.dirname(write_path))

    df_combined.to_csv(write_path, index=True, encoding='utf_8_sig')
    print(df_combined)
    return mean_height, std_deviation

# 调用函数并传入文件夹路径
# folder_path = r'E:\OneDrive\00_To_Do\Image proccessing\ve2.0-eq0.6-H20-BB-photo-cropped-copy'
# folder_path = r'E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.7-H00-BB-photo-cropped'
folder_path = r'E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.8-H00-BB-photo-cropped'
mean_height, std_deviation = process_folder_and_get_statistics(folder_path)
# print(f"均值: {mean_height}; 标准差: {std_deviation}")
