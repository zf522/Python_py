"""
0~100求和
"""
# 首先定义一个结果参数
result = 0

#计数器
i = 0

#循环
while i<=100:
    result += i
    i += 1

print("0~100的最终求和为：%d" % result)
