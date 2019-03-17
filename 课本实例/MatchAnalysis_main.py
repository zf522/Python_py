"""
打球比赛，根据球员的胜率值预测在n场比赛下取胜的概率
"""
# 1.打印程序的介绍信息
# 2.获得程序运行需要的参数，即probA,probB,n
# 3.由运动员的能力值proA,proB,模拟n次比赛
# 4.输出球员A和B获胜比赛的场次和概率

# import MatchAnalysis_tools
from MatchAnalysis_tools import *


def main():
    print_Info()

    proA, proB, n = input_info()

    winsA, winsB = vs_games(proA, proB, n)
    printSummary(winsA, winsB)


if __name__ == "__main__":
    main()
