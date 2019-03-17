"""
by:张飞
date:2.25
title:汇率计算
"""
rmb_str_value = input("人民币的金额是：")
rmb_value = eval(rmb_str_value)
usd_vs_rmb = 6.67
usd_value = rmb_value*usd_vs_rmb
print("对应的美元金额是：",usd_value)    #加上rmb_value???