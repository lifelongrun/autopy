import originpro as op
import pandas as pd
import os

excel_files = [r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月25日19时35分-ve5-eq0.6-H00-BB.xlsx",
               r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月27日15时45分-ve5-eq0.6-H00-BB.xlsx"]
sheet_names = [
               'A_n_T_ave']
template_path = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\template_SCATTER.otpu"  # 替换为您的模板路径

# 确保 Origin 项目已经创建
op.new()

for excel_file_path in excel_files:
    for sheet_name in sheet_names:
        # 读取 Excel 文件中的特定工作表
        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

        # 创建工作表名称
        base_name = os.path.splitext(os.path.basename(excel_file_path))[0]
        wks_name = f"{base_name}_{sheet_name}"

        # 在 Origin 中创建一个新的工作表
        wks = op.new_sheet('w', wks_name)

        # 将 DataFrame 数据写入 Origin 工作表
        wks.from_df(df)

        # 使用模板创建一个新的图表
        graph = op.new_graph(template=template_path)

        # 为这个工作表数据在图表中创建一个新的图层
        new_layer = graph.add_layer()  # 创建新图层

        # 获取数据列的数量
        num_cols = len(df.columns)

        # 为每个 Y 轴数据创建一个 plot
        for i in range(1, num_cols):  # 从第二列开始，因为第一列是 X 轴数据
            # layer = graph[0]
            # layer.add_plot(wks, coly=i, colx=0, type=202)  # 202 是线加符号类型的图
            # layer.rescale()

            # 在新图层中添加 plot
            new_layer.add_plot(wks, coly=1, colx=0, type=202)  # 202 是线加符号类型的图
            new_layer.rescale()

# 保存 Origin 项目
op.save(r'E:\OneDrive\00_To_Do\1.Graduate Paper\Data\xxxxxx-3.opju')  # 替换为您的保存路径

# ---- YOUR CODE HERE above


# Exit running instance of Origin.
if op.oext:
    op.exit()
