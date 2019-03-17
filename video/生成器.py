# 1.使用生成器的表达式
# result = (x for x in range(7))    #若是中括号，生成的是列表
# print(result,type(result))
# 测试：使用next获取下一个值
# value = next(result)
# print(value)

# for i in result:
#     print(i)

# 2.使用yield创建生成器
def show():
    for i in range(4):
        yield i  # 代码遇到yield会暂停，然后把结果返回出去，下次启动生成器在暂停的位置继续往下执行
        # yield特点：可以返回多次值，return只能返回一次值


# print(next(show()))             #生成器只能用next()获取下一个值
g = show()
for i in g:
    print(i)
