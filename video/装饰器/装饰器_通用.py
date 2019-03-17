# 装饰器
def fun_out(new_fun):
    def fun_in(*args, **kwargs):
        print("计算结果如下：")
        # 这里对不定长参数进行拆包
        return new_fun(*args, **kwargs)

    return fun_in


# 1调用装饰器
@fun_out  # sum_num = fun_out(sum_num)
def sum_num(num1, num2):
    sum = num1 + num2
    print(sum)


sum_num(1, 2)


# 2
@fun_out
def sum_one(num1, num2):
    sum = num1 + num2
    return sum


print(sum_one(1, 3))


# 3
@fun_out
def show():
    print("我是一个无参数无返回值的函数！")


show()
result = sum_one(1, 9)
print(result)
