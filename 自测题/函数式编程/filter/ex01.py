"""
filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
filter()函数返回的是一个Iterator，也就是一个惰性序列，
所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
"""


# def fn(n):
#     return n % 2 ==0
# print(list(filter(fn,[1,2,3,4,5,6,7,])))


# 把一个序列中的空字符串删掉:
# def del_str(str):
#     return str and str.strip()
#
#
# print(list(filter(del_str, ['AS', 'xs', ' ', ''])))


def h():
    print('study yield')
    yield 5
    print('go on!')


c = h()
d1 = next(c)

#由于下一句没有yield，所以不会执行并抛出异常
d2 = next(c)
