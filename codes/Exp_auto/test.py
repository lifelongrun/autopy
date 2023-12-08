from PIL import Image

def resize_and_paste_with_aspect_ratio(flame_path, chamber_path, coordinates):
    """
    将火焰图片放缩并粘贴到燃烧腔室图片的指定区域。
    只知道矩形区域的左上角和右上角坐标，保持火焰图片的长宽比。

    参数:
    flame_path (str): 火焰图片的路径。
    chamber_path (str): 燃烧腔室图片的路径。
    coordinates (dict): 包含矩形区域左上角和右上角坐标的字典。
    """
    # 计算目标区域的宽度
    target_width = coordinates['right_top'][0] - coordinates['left_top'][0]

    # 加载图片
    flame_img = Image.open(flame_path)
    chamber_img = Image.open(chamber_path)

    # 保持长宽比，计算新的尺寸
    flame_width, flame_height = flame_img.size
    aspect_ratio = flame_width / flame_height
    new_height = round(target_width / aspect_ratio)
    new_width = target_width

    # 调整火焰图片的大小以适应燃烧腔室区域，保持长宽比
    resized_flame_img = flame_img.resize((new_width, new_height))

    # 粘贴位置的左上角坐标
    paste_x = coordinates['left_top'][0]
    paste_y = coordinates['left_top'][1] - (new_height // 2)  # 根据新高度调整Y坐标，使图片垂直居中

    # 将调整后的火焰图片粘贴到燃烧腔室图片上
    chamber_img.paste(resized_flame_img, (paste_x, paste_y))

    return chamber_img

# 使用示例
flame_path = r"C:\Users\i3tig\Pictures\test\ve4.5-H00-resized.jpg"
chamber_path = r"C:\Users\i3tig\Pictures\test\photo_combine\combustion_chamber_frame.png"
coordinates = {
    'left_top': (489, 136),
    'right_top': (2213, 136)
}
result_img = resize_and_paste_with_aspect_ratio(flame_path, chamber_path, coordinates)
result_img.show()
