"""
52周存钱挑战
第一周：10元
第二周：20元
第三周：30元
求 n 周之后总共存了多少钱？
"""

import math
import datetime


def money_sum(money_per_week, increase_money, total_week):
    """
    计算n周内的存款金额
    :param money_per_week:
    :param increase_money:
    :param total_week:
    :return:
    """
    money_list = []  # 记录每周存款数的列表
    saved_money_list = []  # 记录每周账户累计

    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)

        money_per_week += increase_money
    return saved_money_list


def main():
    total_week = int(input("请输入存款的周数："))
    money_per_week = int(input("请输入每周存款数（元）："))
    increase_money = int(input("请输入每周递增的存款数（元）："))

    # 调用函数
    saved_money_list = money_sum(money_per_week, increase_money, total_week)

    input_date_str = input("请输入日期（yyyy-mm-dd）:")
    #将字符串解析成日期格式
    input_date = datetime.datetime.strptime(input_date_str, "%Y-%m-%d")
    week_num = input_date.isocalendar()[1]
    print("第{}周的存款：{}元".format(week_num, saved_money_list[week_num - 1]))


if __name__ == '__main__':
    main()
