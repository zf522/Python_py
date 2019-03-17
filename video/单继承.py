# 单继承：子类只继承一个父类
# 子类继承父类可以使用父类的方法和属性
# 继承的好处：子类可以复用父类的方法


class person(object):
    def __init__(self):
        self.name = "zhangsan"
        self.age = 12

    def show(self):
        print(self.name, self.age)


# 学生类是子类，person类是父类
class student(person):
    pass


xiaoming = student()
xiaoming.show()
print(xiaoming.name,xiaoming.age)
