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

# -----------------------------------------------BB-----------------------------------------------------------------
# - ve1.5-5.0-eq0.6-H00/20-BB-photo-cropped

    # -- ve1.5-5.0-eq0.6-H00-BB-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve1.5-eq0.6-H00-BB-photo-cropped\ve1.5-eq0.6-H00-BB-02-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve2.0-eq0.6-H00-BB-photo-cropped\Img027-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve2.5-eq0.6-H00-BB-photo-cropped\Img033-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.0-eq0.6-H00-BB-photo-cropped\Img046-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H00-BB-photo-cropped\Img052-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve4.0-eq0.6-H00-BB-photo-cropped\Img068-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve4.5-eq0.6-H00-BB-photo-cropped\Img075-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve5.0-eq0.6-H00-BB-photo-cropped\Img094-cropped.jpg",
    # -- ve1.5-5.0-eq0.6-H20-BB-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve1.5-eq0.6-H20-BB-photo-cropped\Img1139-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve2.0-eq0.6-H20-BB-photo-cropped\Img1115-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve2.5-eq0.6-H20-BB-photo-cropped\Img1092-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.0-eq0.6-H20-BB-photo-cropped\Img1073-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H20-BB-photo-cropped\Img732-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve4.0-eq0.6-H20-BB-photo-cropped\Img1155-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve4.5-eq0.6-H20-BB-photo-cropped\Img1185-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve5.0-eq0.6-H20-BB-photo-cropped\Img1202-cropped.jpg",
# - ve3.5-eq0.6/eq0.8/eq1.0/eq1.2-H00-100-BB-photo-cropped
    # folder name:[ve3.5-eq0.6-Hxx-BB-photo-cropped]
    # -- ve3.5-eq0.6-H00-100-BB-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H00-BB-photo-cropped\Img052-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H20-BB-photo-cropped\Img732-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H40-BB-photo-cropped\Img700-cropped.jpg", #todo to bright and washed out
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H60-BB-photo-cropped\Img355-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H80-BB-photo-cropped\Img330-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H100-BB-photo-cropped\Img388-cropped.jpg",
    # -- ve3.5-eq0.8-H00-100-BB-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.8-H00-BB-photo-cropped\Img809-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.8-H20-BB-photo-cropped\Img749-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.8-H40-BB-photo-cropped\Img678-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.8-H60-BB-photo-cropped\Img538-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.8-H80-BB-photo-cropped\Img488-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.8-H100-BB-photo-cropped\Img409-cropped.jpg",
    # -- ve3.5-eq1.0-H00-100-BB-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.0-H00-BB-photo-cropped\Img839-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.0-H20-BB-photo-cropped\Img770-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.0-H40-BB-photo-cropped\Img641-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.0-H60-BB-photo-cropped\Img555-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.0-H80-BB-photo-cropped\Img493-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.0-H100-BB-photo-cropped\Img432-cropped.jpg",
    # -- ve3.5-eq1.2-H00-100-BB-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.2-H00-BB-photo-cropped\Img850-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.2-H20-BB-photo-cropped\Img793-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.2-H40-BB-photo-cropped\Img660-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.2-H60-BB-photo-cropped\Img583-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.2-H80-BB-photo-cropped\Img518-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.2-H100-BB-photo-cropped\Img461-cropped.jpg",
# - ve3.5-eq0.4-1.2-H00/H20-BB-photo-cropped
    # -- ve3.5-eq0.4-1.2-H00-BB-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.4-H00-BB-photo-cropped\Img957-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.5-H00-BB-photo-cropped\Img931-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H00-BB-photo-cropped\Img052-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.7-H00-BB-photo-cropped\Img911-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.8-H00-BB-photo-cropped\Img809-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.9-H00-BB-photo-cropped\Img888-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.0-H00-BB-photo-cropped\Img834-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.1-H00-BB-photo-cropped\Img868-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.2-H00-BB-photo-cropped\Img848-cropped.jpg",
    # -- ve3.5-eq0.4-1.2-H20-BB-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.4-H20-BB-photo-cropped\Img970-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.5-H20-BB-photo-cropped\Img995-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.6-H20-BB-photo-cropped\Img732-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.7-H20-BB-photo-cropped\Img1015-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.8-H20-BB-photo-cropped\Img749-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq0.9-H20-BB-photo-cropped\Img1034-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.0-H20-BB-photo-cropped\Img770-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.1-H20-BB-photo-cropped\Img1069-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BB\ve3.5-eq1.2-H20-BB-photo-cropped\Img793-cropped.jpg",
    # -----------------------------------------------BBS-45-----------------------------------------------------------------
# - ve1.5-5.0-eq0.6-H00/20-BBS-45-photo-cropped
    # -- ve1.5-5.0-eq0.6-H00-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve1.5-eq0.6-H00-BBS-45-photo-cropped\Img316-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve2.0-eq0.6-H00-BBS-45-photo-cropped\Img333-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve2.5-eq0.6-H00-BBS-45-photo-cropped\Img357-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.0-eq0.6-H00-BBS-45-photo-cropped\Img380-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H00-BBS-45-photo-cropped\Img395-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve4.0-eq0.6-H00-BBS-45-photo-cropped\Img414-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve4.5-eq0.6-H00-BBS-45-photo-cropped\Img435-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve5.0-eq0.6-H00-BBS-45-photo-cropped\Img455-cropped.jpg",
    # -- ve1.5-5.0-eq0.6-H20-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve1.5-eq0.6-H20-BBS-45-photo-cropped\Img619-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve2.0-eq0.6-H20-BBS-45-photo-cropped\Img597-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve2.5-eq0.6-H20-BBS-45-photo-cropped\Img578-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.0-eq0.6-H20-BBS-45-photo-cropped\Img568-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H20-BBS-45-photo-cropped\Img539-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve4.0-eq0.6-H20-BBS-45-photo-cropped\Img518-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve4.5-eq0.6-H20-BBS-45-photo-cropped\Img499-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve5.0-eq0.6-H20-BBS-45-photo-cropped\Img487-cropped.jpg",
# - ve3.5-eq0.6/eq0.8/eq1.0/eq1.2-H00-100-BBS-45-photo-cropped
    # folder name:[ve3.5 - eq0.6 - Hxx - BBS - 45 - photo - cropped]
    # -- ve3.5-eq0.6-H00-100-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H00-BBS-45-photo-cropped\Img395-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H20-BBS-45-photo-cropped\Img539-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H40-BBS-45-photo-cropped\Img869-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H60-BBS-45-photo-cropped\Img890-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H80-BBS-45-photo-cropped\Img1029-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H100-BBS-45-photo-cropped\Img1063-cropped.jpg",
    # -- ve3.5-eq0.8-H00-100-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.8-H00-BBS-45-photo-cropped\Img728-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.8-H20-BBS-45-photo-cropped\Img748-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.8-H40-BBS-45-photo-cropped\Img845-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.8-H60-BBS-45-photo-cropped\Img908-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.8-H80-BBS-45-photo-cropped\Img1009-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.8-H100-BBS-45-photo-cropped\Img1074-cropped.jpg",
    # -- ve3.5-eq1.0-H00-100-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.0-H00-BBS-45-photo-cropped\Img711-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.0-H20-BBS-45-photo-cropped\Img765-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.0-H40-BBS-45-photo-cropped\Img835-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.0-H60-BBS-45-photo-cropped\Img930-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.0-H80-BBS-45-photo-cropped\Img990-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.0-H100-BBS-45-photo-cropped\Img1099-cropped.jpg",
    # -- ve3.5-eq1.2-H00-100-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.2-H00-BBS-45-photo-cropped\Img689-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.2-H20-BBS-45-photo-cropped\Img785-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.2-H40-BBS-45-photo-cropped\Img806-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.2-H60-BBS-45-photo-cropped\Img963-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.2-H80-BBS-45-photo-cropped\Img981-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.2-H100-BBS-45-photo-cropped\Img1126-cropped.jpg",
# - ve3.5-eq0.4-1.2-H00/H20-BBS-45-photo-cropped
    # -- ve3.5-eq0.4-1.2-H00-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.4-H00-BBS-45-photo-cropped\Img1260-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.5-H00-BBS-45-photo-cropped\Img1267-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H00-BBS-45-photo-cropped\Img395-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.7-H00-BBS-45-photo-cropped\Img1294-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.8-H00-BBS-45-photo-cropped\Img728-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.9-H00-BBS-45-photo-cropped\Img1311-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.0-H00-BBS-45-photo-cropped\Img712-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.1-H00-BBS-45-photo-cropped\Img1339-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.2-H00-BBS-45-photo-cropped\Img690-cropped.jpg",
    # -- ve3.5-eq0.4-1.2-H20-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.4-H20-BBS-45-photo-cropped\Img1235-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.5-H20-BBS-45-photo-cropped\Img1205-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.6-H20-BBS-45-photo-cropped\Img539-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.7-H20-BBS-45-photo-cropped\Img1183-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.8-H20-BBS-45-photo-cropped\Img748-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq0.9-H20-BBS-45-photo-cropped\Img1166-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.0-H20-BBS-45-photo-cropped\Img765-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.1-H20-BBS-45-photo-cropped\Img1136-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-45\ve3.5-eq1.2-H20-BBS-45-photo-cropped\Img785-cropped.jpg",
# -----------------------------------------------BBS-55(文件名为55，实际为45的重复拍摄组)-----------------------------------------------------------------
# - ve1.5-5.0-eq0.6-H00/20-BBS-45-photo-cropped
    # -- ve1.5-5.0-eq0.6-H00-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve1.5-eq0.6-H00-BBS-55-photo-cropped\Img292-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve2.0-eq0.6-H00-BBS-55-photo-cropped\Img311-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve2.5-eq0.6-H00-BBS-55-photo-cropped\Img346-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.0-eq0.6-H00-BBS-55-photo-cropped\Img399-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H00-BBS-55-photo-cropped\Img382-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve4.0-eq0.6-H00-BBS-55-photo-cropped\Img420-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve4.5-eq0.6-H00-BBS-55-photo-cropped\Img448-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve5.0-eq0.6-H00-BBS-55-photo-cropped\Img475-cropped.jpg",
    # -- ve1.5-5.0-eq0.6-H20-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve1.5-eq0.6-H20-BBS-55-photo-cropped\Img645-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve2.0-eq0.6-H20-BBS-55-photo-cropped\Img620-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve2.5-eq0.6-H20-BBS-55-photo-cropped\Img594-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.0-eq0.6-H20-BBS-55-photo-cropped\Img569-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H20-BBS-55-photo-cropped\Img545-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve4.0-eq0.6-H20-BBS-55-photo-cropped\Img535-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve4.5-eq0.6-H20-BBS-55-photo-cropped\Img517-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve5.0-eq0.6-H20-BBS-55-photo-cropped\Img487-cropped.jpg",
# - ve3.5-eq0.6/eq0.8/eq1.0/eq1.2-H00-100-BBS-45-photo-cropped
    # folder name:[ve3.5 - eq0.6 - Hxx - BBS - 45 - photo - cropped]
    # -- ve3.5-eq0.6-H00-100-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H00-BBS-55-photo-cropped\Img382-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H20-BBS-55-photo-cropped\Img545-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H40-BBS-55-photo-cropped\Img820-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H60-BBS-55-photo-cropped\Img978-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H80-BBS-55-photo-cropped\Img1004-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H100-BBS-55-photo-cropped\Img1164-cropped.jpg",
    # -- ve3.5-eq0.8-H00-100-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.8-H00-BBS-55-photo-cropped\Img668-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.8-H20-BBS-55-photo-cropped\Img788-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.8-H40-BBS-55-photo-cropped\Img840-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.8-H60-BBS-55-photo-cropped\Img951-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.8-H80-BBS-55-photo-cropped\Img1021-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.8-H100-BBS-55-photo-cropped\Img1131-cropped.jpg",
    # -- ve3.5-eq1.0-H00-100-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.0-H00-BBS-55-photo-cropped\Img693-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.0-H20-BBS-55-photo-cropped\Img760-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.0-H40-BBS-55-photo-cropped\Img862-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.0-H60-BBS-55-photo-cropped\Img933-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.0-H80-BBS-55-photo-cropped\Img1048-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.0-H100-BBS-55-photo-cropped\Img1116-cropped.jpg",
    # -- ve3.5-eq1.2-H00-100-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.2-H00-BBS-55-photo-cropped\Img719-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.2-H20-BBS-55-photo-cropped\Img740-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.2-H40-BBS-55-photo-cropped\Img882-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.2-H60-BBS-55-photo-cropped\Img908-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.2-H80-BBS-55-photo-cropped\Img1069-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.2-H100-BBS-55-photo-cropped\Img1109-cropped.jpg",
# - ve3.5-eq0.4-1.2-H00/H20-BBS-45-photo-cropped
    # -- ve3.5-eq0.4-1.2-H00-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.4-H00-BBS-55-photo-cropped\Img1397-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.5-H00-BBS-55-photo-cropped\Img1371-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H00-BBS-55-photo-cropped\Img382-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.7-H00-BBS-55-photo-cropped\Img1343-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.8-H00-BBS-55-photo-cropped\Img668-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.9-H00-BBS-55-photo-cropped\Img1321-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.0-H00-BBS-55-photo-cropped\Img700-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.1-H00-BBS-55-photo-cropped\Img1297-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.2-H00-BBS-55-photo-cropped\Img719-cropped.jpg",
    # -- ve3.5-eq0.4-1.2-H20-BBS-45-photo-cropped✅(#todo selective ones need to adjust)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.4-H20-BBS-55-photo-cropped\Img1178-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.5-H20-BBS-55-photo-cropped\Img1204-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.6-H20-BBS-55-photo-cropped\Img545-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.7-H20-BBS-55-photo-cropped\Img1225-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.8-H20-BBS-55-photo-cropped\Img788-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq0.9-H20-BBS-55-photo-cropped\Img1258-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.0-H20-BBS-55-photo-cropped\Img760-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.1-H20-BBS-55-photo-cropped\Img1265-cropped.jpg",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-55\ve3.5-eq1.2-H20-BBS-55-photo-cropped\Img740-cropped.jpg",

# -----------------------------------------------BBS-55-----------------------------------------------------------------
# - ve1.5-5.0-eq0.6-H00/20-BBS-55-photo-cropped

    # -- ve1.5-5.0-eq0.6-H00-BBS-55-photo-cropped
# r"",
# r"",
# r"",
    # -- ve1.5-5.0-eq0.6-H20-BBS-55-photo-cropped
# r"",
# r"",
# r"",
# - ve3.5-eq0.6/eq0.8/eq1.0/eq1.2-H00-100-BBS-55-photo-cropped

    # -- ve3.5-eq0.6-H00-100-BBS-55-photo-cropped - folder name:[ve3.5-eq0.6-Hxx-BBS-55-photo-cropped]
# r"",
# r"",
# r"",
    # -- ve3.5-eq0.8-H00-100-BBS-55-photo-cropped
# r"",
# r"",
# r"",
    # -- ve3.5-eq1.0-H00-100-BBS-55-photo-cropped
# r"",
# r"",
# r"",
    # -- ve3.5-eq1.2-H00-100-BBS-55-photo-cropped
# r"",
# r"",
# r"",
# - ve3.5-eq0.4-1.2-H00/H20-BBS-55-photo-cropped

    # -- ve3.5-eq0.4-1.2-H00-BBS-55-photo-cropped
# r"",
# r"",
# r"",
    # -- ve3.5-eq0.4-1.2-H20-BBS-55-photo-cropped
# r"",
# r"",
# r"",



# ------File directory format of experiment operation conditions for BBS-45-below15mm👇👇👇------
# 不同燃料流速(ve1.5-5.0-eq0.6-H00/H20)，3mm热电偶测温（加6.3mm套管后）
    # ve---ve1.5-5.0-eq0.6-H00-BBS-45---🟢
    # ve---ve1.5-5.0-eq0.6-H20-BBS-45---🔴
# 不同掺氢比(eq0.6/eq0.8/eq1.0/eq1.2-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BBS-45--- 🔴
    # Hy---ve3.5-eq0.8-H00-100-BBS-45--- 🔴
    # Hy---ve3.5-eq1.0-H00-100-BBS-45--- 🔴
    # Hy---ve3.5-eq1.2-H00-100-BBS-45--- 🔴
# 不同当量比(eq0.4-1.2-H00/H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.4-1.2-H00-BBS-45---🔴
    # eq---ve3.5-eq0.4-1.2-H20-BBS-45---🔴
# ----------------------------------------------------------------------------------------End👆👆👆------
# ------File directory format of experiment operation conditions for BBS-55-below15mm👇👇👇------
# 不同燃料流速(ve1.5-5.0-eq0.6-H00/H20)，3mm热电偶测温（加6.3mm套管后）
    # ve---ve1.5-5.0-eq0.6-H00-BBS-55---🟢
    # ve---ve1.5-5.0-eq0.6-H20-BBS-55---🔴
# 不同掺氢比(eq0.6/eq0.8/eq1.0/eq1.2-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BBS-55--- 🔴
    # Hy---ve3.5-eq0.8-H00-100-BBS-55--- 🔴
    # Hy---ve3.5-eq1.0-H00-100-BBS-55--- 🔴
    # Hy---ve3.5-eq1.2-H00-100-BBS-55--- 🔴
# 不同当量比(eq0.4-1.2-H00/H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.4-1.2-H00-BBS-55---🔴
    # eq---ve3.5-eq0.4-1.2-H20-BBS-55---🔴
# ----------------------------------------------------------------------------------------End👆👆👆------
# ------File directory format of experiment operation conditions for BBS-65-below15mm👇👇👇------
# 不同燃料流速(ve1.5-5.0-eq0.6-H00/H20)，3mm热电偶测温（加6.3mm套管后）
    # ve---ve1.5-5.0-eq0.6-H00-BB---🟢/🕝➡️/👀/✅
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve1.5-eq0.6-H00-BBS-65-photo-below15mm-cropped\Img302-cropped.jpg",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve2.0-eq0.6-H00-BBS-65-photo-below15mm-cropped\Img326-cropped.jpg",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve2.5-eq0.6-H00-BBS-65-photo-below15mm-cropped\Img340-cropped.jpg",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.0-eq0.6-H00-BBS-65-photo-below15mm-cropped\Img369-cropped.jpg",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve3.5-eq0.6-H00-BBS-65-photo-below15mm-cropped\Img391-cropped.jpg",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve4.0-eq0.6-H00-BBS-65-photo-below15mm-cropped\Img410-cropped.jpg",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve4.5-eq0.6-H00-BBS-65-photo-below15mm-cropped\Img443-cropped.jpg",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo-BBS-65-Below15mm\ve5.0-eq0.6-H00-BBS-65-photo-below15mm-cropped\Img456-cropped.jpg",
    # ve---ve1.5-5.0-eq0.6-H20-BB---🔴
# 不同掺氢比(eq0.6/eq0.8/eq1.0/eq1.2-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BB--- 🔴
    # Hy---ve3.5-eq0.8-H00-100-BB--- 🔴
    # Hy---ve3.5-eq1.0-H00-100-BB--- 🔴
    # Hy---ve3.5-eq1.2-H00-100-BB--- 🔴
# 不同当量比(eq0.4-1.2-H00/H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.4-1.2-H00-BB---🔴
    # eq---ve3.5-eq0.4-1.2-H20-BB---🔴
# ----------------------------------------------------------------------------------------End👆👆👆------


]  # 替换为您的图片路径
print(f"input image quantities: {len(image_paths)} unit: images")

# 设置网格参数
grid = {'rows': 1,
        'cols': 9
        }  # 2行2列, 替换为您的行列数，例如{'rows': 2, 'cols': 2}, 注意这里的行列数要与图片数量匹配

grid['cols'] = len(image_paths) # 若采用一维网格，则无需设定网格参数，则用图片数量替换列数

dire_path = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Thesis Graph\Flame integration"  # 替换为您的图片所在文件夹路径
# 确保输出文件夹存在，如果不存在则创建它
if not os.path.exists(dire_path):
    os.makedirs(dire_path)
# 为实验工况命名
exp_condition_name = {
"ve": "ve1.5-5.0", # ve for velocity
"eq": "eq0.6", # eq for equivalence ratio
"H": "H00", # H for Hydrogen blending ratio
"Struct": "BBS-65" # BB/BBS-x for combustion chamber structure
}

# 使用os.path.join来拼接路径
output_path = os.path.join(dire_path, f"integration_flame+r{grid['rows']}-c{grid['cols']}-{exp_condition_name['ve']}-{exp_condition_name['eq']}-{exp_condition_name['H']}-{exp_condition_name['Struct']}.png") # 替换为输出图片的路径, 注意这里的图片命名修改为你想要的名字
print(f"output image matrix [Row*Column]: {grid['rows']}*{grid['cols']}")
print(f"output image path: {output_path}")

# 调用函数, 生成图片
combine_images(grid, image_paths, output_path)