
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

# 以下为针对矩形入口，预先设定参数计算水利直径
# # Fuel inlet
# length = 1.5
# width = 2
# d_h = 2 * length * width / (length + width)
# print(f'Hydraulic diameter of fuel inlet is :{d_h:.8f} (mm), {d_h/1000:.8f} (m)')
#
# # Air inlet
# length = 2
# width = 3
# d_h = 2 * length * width / (length + width)
# print(f'Hydraulic diameter of air inlet is :{d_h:.8f} (mm), {d_h/1000:.8f} (m)')