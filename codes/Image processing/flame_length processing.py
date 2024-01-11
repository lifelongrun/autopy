import cv2
import matplotlib.pyplot as plt

# ------Function definition------
def display_image(image):
    plt.imshow(image)
    plt.show()

def apply_median_blur(input_image_path, kernel_size):
    # 读取输入图像
    img = cv2.imread(input_image_path)
    # 应用中值模糊，使用指定大小的核(奇数，越大导致更强的模糊效果)
    blurred_img = cv2.medianBlur(img, kernel_size)
    # 显示原始图像和模糊后的图像
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Blurred Image')
    plt.imshow(cv2.cvtColor(blurred_img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
    return blurred_img

def apply_gaussian_blur(image_path, kernel_size=(3, 3), sigma=0):
    """
    对指定图像应用高斯滤波。

    :param image_path: 要处理的图像的路径。
    :param kernel_size: 高斯核的大小，以元组形式表示 (width, height)。
    :param sigma: 高斯核的标准差，如果为0，则根据核大小自动计算。
    :return: 高斯滤波后的图像。
    """
    # 加载图像
    img = cv2.imread(image_path)

    # 应用高斯滤波
    gaussian_blur = cv2.GaussianBlur(img, kernel_size, sigma)

    return gaussian_blur

def binary_threshold(blurrd_image, threshold=127, max_value=255):
    """
    对图像进行二值化处理。

    :param image_path: 图像的路径。
    :param threshold: 用于二值化的阈值。
    :param max_value: 超过阈值时赋予的新值（通常为255）。
    :return: 二值化后的图像。
    """
    # 应用二值化
    _, binary_img = cv2.threshold(blurrd_image, threshold, max_value, cv2.THRESH_BINARY)

    return binary_img

# ------Variable definition------

images_path = [
    r'E:\Github-autopy\codes\Image processing\swirl_flame.jpg',
    r'E:\Github-autopy\codes\Image processing\pure_h2.jpg',
    r'E:\Github-autopy\codes\Image processing\thin_flame.jpg'
]

images = []
for i in range(len(images_path)):
    img = cv2.imread(images_path[i])
    images.append(img)
    print(images)

# ------Main program------


# display_image(img_1)


#
# for i in range(3):
#     plt.subplot(1, 3, i+1)
#     plt.imshow(thresh1[:, :, i])
#     plt.xticks([])
#     plt.yticks([])
# plt.show()

# median blur
blur1 = apply_median_blur(images_path[2],7)
gray1 = cv2.cvtColor(blur1, cv2.COLOR_BGR2GRAY)
# display_image(gray1)

# gaussian blur
# blur2 = apply_gaussian_blur(images_path[0])  # 替换为你的图像文件路径
# blur2_rgb = cv2.cvtColor(blur2, cv2.COLOR_BGR2RGB)
# blur2_gray = cv2.cvtColor(blur2, cv2.COLOR_BGR2GRAY)
# blur2_gray_binary = binary_threshold(blur2_gray, 50, 255)
# plt.imshow(blur2_gray_binary, cmap='gray') # viridis, jet, coolwarm, gray
# plt.show()


# golbal thresholding
# binary_img_global = binary_threshold(blur2_gray, 27, 255)

# adaptive thresholding
## 使用cv2.adaptiveThreshold进行自适应阈值二值化
# binary_img = cv2.adaptiveThreshold(blur2_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 4)
# binary_img = cv2.adaptiveThreshold(blur2_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
# plt.imshow(binary_img, cmap='gray')
# plt.show()


# 使用Otsu's阈值分割
ret, thresholded_image = cv2.threshold(gray1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
plt.imshow(thresholded_image, cmap='gray')
plt.show()