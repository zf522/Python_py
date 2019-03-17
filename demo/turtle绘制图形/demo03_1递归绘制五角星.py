"""
递归画一个五角星
"""

import turtle
turtle.speed(10)
turtle.penup()
turtle.backward(200)
turtle.pensize(2)
turtle.pencolor('red')
turtle.down()


def  digui_star(size):
    """
    使用递归函数
    """
    count = 0
    while count < 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1
    size += 10
    if size <= 100:
        digui_star(size)


def main():
    """
    主函数
    """
    # 计数器
    size = 50
    digui_star(size)
    turtle.exitonclick()


if __name__ == "__main__":
    main()
