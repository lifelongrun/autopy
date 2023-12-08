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

# 示例用法
input_image_path = r"C:\Users\i3tig\Pictures\test\ve4.5-H00.jpg"  # 替换为你的图片路径

# 获取输入文件所在的文件夹路径
input_folder_path = os.path.dirname(input_image_path)

file_name = os.path.basename(input_image_path) # 去掉路径，仅获取文件名与扩展名
output_image_path = os.path.join(input_folder_path, f"{os.path.splitext(file_name)[0]}-resized.jpg")  # 替换为裁剪后的图片保存路径：获取文件名，再joint一个新的标记后缀，组成新的文件名

# 使用字典存储燃烧腔室边框的坐标
chamber_coords = {
    "x1": 2520,     # 替换为燃烧腔室边框的左上角x坐标
    "y1": 304,     # 替换为燃烧腔室边框的左上角y坐标
    "x2": 3480,  # 替换为燃烧腔室边框的右下角x坐标
    "y2": 3692   # 替换为燃烧腔室边框的右下角y坐标
}

# 当需要使用这些坐标时，你可以通过字典键来访问它们。例如，在裁剪函数中使用这些坐标：
crop_rectangle = (chamber_coords["x1"], chamber_coords["y1"], chamber_coords["x2"], chamber_coords["y2"])
# 然后将这个变量传递给裁剪函数：
crop_to_burner_chamber(input_image_path, output_image_path, crop_rectangle)
print(f"Input file path: {input_image_path} \nOutput file path: {output_image_path}")
