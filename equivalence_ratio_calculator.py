# 预设的基本常量

# unit m 几何尺寸 （(默认的几何结构参数)
inlet_diameter_of_fuel = 0.00425    #0.005 * 2   # 王珂的二维模型0.00425      #
bluff_thickness = 0.001             #0.004       # 王珂的二维模0.001          #
inlet_diameter_of_air_out = 0.082   #0.225 * 2   # 王珂的二维模0.082          #
inlet_diameter_of_air_in = 2 * bluff_thickness + inlet_diameter_of_fuel

# unit kg/m3 密度 (通用)
density_ch4 = 0.65
density_air = 1.23
density_h2 = 0.09

# 同轴射流燃烧器结构示意图
print('''
              =======================================
   air-inlet->|___->                                |
               ___|                                 |
  fuel-inlet->|___->       2-D Combustor            |
               ___|                                 |
   air-inlet->|   ->                                |
              =======================================
''')

print(f'''
如上图所示,本次计算的几何模型为同轴燃烧器,其中心轴为燃料入口,外环为空气入口,其间隔着一个( (⚪) )圆环形且厚度为thickness的bluff body。
      默认结构参数如下:
      inlet diameter of fuel = {inlet_diameter_of_fuel}
      inlet thickness of bluff body = {bluff_thickness}
      inlet outer diameter of air = {inlet_diameter_of_air_out}
      inlet inner diameter of air = {inlet_diameter_of_air_in}
      ''')

print("-----燃烧器的几何参数确定-----")
geometry_parameter_confirm = input("[in]请确认是否需要修改以上参数?[y/n]:")

if 'y' == geometry_parameter_confirm:
    print("[tip]若要调整此次计算的结构参数，请分别指定以下参数值(Unit:m):")
    inlet_diameter_of_fuel = float(input("[in]inlet diameter of fuel :"))
    bluff_thickness = float(input("[in]inlet thickness of bluff body :"))
    inlet_diameter_of_air_out = float(input("[in]inlet outer diameter of air :"))
else:
    print("[tip]以下将根据默认结构参数进行计算")


# unit m2 流通截面积 (根据几何模型参数计算)
cross_area_air = 3.14 * (inlet_diameter_of_air_out ** 2 - inlet_diameter_of_air_in ** 2) / 4
cross_area_fuel = 3.14 * inlet_diameter_of_fuel ** 2 / 4

    
print("-----情景选择-----")
situation = int(input("[in]情景一:计算单一燃料CH4的当量比，请输入数字1；\n    情景二:变当量比,变掺氢比,求空气流量，请输入数字2.\n    [1/2]:"))

# 对于单一燃料甲烷而言，计算其当量比大小（针对的边界条件为同轴燃烧器）
if situation == 1:
    print("[tip]此次选择的是情景1:")

    velocity_air = float(input("[in]请输入空气入口流速(m/s):"))
    velocity_fuel = float(input("[in]请输入燃料入口流速(m/s):"))

    # 当量比定义=理论空燃比/实际空燃比(kg/kg)
    air_to_fuel_stoic = 17.16
    air_to_fuel_actual = (density_air*velocity_air*cross_area_air)/(density_ch4*velocity_fuel*cross_area_fuel)
    equivalence_ratio = air_to_fuel_stoic/air_to_fuel_actual
    equivalence_ratio_percent = equivalence_ratio*100

    excess_air = (1-equivalence_ratio)/equivalence_ratio

    print(
        f"[output]计算结果:  当量比{str(chr(934))}: {equivalence_ratio:.4f}; "
        f"以百分比表示: {equivalence_ratio_percent:.2f}%; "
        f"过量空气系数{str(chr(955))}:{excess_air:.2f}")
# todo write to a .txt file

# 对于CH4-H2混合燃料而言，求特定当量比和掺氢比下的空气流速，包括定当量比，变掺氢比与定掺氢比，变当量比两种选择(d、c)（针对的边界条件为同轴燃烧器）
elif situation == 2:
    print("[tip]此次选择的是情景2:")
    # 锁定当量比还是掺氢比条件判断
    choices = input("[in]定当量比计算请输入小写字母'd';定掺氢比计算请输入小写字母'c'。[c/d]")
    computation_numbers = int(input("[in]请输入接下来要计算多少组数据(多少个不同工况下对应的空气流速):"))
    velocity_fuel = float(input("[in]请输入燃料入口流速(m/s):"))

    # 选择d：定当量比，变掺氢比，求对应的空气流速
    if 'd' == choices:
        print("-----定当量比,变掺氢比,求空气流速-----")
        equivalence_ratio = float(input("[in]请输入定当量比的值:"))
        for i in range(1,computation_numbers+1):
            xh_2 = float(input("[in]请输入此次变掺氢比的值:"))
            
            # air to fuel stoic of ch4 & h2 mixture fuel
            air_to_fuel_stoic = 137.25 * (2 - 1.5 * xh_2) / (16 - 14 * xh_2)
            
            # velocity of air supply
            velocity_air = (air_to_fuel_stoic / equivalence_ratio) * ((1 - xh_2) * density_ch4 * velocity_fuel + xh_2 * density_h2 * velocity_fuel) * cross_area_fuel / ( density_air * cross_area_air)
            print(f"[output]第{i}组,已知:定当量比={equivalence_ratio}，变掺氢比={xh_2};此时计算的空气流速大小为:{velocity_air:4f}m/s")
        print(f"[over]定当量比={equivalence_ratio}，空气流速计算结束")

    # 选择c：定掺氢比，变当量比，求对应的空气流速
    elif 'c' == choices:
        print("-----定掺氢比,变当量比,求空气流速-----")
        xh_2 = float(input("[in]请输入此次定掺氢比的值:"))
        for i in range(1, computation_numbers+1):
            equivalence_ratio = float(input("[in]请输入变当量比的值:"))
            
            # air to fuel stoic of ch4 & h2 mixture fuel
            air_to_fuel_stoic = 137.25 * (2 - 1.5 * xh_2) / (16 - 14 * xh_2)
            
            # velocity of air supply
            velocity_air = (air_to_fuel_stoic / equivalence_ratio) * ((1 - xh_2) * density_ch4 * velocity_fuel + xh_2 * density_h2 * velocity_fuel) * cross_area_fuel / (density_air * cross_area_air)
            print(f"[output]第{i}组,已知:定掺氢比={xh_2}，变当量比={equivalence_ratio};此时计算的空气流速大小为:{velocity_air:4f}m/s")
        print(f"[over]定掺氢比={xh_2}，空气流速计算结束")
    else:
        print("[tip]锁定条件选择错误，请重新开始。")
else:
    print("[tip]情景选择错误，请重新开始。")

# 保持窗口处于待命状态，退出/结束程序需键入回车指令：Enter
input("Press Enter to exit ;)")
