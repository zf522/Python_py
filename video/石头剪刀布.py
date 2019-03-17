"""
从控制台输入想要出的拳-石头(1)、剪刀(2)、布(3)
电脑随机出拳-假定电脑只会出石头，完成整体代码功能
比较胜负
"""
# 导入随机工具包：random
import random

# 循环：三局两胜
i = 0
while i < 3:
    player = int(input("请输入您要出的拳(石头(1)、剪刀(2)、布(3))："))
    computer = random.randint(1, 3)
    # 显示出拳结果
    print("您出的拳是 %d，电脑出的拳是 %d" % (player, computer))
    # 判断胜负
    if ((player == 1 and computer == 2)
            or (player == 2 and computer == 3)
            or (player == 3 and computer == 1)):
        print("玩家胜利！")
    elif player == computer:
        print("平局！")
    else:
        print("电脑胜利！")
    i += 1
