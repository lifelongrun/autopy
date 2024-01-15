import cv2
import matplotlib.pyplot as plt
# 读取火焰图像
image = cv2.imread(r'E:\Github-autopy\codes\Image processing\Img1668-cropped.jpg')

# 转换图像为灰度
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Normalize the image histogram
normalized_image = cv2.normalize(gray_image, None, 0, 255, cv2.NORM_MINMAX)

gray_image = cv2.medianBlur(gray_image, 3)
# 使用自适应阈值处理
binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 33, 2)
binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

title = [ "image", "gray", "normalized", "binary"]
images = [image, gray_image, normalized_image, binary_image]
# plot size
# Create a subplot with 2 rows and 2 columns
plt.figure(figsize=(50, 50))  # Adjust the figure size as needed
for i in range(4):
    plt.subplot(2, 2, i+1)
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
