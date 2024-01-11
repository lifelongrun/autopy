import cv2
import matplotlib.pyplot as plt
import numpy as np
# 指定使用的字体，例如 SimHei 是一个包含中文字符的字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 载入图片
# image_path = "E:\Github-autopy\codes\Image processing\swirl_flame.jpg"
# image_path = "E:\Github-autopy\codes\Image processing\pure_h2.jpg"
# image_path = r"E:\Github-autopy\codes\Image processing\night.jpg"
# image_path = r"E:\Github-autopy\codes\Image processing\flame-test.jpg"
# image_path = r"E:\Github-autopy\codes\Image processing\Img1660-cropped.jpg"
# image_path = r"E:\Github-autopy\codes\Image processing\more_blue.jpg"
image_path = r"E:\Github-autopy\codes\Image processing\Img1660-cropped.jpg"
# image_path = r"E:\Github-autopy\codes\Image processing\Img1657-cropped.jpg"
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# 锐化图片
# 定义一个锐化的核
sharpening_kernel = np.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])
sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
plt.imshow(sharpened_image)
plt.title("锐化后的图片")
# plt.show()
# 中值滤波
median_blur = cv2.medianBlur(sharpened_image, 13)
median_blur_gray = cv2.cvtColor(median_blur, cv2.COLOR_BGR2GRAY)
# 高斯处理
gaussian_blur = cv2.GaussianBlur(median_blur, (11, 11), 0)
gaussian_blur_gray = cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2GRAY)
# 二值化处理
# 转换为灰度图像
gray_image = cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2GRAY)
# 应用二值化
_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
plt.imshow(binary_image, "gray")
plt.title("OTSU算法(中值模糊后+高斯模糊后)")
plt.show()

# --new
th3 = cv2.adaptiveThreshold(median_blur_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,2)
# plt.imshow(th3, "gray")
# plt.title("自适应: median模糊+高斯自适应")
# plt.show()
# --end


# --new
th4 = cv2.adaptiveThreshold(gaussian_blur_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# plt.imshow(th4, "gray")
# plt.title("自适应:median模糊+高斯模糊+高斯自适应")
# plt.show()
# --end

# --new
th5 = cv2.adaptiveThreshold(gaussian_blur_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
# plt.imshow(th5, "gray")
# plt.title("自适应:median模糊后+均值自适应")
# plt.show()
# --end

titles = ['Origin', 'Sharp', 'OTSU算法(Blur-M+G)', 'Blur-M+Adap-G', 'Blur-M+G+Adap-G', 'Blur-M+Adap-M']
images = [image, sharpened_image, binary_image, th3, th4, th5]
# 设置图形大小
plt.figure(figsize=(12, 8))  # 这里的12和8是图形的宽和高，可以根据需要调整
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('on')
    plt.xticks([]),plt.yticks([])
# plt.show()
# --边缘检测
# 使用Canny边缘检测
edges = cv2.Canny(th4, threshold1=10, threshold2=200)  # 调整阈值根据图像的特性

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
# 转为numpy格式储存像素信息
# numpy_array = np.array(binary_image) # OTSU算法
numpy_array = np.array(binary_image) # 自适应高斯


# 寻找火焰最顶部的像素
# 由于二值化后，火焰应该是白色（255），我们搜索最顶部的白色像素
non_zero_rows = np.where(numpy_array.max(axis=1) > 0)[0]

if non_zero_rows.any():
    top_row = non_zero_rows[0]

    # 根据题目要求，原图高度像素为500mm，计算火焰的实际高度
    image_height_mm = 500
    image_height_px = numpy_array.shape[0]
    pixel_to_mm_ratio = image_height_mm / image_height_px

    # 计算火焰长度，火焰长度为最顶部白色像素到底部边界的长度
    flame_height_px = image_height_px - top_row
    flame_height_mm = flame_height_px * pixel_to_mm_ratio

    # 输出火焰长度
    print(f"Fire length in pixels: {flame_height_px}px")
    print(f"Fire length in mm: {flame_height_mm}mm")

    # 在图片上标记火焰的长度
    marked_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)
    cv2.line(marked_image, (0, top_row), (marked_image.shape[1], top_row), (0, 255, 0), 2)

    # 保存标记后的图片
    marked_image_path = 'Image-marker-01-11.jpg'
    cv2.imwrite(marked_image_path, marked_image)
else:
    print("Unable to find the flame in the image.")
    flame_height_mm = None
    marked_image_path = None

# 返回火焰高度和标记后的图片路径
flame_height_mm, marked_image_path
