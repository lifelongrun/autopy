import seaborn as sns

# 列出所有内置色卡的名称
palette_names = sns.palettes.SEABORN_PALETTES.keys()
print(palette_names)

for name in palette_names:
    sns.palplot(sns.color_palette(name))
    plt.show()
