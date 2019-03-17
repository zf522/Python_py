import random


def roll_dice():
    """
    模拟掷骰子
    :return:
    """
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 100000
    # 初始化列表，用以存放每个点数出现的次数
    l = [0] * 6

    for i in range(total_times):
        roll = roll_dice()
        # 采用循环：当骰子的点数roll为1时，在l[0]上加1
        for j in range(1, 7):  # 列表l只有6个值，循环6次，判断1到6六个数字
            if roll == j:  # 当骰子点数为1的时候，在l[0]上加个1，当骰子点数为3的时候，在l[2]上加个1，
                l[j - 1] += 1
    # enumerate一般用于for循环中，同时列出元素索引号和元素值
    for i, result in enumerate(l):  # i为索引号，i+1即点数，result即为元素值
        print("点数{}的次数是：{}，频率是：{}".format(i + 1, result, result / total_times))


if __name__ == '__main__':
    main()
