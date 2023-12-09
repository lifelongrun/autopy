import os

def get_folder_paths(parent_folder):
    """
    获取指定父文件夹中所有文件夹的根路径。

    参数:
    parent_folder (str): 包含文件夹的父文件夹路径。

    返回:
    list: 包含所有文件夹的根路径的列表。
    """
    # 使用列表推导式获取文件夹路径
    folder_paths = [os.path.join(parent_folder, folder_name) for folder_name in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, folder_name))]
    return folder_paths

# 示例用法
parent_folder = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo"  # 替换为包含文件夹的父文件夹路径

# 获取文件夹路径
folder_paths = get_folder_paths(parent_folder)

# 输出文件夹路径
for folder_path in folder_paths:
    print(f'r"{folder_path}",')
