import cv2
import numpy as np

# 载入图片
image_path = '/mnt/data/Img1097-cropped.jpg'
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# 锐化图片
# 定义一个锐化的核
sharpening_kernel = np.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])
sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

# 高斯处理
gaussian_blur = cv2.GaussianBlur(sharpened_image, (5, 5), 0)

# 二值化处理
# 转换为灰度图像
gray_image = cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2GRAY)
# 应用二值化
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 转为numpy格式储存像素信息
numpy_array = np.array(binary_image)

# 寻找火焰最顶部和最底部的像素
# 因为火焰和背景对比度高，可以通过找到最顶端和最底端的白色像素来确定火焰的长度
# 由于二值化后，火焰应该是白色（255），我们搜索最顶部和最底部的白色像素
non_zero_columns = np.where(numpy_array.max(axis=0) > 0)[0]
non_zero_rows = np.where(numpy_array.max(axis=1) > 0)[0]

if non_zero_columns.any() and non_zero_rows.any():
    top_row = non_zero_rows[0]
    bottom_row = non_zero_rows[-1]

    # 根据题目要求，原图高度像素为500mm，计算火焰的实际高度
    image_height_mm = 500
    image_height_px = image.shape[0]
    pixel_to_mm_ratio = image_height_mm / image_height_px

    # 计算火焰长度
    flame_height_px = bottom_row - top_row
    flame_height_mm = flame_height_px * pixel_to_mm_ratio

    # 输出火焰长度
    print(f"Fire length in pixels: {flame_height_px}px")
    print(f"Fire length in mm: {flame_height_mm}mm")

    # 在图片上标记火焰的长度
    marked_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)
    cv2.line(marked_image, (0, top_row), (marked_image.shape[1], top_row), (0, 255, 0), 2)
    cv2.line(marked_image, (0, bottom_row), (marked_image.shape[1], bottom_row), (0, 0, 255), 2)

    # 保存标记后的图片
    marked_image_path = '/mnt/data/Img1097-marked.jpg'
    cv2.imwrite(marked_image_path, marked_image)
else:
    print("Unable to find the flame in the image.")
    flame_height_mm = None
    marked_image_path = None

# 返回火焰高度和标记后的图片路径
flame_height_mm, marked_image_path

