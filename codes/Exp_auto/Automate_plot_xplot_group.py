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
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月29日21时54分-ve3.5-eq0.6-H100-BB.xlsx",
    # Hy---ve3.5-eq0.8-H00-100-BB--- ✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日17时26分-ve3.5-eq0.8-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月30日11时49分-ve3.5-eq0.8-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日22时24分-ve3.5-eq0.8-H40-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月05日10时05分-ve3.5-eq0.8-H60-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月05日10时54分-ve3.5-eq0.8-H80-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日10时57分-ve3.5-eq0.8-H100-BB.xlsx",
    # Hy---ve3.5-eq1.0-H00-100-BB--- ✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日19时16分-ve3.5-eq1.0-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年11月30日13时26分-ve3.5-eq1.0-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日14时04分-ve3.5-eq1.0-H40-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日13时13分-ve3.5-eq1.0-H60-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日12时23分-ve3.5-eq1.0-H80-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日11时41分-ve3.5-eq1.0-H100-BB.xlsx",
    # Hy---ve3.5-eq1.2-H00-H100-BB---✅ 已导出：
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日20时45分-ve3.5-eq1.2-H00-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月04日21时48分-ve3.5-eq1.2-H20-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日14时41分-ve3.5-eq1.2-H40-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日15时59分-ve3.5-eq1.2-H60-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日16时37分-ve3.5-eq1.2-H80-BB.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BB\2023年12月06日17时18分-ve3.5-eq1.2-H100-BB.xlsx",
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
    # Hy---ve3.5-eq0.6-H00-100-BBS-45--- ✅
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日15时40分-ve3.5-eq0.6-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月21日21时45分-ve3.5-eq0.6-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日16时23分-ve3.5-eq0.6-H40-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日16时58分-ve3.5-eq0.6-H60-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日17时49分-ve3.5-eq0.6-H80-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日18时22分-ve3.5-eq0.6-H100-BBS-45-below15mm.xlsx",
    # Hy---ve3.5-eq0.8-H00-100-BBS-45--- ✅
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日21时42分-ve3.5-eq0.8-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日21时10分-ve3.5-eq0.8-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日20时37分-ve3.5-eq0.8-H40-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日20时05分-ve3.5-eq0.8-H60-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日19时31分-ve3.5-eq0.8-H80-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日18时55分-ve3.5-eq0.8-H100-BBS-45-below15mm.xlsx",
    # Hy---ve3.5-eq1.0-H00-100-BBS-45--- ✅
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日15时08分-ve3.5-eq1.0-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日15时39分-ve3.5-eq1.0-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日16时11分-ve3.5-eq1.0-H40-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日16时43分-ve3.5-eq1.0-H60-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日17时14分-ve3.5-eq1.0-H80-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日17时49分-ve3.5-eq1.0-H100-BBS-45-below15mm.xlsx",
    # Hy---ve3.5-eq1.2-H00-100-BBS-45--- ✅
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日21时19分-ve3.5-eq1.2-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日20时46分-ve3.5-eq1.2-H20-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日20时14分-ve3.5-eq1.2-H40-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日19时42分-ve3.5-eq1.2-H60-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日18时59分-ve3.5-eq1.2-H80-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日18时21分-ve3.5-eq1.2-H100-BBS-45-blow15mm.xlsx",
# 不同当量比(eq0.6-1.2-H00/H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.6-1.2-H00-BBS-45---✅
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日15时40分-ve3.5-eq0.6-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月24日14时06分-ve3.5-eq0.7-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月22日21时42分-ve3.5-eq0.8-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月24日15时09分-ve3.5-eq0.9-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日15时08分-ve3.5-eq1.0-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月24日16时26分-ve3.5-eq1.1-H00-BBS-45-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-45-below15mm\2023年12月23日21时19分-ve3.5-eq1.2-H00-BBS-45-below15mm.xlsx",
    # eq---ve3.5-eq0.6-1.2-H20-BBS-45---✅
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
    # ve---ve1.5-4.0-eq0.6-H20-BBS-55---✅
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日14时17分-ve1.5-eq0.6-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日14时53分-ve2.0-eq0.6-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日15时24分-ve2.5-eq0.6-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日16时09分-ve3.0-eq0.6-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日16时42分-ve3.5-eq0.6-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日17时14分-ve4.0-eq0.6-H20-BBS-55-below15mm.xlsx",
# 不同掺氢比(eq0.6/eq0.8/eq1.0/eq1.2-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BBS-55--- ✅
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日17时49分-ve3.5-eq0.6-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日16时42分-ve3.5-eq0.6-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日11时32分-ve3.5-eq0.6-H40-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日12时05分-ve3.5-eq0.6-H60-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日12时42分-ve3.5-eq0.6-H80-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日13时18分-ve3.5-eq0.6-H100-BBS-55-below15mm.xlsx",
    # Hy---ve3.5-eq0.8-H00-100-BBS-55--- ✅
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日17时16分-ve3.5-eq0.8-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日16时42分-ve3.5-eq0.8-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日16时06分-ve3.5-eq0.8-H40-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日15时00分-ve3.5-eq0.8-H60-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日14时26分-ve3.5-eq0.8-H80-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日13时52分-ve3.5-eq0.8-H100-BBS-55-below15mm.xlsx",
    # Hy---ve3.5-eq1.0-H00-100-BBS-55--- ✅
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日18时20分-ve3.5-eq1.0-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日19时32分-ve3.5-eq1.0-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日20时03分-ve3.5-eq1.0-H40-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日20时34分-ve3.5-eq1.0-H60-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日21时05分-ve3.5-eq1.0-H80-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月21日14时12分-ve3.5-eq1.0-H100-BBS-55-below15mm.xlsx"
    # Hy---ve3.5-eq1.2-H00-100-BBS-55--- ✅
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日20时42分-ve3.5-eq1.2-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日21时41分-ve3.5-eq1.2-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日22时18分-ve3.5-eq1.2-H40-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日22时49分-ve3.5-eq1.2-H60-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日23时21分-ve3.5-eq1.2-H80-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日23时54分-ve3.5-eq1.2-H100-BBS-55-below15mm.xlsx",
# 不同当量比(eq0.6-1.2-H00/H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.6-1.2-H00-BBS-55---✅ done
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日17时49分-ve3.5-eq0.6-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月21日17时51分-ve3.5-eq0.7-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日17时16分-ve3.5-eq0.8-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月21日15时57分-ve3.5-eq0.9-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日18时20分-ve3.5-eq1.0-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月21日15时24分-ve3.5-eq1.1-H00-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日20时42分-ve3.5-eq1.2-H00-BBS-55-below15mm.xlsx",
    # eq---ve3.5-eq0.6-1.2-H20-BBS-55---✅
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月18日16时42分-ve3.5-eq0.6-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月21日17时20分-ve3.5-eq0.7-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日16时42分-ve3.5-eq0.8-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月21日16时49分-ve3.5-eq0.9-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月19日19时32分-ve3.5-eq1.0-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月21日14时50分-ve3.5-eq1.1-H20-BBS-55-below15mm.xlsx",
    #     r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-55-below15mm\2023年12月20日21时41分-ve3.5-eq1.2-H20-BBS-55-below15mm.xlsx",
# ----------------------------------------------------------------------------------------End👆👆👆------

# ------File directory format of experiment operation conditions for BBS-65-below15mm👇👇👇------
# 不同燃料流速(ve1.5-5.0-eq0.6-H00/H20)，3mm热电偶测温（加6.3mm套管后）
    # ve---ve1.5-4.0-eq0.6-H00-BBS-65---✅ ve4.5/5.0 is forsaked -> redo ve1.5-4.5-eq0.6-H00-BBS-65
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日11时49分-ve1.5-eq0.6-H00-BBS-65-redo.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日12时25分-ve2.0-eq0.6-H00-BBS-65-redo.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日13时15分-ve2.5-eq0.6-H00-BBS-65-redo.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日13时49分-ve3.0-eq0.6-H00-BBS-65-redo.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日14时22分-ve3.5-eq0.6-H00-BBS-65-redo.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日14时59分-ve4.0-eq0.6-H00-BBS-65-redo.xlsx",
    # ve---ve1.5-4.0-eq0.6-H20-BBS-65---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日18时37分-ve4.0-eq0.6-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日19时09分-ve3.5-eq0.6-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日19时42分-ve3.0-eq0.6-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日20时18分-ve2.5-eq0.6-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日20时50分-ve2.0-eq0.6-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日21时07分-ve1.5-eq0.6-H20-BBS-65-below15mm.xlsx",
# 不同掺氢比(eq0.6/eq0.8/eq1.0/eq1.2-H00-100): 3mm热电偶测温（加6.3mm套管后）
    # Hy---ve3.5-eq0.6-H00-100-BBS-65--- ✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日13时49分-ve3.0-eq0.6-H00-BBS-65-redo.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日19时09分-ve3.5-eq0.6-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日15时39分-ve3.5-eq0.6-H40-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日16时40分-ve3.5-eq0.6-H60-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日17时15分-ve3.5-eq0.6-H80-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日17时47分-ve3.5-eq0.6-H100-BBS-65-below15mm.xlsx",
    # Hy---ve3.5-eq0.8-H00-100-BBS-65--- ✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日18时21分-ve3.5-eq0.8-H00-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日19时25分-ve3.5-eq0.8-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日19时57分-ve3.5-eq0.8-H40-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日20时32分-ve3.5-eq0.8-H60-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日21时05分-ve3.5-eq0.8-H80-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日21时37分-ve3.5-eq0.8-H100-BBS-65-below15mm.xlsx",
    # Hy---ve3.5-eq1.0-H00-100-BBS-65--- ✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日22时12分-ve3.5-eq1.0-H00-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日16时40分-ve3.5-eq1.0-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日17时16分-ve3.5-eq1.0-H40-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日17时47分-ve3.5-eq1.0-H60-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日18时19分-ve3.5-eq1.0-H80-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日18时51分-ve3.5-eq1.0-H100-BBS-65-below15mm.xlsx",
    # Hy---ve3.5-eq1.2-H00-100-BBS-65--- ✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日19时25分-ve3.5-eq1.2-H00-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日19时57分-ve3.5-eq1.2-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日20时42分-ve3.5-eq1.2-H40-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日21时19分-ve3.5-eq1.2-H60-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日21时50分-ve3.5-eq1.2-H80-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日22时25分-ve3.5-eq1.2-H100-BBS-65-below15mm.xlsx",
# 不同当量比(eq0.6-1.2-H00/H20): 3mm热电偶测温（加6.3mm套管后）
    # eq---ve3.5-eq0.6-1.2-H00-BBS-65---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日14时22分-ve3.5-eq0.6-H00-BBS-65-redo.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月18日13时15分-ve3.5-eq0.7-H00-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日18时21分-ve3.5-eq0.8-H00-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月18日12时39分-ve3.5-eq0.9-H00-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日22时12分-ve3.5-eq1.0-H00-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月18日12时06分-ve3.5-eq1.1-H00-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日19时25分-ve3.5-eq1.2-H00-BBS-65-below15mm.xlsx",
    # eq---ve3.5-eq0.6-1.2-H20-BBS-65---✅
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月15日19时09分-ve3.5-eq0.6-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月18日11时01分-ve3.5-eq0.7-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月16日19时25分-ve3.5-eq0.8-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月18日11时33分-ve3.5-eq0.9-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日16时40分-ve3.5-eq1.0-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日23时14分-ve3.5-eq1.1-H20-BBS-65-below15mm.xlsx",
    # r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\Data-BBS-65-Below15mm\2023年12月17日19时57分-ve3.5-eq1.2-H20-BBS-65-below15mm.xlsx",
# ----------------------------------------------------------------------------------------End👆👆👆------
]



# 为第一张图创建DataFrame
# ---将dataframe中的数据写入到Excel文件中---
# 指定 Excel 文件路径及文件名（无论是否存在）
output_excel_file = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Thesis paper\Data_output_ve1.5-4.0-eq0.6-H20_BBS45.xlsx"
prefix_sheet_name = "vex"
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
num_of_cols = 6  # 假设您想在每个文件中为前4列（除了X轴列）创建图表
# 字母序号列表
letters = ['a', 'b', 'c', 'd', 'e', 'f']  # 根据需要的子图数量调整
colors = ['red', 'green', 'blue', 'orange', 'yellow', 'black']  # 根据需要的子图数量调整
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
        plt.subplot(2, 3, i)  # 创建2x2的子图布局
        plt.plot(df[x_column], df[y_col], linestyle='-', marker='s', label=f"{base_name}: {y_col}")
        plt.xlabel(f"X轴 - {y_col}的X-Y图")  # 将标题作为X轴标签的一部分
        plt.ylabel('数值')
        plt.title(f"({letters[i-1]}){y_col}的X-Y图")
        plt.legend()

# plt.tight_layout()  # 调整子图布局
plt.show()

# 将列表中的DataFrame合并为一个DataFrame, 采用concat合并这些DataFrame
df_list_of_second_chart_df = pd.concat(df_R_n_list_of_second_chart, keys=index_list_second_chart)
# 输出结果前，打印结果
print(df_list_of_second_chart_df)

# 输出两种图表的结果到同个Excel文件中的两张分表中
# ---将dataframe中的数据写入到Excel文件中---
if "y" == input("是否将表中数据（轴向&径向温度）输出为Excel文件？[y/n]"):
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
else:
    print("不输出Excel文件。")