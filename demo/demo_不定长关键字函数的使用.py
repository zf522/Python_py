def show(**kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key,value)


# 定义不定长关键字函数
def show_msg(**kwargs):
    # 把关键字函数封装到字典里

    # print(kwargs, type(kwargs))
    # 对字典进行拆包

    show(**kwargs)


# show(**kwargs)

show_msg(name="zhangsan", age=10)
