# 魔法方法：以__开始，以__(self)结束，当创建对象时，会自动调用魔法方法

# __str__:当使用print打印对象的时候会自动的调用对象的__str__方法
class Teacher(object):
    def __init__(self, name, age):
        # self:表示当前对象
        # 给对象初始化，添加对象属性
        print("对象被调用了!")
        self.name = name
        self.age = age

    # 返回对象的描述信息
    def __str__(self):
        # 返回一个字符串信息
        return "我叫{}，年龄是{}".format(self.name, self.age)


teacher = Teacher(name="张三", age=21)
print(teacher)
