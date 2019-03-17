# 闭包：在函数嵌套的情况下，内部函数使用了外部函数的参数或者变量，并把这个内部函数返回，那么返回的函数可以称为闭包
def fun_out():
    num = 1

    def fun_in():       #闭包
        print(num)

    return fun_in       # 返回一个内部函数（闭包）


# 接收函数
show = fun_out()
print(show)
# 调用函数
show()
