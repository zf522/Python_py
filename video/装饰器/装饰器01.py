# 装饰器
def fun_out(new_fun):
    def fun_in(num1, num2):
        print("计算结果如下：")
        new_fun(num1, num2)

    return fun_in


@fun_out  # sum_num = fun_out(sum_num)
def sum_num(num1, num2):
    sum = num1 + num2
    print(sum)


sum_num(1, 2)
