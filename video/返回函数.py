# 嵌套函数，函数中返回一个函数
def fun(operator):
    if operator == "+":
        def sum_s(a,b):
            return a+b
        return sum_s
    if operator == "-":
        def jf_s(a,b):
            return a-b
        return jf_s


# 获取返回的函数
new_op = fun("+")
# 执行返回的函数
result = new_op(1, 2)
print(result)
