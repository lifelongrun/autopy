'''
-----本例子针对给定的window一个文件路径，将其中的单倒斜杠替换为倒双斜杠-----
- 涉及字符串替换
'''

object_directory = 'E:\John Mike\OneDrive\Pictures\Screenshots'
#
# 使用str.replace(old,new), 返回一个被替换掉子字符串的新字符串
# Refer to: https://docs.python.org/3/library/stdtypes.html#str.replace
print('替换后的字符串：' + object_directory.replace('\\','\\\\'))
print('原字符串：' + object_directory)