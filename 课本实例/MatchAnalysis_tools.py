from random import random


def print_Info():
    print("欢迎使用模拟比赛系统！")


def input_info():
    proA = eval(input("请输入A运动员的能力值[0-1]："))
    proB = eval(input("请输入B运动员的能力值[0-1]："))
    n = input("请输入模拟比赛次数：")
    return proA, proB, n


def vs_games(proA, proB, n):
    winA, winB = 0, 0
    for i in range(n):
        scoreA, scoreB = vs_onegame(proA, proB)
        if scoreA > scoreB:
            winA += 1
        else:
            winB += 1
    return winA, winB


def vs_onegame(proA, proB):
    scoreA, scoreB = 0,0
    serving = "A"
    while not game_over(scoreA, scoreB):
        if serving == "A":
            if random() < proA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < proB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB


def game_over(a, b):
    return a == 15 or b == 15


def printSummary(winA, winB):
    n = winA+winB
    print("一共模拟{}场比赛".format(n))
    print("A选手获胜{}场比赛，占比{:0.1%}".format(winA, winA/n))
    print("B选手获胜{}场比赛，占比{:0.1%}".format(winB, winB / n))
