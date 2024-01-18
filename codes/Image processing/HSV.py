import cv2
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 例如使用"SimHei"字体
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False    # 解决负号'-'显示为方块的问题


# 读取火焰图像
image = cv2.imread(r'E:\Github-autopy\codes\Image processing\thin_blue_tail.jpg', cv2.COLOR_BGR2RGB)

# ------新增代码
# 将图像转换为HSV格式
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 对HSV格式的图像进行直方图均衡化（只对V通道进行）
hsv_img[:,:,2] = cv2.equalizeHist(hsv_img[:,:,2])

# 将处理后的HSV图像转换回BGR格式以显示
equ_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
equ_img_gray = cv2.cvtColor(equ_img, cv2.COLOR_BGR2GRAY)
equ_img_gray_blur = cv2.medianBlur(equ_img_gray, 3)


# 使用matplotlib显示原始图像和处理后的图像
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) # OpenCV使用BGR格式，而matplotlib使用RGB格式
plt.title('原始图像')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(equ_img, cv2.COLOR_BGR2RGB))
plt.title('直方图均衡化后的图像')
plt.axis('off')

plt.show()
# -----------------


# 转换图像为灰度
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
plt.imshow(image)
plt.show()
# Normalize the image histogram
normalized_image = cv2.normalize(gray_image, None, 0, 255, cv2.NORM_MINMAX)

gray_image = cv2.medianBlur(gray_image, 7)
# 使用自适应阈值处理
# binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 33, 2)
binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# threading = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 33, 2)
threading = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
title = [ "image", "gray", "normalized", "binary", "equ_img_gray_blur", "threading"]
images = [image, gray_image, normalized_image, binary_image, equ_img_gray_blur, threading]
# plot size
# Create a subplot with 2 rows and 2 columns
plt.figure(figsize=(50, 50))  # Adjust the figure size as needed
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
# 保存处理后的图像hn                                       n
# cv2.imwrite('adaptive_threshold_image.jpg', binary_image)

# # 显示结果
# cv2.imshow('Adaptive Threshold Image', binary_image)
#
# # 等待按键退出
# cv2.waitKey(0)
# cv2.destroyAllWindows()
