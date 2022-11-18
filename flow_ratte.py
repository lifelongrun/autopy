print('--------根据燃气灶的功率计算燃气灶入口的体积流量大小--------')
# 定义函数用于体积流量单位转换：m3/h -> L/min
def volume_converted(m3_per_h):
    # define a function to convert the flow rate in volume per h into liter per min
    L_per_min = 60/10**3*m3_per_h
    return L_per_min

'''       
计算公式
低热值华白数（net Wobbe nubmer）                            = 燃气的低热值与其相对密度平方根之比。（注：空气的相对密度为1）
额定热负荷（额定热流量）（nominal heat input）                = 厂家标识在额定燃气供气压力下，使用基准状态下的基准气时灶具热负荷的设计值。
实测热负荷（实测热流量）（actual heat input）                 = 试验状态下，试验气的低热值与实测燃气流量的乘积。
实测折算热负荷（实测折算热流量）（converted actual heat input）= 设计燃气低热值与实测燃气流量折算到设计燃气基准状态流量的乘积。
'''

# 低位热值（低位体积热值）Hi，单位：MJ/m3
LHV_ch4 = 34.0160
LHV_h2 = 10.2169

# 假定燃气灶的额定热流量大小为4.0，单位：kW
nominal_heat_input = 4.0

# 根据低热值华白数与额定热流量计算燃气流量(m3/h)，ng即: natural gas
volume_flow_rate_ng = nominal_heat_input*3.6/LHV_ch4

# 打开一个txt文本开始写入内容
f = open('flow_rate.txt','w+')
#f2 = open('address.csv','w')

f.write('--------根据燃气灶的功率计算燃气灶入口的体积流量大小--------\n')

#f.write(f'燃料体积流量为: {volume_flow_rate_ng:.4f} m3/h {volume_converted(volume_flow_rate_ng):4f} L/min \n')
print(f'燃料体积流量为: {volume_flow_rate_ng:.4f} m3/h {volume_converted(volume_flow_rate_ng):4f} L/min \n')
#f2.write(f'燃料体积流量为: {volume_flow_rate_ng:.4f} m3/h {volume_converted(volume_flow_rate_ng):4f} L/min \n')

flow_rate_ng = volume_converted(volume_flow_rate_ng) # 天然气流量
flow_rate_h2 = 0 # 氢气流量
h2_ratio_in_vol= 0.00  # 氢气的初始体积分数

# print the header for reference
print("掺氢比 | 天然气流量 (L/min) | 氢气流量 (L/min)")

# make a template aligns and displays the datas in the proper format
# 'Formatted string literals': which contain replacement fields, which are expressions delimited by curly braces{}

write_template = '{h2_ratio:>7} | {ng_flow_rate:>7} | {h2_flow_rate}'

# 采用一个循环写入各个掺氢比下的 [天然气流量] 以及[空气流量]
while h2_ratio_in_vol <= 0.30 :
     # 依次写入 掺氢比 天然气流量 氢气流量
    #f.write(f'{h2_ratio_in_vol:.2f} | 天然气流量:  {flow_rate_ng*(1-h2_ratio_in_vol):.4f}  L/min; 氢气流量:  {flow_rate_ng*h2_ratio_in_vol:.4f}  L/min;\n')
    row = write_template.format(h2_ratio=h2_ratio_in_vol,ng_flow_rate=flow_rate_ng*(1-h2_ratio_in_vol),h2_flow_rate=flow_rate_ng*h2_ratio_in_vol)
    f.write(f'{h2_ratio_in_vol:.2f} | 天然气流量:  {flow_rate_ng*(1-h2_ratio_in_vol):.4f}  L/min; 氢气流量:  {flow_rate_ng*h2_ratio_in_vol:.4f}  L/min;\n')

    print(f'掺氢比为: {h2_ratio_in_vol:.2f} ; 天然气流量为: {flow_rate_ng*(1-h2_ratio_in_vol):.4f} L/min; 氢气流量为: {flow_rate_ng*h2_ratio_in_vol:.4f} L/min\n')
    #f2.write(f'掺氢比为：{h2_ratio_in_vol:.2f} ; 天然气流量为：{flow_rate_ng*(1-h2_ratio_in_vol):.4f} L/min; 氢气流量为: {flow_rate_ng*h2_ratio_in_vol:.4f}\n')
    h2_ratio_in_vol +=0.05

# 关闭所打开文件
f.close()
