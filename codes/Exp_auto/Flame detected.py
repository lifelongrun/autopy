import cv2
from PIL import Image, ImageDraw

def mark_flame_contours(input_path, output_path, threshold=50):
    # 打开图片
    image = cv2.imread(input_path)

    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 应用阈值处理以分离火焰部分
    _, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    # 查找轮廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 创建一个带有轮廓的副本
    marked_image = image.copy()

    # 绘制轮廓
    cv2.drawContours(marked_image, contours, -1, (0, 255, 0), 2)  # 在图像上绘制绿色轮廓

    # 将OpenCV图像转换为Pillow图像
    pil_image = Image.fromarray(cv2.cvtColor(marked_image, cv2.COLOR_BGR2RGB))

    # 保存标记后的图像
    pil_image.save(output_path)

# 使用示例
input_path = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Thesis Graph\test\detectaion\Img875.jpg" # 替换为您的燃烧火焰图片路径
output_path = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Thesis Graph\test\detectaion\ve5.0-H00-resized-combined-detected-.png"  # 保存标记后的图片路径
mark_flame_contours(input_path, output_path)
