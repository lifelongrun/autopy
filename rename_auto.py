import os, shutil

'''
NOTES
① 使用os.walk()依次遍历工作路径下的所有子文件夹以及文件，并同时返回三个值：
    1.当前文件夹名称的字符串。 即root
    2.当前文件夹中子文件夹的字符串的列表。 即dirs
    3.当前文件夹中文件里的字符串的列表。 即files
    所谓的当前文件夹，是指for循环当前迭代的文件夹。而程序当前的工作目录并不会改变。
② 使用shutil.move()对目标文件进行移动与重命名操作
'''
# ----实现功能：调整单'\'->双'\\'----
# ✍输入文件的目录
object_directory = r'E:\John Mike\OneDrive\Pictures\电脑壁纸\rename'
rename_directory = r'E:\John Mike\OneDrive\Pictures\电脑壁纸' # 此路径不能在object_directory下，否则后续文件及文件夹会被重复遍历
replaced_object_directory = object_directory.replace('\\', '\\\\')
replaced_rename_directory = rename_directory.replace('\\','\\\\')
# 使用str.replace(old,new), 返回一个被替换掉子字符串的新字符串
# Refer to: https://docs.python.org/3/library/stdtypes.html#str.replace
# 另一用法，r'a\b\c'：使用'r'声明其后的字符串无需进行转义

# ----判断是否已有即将创建的同名文件夹----
# ✍输入存放重命名后的文件夹名称（此文件夹包含于原文件目录下）
rename_dir = 'renamed_backgrounds'
if not os.path.exists(replaced_rename_directory + '\\\\' + rename_dir):
    os.mkdir(replaced_rename_directory + f'./{rename_dir}')
    print(f'创建了新的文件夹{rename_dir}')
else:
    print(f'文件夹{rename_dir}已存在，无需再创建')
# 说明：对文件夹进行操作使用'/'或'./'+文件夹名称

# ----开始遍历所有文件夹以及子文件夹和文件，对每次遍历到的文件进行重命名操作----
i = 0
for root, dirs, files in os.walk(replaced_object_directory):
    print(f'当前在根目录：<{root}> 下')
    for dir_name in dirs:
        print(f'<{root}>的子目录：<{dir_name}>')
    for file_name in files:
        print(f'在<{root}>中的文件名为：<{file_name}>')
        # ----判断需进行重命名操作的文件格式----
        if '.jpg' in file_name:
            shutil.move(f'{root}\\{file_name}',
                        f'{replaced_rename_directory}\\{rename_dir}\\{i}.jpg')
            print(f'源文件名称->更名后为：{file_name}->{i}.jpg')
            i += 1
        elif '.png' in file_name:
            shutil.move(f'{root}\\{file_name}',
                        f'{replaced_rename_directory}\\{rename_dir}\\{i}.png')
            print(f'源文件名称->更名后为：{file_name}->{i}.jpg')
            i += 1
        else:
            print('跳过一个存在非.jpg与.png格式的文件，请手动重命名。')
        print(" ")
print('更名完毕！')
