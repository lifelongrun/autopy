import pandas as pd
from pandas import ExcelWriter
from openpyxl import load_workbook  # 导入 load_workbook
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os
# 设置字体以支持中文字符
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 定义函数来处理单个文件
# def process_excel_file(file, columns, num_rows):
#     """ 读取指定Excel文件中的特定列，计算这些列最后num_rows行的平均值。 """
#     df = pd.read_excel(file, sheet_name='testo', usecols=columns)
#     last_rows = df.tail(num_rows)
#     # 返回包含平均值和标准差的字典
#     return {"mean": last_rows.mean(), "std": last_rows.std()}

# 定义处理单个Excel文件的函数
def process_excel_file(file_path, columns, num_rows):
    """
    处理单个Excel文件，提取指定列的数据，并计算这些列的平均值和标准差。

    参数:
    - file_path: Excel文件的路径
    - columns_of_interest: 一个包含感兴趣的列名的列表
    - num_rows: 读取的行数，默认为None，表示读取所有行

    返回值:
    - 包含平均值和标准差的字典
    """
    df = pd.read_excel(file_path, sheet_name='testo', usecols=columns)
    last_rows = df.tail(num_rows)
    means = last_rows.mean()
    stds = last_rows.std()
    return {"mean": means, "std": stds}

# Excel文件和列名，报错的话注意r及逗号分隔符
excel_files = [
    # 文件路径列表, 报错信息，逗号分隔符
    # ...✅/❎/🟢/🔴/🕝➡️/👀
    # ------File directory format of experiment operation conditions for BB-below15mm👇👇👇------
    # 不同燃料流速(ve1.5-5.0-eq0.6-H20)，3mm热电偶测温（加6.3mm套管后）
    # ve---ve1.5-5.0-eq0.6-H20-BB---✅ output to 2024-02-26-eq0.6-ve1.5-5.0-H20-BB-exit.xlsx✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.6-ve1.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.6-ve2.0-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.6-ve2.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.6-ve3.0-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.6-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.6-ve4.0-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.6-ve4.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.6-ve5.0-H20-BB-exit.xlsx",
    # 不同掺氢比(eq0.6-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BB--- ✅ output to 2024-02-26-eq0.6-ve3.5-H00-100-BB-exit.xlsx✅
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.6-ve3.5-H00-BB-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.6-ve3.5-H20-BB-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.6-ve3.5-H40-BB-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.6-ve3.5-H60-BB-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.6-ve3.5-H80-BB-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.6-ve3.5-H100-BB-exit.xlsx",
    # 不同当量比(eq0.4-1.2-H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.4-1.2-H20-BB---✅ output to 2024-02-26-eq0.4-1.2-ve3.5-H20-BB-exit.xlsx✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.4-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.5-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.6-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.7-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.8-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq0.9-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq1.0-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq1.1-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\2024-02-26-eq1.2-ve3.5-H20-BB-exit.xlsx",
    # ----------------------------------------------------------------------------------------End👆👆👆------

    # ...✅/❎/🟢/🔴/🕝➡️/👀
    # ------File directory format of experiment operation conditions for BBS-55-below15mm👇👇👇------
    # 不同燃料流速(ve1.5-3.5-eq0.6-H20)，3mm热电偶测温（加6.3mm套管后
    # ve---ve1.5-3.5-eq0.6-H20-BBS-55---✅ output to 2024-02-27-eq0.6-ve1.5-3.5-H20-BBS-55-exit.xlsx✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq0.6-ve1.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq0.6-ve2.0-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq0.6-ve2.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq0.6-ve3.0-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq0.6-ve3.5-H20-BBS-55-exit.xlsx",

    # 不同掺氢比(eq0.6-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BBS-55--- ✅ output to 2024-02-27-eq0.6-ve3.5-H00-100-BBS-55-exit.xlsx✅
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq0.6-ve3.5-H00-BBS-55-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq0.6-ve3.5-H20-BBS-55-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq0.6-ve3.5-H40-BBS-55-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq0.6-ve3.5-H60-BBS-55-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq0.6-ve3.5-H80-BBS-55-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq0.6-ve3.5-H100-BBS-55-exit.xlsx",
    # 不同当量比(eq0.6-1.2-H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.6-1.2-H20-BBS-55---✅ output to 2024-02-27-eq0.6-ve3.5-H20-BBS-55-exit.xlsx✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq0.6-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq0.7-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq0.8-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq0.9-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq1.0-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq1.1-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-55-Exit\2024-02-27-eq1.2-ve3.5-H20-BBS-55-exit.xlsx",
    # ----------------------------------------------------------------------------------------End👆👆👆------

    # ...✅/❎/🟢/🔴/🕝➡️/👀
    # ------File directory format of experiment operation conditions for BBS-45&65-below15mm👇👇👇------
    # 不同掺氢比(eq0.6/eq0.8/eq1.0/eq1.2-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BBS-45---✅
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-45 and 65-Exit\2024-02-27-eq0.6-ve3.5-H00-BBS-45-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-45 and 65-Exit\2024-02-27-eq0.6-ve3.5-H20-BBS-45-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-45 and 65-Exit\2024-02-27-eq0.6-ve3.5-H40-BBS-45-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-45 and 65-Exit\2024-02-27-eq0.6-ve3.5-H60-BBS-45-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-45 and 65-Exit\2024-02-27-eq0.6-ve3.5-H80-BBS-45-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-45 and 65-Exit\2024-02-27-eq0.6-ve3.5-H100-BBS-45-exit.xlsx",
    # Hy---ve3.5-eq0.6-H00-100-BBS-65---✅
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-45 and 65-Exit\2024-02-27-eq0.6-ve3.5-H00-BBS-65-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-45 and 65-Exit\2024-02-27-eq0.6-ve3.5-H20-BBS-65-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-45 and 65-Exit\2024-02-27-eq0.6-ve3.5-H40-BBS-65-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-45 and 65-Exit\2024-02-27-eq0.6-ve3.5-H60-BBS-65-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-45 and 65-Exit\2024-02-27-eq0.6-ve3.5-H80-BBS-65-exit.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Supplement-BBS-45 and 65-Exit\2024-02-27-eq0.6-ve3.5-H100-BBS-65-exit.xlsx",
    # ----------------------------------------------------------------------------------------End👆👆👆------
               ]  # 替换为实际文件名
columns_of_interest = ["% O2", "ppm CO", "ppm NO", "°C 烟温", 'ppm NOx', "% CO2IR"]  # 替换为实际列名
num_rows = 12  # 指定要读取的最后x行（5s采集一次，即5s写入一行，取最后1分钟的烟气数据）

# 提取每个文件名中特定的部分作为索引
file_indices = [os.path.splitext(os.path.basename(file))[0].split('-', 3)[-1] for file in excel_files]
# split('-', 3)在第三个破折号处分割字符串，然后通过[-1]选择分割后的最后一部分。因此，对于2023 - 11 - 28 - ve1.5 - eq0.6 - H20 - BB，这会正确提取出ve1.5 - eq0.6 - H20 - BB
# 通过这种方式，如果文件名是 2023-11-28-ve1.5-eq0.6-H20-BB.xlsx，这段代码会正确地提取出 ve1.5-eq0.6-H20-BB 这部分作为索引。

# 将结果转换为DataFrame, 并设置新的索引
# average_df = pd.DataFrame(averages, index=file_indices) # index=excel_files

# 处理每个文件并收集平均值和标准差
results = [process_excel_file(file, columns_of_interest, num_rows) for file in excel_files]

# 创建空DataFrame用于存储平均值和标准差
average_df = pd.DataFrame(index=file_indices)
std_df = pd.DataFrame(index=file_indices)

# 为每个列填充平均值和标准差
for col in columns_of_interest:
    average_df[col + " Mean"] = [result["mean"][col] for result in results]
    std_df[col + " Std"] = [result["std"][col] for result in results]

# 将平均值和标准差的DataFrame合并
combined_df = pd.concat([average_df, std_df], axis=1)

# print(combined_df)

# 对合并后的DataFrame进行排序
# 重新排列列的顺序（如果您想要对特定的列进行排序，以确保这些列的顺序符合您的要求，您可以使用Pandas的.reindex方法或简单地使用列选择语法来重新排列列的顺序。这不会改变每列内部的数据顺序，而是改变列作为整体在DataFrame中的位置。）
df_sorted_columns = combined_df[[
    '% O2 Mean', '% O2 Std', 'ppm CO Mean', 'ppm CO Std',
    'ppm NO Mean', 'ppm NO Std', '°C 烟温 Mean', '°C 烟温 Std',
    'ppm NOx Mean', 'ppm NOx Std', '% CO2IR Mean', '% CO2IR Std'
]]

# 打印重新排列后的DataFrame
print(df_sorted_columns)


# ---绘制图表---
# 设置子图的数量和布局
fig, axs = plt.subplots(3, 3, figsize=(15, 15))  # 3行3列的布局

# print(f"average_df columns:\n{average_df.columns}")

# 为每个列创建一个柱状图
for i, column in enumerate(average_df.columns):
    # 计算行和列的索引
    row_index = i // 3
    col_index = i % 3

    # 获取当前子图
    ax = axs[row_index, col_index]
    # 绘制柱状图
    ax.bar(average_df.index, average_df[column])
    ax.set_title(f'Average of {column}')
    ax.set_xlabel('Excel Files (Different Conditions)')
    ax.set_ylabel(f'Average of {column}')
    # 设置x轴标签倾斜
    # 设置x轴标签倾斜
    ax.xaxis.set_major_locator(ticker.FixedLocator(range(len(average_df.index))))
    ax.set_xticklabels(average_df.index, rotation=45, ha="right")  # 旋转45度，水平对齐方式为右对齐

# 隐藏多余的子图
for j in range(i + 1, 9):
    fig.delaxes(axs[j // 3, j % 3])

plt.tight_layout()  # 调整布局以避免重叠
plt.show()

# print(average_df)
# ---将dataframe中的数据写入到Excel文件中---
if "y" == input("是否将表中数据（烟气数据）输出为Excel文件？[y/n]"):
    # 指定 Excel 文件路径及文件名（无论是否存在）
    output_excel_file = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\supplement-BB-Exit\exit-output-please name this file.xlsx" # 替换为实际文件名
    new_sheet_name = 'vexx-eqxx-Hxx' # 每次运行前，修改这里的工作表名称
    # 将数据写入到 Excel 文件的指定工作表中
    # average_df.to_excel(output_excel_file, sheet_name=new_sheet_name, index=True)

    try:
        with ExcelWriter(output_excel_file, engine='openpyxl', mode='a' if os.path.exists(output_excel_file) else 'w') as writer:
            df_sorted_columns.to_excel(writer, sheet_name=new_sheet_name, index=True)
    except PermissionError:
        print(f"Permission denied when writing to {output_excel_file}. Please close the file if it's open in another program.")
else:
    print("不输出Excel文件。")