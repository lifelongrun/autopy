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
i = 0
for root, dirs, files in os.walk(
        'E:\\John Mike\\OneDrive\\Pictures\\Screenshots'):  # todo 如何使用os.path.join(), 将文件路径传递给os.walk()?
    print(f'当前在根目录：<{root}> 下')
    for dir_name in dirs:
        print(f'<{root}>的子目录：<{dir_name}>')
    for file_name in files:
        print(f'在<{root}>中的文件名为：<{file_name}>')

        if '.jpg' or '.JPG' in file_name:
            shutil.move(f'{root}\\{file_name}',
                        f'E:\\John Mike\\OneDrive\\Pictures\\rename_Screenshots\\{i}.jpg')
            print(f'源文件名称->更名后为：{file_name}->{i}.jpg')
            i += 1
        elif '.png' or '.PNG' in file_name:
            shutil.move(f'{root}\\{file_name}',
                        f'E:\\John Mike\\OneDrive\\Pictures\\rename_Screenshots\\{i}.png')
            print(f'源文件名称->更名后为：{file_name}->{i}.jpg')
            i += 1
        else:
            print('跳过一个存在非.jpg与.png格式的文件，请手动重命名。')

        print(" ")
