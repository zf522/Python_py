result = 0

#计数器
i = 0

#循环
while i<=100:
    #i = 2*i
    if i % 2 == 0:  #判断i的结果是否是偶数
        result += i
    i += 1

print("0~100的最终求和为：%d" % result)
