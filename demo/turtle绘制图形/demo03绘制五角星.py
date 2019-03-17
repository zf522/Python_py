"""
画一个五角星
"""

import turtle


def draw_star(x):
    """
    绘制五角星
    """
    count = 0
    while count < 5:
        turtle.forward(x)
        turtle.right(144)
       # turtle.forward(x)
        count += 1

turtle.speed(10)
turtle.penup()
turtle.backward(200)
turtle.pensize(2)
turtle.pencolor('red')
turtle.down()


def main():
    """
    主函数
    """
    # 计数器
    i = 0
    size = 30
    # 连续画五个五角星
    while i < 5:
        size += 30
        draw_star(size)
        i += 1
    turtle.exitonclick()


if __name__ == "__main__":
    main()
