from PIL import Image
import os
def resize_and_paste_with_exact_fit(flame_path, chamber_path, coordinates):
    """
    将火焰图片放缩并粘贴到燃烧腔室图片的特定区域。
    火焰图片在底层，燃烧腔室图片在上层。
    参数:
    flame_path (str): 火焰图片的路径。
    chamber_path (str): 燃烧腔室图片的路径。
    coordinates (dict): 包含矩形区域左上角和右下角坐标的字典。
    """
    # 计算目标区域的宽度和高度
    target_width = coordinates['right_bottom'][0] - coordinates['left_top'][0]
    target_height = coordinates['right_bottom'][1] - coordinates['left_top'][1]

    # 加载图片
    flame_img = Image.open(flame_path)
    chamber_img = Image.open(chamber_path)

    # 调整火焰图片的大小以适应燃烧腔室区域
    resized_flame_img = flame_img.resize((target_width, target_height))

    # 创建一个新的空白图片，尺寸与燃烧腔室图片相同
    result_img = Image.new("RGBA", chamber_img.size)

    # 首先在新图片上粘贴火焰图片
    paste_x = coordinates['left_top'][0]
    paste_y = coordinates['left_top'][1]
    result_img.paste(resized_flame_img, (paste_x, paste_y))

    # 然后在火焰图片上粘贴燃烧腔室图片
    result_img.paste(chamber_img, (0, 0), chamber_img)

    return result_img

# 使用示例
flame_path =     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.6-H40-BB-photo-cropped\Img700-cropped.jpg"
chamber_path = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Thesis Graph\test\photo_combine\combustion_chamber_frame.png" # 替换为燃烧腔室图片的路径
coordinates = {
    # paste the flame image to the combustion chamber image at the following coordinates
    'left_top': (489, 136),
    'right_bottom': (2208, 6341)
}
# 调用函数
result_img = resize_and_paste_with_exact_fit(flame_path, chamber_path, coordinates)

# 获取输入文件所在的文件夹路径
input_folder_path = os.path.dirname(flame_path)
# 基于输入文件路径及名称对输出文件重命名，去掉路径，仅获取文件名与扩展名
file_name = os.path.basename(flame_path)
output_image_path = os.path.join(input_folder_path, f"{os.path.splitext(file_name)[0]}-pasted.png")  # 替换为裁剪后的图片保存路径：获取文件名，再joint一个新的标记后缀，组成新的文件名
print(f"output image path: {output_image_path}")
result_img.save(output_image_path)
result_img.show()