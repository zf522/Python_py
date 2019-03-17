"""
新增功能：模拟投掷两个骰子并可视化

"""
import random
import matplotlib.pyplot as plt


def roll_dice():
    """
    模拟掷骰子
    :return:
    """
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 100
    # 初始化列表，用以存放每两个点数之和出现的次数，2~12，一共11个元素
    result_list = [0] * 11
    # 初始化点数列表
    roll_list = list(range(2, 13))  # 列表存放两个骰子点数和
    roll_dict = dict(zip(roll_list, result_list))  # zip()函数将两个列表包装成一个元组，因为元组值不可改变，再用dict转换成字典
    # 记录骰子每个点数的次数
    roll1_list = []
    roll2_list = []

    for i in range(total_times):
        roll1 = roll_dice()  # 骰子1的点数
        roll2 = roll_dice()  # 骰子2的点数

        roll1_list.append(roll1)
        roll2_list.append(roll2)

        for j in range(2, 13):  # 在2-12这些数字中循环，当在j这个数字上满足if语句，j就加1，j表示列表中每个值的下标（从1开始）
            if (roll1 + roll2) == j:
                roll_dict[j] += 1

    for i, result in roll_dict.items():
        print("点数{}的次数是：{}，频率是：{}".format(i, result, result / total_times))

    # 进行可视化(散点图)
    x = range(1, total_times +1)
    plt.scatter(x, roll1_list, c="red", alpha=0.5)
    plt.scatter(x, roll2_list, c="blue", alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()
