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
def process_excel_file(file, columns, num_rows):
    """ 读取指定Excel文件中的特定列，计算这些列最后num_rows行的平均值。 """
    df = pd.read_excel(file, sheet_name='testo', usecols=columns)
    last_rows = df.tail(num_rows)
    return last_rows.mean()

# Excel文件和列名，报错的话注意r及逗号分隔符
excel_files = [
    # 文件路径列表, 报错信息，逗号分隔符
    # ...✅/❎/🟢/🔴/🕝➡️/👀
# ------File directory format of experiment operation conditions for BB/BBS-45/55/65-below15mm👇👇👇------
# 不同燃料流速(ve1.5-5.0-eq0.6-H00/H20)，3mm热电偶测温（加6.3mm套管后）
    # ve---ve1.5-5.0-eq0.6-H00-BB---🟢/🕝➡️/👀/✅
    # ve---ve1.5-5.0-eq0.6-H20-BB---🔴
# 不同掺氢比(eq0.6/eq0.8/eq1.0/eq1.2-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BB--- 🔴
    # Hy---ve3.5-eq0.8-H00-100-BB--- 🔴
    # Hy---ve3.5-eq1.0-H00-100-BB--- 🔴
    # Hy---ve3.5-eq1.2-H00-100-BB--- 🔴
# 不同当量比(eq0.4-1.2-H00/H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.4-1.2-H00-BB---🔴
    # eq---ve3.5-eq0.4-1.2-H20-BB---🔴
# ----------------------------------------------------------------------------------------End👆👆👆------

    # 文件路径列表, 报错信息，逗号分隔符
    # ...✅/❎/🟢/🔴/🕝➡️/👀
# ------File directory format of experiment operation conditions for BB-below15mm👇👇👇------
# 不同燃料流速(ve1.5-5.0-eq0.6-H00/H20)，3mm热电偶测温（加6.3mm套管后）
    # ve---ve1.5-5.0-eq0.6-H00-BB---redo✅---
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve1.5-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve2.0-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve2.5-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve3.0-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve3.5-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve4.0-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve4.5-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve4.5-H00-BB-exit.xlsx",
    # ve---ve1.5-5.0-eq0.6-H20-BB---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve1.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve2.0-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve2.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve3.0-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve4.0-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve4.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve5.0-H20-BB-exit.xlsx",
# 不同掺氢比(eq0.6/eq0.8/eq1.0/eq1.2-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BB--- ✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve3.5-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve3.5-H40-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve3.5-H60-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve3.5-H80-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve3.5-H100-BB-exit.xlsx",
    # # Hy---ve3.5-eq0.8-H00-100-BB--- ✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.8-ve3.5-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.8-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.8-ve3.5-H40-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.8-ve3.5-H60-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.8-ve3.5-H80-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.8-ve3.5-H100-BB-exit.xlsx",
    # # Hy---ve3.5-eq1.0-H00-100-BB--- ✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.0-ve3.5-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.0-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.0-ve3.5-H40-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.0-ve3.5-H60-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.0-ve3.5-H80-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.0-ve3.5-H100-BB-exit.xlsx",
    # # Hy---ve3.5-eq1.2-H00-100-BB--- ✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.2-ve3.5-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.2-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.2-ve3.5-H40-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.2-ve3.5-H60-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.2-ve3.5-H80-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.2-ve3.5-H100-BB-exit.xlsx",
# 不同当量比(eq0.4-1.2-H00/H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.4-1.2-H00-BB---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.4-ve3.5-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.5-ve3.5-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve3.5-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.7-ve3.5-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.8-ve3.5-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.9-ve3.5-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.0-ve3.5-H00-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.1-ve3.5-H00-BB-exit.xlsx",

    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.2-ve3.5-H00-BB-exit.xlsx",
    # eq---ve3.5-eq0.4-1.2-H20-BB---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.4-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.5-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.6-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.7-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.8-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq0.9-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.0-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.1-ve3.5-H20-BB-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB-Exit\2023-12-29-eq1.2-ve3.5-H20-BB-exit.xlsx",
# ----------------------------------------------------------------------------------------End👆👆👆------


    # ...✅/❎/🟢/🔴/🕝➡️/👀
# ------File directory format of experiment operation conditions for BB/BBS-45/55/65-below15mm👇👇👇------
# 不同燃料流速(ve1.5-4.0-eq0.6-H20)，3mm热电偶测温（加6.3mm套管后
    # ve---ve1.5-4.0-eq0.6-H20-BBS-45---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.6-ve1.5-H20-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.6-ve2.0-H20-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.6-ve2.5-H20-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.6-ve3.0-H20-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.6-ve3.5-H20-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.6-ve4.0-H20-BBS-45-exit.xlsx",
# 不同掺氢比(eq0.6/eq0.8/eq1.0/eq1.2-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BBS-45--- ✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.6-ve3.5-H00-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.6-ve3.5-H20-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.6-ve3.5-H40-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.6-ve3.5-H60-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.6-ve3.5-H80-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.6-ve3.5-H100-BBS-45-exit.xlsx",
    # Hy---ve3.5-eq0.8-H00-100-BBS-45--- ✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.8-ve3.5-H00-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.8-ve3.5-H20-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.8-ve3.5-H40-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.8-ve3.5-H60-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.8-ve3.5-H80-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.8-ve3.5-H100-BBS-45-exit.xlsx",
    # Hy---ve3.5-eq1.0-H00-100-BBS-45--- ✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.0-ve3.5-H00-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.0-ve3.5-H20-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.0-ve3.5-H40-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.0-ve3.5-H60-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.0-ve3.5-H80-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.0-ve3.5-H100-BBS-45-exit.xlsx",
    # Hy---ve3.5-eq1.2-H00-100-BBS-45--- ✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.2-ve3.5-H00-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.2-ve3.5-H20-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.2-ve3.5-H40-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.2-ve3.5-H60-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.2-ve3.5-H80-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.2-ve3.5-H100-BBS-45-exit.xlsx",
# 不同当量比(eq0.6-1.2-H00/H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.6-1.2-H00-BBS-45---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.6-ve3.5-H00-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.7-ve3.5-H00-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.8-ve3.5-H00-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.9-ve3.5-H00-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.0-ve3.5-H00-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.1-ve3.5-H00-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.2-ve3.5-H00-BBS-45-exit.xlsx",
    # eq---ve3.5-eq0.6-1.2-H20-BBS-45---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.6-ve3.5-H20-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.7-ve3.5-H20-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.8-ve3.5-H20-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq0.9-ve3.5-H20-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.0-ve3.5-H20-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.1-ve3.5-H20-BBS-45-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm-exit\2023-12-30-eq1.2-ve3.5-H20-BBS-45-exit.xlsx",
# ----------------------------------------------------------------------------------------End👆👆👆------


    # ...✅/❎/🟢/🔴/🕝➡️/👀
# ------File directory format of experiment operation conditions for BBS-55-below15mm👇👇👇------
# 不同燃料流速(ve1.5-4.0-eq0.6-H00/H20)，3mm热电偶测温（加6.3mm套管后）
    # ve---ve1.5-4.0-eq0.6-H20-BBS-55---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.6-ve1.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.6-ve2.0-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.6-ve2.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.6-ve3.0-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.6-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.6-ve4.0-H20-BBS-55-exit.xlsx",
# 不同掺氢比(eq0.6/eq0.8/eq1.0/eq1.2-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BBS-55---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.6-ve3.5-H00-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.6-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.6-ve3.5-H40-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.6-ve3.5-H60-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.6-ve3.5-H80-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.6-ve3.5-H100-BBS-55-exit.xlsx",
    # Hy---ve3.5-eq0.8-H00-100-BBS-55---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.8-ve3.5-H00-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.8-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.8-ve3.5-H40-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.8-ve3.5-H60-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.8-ve3.5-H80-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.8-ve3.5-H100-BBS-55-exit.xlsx",
    # Hy---ve3.5-eq1.0-H00-100-BBS-55---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.0-ve3.5-H00-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.0-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.0-ve3.5-H40-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.0-ve3.5-H60-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.0-ve3.5-H80-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.0-ve3.5-H100-BBS-55-exit.xlsx",
    # Hy---ve3.5-eq1.2-H00-100-BBS-55---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.2-ve3.5-H00-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.2-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.2-ve3.5-H40-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.2-ve3.5-H60-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.2-ve3.5-H80-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.2-ve3.5-H100-BBS-55-exit.xlsx",
# 不同当量比(eq0.6-1.2-H00/H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.6-1.2-H00-BBS-55---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.6-ve3.5-H00-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.7-ve3.5-H00-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.8-ve3.5-H00-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.9-ve3.5-H00-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.0-ve3.5-H00-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.1-ve3.5-H00-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.2-ve3.5-H00-BBS-55-exit.xlsx",
    # eq---ve3.5-eq0.6-1.2-H20-BBS-55---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.6-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.7-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.8-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq0.9-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.0-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.1-ve3.5-H20-BBS-55-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm-exit\2023-12-30-eq1.2-ve3.5-H20-BBS-55-exit.xlsx",
# ----------------------------------------------------------------------------------------End👆👆👆------

    # ...✅/❎/🟢/🔴/🕝➡️/👀
# ------File directory format of experiment operation conditions for BBS-55-below15mm👇👇👇------
# 不同燃料流速(ve1.5-4.0-eq0.6-H20)，3mm热电偶测温（加6.3mm套管后）
    # ve---ve1.5-4.0-eq0.6-H20-BBS-65---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.6-ve1.5-H20-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.6-ve2.0-H20-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.6-ve2.5-H20-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.6-ve3.0-H20-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.6-ve3.5-H20-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.6-ve4.0-H20-BBS-65-exit.xlsx",
# 不同掺氢比(eq0.6/eq0.8/eq1.0/eq1.2-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BBS-65--- 🔴🕝➡️/👀
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.6-ve3.5-H00-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.6-ve3.5-H20-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.6-ve3.5-H40-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.6-ve3.5-H60-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.6-ve3.5-H80-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.6-ve3.5-H100-BBS-65-exit.xlsx",
    # # Hy---ve3.5-eq0.8-H00-100-BBS-65--- 🔴🕝➡️/👀
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.8-ve3.5-H00-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.8-ve3.5-H20-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.8-ve3.5-H40-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.8-ve3.5-H60-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.8-ve3.5-H80-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.8-ve3.5-H100-BBS-65-exit.xlsx",
    # # Hy---ve3.5-eq1.0-H00-100-BBS-65--- 🔴🕝➡️/👀
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.0-ve3.5-H00-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.0-ve3.5-H20-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.0-ve3.5-H40-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.0-ve3.5-H60-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.0-ve3.5-H80-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.0-ve3.5-H100-BBS-65-exit.xlsx",
    # # Hy---ve3.5-eq1.2-H00-100-BBS-65--- 🔴🕝➡️/👀
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.2-ve3.5-H00-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.2-ve3.5-H20-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.2-ve3.5-H40-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.2-ve3.5-H60-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.2-ve3.5-H80-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.2-ve3.5-H100-BBS-65-exit.xlsx",
# 不同当量比(eq0.6-1.2-H00/H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.6-1.2-H00-BBS-65---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.6-ve3.5-H00-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.7-ve3.5-H00-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.8-ve3.5-H00-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.9-ve3.5-H00-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.0-ve3.5-H00-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.1-ve3.5-H00-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.2-ve3.5-H00-BBS-65-exit.xlsx",
    # eq---ve3.5-eq0.6-1.2-H20-BBS-65---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.6-ve3.5-H20-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.7-ve3.5-H20-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.8-ve3.5-H20-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq0.9-ve3.5-H20-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.0-ve3.5-H20-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.1-ve3.5-H20-BBS-65-exit.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-below15mm-exit\2023-12-30-eq1.2-ve3.5-H20-BBS-65-exit.xlsx",
# ----------------------------------------------------------------------------------------End👆👆👆------




















               ]  # 替换为实际文件名
columns_of_interest = ["% O2", "ppm CO", "ppm NO", "°C 烟温", 'ppm NOx', "% CO2IR", "ppm HC"]  # 替换为实际列名
num_rows = 12  # 指定要读取的最后x行（5s采集一次，即5s写入一行，取最后0.5-1分钟的烟气数据）

# 处理每个文件并收集平均值
averages = [process_excel_file(file, columns_of_interest, num_rows) for file in excel_files]
# 提取每个文件名中特定的部分作为索引
file_indices = [os.path.splitext(os.path.basename(file))[0].split('-', 3)[-1] for file in excel_files]
# split('-', 3)在第三个破折号处分割字符串，然后通过[-1]选择分割后的最后一部分。因此，对于2023 - 11 - 28 - ve1.5 - eq0.6 - H20 - BB，这会正确提取出ve1.5 - eq0.6 - H20 - BB
# 通过这种方式，如果文件名是 2023-11-28-ve1.5-eq0.6-H20-BB.xlsx，这段代码会正确地提取出 ve1.5-eq0.6-H20-BB 这部分作为索引。


# 将结果转换为DataFrame, 并设置新的索引
average_df = pd.DataFrame(averages, index=file_indices) # index=excel_files


# ---绘制图表---
# 设置子图的数量和布局
fig, axs = plt.subplots(3, 3, figsize=(15, 15))  # 3行3列的布局

# 为每个列创建一个柱状图
for i, column in enumerate(columns_of_interest):
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


print(average_df)
# ---将dataframe中的数据写入到Excel文件中---
if "y" == input("是否将表中数据（烟气数据）输出为Excel文件？[y/n]"):
    # 指定 Excel 文件路径及文件名（无论是否存在）
    output_excel_file = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\exit-ve3.5-eq0.4-1.2-H20-BB-12-29.xlsx" # 替换为实际文件名
    new_sheet_name = 'vexx-eqxx-Hxx' # 每次运行前，修改这里的工作表名称
    # 将数据写入到 Excel 文件的指定工作表中
    # average_df.to_excel(output_excel_file, sheet_name=new_sheet_name, index=True)

    try:
        with ExcelWriter(output_excel_file, engine='openpyxl', mode='a' if os.path.exists(output_excel_file) else 'w') as writer:
            average_df.to_excel(writer, sheet_name=new_sheet_name, index=True)
    except PermissionError:
        print(f"Permission denied when writing to {output_excel_file}. Please close the file if it's open in another program.")
else:
    print("不输出Excel文件。")