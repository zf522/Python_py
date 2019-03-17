"""
系统需求
1.程序启动，显示界面
2.用户用数字选择不同的功能
3.根据功能选择，执行不同的功能
4.用户名片需要记录用户的姓名、电话、QQ、邮件
5.如果查询到指定的名片，用户可以选择修改或者删除名片

步骤：
1.框架搭建
2.新增名片
3.显示所有名片
4.查询名片
4.查询成功后，修改、删除名片
让python程序能够直接运行
"""

import card_tools

while True:
    # TODO（阿飞） 显示菜单
    card_tools.show_menu()
    in_str = input("请输入您要进行的操作：")
    print("您选择的操作是【%s】" %in_str)
    if in_str in ["1", "2", "3"]:
        if in_str == "1":
            #新增名片
            card_tools.new_card()
        elif in_str == "2":
            #显示名片
            card_tools.show_all()
        elif in_str == "3":
            #查询名片
            card_tools.search_card()
    elif in_str == "0":
        print("您已退出【名片管理系统】！")
        break
    else:
        print("您输入的操作不正确！")

