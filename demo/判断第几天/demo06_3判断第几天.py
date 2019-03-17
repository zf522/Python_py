from datetime import datetime

"""
将月份划分为不同的集合进行操作
"""


# 判断闰年
def is_leap_year(year):
    is_leap = False
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True
    return is_leap


def main():
    input_str_date = input("请输入日期(yyyy-mm-dd)：")  # 只能用固定格式输入：yyyy/mm/dd
    input_date = datetime.strptime(input_str_date, "%Y-%m-%d")
    print(input_date)
    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 集合
    _30_day_month_set = {4, 6, 9, 11}  # 包含30天的月份集合
    _31_day_month_set = {1, 3, 5, 7, 8, 10, 12}
    # 初始化天数
    days = 0
    days += day
    for i in range(1, month):  # 对集合进行遍历，从1开始选择月份
        if i in _30_day_month_set:
            days += 30
        elif i in _31_day_month_set:
            days += 31
        else:
            days += 28

    # 判断闰年
    if month > 2 and is_leap_year(year):
        days += 1

    print('这是第{}天。'.format(days))


if __name__ == '__main__':
    main()
