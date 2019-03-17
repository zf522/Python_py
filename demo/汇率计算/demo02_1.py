"""
by:张飞
date:2.26
title:根据单位判断是人民币还是美元
"""
# eval将字符串中的数字转换成整型
# <a>[0:3]表示：取字符串中的前三个字符

#带单位的货币输入
currency_str_value = input("输入带单位的货币金额是：")
#获取货币的单位
unit = currency_str_value[-3:]
usd_vs_rmb = 6.67
#判断货币的种类
if unit == 'CNY':
    #输入的是人民币
    rmb_value = eval(currency_str_value[:-3])   #将字符串转换成数字
    #汇率计算
    usd_value = rmb_value * usd_vs_rmb
    print("对应的美元金额是：",usd_value)
elif unit == 'USD':
    usd_value = eval(currency_str_value[:-3])  # 将字符串转换成数字
    rmb_value = usd_value/usd_vs_rmb
    print("对应的人民币金额是：",rmb_value)
else:
    print("该版本不支持此货币！")


# rmb_value = eval(rmb_str_value)
# usd_vs_rmb = 6.67
# usd_value = rmb_value*usd_vs_rmb
# print("对应的美元金额是：",usd_value)    #加上rmb_value???