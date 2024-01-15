import cv2
import matplotlib.pyplot as plt
import numpy as np

def find_fire_height(binary_image_path, image_height_mm=500):
    # 加载已经处理过的二值化图像
    # binary_image = cv2.imread(binary_image_path, cv2.IMREAD_GRAYSCALE)
    binary_image = binary_image_path

    if binary_image is None:
        raise ValueError("Error: Binary image not found.")

    # 寻找火焰最顶部的像素
    top_row = find_top_row(binary_image)

    if top_row is not None:
        # 计算火焰的实际高度
        pixel_to_mm_ratio = image_height_mm / binary_image.shape[0]
        flame_height_px = binary_image.shape[0] - top_row
        flame_height_mm = flame_height_px * pixel_to_mm_ratio

        # 标记火焰的长度并保存标记后的图像
        marked_image = mark_fire_height(binary_image.copy(), top_row)
        marked_image_path = 'mage-marker-01-11.jpg'
        plt.imshow(marked_image)
        plt.title("标记后的图片")
        plt.axis('on')
        plt.show()
        # cv2.imwrite(marked_image_path, marked_image)

    else:
        print("Unable to find the flame in the image.")
        flame_height_mm = None
        marked_image_path = None

    return flame_height_mm, marked_image_path

def find_top_row(binary_image):
    non_zero_rows = np.where(binary_image.max(axis=1) > 0)[0]
    if non_zero_rows.any():
        return non_zero_rows[0]
    else:
        return None

def mark_fire_height(image, top_row):
    cv2.line(image, (0, top_row), (image.shape[1], top_row), (255, 0, 0), 5)
    return image

# 指定使用的字体，例如 SimHei 是一个包含中文字符的字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 载入图片
# image_path = "E:\Github-autopy\codes\Image processing\swirl_flame.jpg"
# image_path = "E:\Github-autopy\codes\Image processing\pure_h2.jpg"
# image_path = r"E:\Github-autopy\codes\Image processing\Img1660-cropped.jpg"
# image_path = r"E:\Github-autopy\codes\Image processing\more_blue.jpg"
# image_path = r"E:\Github-autopy\codes\Image processing\Img1660-cropped.jpg"
# image_path = r"E:\Github-autopy\codes\Image processing\Img1657-cropped.jpg"
# image_path = r"E:\Github-autopy\codes\Image processing\thin_film.jpg"
image_path = r"E:\Github-autopy\codes\Image processing\thin_blue_tail.jpg"
# image_path = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.7-H00-BB-photo-cropped\Img913-cropped.jpg"
# image = cv2.imread(image_path, cv2.IMREAD_COLOR)
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
origin_image = image
# ------图像预处理

# 预处理A: 锐化图片
# 获取图像的尺寸
height, width = image.shape[:2]
ksize = int(min(height, width) * 0.05)
if ksize % 2 == 0:
    ksize += 1
print(f"Ksize: {ksize}")
# 定义一个锐化的核
sharpening_kernel = np.array([[-1, -1, -1],
                              [-1, ksize/2, -1],
                              [-1, -1, -1]])
# image = cv2.filter2D(image, -1, sharpening_kernel) #深度为-1，表示输出图像与原图像有相同的深度
sharpened_image = image

print(image.shape)
image = cv2.medianBlur(image, ksize)
# median_blur_gray = cv2.cvtColor(median_blur, cv2.COLOR_BGR2GRAY)  # 转换为灰度图像

image = cv2.filter2D(image, -1, sharpening_kernel) #深度为-1，表示输出图像与原图像有相同的深度

image = cv2.medianBlur(image, ksize)

# 高斯处理
gaussian_blur = cv2.GaussianBlur(image, (ksize, ksize), 0.5) #sigmaX=0,sigmaY=0，表示从ksize计算, sigma越大，图像越模糊
# gaussian_blur_gray = cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2GRAY) # 转换为灰度图像
# --一级预处理结束
median_blur = gaussian_blur
# 全局threshold
thg = cv2.threshold(median_blur,50,255, cv2.THRESH_BINARY)[1]

# 应用二值化:OTSU算法
_, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#
plt.imshow(binary_image, "gray")
plt.title("OTSU算法(中值模糊后+高斯模糊后)")
plt.show()

# 应用二值化:blur-M+Adap-G
th3 = cv2.adaptiveThreshold(median_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,17,2)
# plt.imshow(th3, "gray")
# plt.title("自适应: median模糊+高斯自适应")
# plt.show()
# --end


# 应用二值化:blur-M+G+Adap-G
th4 = cv2.adaptiveThreshold(gaussian_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,2)
# plt.imshow(th4, "gray")
# plt.title("自适应:median模糊+高斯模糊+高斯自适应")
# plt.show()
# --end

# 应用二值化:blur-M+Adap-M
th5 = cv2.adaptiveThreshold(gaussian_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,2)
# plt.imshow(th5, "gray")
# plt.title("自适应:median模糊后+均值自适应")
# plt.show()
# --end
# 应用二值化:继th3后-OTSU算法
th6 = cv2.threshold(th3, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# --end


# 显示图像
titles = ['Origin', 'Sharp', 'blur_M+G', 'thg', 'binary_image:OTSU算法(Blur-M+G)', 'th3:Blur-M+Adap-G', 'th4:Blur-M+G+Adap-G', 'th5:Blur-M+Adap-M', 'th6:继th3后-OTSU算法']
images = [origin_image, sharpened_image, gaussian_blur, thg, binary_image, th3, th4, th5, th6]
# 设置图形大小
plt.figure(figsize=(12, 8))  # 这里的12和8是图形的宽和高，可以根据需要调整
for i in range(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('on')
    plt.xticks([]),plt.yticks([])

# 将以上所有图的直方图归一化后的都显示出来
plt.figure(figsize=(12, 8))
for i in range(9):
    plt.subplot(2, 5, i + 1), plt.hist(images[i].ravel(), 256)
    plt.title(titles[i])
    plt.axis('on')
    plt.xlim([0, 255])  # 设置x轴范围为0到255
    plt.ylim([0, 50000])  # 设置y轴范围
    plt.xticks([0, 255])  # 设置x轴刻度标签
    plt.yticks([0, 50000])  # 设置y轴刻度标签
plt.show()
# 直方图均衡化
# normalized_image = cv2.equalizeHist(image)
#
# # 显示原始图像和归一化后的图像
# cv2.imshow("Original Image", image)
# cv2.imshow("Normalized Image", normalized_image)



# plt.show()
# --边缘检测
# 使用Canny边缘检测
# edges = cv2.Canny(th4, threshold1=10, threshold2=200)  # 调整阈值根据图像的特性
# plt.imshow(edges, cmap='gray')
# plt.title("Canny detection")
# plt.axis('on')
# plt.show()

# 显示原始图像和Canny边缘检测结果
# plt.subplot(121), plt.imshow(th4, cmap='gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(edges, cmap='gray')
# plt.title('Canny Edge Image'), plt.xticks([]), plt.yticks([])
#
# plt.show()
# --end

OTSU_after_adaptive = cv2.threshold(th4, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
plt.imshow(th3, cmap='gray')
plt.show()

# 调用函数并传入二值化图像的文件路径
flame_height_mm, marked_image_path = find_fire_height(binary_image)
print(f"Fire length in mm: {flame_height_mm}mm, marked_image_path: {marked_image_path}")

# -----------------以下为火焰长度计算-----------------
# 转为numpy格式储存像素信息
# # numpy_array = np.array(binary_image) # OTSU算法
# numpy_array = np.array(binary_image) # 自适应高斯
#
#
# # 寻找火焰最顶部的像素
# # 由于二值化后，火焰应该是白色（255），我们搜索最顶部的白色像素
# non_zero_rows = np.where(numpy_array.max(axis=1) > 0)[0]
#
# if non_zero_rows.any():
#     top_row = non_zero_rows[0]
#
#     # 根据题目要求，原图高度像素为500mm，计算火焰的实际高度
#     image_height_mm = 500
#     image_height_px = numpy_array.shape[0]
#     pixel_to_mm_ratio = image_height_mm / image_height_px
#
#     # 计算火焰长度，火焰长度为最顶部白色像素到底部边界的长度
#     flame_height_px = image_height_px - top_row
#     flame_height_mm = flame_height_px * pixel_to_mm_ratio
#
#     # 输出火焰长度
#     print(f"Fire length in pixels: {flame_height_px}px")
#     print(f"Fire length in mm: {flame_height_mm}mm")
#
#     # 在图片上标记火焰的长度
#     marked_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)
#     cv2.line(marked_image, (0, top_row), (marked_image.shape[1], top_row), (255, 0, 0), 5)
#
#     # 保存标记后的图片
#     marked_image_path = 'Image-marker-01-11.jpg'
#     plt.imshow(marked_image)
#     plt.title("标记后的图片")
#     plt.axis('on')
#     plt.show()
#     # cv2.imwrite(marked_image_path, marked_image)
# else:
#     print("Unable to find the flame in the image.")
#     flame_height_mm = None
#     marked_image_path = None
#
# # 返回火焰高度和标记后的图片路径
# flame_height_mm, marked_image_path
#-----------------以上为火焰长度计算-----------------

