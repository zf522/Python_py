"""
乘号前面的数字是列号，后面的数字是行号
"""
row = 1     #行数
while row <= 9:
    col = 1     #列数
    while col <= row:
        print("%d * %d = %d" % (col, row, col*row), end="\t")       #\t制表符，协助在输出文本时 垂直方向保持对齐
        col += 1
    print("")
    row += 1