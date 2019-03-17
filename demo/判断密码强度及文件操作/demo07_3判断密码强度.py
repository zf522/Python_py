"""
判断密码强度
密码长度大于8，
密码包含数字
密码包含字母
新增功能：循环的终止和设置循环次数
        定义一个password工具类(用类封装）
        定义一个文件工具类
"""


# password工具类
class PasswordTools():
    def __init__(self, kw):
        self.kw = kw
        self.strength_level = 0

    def check_num(self, kw):
        has_num = False
        for i in kw:
            if i.isnumeric():
                has_num = True
                break
        return has_num

    def check_letter(self, kw):
        has_letter = False
        for i in kw:
            if i.isalpha():
                has_letter = True
                return has_letter
        return has_letter

    def process_check(self):
        # 密码长度大于8
        if len(self.kw) >= 8:
            self.strength_level += 1
        else:
            print("密码长度须大于8！")

        # 密码包含数字
        if self.check_num(self.kw):
            self.strength_level += 1
        else:
            print("密码须包含数字！")

        # 密码包含字母
        if self.check_letter(self.kw):
            self.strength_level += 1
        else:
            print("密码须包含字母！")


# 文件工具类
class FileTools():
    def __init__(self, filepath):
        self.filepath = filepath

    def write_file(self, line):
        f = open(self.filepath, "a", encoding="utf-8")
        f.write(line)
        f.close()

    def read_file(self):
        f = open(self.filepath, 'r', encoding="utf-8")
        lines = f.readlines()
        f.close()
        return lines


def main():
    try_times = 5
    # 实例化文件类对象
    filepath = "password.txt"
    filetool = FileTools(filepath)

    while try_times > 0:
        kw = input("请输入密码：")
        # 实例化密码工具类对象
        passwordtool = PasswordTools(kw)
        passwordtool.process_check()

        # 文件写操作
        line = "密码：{}，强度：{}\n".format(kw, passwordtool.strength_level)
        filetool.write_file(line)

        if passwordtool.strength_level == 3:
            print("密码合格！")
            break

        else:
            print("密码不合格！")
            try_times -= 1
        print()
    if try_times <= 0:
        print("尝试次数过多，密码设置失败！")
    # 文件读操作
    lines = filetool.read_file()
    print(lines)


if __name__ == '__main__':
    main()
