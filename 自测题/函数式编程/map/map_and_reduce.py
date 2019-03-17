"""
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
"""
from functools import reduce


# def str2float(s):
#     def fn(x, y):
#
#         return x * 10 +y
#
#     def char2num(s):
#         digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#         return digits[s]
#
#     reduce(fn, map(char2num, s))

def str2float(s):
    def fn(x, y):
        return x * 10 + y
    
    n = s.index(".")
    # 对字符串进行切片
    s1 = list(map(int, [x for x in s[:n]]))
    s2 = list(map(int, [x for x in s[n + 1:]]))
    return reduce(fn, s1) + reduce(fn, s2) / 10 ** len(s2)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
