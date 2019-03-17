def show_msg(*args):
    print(args)
    for value in args:
        print(value)


# 定义不定长位置参数
def show(*args):
    print(args, type(args))

    # 对元组进行拆包
    show_msg(*args)


show(2, 3)
