import os


# 读取每个文件夹中的chamber_coords.txt文本文件
coords_file_path = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Photo\ve2.0-eq0.6-H20-BB-photo\chamber_coords.txt"
with open(coords_file_path, "r") as coords_file:
    coords_data = coords_file.read().splitlines()

# 将读取到的坐标信息解析到chamber_coords字典中
chamber_coords = {}
for line in coords_data:
    print(f"Processing line: {line}")
    if line.startswith("#"):
        continue  # 跳过注释行
    key, value = line.split(":")
    chamber_coords[key.strip()] = int(value.strip())
print(f"corresponding coordinate of the chamber: {chamber_coords}")


