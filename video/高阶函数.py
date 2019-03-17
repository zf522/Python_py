# 高阶函数：当一个函数的参数可以接受另外一个函数，或者可以返回一个函数，那么这个函数就称为高阶函数
# 高阶函数接收的是函数或者返回的是函数，那么类似于这样的函数统称为高阶函数


def sum_num(num1, num2):
    return num1 + num2


# 接收一个函数作为参数
def fun_cal(num1, num2, new_fun):
    value = new_fun(num1, num2)
    return value


# fun_cal就称为高阶函数
result = fun_cal(4, 7, sum_num)
print(result)
