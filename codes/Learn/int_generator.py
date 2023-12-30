import random
import openpyxl

def generate_random_numbers():
    # 创建一个新的Excel工作簿
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # 循环39次生成随机整数并写入Excel表格
    for _ in range(39):
        # 生成85到95之间的随机整数
        random_number = random.randint(85, 95)

        # 将随机整数写入Excel表格的下一行
        sheet.append([random_number])

    # 保存Excel文件
    workbook.save(r"E:\OneDrive\00_To_Do\random_numbers-2.xlsx")

if __name__ == "__main__":
    generate_random_numbers()
