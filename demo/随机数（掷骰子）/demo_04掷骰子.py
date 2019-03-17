"""
新增功能：模拟投掷两个骰子并可视化
新增功能：科学计算：使用矩阵

"""
import numpy as np
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体为中文黑体
plt.rcParams["axes.unicode_minus"] = False  # 设置符号问题


def main():
    total_times = 10000
    # 用矩阵记录骰子每个点数的次数
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    roll_result = roll1_arr + roll2_arr

    # 进行可视化(直方图)
    # roll_result为y轴的数据,bins为x轴的边界，density固定y轴数据为小数点后一位（即概率和为1）
    plt.hist(roll_result, bins=range(2, 14), density=1, edgecolor="black", linewidth=1,rwidth=0.8)

    # 设置x轴坐标点显示
    tick_labels = ['2点', '3点', '4点', '5点', '6点', '7点',
                   '8点', '9点', '10点', '11点', '12点']
    tick_pos = np.arange(2, 13) + 0.5
    plt.xticks(tick_pos, tick_labels)

    plt.title("骰子点数统计")
    plt.xlabel("点数和")
    plt.ylabel("概率")
    plt.show()


if __name__ == '__main__':
    main()
