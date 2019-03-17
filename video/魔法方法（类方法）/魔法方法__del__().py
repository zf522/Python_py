# 魔法方法：以__开始，以__(self)结束，当创建对象时，会自动调用魔法方法

# __del__:当对象释放的时候会自动调用__del__方法
# 1.程序退出，程序中所使用的对象全部销毁
# 2.当前对象的内存地址没有变量使用的时候，那么对象会被销毁
import time


class Teacher(object):
    def __init__(self, name, age):
        # self:表示当前对象
        # 给对象初始化，添加对象属性
        print("对象被调用了!")
        self.name = name
        self.age = age

    # 当引用次数为0时，会调用__del__方法
    def __del__(self):
        print("对象释放了！", self)


teacher1 = Teacher(name="张三", age=21)
print(teacher1)
teacher2 = teacher1
# 删除变量
del teacher1
del teacher2
# 引用次数：内存地址被变量使用的次数，当引用次数为0时，表示对象被销毁

time.sleep(3)
print("程序退出了！")
