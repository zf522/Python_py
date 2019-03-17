"""
判断密码强度
密码长度大于8，
密码包含数字
密码包含字母
新增功能：循环的终止和设置循环次数
"""


def check_num(kw):
    has_num = False
    for i in kw:
        if i.isnumeric():
            has_num = True
            break
    return has_num


def check_letter(kw):
    has_letter = False
    for i in kw:
        if i.isalpha():
            has_letter = True
            return has_letter
    return has_letter


def main():
    try_times = 5
    while try_times > 0:
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
            break
        else:
            print("密码不合格！")
            try_times -= 1


if __name__ == '__main__':
    main()
