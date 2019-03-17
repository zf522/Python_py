"""
by:张飞
date:2.26
title:循环根据单位判断是人民币还是美元
"""
#带单位的货币输入
usd_vs_rmb = 6.6
currency_str_value = input("输入带单位的货币金额是（退出输入Q）：")
i=0
while currency_str_value != 'Q':
    i = i+1
    print('循环次数：',i)
    #获取货币的单位
    unit = currency_str_value[-3:]
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
    currency_str_value = input("输入带单位的货币金额是（退出输入Q）：")
print("已退出！")


# rmb_value = eval(rmb_str_value)
# usd_vs_rmb = 6.67
# usd_value = rmb_value*usd_vs_rmb
# print("对应的美元金额是：",usd_value)    #加上rmb_value???

