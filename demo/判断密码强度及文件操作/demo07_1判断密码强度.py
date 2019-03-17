"""
判断密码强度
密码长度大于8，
密码包含数字
密码包含字母
"""


def check_num(kw):
    for i in kw:
        if i.isnumeric():
            return True
    return False


def check_letter(kw):
    for i in kw:
        if i.isalpha():
            return True
    return False


def main():
    strength_level = 0
    kw = input("请输入密码：")
    # 密码长度大于8
    if len(kw) >= 8:
        strength_level += 1
    else:
        print("密码长度须大于8！")

    # 密码包含数字
    if check_num(kw):
        strength_level += 1
    else:
        print("密码须包含数字！")

    # 密码包含字母
    if check_letter(kw):
        strength_level += 1
    else:
        print("密码须包含字母！")

    if strength_level == 3:
        print("密码合格！")
    else:
        print("密码不合格！")


if __name__ == '__main__':
    main()
