"""
请编写一个prod()函数，可以接受一个list并利用reduce()求积：
"""
"""
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
"""

from functools import reduce


def prod(L):
    def acc(a, b):
        return a * b
    return reduce(acc, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
