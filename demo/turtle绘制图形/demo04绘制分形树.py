"""
利用递归绘制一个分形树
"""

import turtle


def draw_branch(angle, branch_length):
    if branch_length > 5:

        # 绘制右侧树枝
        turtle.forward(branch_length)
        turtle.right(angle)
        draw_branch(angle, branch_length-10)

        # 绘制左侧树枝
        turtle.left(angle*2)
        draw_branch(angle, branch_length - 10)

        #返回之前树枝
        turtle.right(angle)
        turtle.backward(branch_length)


def main():
    """
    主函数
    """
    turtle.color("red")
    turtle.speed(10)
    turtle.left(90)
    draw_branch(20, 60)
    turtle.exitonclick()


if __name__ == "__main__":
    main()
