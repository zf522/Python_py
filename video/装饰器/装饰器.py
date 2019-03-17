# 装饰器：本质上就是一个函数，可以给原函数的功能进行扩展，这样的好处是，不改变原函数的定义及调用的操作


# 原函数
# def show():
#     print("zzz")
#
#
# # 装饰器：通过闭包完成装饰器
# def fun_out(new_fun):
#     def fun_in():
#         print("*" * 60)
#         new_fun()
#
#     # 返回的函数是闭包
#     return fun_in
#
#
# show = fun_out(show)
# show()


# 装饰器
def fun_out(new_fun):

    def fun_in():
        print("*" * 60)
        new_fun()
    # 返回的函数是闭包
    return fun_in


# 调用装饰器
@fun_out    # show = fun_out(show)
def show():
    print("zzz")


show()
