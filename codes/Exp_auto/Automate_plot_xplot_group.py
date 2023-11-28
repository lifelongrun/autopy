import pandas as pd
from pandas import ExcelWriter
import matplotlib.pyplot as plt
import os
import seaborn as sns

# 设置Seaborn样式
# sns.set()
# 设置字体以支持中文字符
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Excel文件路径列表
excel_files = [
    # 文件路径列表, 报错信息，逗号分隔符
    # ...
# 不同流速，3mm热电偶测温（加6.3mm套管后）
    # ---eq0.6-ve1.5-5-H00---
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日15时23分-ve5.0-eq0.6-H00-BB.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日15时56分-ve4.5-eq0.6-H00-BB.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日16时26分-ve4-eq0.6-H00-BB.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日17时12分-ve3.5-eq0.6-H00-BB.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日17时44分-ve3.0-eq0.6-H00-BB.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日18时48分-ve2.5-eq0.6-H00-BB.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日18时16分-ve2.0-eq0.6-H00-BB.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日19时37分-ve1.5-eq0.6-H00-BB.xlsx",
    # ---eq0.6-ve1.5-5-H20---
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日20时30分-ve1.5-eq0.6-H20-BB.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日21时09分-ve2.5-eq0.6-H20-BB.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日21时40分-ve3.5-eq0.6-H20-BB.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日22时12分-ve4.5-eq0.6-H20-BB.xlsx",
    # 添加更多文件路径...
]



# 为第一张图创建DataFrame
# ---将dataframe中的数据写入到Excel文件中---
# 指定 Excel 文件路径及文件名（无论是否存在）
output_excel_file = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Exit\vex-eq0.6-BB_A_R_n_T-test111.xlsx"
prefix_sheet_name = "vex-eq0.5-H20-BB"
new_sheet_name_for_A_n = prefix_sheet_name + '_A_n_T'
new_sheet_name_for_R_n = prefix_sheet_name + '_R_n_T'

df_A_n_list_of_first_chart = []
index_list_first_chart = []
plt.figure(figsize=(10, 6))
for file_path in excel_files:
    df = pd.read_excel(file_path, sheet_name='A_n_T_ave')
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    wks_name = f"{base_name}_A_n_T_ave"
    df_A_n_list_of_first_chart.append(df)  # 将每个文件的DataFrame添加到列表中
    index_list_first_chart.append(wks_name)
    x_column = df.columns[0]
    y_columns = df.columns[1:]
    for y_col in y_columns:
        plt.plot(df[x_column], df[y_col], linestyle='-', marker='s', label=f"{wks_name}: {y_col}")

plt.xlabel('X轴')
plt.ylabel('数值')
plt.title('A_n_T_ave工作表的X-Y图')
plt.legend()
plt.show()

# 将列表中的DataFrame合并为一个DataFrame, 采用concat合并这些DataFrame
df_list_first_chart_df = pd.concat(df_A_n_list_of_first_chart, keys=index_list_first_chart)

# 输出结果前，打印结果
print(df_list_first_chart_df)


# ---第2张图---
# 为每个y列创建一个子图
num_of_cols = 4  # 假设您想在每个文件中为前4列（除了X轴列）创建图表
# 字母序号列表
letters = ['a', 'b', 'c', 'd']  # 根据需要的子图数量调整
colors = ['red', 'green', 'blue', 'orange']  # 根据需要的子图数量调整
plt.figure(figsize=(10, 10))  # 调整图表大小

df_R_n_list_of_second_chart = []
index_list_second_chart = []
for file_path in excel_files:
    df = pd.read_excel(file_path, sheet_name='R_n_T_ave')
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    # 获得索引名称
    wks_name = f"{base_name}_R_n_T_ave"
    index_list_second_chart.append(wks_name)
    df_R_n_list_of_second_chart.append(df)  # 将每个文件的DataFrame添加到列表中

    x_column = df.columns[0]
    y_columns = df.columns[1:num_of_cols+1]

    for i, y_col in enumerate(y_columns, start=1):
        plt.subplot(2, 2, i)  # 创建2x2的子图布局
        plt.plot(df[x_column], df[y_col], linestyle='-', marker='s', label=f"{base_name}: {y_col}")
        plt.xlabel(f"X轴 - {y_col}的X-Y图")  # 将标题作为X轴标签的一部分
        plt.ylabel('数值')
        plt.title(f"({letters[i-1]}){y_col}的X-Y图")
        plt.legend()

plt.tight_layout()  # 调整子图布局
plt.show()

# 将列表中的DataFrame合并为一个DataFrame, 采用concat合并这些DataFrame
df_list_of_second_chart_df = pd.concat(df_R_n_list_of_second_chart, keys=index_list_second_chart)
# 输出结果前，打印结果
print(df_list_of_second_chart_df)

# 输出两种图表的结果到同个Excel文件中的两张分表中
# ---将dataframe中的数据写入到Excel文件中---


try:
    # 写入数据到 Excel 文件
    # 检查文件是否存在，如果不存在则使用写入模式
    if os.path.exists(output_excel_file):
        mode = 'a'  # 追加模式
    else:
        mode = 'w'  # 写入模式
    # df_list_first_chart_df.to_excel(output_excel_file, sheet_name=new_sheet_name_for_R_n, index=True)
    with pd.ExcelWriter(output_excel_file, engine='openpyxl', mode=mode) as writer:
        # 检查工作簿中是否已存在这些工作表
        if 'new_sheet_name_for_A_n' not in writer.book.sheetnames:
            df_list_first_chart_df.to_excel(writer, sheet_name=new_sheet_name_for_A_n)
        if 'A_n_T_ave' not in writer.book.sheetnames:
            df_list_of_second_chart_df.to_excel(writer, sheet_name=new_sheet_name_for_R_n)
except PermissionError:
    print(f"Permission denied when writing to {output_excel_file}. Please close the file if it's open in another program.")