import originpro as op

# 启动 Origin 会话
app = op.Application()

# 导入 Excel 文件
excel_file_path = r"E:\OneDrive\00_To_Do\1.Graduate Paper\Data\2023年11月25日20时23分-ve3.5-eq0.6-H100-BB.xlsx"
worksheet = app.open_excel(excel_file_path, 'A_n_T_ave')  # 假设你的数据在 "Sheet1" 上

# 创建图表
graph = app.create_graph('Scatter')  # 创建一个散点图
graph_layer = graph.Layers(0)
graph_layer.add_plot('scatter', worksheet.Columns(0), worksheet.Columns(1))  # 假设你想用第一列和第二列的数据

# 自定义图表
graph_layer.x_axis.title = 'X轴标题'
graph_layer.y_axis.title = 'Y轴标题'

graph.export('E:\OneDrive\00_To_Do\1.Graduate Paper\Data\ve3.5-eq0.6-H100-BB-A_n_T_ave.eps')
