"""
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
"""
"""
map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
"""

# def normalize(name):
#     name = name[0].upper() + name[1:].lower()
#     return name
#
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


# 输入名字，变成首字母大写，其他字母小写的标准格式
def normalize(name):
    str1 = ''
    for i, ch in enumerate(name):
        if i == 0:
            str1 = str1 + ch.upper()  # str.upper() 方法让字母转大写
        else:
            str1 = str1 + ch.lower()  # str.lower() 方法让字母转小写
    return str1


# 输入：
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
