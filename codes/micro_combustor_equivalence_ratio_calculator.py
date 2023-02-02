
print('''
针对长方体式的微型燃烧器
              =======================================
   air-inlet->|___->                                |
               ___|                                 |
  fuel-inlet->|___->    2-D Micro Combustor         |
               ___|                                 |
   air-inlet->|   ->                                |
              =======================================
''')

# unit m2 流通截面积 (根据几何模型参数计算【单位：mm】, 注意结果单位需由mm2转换为m2)

cross_area_air = 2 * 1 * 1.75 / 10**(-6) # 2 为左右两个空气入口， 1 为高度，1.75为宽度
cross_area_fuel = 1 * 0.3 / 10**(-6) # 0.3 为中心燃料入口宽度

# unit kg/m3 密度 (通用)
density_ch4 = 0.65
density_air = 1.23
density_h2 = 0.09

# 对于CH4-H2混合燃料而言，求特定当量比和掺氢比下的空气流速，包括定当量比，变掺氢比与定掺氢比，变当量比两种选择

print("-----定当量比,变掺氢比,求空气流速-----")
print("-----定当量比,变掺氢比,求空气流速-----")
computation_numbers = int(input("[in]请输入接下来要计算多少组数据(多少个不同工况下对应的空气流速):"))
velocity_fuel = float(input("[in]请输入燃料入口流速(m/s):"))

# 选择d：定当量比，变掺氢比，求对应的空气流速

equivalence_ratio = float(input("[in]请输入定当量比的值:"))
for i in range(1, computation_numbers + 1):
    xh_2 = float(input("[in]请输入此次变掺氢比的值(以小数表示):"))

    # air to fuel stoic of ch4 & h2 mixture fuel
    # 下面一行的详细说明见OneNote笔记"掺氢燃烧二维模型尺寸-文章"
    # 主要解决的是由掺氢带来的理论当量比的变化; 对于纯甲烷燃料燃烧; 这是一个定值, 而对于甲烷掺氢混合燃料而言, 该值将随着掺氢比的变化而变化, 即与掺氢比有关, 关系式如下:
    air_to_fuel_stoic = 137.25 * (2 - 1.5 * xh_2) / (16 - 14 * xh_2)

    # velocity of air supply
    velocity_air = (air_to_fuel_stoic / equivalence_ratio) * (
                (1 - xh_2) * density_ch4 * velocity_fuel + xh_2 * density_h2 * velocity_fuel) * cross_area_fuel / (
                               density_air * cross_area_air)
    print(
        f"[output]第{i}组,已知:定当量比={equivalence_ratio}, 变掺氢比={xh_2}; 此时计算的空气流速大小为:{velocity_air:4f}m/s")

print(f"[over]定当量比={equivalence_ratio}，空气流速计算结束")

# 保持窗口处于待命状态，退出/结束程序需键入回车指令：键入Enter

input("Press Enter to exit ;)")