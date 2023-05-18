print('''
------入口雷诺数判断计算说明------
计算前，已知信息如下：
- 流体密度(kg/m3)：density_of_fluid
- 流体黏度(Pa·s)：viscosity_of_fluid 
- 流体流速(m/s)：velocity_of_fluid_flow
- 特征长度(m)：reference_length  # 一般取为当量直径
求：
- 雷诺数(1): reynolds_number
''')

# ------物性参数------
density_of_h2 = 0.09 # kg/m3
density_of_air = 1.23 # kg/m3
# ------END------

# ------运行前请检查各个参数是否有误------
density_of_fluid = density_of_air

# vicosity : H2: 8.915e-6 Pa·s; air: 18.448e-6 Pa·s
# 注意 1 μpa = 1 x 10e-6 pa (采用国际制单位Pa代入计算)
viscosity_of_fluid = 18.448e-6

velocity_of_fluid_flow = 3 # 先计算燃烧入口
reference_length = 4*2.22E-3 #参考该入口当量直径,注意当量直径为水利直径的4倍.对此micro-combustor而言，水利直径：fuel inlet: 4.615E-4; air:inlet：2.22E-3
# ------END------

# ------公式------

reynolds_number = (density_of_fluid * velocity_of_fluid_flow * reference_length) / viscosity_of_fluid

print(f"当入口流速为{velocity_of_fluid_flow}时，Reynolds number = {reynolds_number} ")