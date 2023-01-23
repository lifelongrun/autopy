
print('''
根据水利直径定义，计算该值，用于fluent setup
''')

choice = input("所计算截面是矩形、圆形，还是圆环？")
if '矩形' == choice:
    length = float(input('矩形的长为(mm): '))/1000
    width = float(input('矩形的宽为(mm): '))/1000
    wetted_perimeter = 2 * (length + width)
    flow_section = length * width

    d_h = 4 * flow_section / wetted_perimeter
    print(f'Hydraulic diameter of this time is (m):{d_h:8f}')
else:
    print("Sorry! 目前只考虑了矩形的水利直径。")

# ---------------------------对于圆管入口，水利直径等于入口横截面直径
# --------------------以下为针对矩形入口，预先设定参数计算水利直径--------------------


# # 针对Fuel inlet （单位, mm）
# length = 1
# width = 0.30
# d_h = 2 * length * width / (length + width) # 水利直径计算公式（2倍流通截面积与润湿周边的比值）
# print(f'Hydraulic diameter of fuel inlet is :{d_h:.8f} (mm), {d_h/1000:.8f} (m)')
#----------------------------------------------------------------------------------
# # 针对Air inlet（单位, mm）
# length = 1
# width = 1.75
# d_h = 2 * 2 * length * width / (length + width) # 空气共有两个入口，因此此处考虑为单个水利直径的2倍
# print(f'Hydraulic diameter of air inlet is :{d_h:.8f} (mm), {d_h/1000:.8f} (m)')
#----------------------------------------------------------------------------------
# # 针对outlet（单位, mm）
# length = 1
# width = 4
# d_h = 2 * length * width / (length + width) # 水利直径计算公式（2倍流通截面积与润湿周边的比值）
# print(f'Hydraulic diameter of outlet is :{d_h:.8f} (mm), {d_h/1000:.8f} (m)')
#----------------------------------------------------------------------------------
# 以上行运行结果：
# Hydraulic diameter of fuel inlet is :0.46153846 (mm), 0.00046154 (m)
# Hydraulic diameter of air inlet is :2.54545455 (mm), 0.00254545 (m)
# Hydraulic diameter of outlet is :1.60000000 (mm), 0.00160000 (m)

# ----------------------------------------完----------------------------------------