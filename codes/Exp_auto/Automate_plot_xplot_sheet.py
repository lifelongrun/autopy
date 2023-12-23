import pandas as pd
import matplotlib.pyplot as plt
import os

# 代码说明: 本代码用于从多个Excel文件中读取指定某个名称的工作表数据并绘制图表。

# 设置字体以支持中文字符
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Excel文件路径列表
excel_files = [

# 不同流速，6mm热电偶测温
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月27日17时25分-ve2.5-eq0.6-H00-BB.xlsx",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月27日18时31分-ve3-eq0.6-H00-BB.xlsx",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月27日19时38分-ve3.5-eq0.6-H00-BB.xlsx",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月27日20时56分-ve4-eq0.6-H00-BB.xlsx",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月27日21时28分-ve4.5-eq0.6-H00-BB.xlsx",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月27日15时45分-ve5-eq0.6-H00-BB.xlsx",


# 不同流速，3mm热电偶测温
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月23日19时48分-ve2.5-eq0.6-H00-BB.xlsx",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月23日20时41分-ve3-eq0.6-H00-BB.xlsx",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月23日21时21分-ve3.5-eq0.6-H00-BB.xlsx",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月23日21时59分-ve4-eq0.6-H00-BB.xlsx",
#     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月24日16时59分-ve4.5-eq0.6-H00-BB.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月25日19时35分-ve5-eq0.6-H00-BB.xlsx",


    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月27日18时00分-ve2.5-eq0.6-H20-BB.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月27日19时06分-ve3-eq0.6-H20-BB.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月27日20时23分-ve3.5-eq0.6-H20-BB.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月27日16时29分-ve4-eq0.6-H20-BB.xlsx"
    
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月23日19时48分-ve2.5-eq0.6-H00-BB.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月27日17时25分-ve2.5-eq0.6-H00-BB.xlsx"

# 不同流速，3mm热电偶测温（加6.3mm套管后）
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日15时23分-ve5.0-eq0.6-H00-BB.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日15时56分-ve4.5-eq0.6-H00-BB.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日16时26分-ve4-eq0.6-H00-BB.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日17时12分-ve3.5-eq0.6-H00-BB.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日17时44分-ve3.0-eq0.6-H00-BB.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日18时48分-ve2.5-eq0.6-H00-BB.xlsx",
    r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月28日18时16分-ve2.0-eq0.6-H00-BB.xlsx",

    # 添加更多文件路径...

]

sheet_name = 'A_n_T_ave'  # 工作表名称
# start_value = 100 # 起始行（对应目标数据x_start)这一行开始读取数据，改轴向位置的数据
# end_value = 400 # 结束行（对应目标数据x_end)这一行结束读取数据，改轴向位置的数据

plt.figure(figsize=(10, 6))

for file_path in excel_files:

    # 读取特定工作表
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # # ----查看特定x轴范围-开始---- 从数据中
    # # ----找到等于 start_value 和 end_value 的索引----
    # # (start_index 和 end_index 是布尔序列，用于标记列中等于 start_value 和 end_value 的行。然后使用 start_index.idxmax() 和 end_index.idxmax() 获取这些值对应的第一个索引。如果找到了这些值，则选择这个范围内的数据进行绘图。)
    # start_index = df[df.columns[0]] == start_value
    # end_index = df[df.columns[0]] == end_value
    #
    # if start_index.any() and end_index.any():
    #     df = df.loc[start_index.idxmax():end_index.idxmax()]
    # # ----查看特定x轴范围-结束----


    # 获取文件和工作表名称
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    wks_name = f"{base_name}_{sheet_name}"

    # 第一列为X轴，其余列为Y轴
    x_column = df.columns[0]
    y_columns = df.columns[1:]


    # 绘制每个文件的数据
    for y_col in y_columns:
        plt.plot(df[x_column], df[y_col], linestyle='-', marker='s', label=f"{wks_name}: {y_col}")

plt.xlabel('X Axis')
plt.ylabel('Values')
plt.title('X-Y Plots from Multiple Excel Sheets')
plt.legend()
plt.show()
