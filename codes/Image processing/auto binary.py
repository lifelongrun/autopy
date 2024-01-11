import cv2
import numpy as np
import matplotlib.pyplot as plt

def yen_threshold(image):
    # 计算图像的直方图
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # 归一化直方图
    hist /= hist.sum()

    # 初始化变量
    max_variance = 0
    threshold = 0
    sum_pixels = 0
    sum_pixels_sq = 0

    for t in range(256):
        sum_pixels += t * hist[t]
        sum_pixels_sq += t * t * hist[t]

        # 计算类间方差
        if sum_pixels == 0 or sum_pixels == 1:
            continue
        w0 = sum_pixels
        w1 = 1 - w0
        mu0 = sum_pixels_sq / w0
        mu1 = (sum_pixels_sq - sum_pixels_sq) / w1  # 修正此处的错误
        variance = w0 * w1 * (mu0 - mu1) ** 2

        # 更新阈值和最大方差
        if variance > max_variance:
            max_variance = variance
            threshold = t

    return threshold

images_path = [
    r'E:\Github-autopy\codes\Image processing\swirl_flame.jpg',
    r'E:\Github-autopy\codes\Image processing\pure_h2.jpg',
    r'E:\Github-autopy\codes\Image processing\thin_flame.jpg'
]

# 读取图像

image = cv2.imread(images_path[2])

# 应用高斯滤波
# gaussian_blur = cv2.GaussianBlur(image, (7, 7), 0)

# 应用中值滤波
gaussian_blur = cv2.medianBlur(image, 7 )
gaussian_blur_gray = cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2GRAY)


# 计算Yen阈值
yen_thresh = yen_threshold(gaussian_blur_gray)

# 应用Yen阈值进行二值化
binary_image = np.zeros_like(image)
binary_image[image >= yen_thresh] = 255

# 显示原始图像和二值化图像
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(binary_image, cmap='gray')
plt.title('Binary Image')

plt.show()
