import pandas as pd
import numpy as np
from pandas import ExcelWriter
import matplotlib.pyplot as plt
import os
import seaborn as sns


def save_df_to_excel(df, output_excel_file, sheet_name_for_df, index, prompt=True):
    """
    将指定的 DataFrame 保存到 Excel 文件中。

    :param df: 要保存的 DataFrame
    :param output_excel_file: 输出 Excel 文件的路径
    :param sheet_name_for_df: 工作表的名称
    :param prompt: 是否提示用户确认保存操作
    """
    # 如果设置了提示，则询问用户是否要保存
    if prompt and input("是否将表中数据输出为Excel文件？[y/n]") != "y":
        print("不输出Excel文件。")
        return

    try:
        # 检查文件是否存在，以确定写入模式
        if os.path.exists(output_excel_file):
            mode = 'a'  # 追加模式
        else:
            mode = 'w'  # 写入模式

        # 使用 ExcelWriter 写入数据
        with pd.ExcelWriter(output_excel_file, engine='openpyxl', mode=mode) as writer:
            # 检查工作簿中是否已存在这个工作表
            if sheet_name_for_df not in writer.book.sheetnames:
                df.to_excel(writer, sheet_name=sheet_name_for_df, index=index)
            else:
                print(f"工作表 {sheet_name_for_df} 已存在，未执行写入。")

    except PermissionError:
        print(
            f"Permission denied when writing to {output_excel_file}. Please close the file if it's open in another program.")


# 设置Seaborn样式
# sns.set()
# 设置字体以支持中文字符
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Excel文件路径列表
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

# ------File directory format of experiment operation conditions for BB👇👇👇------
# 不同燃料流速，3mm热电偶测温（加6.3mm套管后）
    # ---ve1.5-5.0-eq0.6-H00-BB---✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日15时23分-ve5.0-eq0.6-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日15时56分-ve4.5-eq0.6-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日16时26分-ve4-eq0.6-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日17时12分-ve3.5-eq0.6-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日17时44分-ve3.0-eq0.6-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日18时48分-ve2.5-eq0.6-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日18时16分-ve2.0-eq0.6-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日19时37分-ve1.5-eq0.6-H00-BB.xlsx",
    # ---ve1.5-5-eq0.6-H20-BB---✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日20时30分-ve1.5-eq0.6-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月29日13时52分-ve2.0-eq0.6-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日21时09分-ve2.5-eq0.6-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月29日14时29分-ve3.0-eq0.6-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日21时40分-ve3.5-eq0.6-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月29日15时07分-ve4.0-eq0.6-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日22时12分-ve4.5-eq0.6-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月29日16时48分-ve5.0-eq0.6-H20-BB.xlsx",
# 不同掺氢比(eq0.6/0.8/1.0/1.2-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BB--- ✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日17时12分-ve3.5-eq0.6-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日21时40分-ve3.5-eq0.6-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月29日19时03分-ve3.5-eq0.6-H40-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月29日19时39分-ve3.5-eq0.6-H60-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月29日20时52分-ve3.5-eq0.6-H80-BB.xlsx",
        r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月29日21时54分-ve3.5-eq0.6-H100-BB.xlsx",
    # Hy---ve3.5-eq0.8-H00-100-BB--- ✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日17时26分-ve3.5-eq0.8-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月30日11时49分-ve3.5-eq0.8-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日22时24分-ve3.5-eq0.8-H40-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月05日10时05分-ve3.5-eq0.8-H60-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月05日10时54分-ve3.5-eq0.8-H80-BB.xlsx",
        r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日10时57分-ve3.5-eq0.8-H100-BB.xlsx",
    # Hy---ve3.5-eq1.0-H00-100-BB--- ✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日19时16分-ve3.5-eq1.0-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月30日13时26分-ve3.5-eq1.0-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日14时04分-ve3.5-eq1.0-H40-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日13时13分-ve3.5-eq1.0-H60-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日12时23分-ve3.5-eq1.0-H80-BB.xlsx",
        r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日11时41分-ve3.5-eq1.0-H100-BB.xlsx",
    # Hy---ve3.5-eq1.2-H00-H100-BB---✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日20时45分-ve3.5-eq1.2-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日21时48分-ve3.5-eq1.2-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日14时41分-ve3.5-eq1.2-H40-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日15时59分-ve3.5-eq1.2-H60-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日16时37分-ve3.5-eq1.2-H80-BB.xlsx",
        r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日17时18分-ve3.5-eq1.2-H100-BB.xlsx",
# 不同当量比(H00/H20): 3mm热电偶测温（加6.3mm套管后）
    # ---ve3.5-eq0.4-1.2-H00-BB---✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日15时58分-ve3.5-eq0.4-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月03日15时12分-ve3.5-eq0.5-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日17时12分-ve3.5-eq0.6-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日16时39分-ve3.5-eq0.7-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日17时26分-ve3.5-eq0.8-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日18时32分-ve3.5-eq0.9-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日19时16分-ve3.5-eq1.0-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日19时59分-ve3.5-eq1.1-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日20时45分-ve3.5-eq1.2-H00-BB.xlsx",
    # ---ve3.5-eq0.4-1.2-H20-BB---✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月30日10时40分-ve3.5-eq0.4-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月30日10时00分-ve3.5-eq0.5-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月28日21时40分-ve3.5-eq0.6-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月29日22时33分-ve3.5-eq0.7-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月30日11时49分-ve3.5-eq0.8-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月30日12时29分-ve3.5-eq0.9-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月30日13时26分-ve3.5-eq1.0-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月30日14时21分-ve3.5-eq1.1-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日21时48分-ve3.5-eq1.2-H20-BB.xlsx",
# ----------------------------------------------------------------------------------------End👆👆👆------

# ------BBS-45/55/65------
# ------File directory format of experiment operation conditions for BBS-45-below15mm👇👇👇------
# 不同燃料流速(ve1.5-4.0-eq0.6-H20)，3mm热电偶测温（加6.3mm套管后）
    # ve---ve1.5-4.0-eq0.6-H20-BBS-45---✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月21日19时28分-ve1.5-eq0.6-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月21日20时01分-ve2.0-eq0.6-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月21日20时37分-ve2.5-eq0.6-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月21日21时08分-ve3.0-eq0.6-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月21日21时45分-ve3.5-eq0.6-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月21日22时19分-ve4.0-eq0.6-H20-BBS-45-below15mm.xlsx",
# 不同掺氢比(eq0.6/eq0.8/eq1.0/eq1.2-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BBS-45--- ✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日15时40分-ve3.5-eq0.6-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月21日21时45分-ve3.5-eq0.6-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日16时23分-ve3.5-eq0.6-H40-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日16时58分-ve3.5-eq0.6-H60-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日17时49分-ve3.5-eq0.6-H80-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日18时22分-ve3.5-eq0.6-H100-BBS-45-below15mm.xlsx",
    # Hy---ve3.5-eq0.8-H00-100-BBS-45--- ✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日21时42分-ve3.5-eq0.8-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日21时10分-ve3.5-eq0.8-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日20时37分-ve3.5-eq0.8-H40-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日20时05分-ve3.5-eq0.8-H60-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日19时31分-ve3.5-eq0.8-H80-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日18时55分-ve3.5-eq0.8-H100-BBS-45-below15mm.xlsx",
    # Hy---ve3.5-eq1.0-H00-100-BBS-45--- ✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日15时08分-ve3.5-eq1.0-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日15时39分-ve3.5-eq1.0-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日16时11分-ve3.5-eq1.0-H40-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日16时43分-ve3.5-eq1.0-H60-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日17时14分-ve3.5-eq1.0-H80-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日17时49分-ve3.5-eq1.0-H100-BBS-45-below15mm.xlsx",
    # Hy---ve3.5-eq1.2-H00-100-BBS-45--- ✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日21时19分-ve3.5-eq1.2-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日20时46分-ve3.5-eq1.2-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日20时14分-ve3.5-eq1.2-H40-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日19时42分-ve3.5-eq1.2-H60-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日18时59分-ve3.5-eq1.2-H80-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日18时21分-ve3.5-eq1.2-H100-BBS-45-blow15mm.xlsx",
# 不同当量比(eq0.6-1.2-H00/H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.6-1.2-H00-BBS-45---✅ 已导出(1sheet)：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日15时40分-ve3.5-eq0.6-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月24日14时06分-ve3.5-eq0.7-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日21时42分-ve3.5-eq0.8-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月24日15时09分-ve3.5-eq0.9-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日15时08分-ve3.5-eq1.0-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月24日16时26分-ve3.5-eq1.1-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日21时19分-ve3.5-eq1.2-H00-BBS-45-below15mm.xlsx",
    # eq---ve3.5-eq0.6-1.2-H20-BBS-45---✅ 已导出(1sheet)：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月21日21时45分-ve3.5-eq0.6-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月24日14时37分-ve3.5-eq0.7-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日21时10分-ve3.5-eq0.8-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月24日15时42分-ve3.5-eq0.9-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日15时39分-ve3.5-eq1.0-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月24日16时58分-ve3.5-eq1.1-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日20时46分-ve3.5-eq1.2-H20-BBS-45-below15mm.xlsx",
# ----------------------------------------------------------------------------------------End👆👆👆------

# ------File directory format of experiment operation conditions for BBS-55-below15mm👇👇👇------
# 不同燃料流速(ve1.5-4.0-eq0.6-H00/H20)，3mm热电偶测温（加6.3mm套管后）
    # ve---ve1.5-4.0-eq0.6-H20-BBS-55---✅ 已导出(1sheet)：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日14时17分-ve1.5-eq0.6-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日14时53分-ve2.0-eq0.6-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日15时24分-ve2.5-eq0.6-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日16时09分-ve3.0-eq0.6-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日16时42分-ve3.5-eq0.6-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日17时14分-ve4.0-eq0.6-H20-BBS-55-below15mm.xlsx",
# 不同掺氢比(eq0.6/eq0.8/eq1.0/eq1.2-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BBS-55--- ✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日17时49分-ve3.5-eq0.6-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日16时42分-ve3.5-eq0.6-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日11时32分-ve3.5-eq0.6-H40-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日12时05分-ve3.5-eq0.6-H60-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日12时42分-ve3.5-eq0.6-H80-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日13时18分-ve3.5-eq0.6-H100-BBS-55-below15mm.xlsx",
    # Hy---ve3.5-eq0.8-H00-100-BBS-55--- ✅ 已导出(1sheet)：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日17时16分-ve3.5-eq0.8-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日16时42分-ve3.5-eq0.8-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日16时06分-ve3.5-eq0.8-H40-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日15时00分-ve3.5-eq0.8-H60-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日14时26分-ve3.5-eq0.8-H80-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日13时52分-ve3.5-eq0.8-H100-BBS-55-below15mm.xlsx",
    # Hy---ve3.5-eq1.0-H00-100-BBS-55--- ✅ 已导出(1sheet)：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日18时20分-ve3.5-eq1.0-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日19时32分-ve3.5-eq1.0-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日20时03分-ve3.5-eq1.0-H40-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日20时34分-ve3.5-eq1.0-H60-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日21时05分-ve3.5-eq1.0-H80-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月21日14时12分-ve3.5-eq1.0-H100-BBS-55-below15mm.xlsx",
    # Hy---ve3.5-eq1.2-H00-100-BBS-55--- ✅ 已导出(1sheet)：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日20时42分-ve3.5-eq1.2-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日21时41分-ve3.5-eq1.2-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日22时18分-ve3.5-eq1.2-H40-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日22时49分-ve3.5-eq1.2-H60-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日23时21分-ve3.5-eq1.2-H80-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日23时54分-ve3.5-eq1.2-H100-BBS-55-below15mm.xlsx",
# 不同当量比(eq0.6-1.2-H00/H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.6-1.2-H00-BBS-55---✅ 已导出(1sheet)：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日17时49分-ve3.5-eq0.6-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月21日17时51分-ve3.5-eq0.7-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日17时16分-ve3.5-eq0.8-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月21日15时57分-ve3.5-eq0.9-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日18时20分-ve3.5-eq1.0-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月21日15时24分-ve3.5-eq1.1-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日20时42分-ve3.5-eq1.2-H00-BBS-55-below15mm.xlsx",
    # eq---ve3.5-eq0.6-1.2-H20-BBS-55---✅ 已导出(1sheet)：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日16时42分-ve3.5-eq0.6-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月21日17时20分-ve3.5-eq0.7-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日16时42分-ve3.5-eq0.8-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月21日16时49分-ve3.5-eq0.9-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日19时32分-ve3.5-eq1.0-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月21日14时50分-ve3.5-eq1.1-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日21时41分-ve3.5-eq1.2-H20-BBS-55-below15mm.xlsx",
# ----------------------------------------------------------------------------------------End👆👆👆------

# ------File directory format of experiment operation conditions for BBS-65-below15mm👇👇👇------
# 不同燃料流速(ve1.5-4.0-eq0.6-H20)，3mm热电偶测温（加6.3mm套管后）
    # ve---ve1.5-4.0-eq0.6-H20-BBS-65---✅ 已导出(1sheet)：
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日21时07分-ve1.5-eq0.6-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日20时50分-ve2.0-eq0.6-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日20时18分-ve2.5-eq0.6-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日19时42分-ve3.0-eq0.6-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日19时09分-ve3.5-eq0.6-H20-BBS-65-below15mm.xlsx",
#🟢 已解决:Re1-径向靠近中心的温度偏低/分析流速时，不要4m/s这组数据(Sn=45-65)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日18时37分-ve4.0-eq0.6-H20-BBS-65-below15mm.xlsx",
# 不同掺氢比(eq0.6/eq0.8/eq1.0/eq1.2-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BBS-65--- ✅ 已导出(1sheet)
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日14时22分-ve3.5-eq0.6-H00-BBS-65-redo.xlsx", # 重做完成🟢 已经合并；注意：轴向位置为0mm时，径向温度T1(最小方位置的热电偶)测得温度偏高，此时，轴向热电偶使得火焰显胖，导致径向热电偶温度偏高
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日19时09分-ve3.5-eq0.6-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日15时39分-ve3.5-eq0.6-H40-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日16时40分-ve3.5-eq0.6-H60-BBS-65-below15mm.xlsx", # 重做完成🟢 已经合并
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日17时15分-ve3.5-eq0.6-H80-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日17时47分-ve3.5-eq0.6-H100-BBS-65-below15mm.xlsx",
    # Hy---ve3.5-eq0.8-H00-100-BBS-65--- ✅ 已导出(1sheet)：
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日18时21分-ve3.5-eq0.8-H00-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日19时25分-ve3.5-eq0.8-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日19时57分-ve3.5-eq0.8-H40-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日20时32分-ve3.5-eq0.8-H60-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日21时05分-ve3.5-eq0.8-H80-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日21时37分-ve3.5-eq0.8-H100-BBS-65-below15mm.xlsx",
    # Hy---ve3.5-eq1.0-H00-100-BBS-65--- ✅ 已导出(1sheet)：
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日22时12分-ve3.5-eq1.0-H00-BBS-65-below15mm.xlsx", # 🔴  T6温度规律与其他不一致
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日16时40分-ve3.5-eq1.0-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日17时16分-ve3.5-eq1.0-H40-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日17时47分-ve3.5-eq1.0-H60-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日18时19分-ve3.5-eq1.0-H80-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日18时51分-ve3.5-eq1.0-H100-BBS-65-below15mm.xlsx",
    # Hy---ve3.5-eq1.2-H00-100-BBS-65--- ✅ 已导出(1sheet)：
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日19时25分-ve3.5-eq1.2-H00-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日19时57分-ve3.5-eq1.2-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日20时42分-ve3.5-eq1.2-H40-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日21时19分-ve3.5-eq1.2-H60-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日21时50分-ve3.5-eq1.2-H80-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日22时25分-ve3.5-eq1.2-H100-BBS-65-below15mm.xlsx",
# 不同当量比(eq0.6-1.2-H00/H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.6-1.2-H00-BBS-65---✅ 已导出(1sheet)：
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日14时22分-ve3.5-eq0.6-H00-BBS-65-redo.xlsx",  # 重做完成🟢 已经合并到源文件中（23年01月08日数据到24年12月16日）
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月18日13时15分-ve3.5-eq0.7-H00-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日18时21分-ve3.5-eq0.8-H00-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月18日12时39分-ve3.5-eq0.9-H00-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日22时12分-ve3.5-eq1.0-H00-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月18日12时06分-ve3.5-eq1.1-H00-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日19时25分-ve3.5-eq1.2-H00-BBS-65-below15mm.xlsx",
    # eq---ve3.5-eq0.6-1.2-H20-BBS-65---✅ 已导出(1sheet)：
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日19时09分-ve3.5-eq0.6-H20-BBS-65-below15mm.xlsx", # 🟢 径向靠近中心的温度T1偏高(有一个点)，暂视为接受
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月18日11时01分-ve3.5-eq0.7-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日19时25分-ve3.5-eq0.8-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月18日11时33分-ve3.5-eq0.9-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日16时40分-ve3.5-eq1.0-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日23时14分-ve3.5-eq1.1-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日19时57分-ve3.5-eq1.2-H20-BBS-65-below15mm.xlsx",
# ----------------------------------------------------------------------------------------End👆👆👆------
]

# ---write to excel---
# ---将dataframe中的数据写入到Excel文件中---
# 指定 Excel 文件路径及文件名（无论是否存在）
short_name = "ve3.5-eq1.2-H00-100-BBS-65"
# output_excel_file = rf"E:\OneDrive\00_To_Do\1.Graduate Paper\Thesis paper\Data_output_{short_name}-1sheet-kelvin.xlsx"
output_excel_file = rf"E:\OneDrive\00_To_Do\1.Graduate Paper\Thesis paper\Data_output_{short_name}-1sheet-kelvin.xlsx"
# 工作表名称前缀，区别摄氏度"℃"/开尔文"K"
prefix_sheet_name = ["C", "K"]
new_sheet_name_for_A_n_C = prefix_sheet_name[0] + '_A_n_T'
new_sheet_name_for_R_n_C = prefix_sheet_name[0] + '_R_n_T'
new_sheet_name_for_A_n_K = prefix_sheet_name[1] + '_A_n_T'
new_sheet_name_for_R_n_K = prefix_sheet_name[1] + '_R_n_T'
# ---End---
# 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


# 为第一张图创建DataFrame
df_A_n_list_of_first_chart = []
index_list_first_chart = []
# 在 pd.concat() 函数中，keys 参数用于创建一个多级索引（也称为分层索引）。这意味着每个合并后的DataFrame的行将保持其原有的索引，并附加一个额外的外层索引，这个外层索引是由 keys 参数提供的值组成的。

# 初始化一个空的 DataFrame 来存放X-Y plot后最终的数据 #👈
all_A_n_x_ys_df = pd.DataFrame()
index_A_n_x_ys_df = []
df_all_A_n_x_ys_df = []

plt.figure(figsize=(10, 6))
for file_path in excel_files:
    df = pd.read_excel(file_path, sheet_name='A_n_T_ave') # 读取工作表A_n_T_ave
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    wks_name = f"{base_name}_A_n_T_ave"

    # 确保 x 列（假设是第一列）被添加到 final_df 中  #👈
    if all_A_n_x_ys_df.empty:
        all_A_n_x_ys_df['A_n_X轴'] = df.iloc[:, 0]  # 假设 x 列是每个 DataFrame 的第一列

    df_A_n_list_of_first_chart.append(df)  # 将每个文件的DataFrame添加到列表中
    index_list_first_chart.append(wks_name)
    index_A_n_x_ys_df = index_list_first_chart
    x_column = df.columns[0]
    y_columns = df.columns[1:]
    for y_col in y_columns:
        # 添加 y 值到 final_df  #👈
        all_A_n_x_ys_df[f"{wks_name}_{y_col}"] = df[y_col].astype(float)+273.15  #👈

        plt.plot(df[x_column], df[y_col], linestyle='-', marker='s', label=f"{wks_name}: {y_col}")
plt.xlabel('X轴')
plt.ylabel('数值')
plt.title('A_n_T_ave工作表的X-Y图')
plt.legend()
plt.show()

# 将列表中的DataFrame合并为一个DataFrame, 采用concat合并这些DataFrame, keys为多级索引, 也称为分层索引，在本文件中为文件名
df_list_first_chart_df = pd.concat(df_A_n_list_of_first_chart, keys=index_list_first_chart)
# df_list_first_chart_df.to_excel(output_excel_file, sheet_name=new_sheet_name_for_A_n_C, index=True)
# ----------------------End👆👆👆----------------------

# ---第2张图---
# 为每个y列创建一个子图
num_of_cols = 6  # 假设您想在每个文件中为前4列（除了X轴列）创建图表
# 字母序号列表
letters = ['a', 'b', 'c', 'd', 'e', 'f']  # 根据需要的子图数量调整
colors = ['red', 'green', 'blue', 'orange', 'yellow', 'black']  # 根据需要的子图数量调整
plt.figure(figsize=(20, 10))  # 调整图表大小

df_R_n_list_of_second_chart = []
index_list_second_chart = []

# ------method 1: ------#
# 初始化一个空的 DataFrame 来存放所有 y 值
all_R_n_x_ys_df = pd.DataFrame()
index_R_n_x_ys_df = []
# ------为第二张图创建DataFrame, 将多列数据写入到同一个Excel文件的不同工作表中 it works!👍
for file_path in excel_files:
    df = pd.read_excel(file_path, sheet_name='R_n_T_ave')
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    # 获得索引名称
    wks_name = f"{base_name}_R_n_T_ave"
    index_list_second_chart.append(wks_name)
    index_R_n_x_ys_df = index_list_second_chart
    df_R_n_list_of_second_chart.append(df)  # 将每个文件的DataFrame添加到列表中

    # 确保 x 列（假设是第一列）被添加到 all_R_n_x_ys_df中  #👈
    if all_R_n_x_ys_df.empty:
        all_R_n_x_ys_df['R_n_X轴'] = df.iloc[:, 0]  # 假设 x 列是每个 DataFrame 的第一列

    x_column = df.columns[0]
    y_columns = df.columns[1:num_of_cols+1]

    for i, y_col in enumerate(y_columns, start=1):
        # 添加y值并转换为浮点数+273.15,再添加到all_R_n_x_ys_df中
        all_R_n_x_ys_df[f"{wks_name}_{y_col}"] = df[y_col].astype(float) + 273.15  #👈

        plt.subplot(2, 3, i)  # 创建2x2的子图布局
        plt.plot(df[x_column], df[y_col], linestyle='-', marker='s', label=f"{base_name}: {y_col}")
        plt.xlabel(f"X轴 - {y_col}的X-Y图")  # 将标题作为X轴标签的一部分
        plt.ylabel('数值')
        plt.title(f"({letters[i-1]}){y_col}的X-Y图")
        plt.legend()

# plt.tight_layout()  # 调整子图布局
plt.show()
# 将列表中的DataFrame合并为一个DataFrame, 采用concat合并这些DataFrame
df_list_of_second_chart_df = pd.concat(df_R_n_list_of_second_chart, keys=index_list_second_chart, axis=1)
# ----method 1 end----

# #-----good 作用提取所有”温度1“的列, 并将这些列写入到同一个Excel文件的不同工作表中 it works!👍
# # 筛选出所有列名中包含 "温度1" 的列
# columns_with_temp1 = [col for col in all_R_n_x_ys_df.columns if "温度1" in col]
#
# # 提取这些列
# temp1_df = all_R_n_x_ys_df[columns_with_temp1]
# save_df_to_excel(temp1_df, output_excel_file, "temp1", index=True, prompt=False) # 索引选择True, 会将索引列输出到Excel文件中
# #----good end


# ------export data - method 2: awesome'✅------#
# 定义包含所有温度列名关键字的列表
temperature_columns = ["温度1", "温度2", "温度3", "温度4", "温度6", "温度7"]

# 创建一个字典来存储每个温度的 DataFrame
temperature_dfs = {}

for temp in temperature_columns:
    # 筛选出包含当前温度列名关键字的列
    selected_columns = [col for col in all_R_n_x_ys_df.columns if temp in col]

    # 提取这些列并存储在字典中
    temperature_dfs[temp] = all_R_n_x_ys_df[selected_columns]
# print(temperature_dfs["温度2"])
# 现在，temperature_dfs['温度1'] 将包含所有 '温度1' 的列，temperature_dfs['温度2'] 将包含所有 '温度2' 的列，以此类推。
merged_all_R_n_df = pd.concat(temperature_dfs.values(), axis=1) # 将字典中的所有 DataFrame/Series 合并为一个 DataFrame，temperature_dfs.values() 返回一个包含所有 DataFrame 的列表
merged_A_R_df = pd.concat([all_A_n_x_ys_df, merged_all_R_n_df], axis=1)
# -------以单位为K, 将X-Y plot data导出到Excel文件中------
# save_df_to_excel(merged_A_R_df, output_excel_file, "K_both_A_R_n_T", index=True, prompt=False) # 索引选择True, 会将索引列输出到Excel文件中; prompt=True, 会在输出Excel文件时，弹出对话框，询问是否覆盖已有文件
# ------method 2 end----


# # ----------------------Export and save data:----------------------
# # prompt=True, 会在输出Excel文件时，弹出对话框，询问是否覆盖已有文件
# wait_4users_prompt = True
# # worksheet 1-2th, C
# # ✅ save graph data for first chart, units: Celsius
# print(f"1st worksheet: A_n_T(℃)->{new_sheet_name_for_A_n_C}")
# save_df_to_excel(df_list_first_chart_df, output_excel_file, new_sheet_name_for_A_n_C, index_list_first_chart, prompt=wait_4users_prompt) # 输入DataFrame, 输出到Excel文件中的工作表名称, 索引名称列表
#
# # ✅  save graph data for second chart, units: Celsius
# print(f"2st worksheet: A_n_T(℃)->{new_sheet_name_for_A_n_C}")
# save_df_to_excel(df_list_of_second_chart_df, output_excel_file, new_sheet_name_for_R_n_C, index_list_second_chart, prompt=wait_4users_prompt) # 输入DataFrame, 输出到Excel文件中的工作表名称, 索引名称列表
#
# # ✅ save graph data for two charts in one worksheet, units: Kelvin
# df_combined_all_A_R_n_x_ys_df = pd.concat([all_A_n_x_ys_df, all_R_n_x_ys_df], axis=1)
# new_sheet_name_for_df_combined = "K_both_A_R_n_T"
# print(f"3st worksheet: A_n_T(K)+R_n_T(K)->{new_sheet_name_for_df_combined}...")
# save_df_to_excel(df_combined_all_A_R_n_x_ys_df, output_excel_file, new_sheet_name_for_df_combined, index=True, prompt=wait_4users_prompt) # 索引选择True, 会将索引列输出到Excel文件中
# # ----------------------End👆👆👆----------------------
#
