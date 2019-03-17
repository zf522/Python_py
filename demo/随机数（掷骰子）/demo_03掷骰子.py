"""
新增功能：模拟投掷两个骰子并可视化

"""
import random
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体为中文黑体
plt.rcParams["axes.unicode_minus"] = False  # 设置符号问题


def roll_dice():
    """
    模拟掷骰子
    :return:
    """
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 10000
    # 记录骰子每个点数的次数
    roll_list = []

    for i in range(total_times):
        roll1 = roll_dice()  # 骰子1的点数
        roll2 = roll_dice()  # 骰子2的点数

        roll_list.append(roll1 + roll2)

    # 进行可视化(直方图)
    # roll_list为y轴的数据,bins为x轴的边界，density固定y轴数据为小数点后一位（即概率和为1）
    plt.hist(roll_list, bins=range(2, 14), density=1,edgecolor="black", linewidth=1)
    plt.title("骰子点数统计")
    plt.xlabel("点数和")
    plt.ylabel("概率")
    plt.show()


if __name__ == '__main__':
    main()
