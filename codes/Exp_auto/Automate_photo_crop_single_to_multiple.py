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
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve1.5-eq0.6-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve1.5-eq0.6-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve2.0-eq0.6-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve2.0-eq0.6-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve2.5-eq0.6-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve2.5-eq0.6-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.0-eq0.6-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.0-eq0.6-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.4-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.4-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.5-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.5-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.6-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.6-H100-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.6-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.6-H40-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.6-H60-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.6-H80-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.7-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.7-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.8-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.8-H100-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.8-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.8-H40-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.8-H60-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.8-H80-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.9-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.9-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.0-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.0-H100-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.0-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.0-H40-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.0-H60-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.0-H80-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.1-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.1-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.2-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.2-H100-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.2-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.2-H40-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.2-H60-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.2-H80-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve4.0-eq0.6-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve4.0-eq0.6-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve4.5-eq0.6-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve4.5-eq0.6-H20-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve5.0-eq0.6-H00-BB-photo",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve5.0-eq0.6-H20-BB-photo",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Thesis Graph\test\T",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Thesis Graph\test\T - 副本",


    # 可添加多个/单个文件夹路径
]


# 使用字典存储燃烧腔室边框的坐标, 重新调整裁剪边框的大小
chamber_coords = {
    "left": 2520,     # 替换为燃烧腔室边框的左上角x坐标
    "top": 304,       # 替换为燃烧腔室边框的左上角y坐标
    "right": 3480,    # 替换为燃烧腔室边框的右下角x坐标
    "bottom": 3692    # 替换为燃烧腔室边框的右下角y坐标
}

# 遍历文件夹路径列表
n = 1
for input_folder_path in root_folder_path:
    output_folder_path = input_folder_path + "-cropped"
    print(f"Processing folder {n}...")
    n += 1
    batch_crop_images(input_folder_path, output_folder_path, (chamber_coords["left"], chamber_coords["top"], chamber_coords["right"], chamber_coords["bottom"]))
    print(f"[00]Input folder path: {input_folder_path} \n[1]Output folder path: {output_folder_path}")
