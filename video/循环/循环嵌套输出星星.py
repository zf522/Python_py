row = 1
while row <= 5:
    """
    向控制台输出内容结束之后，不会换行
    print("*", end="")
    """
    """
    每一行要打印的星星都和行数相等
    再写一个小循环，负责当前行中，每一列的星星数量
    """
    #定义一个计数器
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    #这行代码的目的就是在输出星星之后添加换行
    print("")
    row += 1