"""
by:张飞
date:2.26
title:循环根据单位判断是人民币还是美元
"""


# 调用函数实现汇率转换


# def exchange_fun(im,er):
#     """
#     汇率计算函数
#     """
#     out = im * er
#     return out


def main():
    """
    主函数
    """
    usd_vs_rmb = 6.77
    currency_str_value = input("输入带单位的货币金额是：")
    # 获取货币的单位
    unit = currency_str_value[-3:]
    # 判断货币的种类
    if unit == 'CNY':
        exchange_rate = 1 / usd_vs_rmb
    elif unit == 'USD':
        exchange_rate = usd_vs_rmb
    else:
        exchange_rate = -1
    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])

        # 调用lambda函数：用于简单的、能够在一行内表示的函数，计算结果为返回值
        # 函数名 = lambda <参数列表>: <表达式>
        exchange_fun2 = lambda x: in_money * exchange_rate
        out_money = exchange_fun2(in_money)
        print("兑换后的金额是：", out_money)
    else:
        print("不支持该货币！")


if __name__ == '__main__':
    main()
