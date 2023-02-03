
print('''
根据水利直径定义(4倍流体流通截面与润湿周边的比率)，计算该值，用于fluent setup
''')

choice = input("所计算截面是矩形、圆形，还是圆环？")
if '矩形' == choice:
    length = float(input('矩形的长为(mm): '))/1000 # 将输入的数值单位为毫米（mm）转换为米(m)
    width = float(input('矩形的宽为(mm): '))/1000
    wetted_perimeter = 2 * (length + width)
    flow_section = length * width

    d_h = 4 * flow_section / wetted_perimeter
    print(f'Hydraulic diameter of the rectangle is (m):{d_h:8f}')
elif '圆形' == choice:
    radius = float(input('圆形的半径为(mm):'))/1000
    flow_section = 3.14 * radius**2 # 流通截面积
    wetted_perimeter = 2 * 3.14 * radius
    d_h = 4 * flow_section / wetted_perimeter
    print(f'Hydraulic diameter of the circle is (m):{d_h:8f}')
elif '圆环' == choice:
    inner_radius = float(input('圆环的内直径为(mm):'))/1000
    outer_radius = float(input('圆环的外直径为(mm):'))/1000
    flow_section = 3.14 * (outer_radius**2 - inner_radius**2)
    wetted_perimeter = 2 * 3.14 * (outer_radius + inner_radius)
    d_h = 4 * flow_section / wetted_perimeter
    print(f'Hydraulic diameter of the annulus is (m):{d_h:8f}')
else:
    print('Please choose the value from the 4 choices!')
# ---------------------------对于圆管入口，水利直径等于入口横截面直径