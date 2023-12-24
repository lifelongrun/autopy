import pandas as pd

# 读取Excel文件
# todo to update the file path of pre-processed data
file_path =   r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日21时42分-ve3.5-eq0.8-H00-BBS-45-below15mm.xlsx"
df = pd.read_excel(file_path, header=3)
# 指定从列标题: header=x 其中x是标题行的行序为第x+1行(默认从0开始)
# sep="\t"

# ---水平轴温度数据---
df['R_n'] = df['水平位置（mm）'].abs()
# 确保R_n列是正确的数据类型，如果是字符串，可能需要转换为数值
df['R_n'] = pd.to_numeric(df['R_n'], errors='coerce')

# 原径向测温，选取的径向高度温度点[only for BB]
# 分组并计算每个R_n下最后两个T1值的平均温度
# average_temperatures_R_n = df.groupby('R_n')[['温度1', '温度2', '温度3', '温度4']].apply(lambda x: x.iloc[-5:-1].mean())
# 或者
# 原径向测温，选取的径向高度温度点[only for BBS-45/55/65];备注：多添加了两个径向高度下温度6和温度7的测量
# 分组并计算每个R_n下最后两个T1值的平均温度
average_temperatures_R_n = df.groupby('R_n')[['温度1', '温度2', '温度3', '温度4', '温度6', '温度7']].apply(lambda x: x.iloc[-5:-1].mean())

# ---竖直轴温度数据---
df['A_n'] = df['竖向位置（mm）'].abs()
# 确保R_n列是正确的数据类型，如果是字符串，可能需要转换为数值
df['A_n'] = pd.to_numeric(df['A_n'], errors='coerce')

# 分组并计算每个R_n下最后几行个T1值的平均温度（最后行不取）, 数据类型为Pandas中的DaraFrame
average_temperatures_A_n = df.groupby('A_n')[['温度5']].apply(lambda x: x.iloc[-5:-1].mean()) # 从倒数第2行开始取，直到倒数第5行，共计4行数据点

# 打印结果(unsorted_dataframe)
print(f"水平位置及对应平均温度(unsorted_dataframe)：\n{average_temperatures_R_n}\n"
      f"竖向位置及对应平均温度(unsorted_dataframe)：\n{average_temperatures_A_n}")

# 单独输出为一个Excel文件(含单个工作表)
# average_temperatures_A_n.to_excel(r'E:\OneDrive\00_To_Do\1.Graduate Paper\Data\ve3.5-eq0.6-H60-A_n.xlsx')


# 假设 your_dataframe 是你要排序的DataFrame
# your_dataframe['R_n'].abs() 会计算 R_n 列的每个值的绝对值，然后使用赋值操作将这些绝对值存回原来的列。这样，所有原本为负数的值都会变为正数。

# 此时R_n中的值为正值，再进行按从小到大进行排序：`sort_values(by='R_n')` 表示按照 `R_n` 列的值进行排序
average_temperatures_A_n = average_temperatures_A_n.sort_values(by='A_n', ascending=True)
average_temperatures_R_n = average_temperatures_R_n.sort_values(by='R_n', ascending=True)

# 原始数据文件路径 file_path
# 创建一个ExcelWriter对象，用于向文件追加内容

with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:
    # 检查工作簿中是否已存在这些工作表
    if 'R_n_T_ave' not in writer.book.sheetnames:
        average_temperatures_R_n.to_excel(writer, sheet_name='R_n_T_ave')
    if 'A_n_T_ave' not in writer.book.sheetnames:
        average_temperatures_A_n.to_excel(writer, sheet_name='A_n_T_ave')

# 注意：这里没有设置 index=False，因此索引也会被写入到工作表中
# 如果你不希望写入索引，请添加 index=False 参数

# 打印排序后的结果
print(f"水平位置及对应平均温度(sorted_dataframe)：\n{average_temperatures_R_n}\n"
      f"竖向位置及对应平均温度(sorted_dataframe)：\n{average_temperatures_A_n}")