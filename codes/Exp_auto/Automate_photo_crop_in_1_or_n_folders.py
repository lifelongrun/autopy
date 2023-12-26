from PIL import Image
import os

def crop_to_burner_chamber(input_path, output_path, chamber_coords):
    """
    裁剪图片至燃烧腔室边框大小。
    :param input_path: 输入图片的路径
    :param output_path: 裁剪后的图片保存路径
    :param chamber_coords: 燃烧腔室边框的坐标，格式为(left, top, right, bottom)
    """
    with Image.open(input_path) as img:
        cropped_image = img.crop(chamber_coords)
        cropped_image.save(output_path)

def batch_crop_images(input_folder, output_folder, chamber_coords):
    """
    批量裁剪文件夹中的所有.jpg图片。
    :param input_folder: 输入图片所在的文件夹路径
    :param output_folder: 裁剪后的图片保存文件夹路径
    :param chamber_coords: 燃烧腔室边框的坐标，格式为(left, top, right, bottom)
    """
    # 确保输出文件夹存在，如果不存在则创建它
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有.jpg图片
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".jpg"):
            input_image_path = os.path.join(input_folder, file_name)
            output_image_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}-cropped.jpg")
            crop_to_burner_chamber(input_image_path, output_image_path, chamber_coords)




# 多个文件夹的根路径列表
root_folder_path = [
# BB photo date: 2023.12.10✅ checked
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve1.5-eq0.6-H00-BB-photo", # 另一裁剪边框坐标
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve1.5-eq0.6-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve2.0-eq0.6-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve2.0-eq0.6-H20-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve2.5-eq0.6-H00-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve2.5-eq0.6-H20-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.0-eq0.6-H00-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.0-eq0.6-H20-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.4-H00-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.4-H20-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.5-H00-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.5-H20-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H00-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅
    # ----以下使用全局裁剪边框坐标----chamber_coords = {'left': 2583, 'top': 291, 'right': 3524, 'bottom': 3672}
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H100-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H20-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H40-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅同前
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H60-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅同前
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H80-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅同前
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.7-H00-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅同前
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.7-H20-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅同前ve3.5-eq0.7-H00-BB-photo
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.8-H00-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅同前ve3.5-eq0.7-H00-BB-photo
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.8-H100-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅同前ve3.5-eq0.7-H00-BB-photo
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.8-H20-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅同前ve3.5-eq0.7-H00-BB-photo
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.8-H40-BB-photo", # 另一裁剪边框坐标,坐标信息见源文件:✅同前ve3.5-eq0.7-H00-BB-photo
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.8-H60-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.8-H80-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.9-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.9-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.0-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.0-H100-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.0-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.0-H40-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.0-H60-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.0-H80-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.1-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.1-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.2-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.2-H100-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.2-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.2-H40-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.2-H60-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.2-H80-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve4.0-eq0.6-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve4.0-eq0.6-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve4.5-eq0.6-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve4.5-eq0.6-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve5.0-eq0.6-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve5.0-eq0.6-H20-BB-photo",

# test
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Thesis Graph\test\T",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Thesis Graph\test\T - 副本",


# BBS-45 photo date: 2023.12.10✅ checked
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve1.5-eq0.6-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve1.5-eq0.6-H20-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve2.0-eq0.6-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve2.0-eq0.6-H20-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve2.5-eq0.6-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve2.5-eq0.6-H20-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.0-eq0.6-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.0-eq0.6-H20-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.4-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.4-H20-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.5-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.5-H20-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H100-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H20-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H40-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H60-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H80-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.7-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.7-H20-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.8-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.8-H100-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.8-H20-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.8-H40-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.8-H60-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.8-H80-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.9-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.9-H20-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.0-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.0-H100-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.0-H20-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.0-H40-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.0-H60-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.0-H80-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.1-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.1-H20-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.2-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.2-H100-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.2-H20-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.2-H40-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.2-H60-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.2-H80-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve4.0-eq0.6-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve4.0-eq0.6-H20-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve4.5-eq0.6-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve4.5-eq0.6-H20-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve5.0-eq0.6-H00-BBS-45-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve5.0-eq0.6-H20-BBS-45-photo",

# BBS-55(实为45的重复实验) photo date: 2023.12.11✅ checked
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve1.5-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve1.5-eq0.6-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve2.0-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve2.0-eq0.6-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve2.5-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve2.5-eq0.6-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.0-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.0-eq0.6-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.4-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.4-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.5-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.5-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H100-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H40-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H60-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H80-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.7-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.7-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.8-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.8-H100-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.8-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.8-H40-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.8-H60-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.8-H80-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.9-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.9-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.0-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.0-H100-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.0-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.0-H40-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.0-H60-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.0-H80-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.1-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.1-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.2-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.2-H100-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.2-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.2-H40-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.2-H60-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.2-H80-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve4.0-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve4.0-eq0.6-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve4.5-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve4.5-eq0.6-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve5.0-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve5.0-eq0.6-H20-BBS-55-photo",

# BBS-55-r photo date: 2023.12.12✅ checked
# chamber_coords = {'left': 2587, 'top': 138, 'right': 3436, 'bottom': 3191} only for below directories
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve1.5-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve1.5-eq0.6-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve2.0-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve2.0-eq0.6-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve2.5-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve2.5-eq0.6-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.0-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.0-eq0.6-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.4-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.4-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.5-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.5-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.6-H100-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.6-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.6-H40-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.6-H60-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.6-H80-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.7-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.7-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.8-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.8-H100-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.8-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.8-H40-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.8-H60-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.8-H80-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.9-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq0.9-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq1.0-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq1.0-H100-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq1.0-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq1.0-H40-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq1.0-H60-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq1.0-H80-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq1.1-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq1.1-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq1.2-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq1.2-H100-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq1.2-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq1.2-H40-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq1.2-H60-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve3.5-eq1.2-H80-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve4.0-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve4.0-eq0.6-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve4.5-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve4.5-eq0.6-H20-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve5.0-eq0.6-H00-BBS-55-photo",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-r\ve5.0-eq0.6-H20-BBS-55-photo",

# BBS-65-below15mm photo date: 2023.12.14✅ checked
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\test",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve1.5-eq0.6-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve1.5-eq0.6-H20-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve2.0-eq0.6-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve2.0-eq0.6-H20-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve2.5-eq0.6-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve2.5-eq0.6-H20-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.0-eq0.6-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.0-eq0.6-H20-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.4-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.4-H20-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.5-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.5-H20-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.6-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.6-H100-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.6-H20-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.6-H40-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.6-H60-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.6-H80-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.7-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.7-H20-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.8-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.8-H100-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.8-H20-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.8-H40-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.8-H60-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.8-H80-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.9-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.9-H20-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq1.0-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq1.0-H100-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq1.0-H20-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq1.0-H40-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq1.0-H60-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq1.0-H80-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq1.1-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq1.1-H20-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq1.2-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq1.2-H100-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq1.2-H20-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq1.2-H40-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq1.2-H60-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq1.2-H80-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve4.0-eq0.6-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve4.0-eq0.6-H20-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve4.5-eq0.6-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve4.5-eq0.6-H20-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve5.0-eq0.6-H00-BBS-65-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve5.0-eq0.6-H20-BBS-65-photo-below15mm",

# BBS-55-below15mm photo date: 2023.12.26✅ checked
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\test folder",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve1.5-eq0.6-H20-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve2.0-eq0.6-H20-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve2.5-eq0.6-H20-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.0-eq0.6-H20-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.6-H00-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.6-H100-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.6-H20-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.6-H40-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.6-H60-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.6-H80-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.7-H00-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.7-H20-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.8-H00-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.8-H100-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.8-H20-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.8-H40-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.8-H60-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.8-H80-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.9-H00-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq0.9-H20-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq1.0-H00-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq1.0-H100-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq1.0-H20-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq1.0-H40-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq1.0-H60-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq1.0-H80-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq1.1-H00-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq1.1-H20-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq1.2-H00-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq1.2-H100-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq1.2-H20-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq1.2-H40-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq1.2-H60-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve3.5-eq1.2-H80-BBS-55-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55-Below15mm\ve4.0-eq0.6-H20-BBS-55-photo-below15mm",

# BBS-45-below15mm photo date: 2023.12.26✅ checked
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\test folder",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve1.5-eq0.6-H20-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve2.0-eq0.6-H20-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve2.5-eq0.6-H20-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.0-eq0.6-H20-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.6-H00-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.6-H100-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.6-H20-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.6-H40-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.6-H60-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.6-H80-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.7-H00-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.7-H20-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.8-H00-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.8-H100-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.8-H20-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.8-H40-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.8-H60-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.8-H80-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.9-H00-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq0.9-H20-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq1.0-H00-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq1.0-H100-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq1.0-H20-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq1.0-H40-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq1.0-H60-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq1.0-H80-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq1.1-H00-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq1.1-H20-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq1.2-H00-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq1.2-H100-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq1.2-H20-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq1.2-H40-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq1.2-H60-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve3.5-eq1.2-H80-BBS-45-photo-below15mm",
# r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45-Below15mm\ve4.0-eq0.6-H20-BBS-45-photo-below15mm",


    # 可添加多个/单个文件夹路径
]

# ------全局变量设定------
# 使用字典存储燃烧腔室边框的坐标, 重新调整裁剪边框的大小
# chamber_coords = {'left': 2631, 'top': 208, 'right': 3446, 'bottom': 3199} # BBS-55 bellow photo date: 2023-12-26
chamber_coords = {'left': 2633, 'top': 187, 'right': 3431, 'bottom': 3189} # BBS-45 bellow photo date: 2023-12-26
# {
#
#     # BBS-45 photo date: 2023-12-10
#     # "left": 2581,  # 替换为燃烧腔室边框的左上角x坐标
#     # "top": 211,  # 替换为燃烧腔室边框的左上角y坐标
#     # "right": 3440,  # 替换为燃烧腔室边框的右下角x坐标
#     # "bottom": 3289,  # 替换为燃烧腔室边框的右下角y坐标
#
#     # BBS-55 photo date: 2023-12-11
#     "left": 2613,  # 替换为燃烧腔室边框的左上角x坐标
#     "top": 132,  # 替换为燃烧腔室边框的左上角y坐标
#     "right": 3458,  # 替换为燃烧腔室边框的右下角x坐标
#     "bottom": 3179,  # 替换为燃烧腔室边框的右下角y坐标
# }

# 遍历文件夹路径列表
n = 1
for input_folder_path in root_folder_path:
    output_folder_path = input_folder_path + "-cropped"
    print(f"Processing folder {n}...")
    n += 1

    # # ------局部变量设定：读取预设的坐标文件(使用全局坐标变量时，以下需注释)------
    # # 读取每个文件夹中的chamber_coords.txt文本文件
    # coords_file_path = os.path.join(input_folder_path, "chamber_coords.txt")
    # with open(coords_file_path, "r") as coords_file:
    #     coords_data = coords_file.read().splitlines()
    #
    # # 将读取到的坐标信息解析到chamber_coords字典中
    # chamber_coords = {}
    # for line in coords_data:
    #     print(f"Processing line: {line}")
    #     if line.startswith("#"):
    #         continue  # 跳过注释行
    #     key, value = line.split(":")
    #     chamber_coords[key.strip()] = int(value.strip())
    # print(f"corresponding coordinate of the chamber: {chamber_coords}")
    # # -----------------------

    # 调用函数批量裁剪图片
    batch_crop_images(input_folder_path, output_folder_path, (chamber_coords["left"], chamber_coords["top"], chamber_coords["right"], chamber_coords["bottom"]))
    print(f"[00]Input folder path: {input_folder_path} \n[1]Output folder path: {output_folder_path}")


