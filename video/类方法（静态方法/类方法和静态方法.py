class Person(object):
    # 定义一个私有属性：以__开头
    __type = "黄种人"

    def __init__(self):
        self.name = "小红"

    # 定义对象方法:在方法的参数里面有self表示对象方法
    def show(self):
        print("我是人类")

    # 定义类方法：cls表示当前类
    @classmethod
    def show_info(cls):
        print(cls)
        print("我是一个类方法")

    # 应用场景：类方法可以修改类属性，更改私有属性
    @classmethod
    def set_type(cls, type):
        cls.__type = type

    @classmethod  # 返回私有属性
    def get_type(cls):
        return cls.__type

    # 定义静态方法：静态方法和当前对象和当前类没有关系
    @staticmethod
    def show_msg():
        print("我是一个静态方法")

    # --------------------------------对象方法是最通用的方法，可以修改对象属性和类属性
    def instance_set_type(self, type, name):
        # 获取对象所对应的类
        self.__class__.__type = type
        print(self.name)  # 原来的name = 小红
        self.name = name  # 给name重新赋值

    def instance_get_type(self):
        # print(self.name)

        return self.name, self.__class__.__type

    @staticmethod  # 既不需要当前对象和当前类
    def sum_num(num1, num2):
        sum = num1 + num2
        return sum


# 创建对象，对象调用方法
p = Person()
p.show()
p.show_info()
p.show_msg()

p.set_type("白种人")
print(p.get_type())

p.instance_set_type("黑种人", "张三")
print(p.instance_get_type())

print(p.sum_num(1, 2))

# 类调用静态方法和类方法不需要传入当前类，如果类调用对象方法需要传入一个实例
Person.show_msg()
Person.show(p)  # 类调用对象方法
Person.show_info()
