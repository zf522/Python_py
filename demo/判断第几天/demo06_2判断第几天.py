from datetime import datetime


# 判断闰年
def is_leap_year(year):
    is_leap = False
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True
    return is_leap


def main():
    input_str_date = input("请输入日期(yyyy/mm/dd)：")        # 只能用固定格式输入：yyyy/mm/dd
    input_date = datetime.strptime(input_str_date, "%Y/%m/%d")
    print(input_date)
    year = input_date.year
    month = input_date.month
    day = input_date.day
    # 计算之前月份天数的总和以及当前月份天数
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 如果是闰年，直接更改列表中二月份的值，列表可以直接更改值，元组不能更改
    if is_leap_year(year):
        days_in_month_list[1] = 29
    days = sum(days_in_month_list[:month-1])+day

    # days = sum(days_in_month_list[:month-1])+day
    # # 判断闰年
    # if month > 2 and is_leap_year(year):
    #     days += 1

    print('这是第{}天。'.format(days))


if __name__ == '__main__':
    main()