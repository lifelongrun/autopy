import os
from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image, text, font_path, text_color, background_color, font_size):
    """ 在图片上添加文本 """
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, size=font_size)

    # 使用textbbox获取文本尺寸
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # 添加带背景的文本
    draw.rectangle([0, 0, text_width, text_height], fill=background_color)
    draw.text((0, 0), text, fill=text_color, font=font)

    return image

def process_images(input_folder, output_folder, font_path, text_color="#FFFFFF", background_color="#000000", font_size=30):
    """ 处理文件夹中的所有.png图片 """
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            with Image.open(input_path) as img:
                img_with_text = add_text_to_image(img, filename, font_path, text_color, background_color, font_size)
                img_with_text.save(output_path)  # 保存到指定的输出文件夹

# 使用示例
input_folder = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Thesis Graph\Flame integration - name"  # 替换为您的输入图片文件夹路径
output_folder = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Thesis Graph\Flame integration - name/named"  # 替换为您想要保存图片的输出文件夹路径
# 确保输出文件夹存在，如果不存在则创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
font_path =  r"E:\Download\Times-New-Roman\Times New Roman\times new roman.ttf"  # 替换为您的字体文件路径
# 调用函数
process_images(input_folder, output_folder, font_path, text_color="#FFD700", background_color="#000000", font_size=100)