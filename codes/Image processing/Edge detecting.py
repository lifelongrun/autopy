import cv2
import matplotlib.pyplot as plt


def process_flame_image(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found.")
        return

    # 转换到灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 应用二值化
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    # 显示二值化图像以进行调试
    cv2.imshow('Binary Image', binary_image)

    # 转换到HSV色彩空间
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 设置黄色和蓝色的HSV阈值
    yellow_lower = (20, 100, 100)
    yellow_upper = (30, 255, 255)
    blue_lower = (100, 100, 100)
    blue_upper = (130, 255, 255)

    # 创建掩模
    yellow_mask = cv2.inRange(hsv_image, yellow_lower, yellow_upper)
    blue_mask = cv2.inRange(hsv_image, blue_lower, blue_upper)

    # 组合掩模
    combined_mask = cv2.bitwise_or(yellow_mask, blue_mask)

    # 应用Canny边缘检测
    edges = cv2.Canny(combined_mask, 100, 200)
    plt.imshow(edges, cmap='gray')
    plt.title("Canny detection")
    plt.axis('on')
    plt.show()
    # 显示结果
    # cv2.imshow('Edges', edges)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# 使用示例
# process_flame_image('path_to_your_image.jpg')



# 使用示例
path_to_your_image = r"/codes/Image processing/thin_flame.jpg"

process_flame_image(r"E:\Github-autopy\codes\Image processing\thin_flame.jpg")
