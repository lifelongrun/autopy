# 计算雷诺数，判断是否为层流还是湍流

# 根据雷诺数公式定义，涉及的参数为流体流速，黏度，密度，当量直径（4倍的水利直径）
# μ=ν*ρ，式中 μ-动力粘度，Pa.s；ρ-密度，kg/m3；ν-运动粘
# 甲烷（CH4）

# unit kg/m3
density = 0.5008

# unit m/s
velocity = 20

# unit m
equivalent_diameter = 4 * 0.001714

# unit m2/s
viscosity = 2.89546/10**(5)

# calculation and output
re = density * velocity * equivalent_diameter / viscosity

print(f'（流体为甲烷）雷诺数大小为：{re}')

# 以上计算结果：（流体为甲烷）雷诺数大小为：2371.6333846780826