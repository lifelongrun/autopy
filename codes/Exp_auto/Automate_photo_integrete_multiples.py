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
    r"C:\Users\i3tig\Pictures\test\ve1.5-H00-resized-combined.png",
    r"C:\Users\i3tig\Pictures\test\ve2.0-H00-resized-combined.png",
    r"C:\Users\i3tig\Pictures\test\ve2.5-H00-resized-combined.png",
    r"C:\Users\i3tig\Pictures\test\ve3.0-H00-resized-combined.png",
    r"C:\Users\i3tig\Pictures\test\ve3.5-H00-resized-combined.png",
    r"C:\Users\i3tig\Pictures\test\ve4.0-H00-resized-combined.png",
    r"C:\Users\i3tig\Pictures\test\ve4.5-H00-resized-combined.png",
    r"C:\Users\i3tig\Pictures\test\ve5.0-H00-resized-combined.png",
]  # 替换为您的图片路径
print(f"图片数量为: {len(image_paths)} 单位: 张")
grid = {'rows': 2, 'cols': 4}  # 2行2列, 替换为您的行列数，例如{'rows': 2, 'cols': 2}, 注意这里的行列数要与图片数量匹配

dire_path = r"C:\Users\i3tig\Pictures\test"  # 替换为您的图片所在文件夹路径
# 使用os.path.join来拼接路径
output_path = os.path.join(dire_path, f"integration_flame+r{grid['rows']}-c{grid['cols']}.png")
print(f"output image path: {output_path}")

# 调用函数
combine_images(grid, image_paths, output_path)
