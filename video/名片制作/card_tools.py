card_list = []


def show_menu():
    # 显示界面
    print("*" * 50)
    print("")
    print("欢迎使用名片管理系统   v1.0")
    print("请选择您要执行的操作：")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出")
    print("*" * 50)


def new_card():
    # 新增名片
    print("-" * 50)
    # 1.提示用户输入新增信息
    print("请输入新增人员信息：")
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ:")
    email = input("请输入Email:")
    # 2.将信息保存到字典中
    card_dict = {"name": name,
                 "phone": phone,
                 "qq": qq,
                 "email": email}
    # 3.将字典保存到列表中
    card_list.append(card_dict)
    print(card_list)
    # 4.提示用户已经完成操作
    print("%s 的名片添加成功！" % name)


def show_all():
    # 显示名片
    print("-" * 50)
    # 判断是否存在名片，如果没有就返回
    if len(card_list) == 0:
        print("当前没有用户，请返回界面添加新用户！")
        # return可以返回一个函数的执行结果
        # 下方的代码不会被执行
        # 如果return后面没有任何的内容，表示会返回到调用函数的位置
        # 并且不会返回任何的结果
        return

    print("以下是所有用户的名片！")
    print("")
    # 打印表头
    for name in ["姓名", "电话", "QQ", "Email"]:
        print(name, end="\t\t")
    print("")

    # 遍历列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))
    print("")


def search_card():
    # 查询名片
    print("-" * 50)
    # 1.提示用户输入查询的姓名
    find_name = input("请输入要查询的姓名：")

    # 2.遍历名片列表，查询要搜索到姓名，如果找到，就显示，找不到，就提示
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\tEmail")
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # 进行修改和删除名片
            deal_card_dict(card_dict)
            break
    else:
        print("未找到%s的名片！" % find_name)


def deal_card_dict(find_dict):
    """修改和删除名片的函数

    :param find_dict:要进行操作的名片字典
    """
    # 1.提示用户是否删除和修改
    action_str = input("【1】修改\t【2】删除\t【0】返回： ")
    if action_str == "1":
        # 2.修改：按下回车，如果没有修改值，则返回原来的值
        find_dict["name"] = input_card_info(find_dict["name"], "输入姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "输入电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "输入QQ：")
        find_dict["email"] = input_card_info(find_dict["email"], "输入email：")
        print("成功修改名片")

        # 3.删除
    elif action_str == "2":
        card_list.remove(find_dict)
        print("成功删除名片！")


def input_card_info(dict_value, tip):
    """输入名片信息

    :param dict_value:字典中原有的值
    :param tip:用户输入的内容
    :return:如果用户输入了内容，就返回内容，否则就返回字典中原有的值
    """
    # 1.提示用户输入内容
    result_str = input(tip)
    # 2.根据输入内容进行判断，如果result_str的长度大于零，即输入了新的值,则返回新值
    if len(result_str) > 0:
        return result_str
    # 3.没有输入新内容，返回原来字典中的值
    else:
        return dict_value
