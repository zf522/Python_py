"""
1.定义布尔型变量has_ticket表示是否偶车票
2.定义整型变量knife_length表示刀的长度，单位：厘米
3.首先检查是否有车票，如果有，才允许进行安检
4.安检时，需要检查刀的长度，判断是否超过20厘米
    .如果超过20厘米，提示刀的长度，不允许上车
    .如果不超过20厘米，安检通过
5.如果没有车票，不允许进门
"""

has_ticket = input("是否有车票：")

if has_ticket == 'true':
    print("请检票！")
    knife_length =eval(input("刀的长度为（单位：厘米）："))
    if knife_length > 20:
        print("刀的长度为%f，禁止上车！" %knife_length)
    else:
        print("请上车！")
else:
    print("无票禁止上车！")
