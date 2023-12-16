import matplotlib.pyplot as plt

# 创建一个示例图形
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

# 保存为PDF矢量图
plt.savefig('plot.pdf', format='pdf')

