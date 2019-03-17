# 魔法方法：以__开始，以__(self)结束，当创建对象时，会自动调用魔法方法


class Teacher(object):
    def __init__(self, name, age):
        # self:表示当前对象
        # 给对象初始化，添加对象属性
        print("对象被调用了!")
        self.name = name
        self.age = age

    # 显示老师信息的方法：
    def show_info(self):
        # self:表示当前对象，哪个对象调用这个方法，这个self就是哪个对象
        print(self.name, self.age)


teacher = Teacher("张三", 21)
teacher.show_info()

teacher = Teacher("李四", 55)
teacher.show_info()
