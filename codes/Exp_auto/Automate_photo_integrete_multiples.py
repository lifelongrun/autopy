from PIL import Image
import os
def combine_images(grid, image_paths, output_path):
    """
    将图片按照指定的行和列组合。

    参数:
    grid (dict): 包含行（'rows'）和列（'cols'）数的字典。
    image_paths (list): 图片路径列表。
    output_path (str): 组合后图片的保存路径。
    """
    # 确保提供了足够的图片
    if len(image_paths) < grid['rows'] * grid['cols']:
        raise ValueError("Not enough images to fill the grid")

    # 加载第一张图片以获取单个图片的尺寸
    first_image = Image.open(image_paths[0])
    image_width, image_height = first_image.size

    # 计算组合图片的总宽度和高度
    total_width = image_width * grid['cols']
    total_height = image_height * grid['rows']

    # 创建新的组合图片
    combined_image = Image.new('RGB', (total_width, total_height))

    # 逐个粘贴图片
    for i, path in enumerate(image_paths):
        image = Image.open(path)
        x = (i % grid['cols']) * image_width
        y = (i // grid['cols']) * image_height
        combined_image.paste(image, (x, y))

    # 保存和显示组合后的图片
    combined_image.save(output_path)
    combined_image.show()

# 使用示例
image_paths = [




# - ve1.5-5.0-eq0.6-H00/20-BB-photo-cropped

    # -- ve1.5-5.0-eq0.6-H00-BB-photo-cropped
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve1.5-eq0.6-H00-BB-photo-cropped\ve1.5-eq0.6-H00-BB-02-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve2.0-eq0.6-H00-BB-photo-cropped\Img027-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve2.5-eq0.6-H00-BB-photo-cropped\Img033-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.0-eq0.6-H00-BB-photo-cropped\Img046-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.6-H00-BB-photo-cropped\Img052-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve4.0-eq0.6-H00-BB-photo-cropped\Img068-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve4.5-eq0.6-H00-BB-photo-cropped\Img075-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve5.0-eq0.6-H00-BB-photo-cropped\Img094-cropped.jpg",

    # -- ve1.5-5.0-eq0.6-H20-BB-photo-cropped
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve1.5-eq0.6-H20-BB-photo-cropped\Img1142-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve2.0-eq0.6-H20-BB-photo-cropped\Img1119-cropped.jpg",
# - ve3.5-eq0.6/eq0.8/eq1.0/eq1.2-H00-100-BB-photo-cropped

    # -- ve3.5-eq0.6-H00-100-BB-photo-cropped-folder name:[ve3.5-eq0.6-Hxx-BB-photo-cropped]
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.6-H00-BB-photo-cropped\Img052-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.6-H20-BB-photo-cropped\Img732-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.6-H40-BB-photo-cropped\Img700-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.6-H60-BB-photo-cropped\Img355-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.6-H80-BB-photo-cropped\Img330-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.6-H100-BB-photo-cropped\Img388-cropped.jpg",

    # -- ve3.5-eq0.8-H00-100-BB-photo-cropped

    # -- ve3.5-eq1.0-H00-100-BB-photo-cropped

    # -- ve3.5-eq1.2-H00-100-BB-photo-cropped

# - ve3.5-eq0.4-1.2-H00/H20-BB-photo-cropped

    # -- ve3.5-eq0.4-1.2-H00-BB-photo-cropped
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.4-H00-BB-photo-cropped\Img957-cropped.jpg",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.5-H00-BB-photo-cropped\Img931-cropped.jpg",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.6-H00-BB-photo-cropped\Img052-cropped.jpg",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.7-H00-BB-photo-cropped\Img911-cropped.jpg",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.8-H00-BB-photo-cropped\Img809-cropped.jpg",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq0.9-H00-BB-photo-cropped\Img888-cropped.jpg",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.0-H00-BB-photo-cropped\Img834-cropped.jpg",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.1-H00-BB-photo-cropped\Img868-cropped.jpg",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve3.5-eq1.2-H00-BB-photo-cropped\Img848-cropped.jpg",
    # -- ve3.5-eq0.4-1.2-H20-BB-photo-cropped




]  # 替换为您的图片路径
print(f"图片数量为: {len(image_paths)} 单位: 张")
grid = {'rows': 1, 'cols': 9}  # 2行2列, 替换为您的行列数，例如{'rows': 2, 'cols': 2}, 注意这里的行列数要与图片数量匹配

dire_path = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Thesis Graph\test"  # 替换为您的图片所在文件夹路径
# 使用os.path.join来拼接路径
output_path = os.path.join(dire_path, f"integration_flame+r{grid['rows']}-c{grid['cols']}-ve3.5-eq0.4-1.2-H00.png")
print(f"output image path: {output_path}")

# 调用函数
combine_images(grid, image_paths, output_path)
