import pandas as pd

# 读取Excel文件
df = pd.read_excel(r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月23日19时48分-ve2.5-eq0.6-H00-BB.xlsx")
# sep="\t"
# ---水平轴温度数据---
df['R_n'] = df['水平位置（mm）']
# 确保R_n列是正确的数据类型，如果是字符串，可能需要转换为数值
df['R_n'] = pd.to_numeric(df['R_n'], errors='coerce')

# 分组并计算每个R_n下最后两个T1值的平均温度
average_temperatures_R_n = df.groupby('R_n')[['温度1', '温度2', '温度3', '温度4']].apply(lambda x: x.iloc[-5:-1].mean())


# ---竖直轴温度数据---

df['A_n'] = df['竖向位置（mm）']
# 确保R_n列是正确的数据类型，如果是字符串，可能需要转换为数值
df['A_n'] = pd.to_numeric(df['A_n'], errors='coerce')

# 分组并计算每个R_n下最后两个T1值的平均温度
average_temperatures_A_n = df.groupby('A_n')[['温度5']].apply(lambda x: x.iloc[-5:-1].mean())



# 打印结果
print(f"水平位置及对应平均温度：{average_temperatures_R_n} \n "
      f"竖向位置及对应平均温度：{average_temperatures_A_n}")
