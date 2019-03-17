# __all__= ["",""]:限定导入的功能代码
# __all__ = ["num","Student"]

num = 10


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


def show_msg():
    print("我是show()函数！")
