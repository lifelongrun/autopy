print('''
------非预混条件下，任一当量比条件下，空气入口流速计算说明------
计算非预混条件下，单一氢气作为燃料，已知信息：
- 燃料入口流速(m/s)：velocity_of_fuel_inlet
- 燃料入口横截面积(m2)：area_of_cross_section_of_fuel_inlet
- 空气入口横截面积(m2)：area_of_cross_section_of_air_inlet
- 当量比(kg/kg)：equivalence_ratio
求：
- 空气入口流速(m/s): velocity_of_air_inlet
''')

# ------物性参数------
density_of_h2 = 0.09 # kg/m3
density_of_air = 1.23 # kg/m3
# ------END------

# ------运行前请检查各个参数是否有误------
velocity_of_fuel_inlet = 6
area_of_cross_section_of_fuel_inlet = 0.3*1e-6
area_of_cross_section_of_air_inlet = 2.5e-6
equivalence_ratio = 0.6
velocity_of_air_inlet = 0.0
# ------END------

# ------公式------
velocity_of_air_inlet = (density_of_h2/(0.029138*equivalence_ratio)*area_of_cross_section_of_fuel_inlet*velocity_of_fuel_inlet)/(density_of_air*area_of_cross_section_of_air_inlet)

print(velocity_of_air_inlet)

