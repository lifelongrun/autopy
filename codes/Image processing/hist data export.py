import cv2
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from PIL import Image



# 示例用法
image_path = r"E:\OneDrive\00_To_Do\Image proccessing\export\Img053-cropped.jpg"  # 替换为你的图像文件路径

img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"


image_median_blur = cv2.medianBlur(img, 17)  # 这里的窗口大小mXm要为奇数
# Otsu's thresholding
ret2, th2 = cv2.threshold(image_median_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 绘制图像与直方图
plt.figure(figsize=(12, 6))

# 显示原始图像
plt.subplot(2, 2, 1)
plt.imshow(img, 'gray')
plt.title('Original Image')
# plt.xticks([]), plt.yticks([])  # 删除此行来显示x、y轴的刻度

# 显示原始图像的直方图
plt.subplot(2, 2, 2)
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Histogram of Original Image')
# plt.xticks([]), plt.yticks([])  # 删除此行来显示x、y轴的刻度

# 显示经Otsu阈值处理后的图像
plt.subplot(2, 2, 3)
plt.imshow(th2, 'gray')
plt.title("Otsu's Thresholding")
# plt.xticks([]), plt.yticks([])  # 删除此行来显示x、y轴的刻度

# 显示经Otsu阈值处理后的图像的直方图
plt.subplot(2, 2, 4)
plt.hist(th2.ravel(), 256, [0, 256])
plt.title("Histogram of Otsu's Thresholding")
# plt.xticks([]), plt.yticks([])  # 删除此行来显示x、y轴的刻度

plt.show()
# 假设hist是直方图的y轴信息，bins是x轴信息
# hist, bins = np.histogram(img.ravel(), 256, [0, 256])

# 将直方图数据转换为pandas DataFrame
# pd.DataFrame({'Gray Level': bins[:-1], 'Frequency': hist}).to_excel("histogram.xlsx")


# 导出滤波后的图像为PDF
# image_median_blur_pil = Image.fromarray(image_median_blur)
# image_median_blur_pil.save('median_blur_image.pdf', "PDF", resolution=600.0)

# 将OpenCV图像转换为PIL图像格式
# th2_pil = Image.fromarray(th2)
# 使用PIL保存图像为PDF
# th2_pil.save('otsu_image.pdf', "PDF", resolution=600.0)
