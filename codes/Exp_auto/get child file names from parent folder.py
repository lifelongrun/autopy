import glob
import os


def find_files(directory, pattern):
    # 构造一个包含路径模式的字符串，这里使用的是通配符模式。
    # f"{directory}/**/{pattern}" 表示在 directory 指定的目录下，
    # 递归查找所有匹配 pattern 模式的文件。例如，如果 pattern 是 '*.txt'，
    # 则会查找所有扩展名为 .txt 的文件。
    path_pattern = f"{directory}/**/{pattern}"

    # glob.glob 返回一个列表，其中包含所有匹配给定模式的文件路径。
    # 参数 recursive=True 允许函数在所有子目录中递归查找，匹配指定模式的文件。
    # 列表解析式 [os.path.basename(file) for file in glob.glob(path_pattern, recursive=True)]
    # 遍历 glob.glob 返回的所有文件路径，然后使用 os.path.basename(file) 提取每个文件的文件名。
    # os.path.basename(file) 函数从一个完整的文件路径中提取出文件名，这样就可以只获取文件名而不包含其路径。
    return [os.path.basename(file) for file in glob.glob(path_pattern, recursive=True)]

# 使用示例
directory = r"E:\OneDrive\00_To_Do\1.Graduate Paper\shijie-exp\Data-Exit"
pattern = '*.xlsx'  # 举例来找所有的txt文件
matched_files = find_files(directory, pattern)
for file in matched_files:
    print(f'r"{file}",\n')