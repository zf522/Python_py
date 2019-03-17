# 单例：在应用程序中，不管创建多少次对象就只有一个实例对象
class Person():
    # 创建一个私有属性
    __instance = None

    # new方法确定实例只创建一次
    def __new__(cls, *args, **kwargs):
        print("创建对象")
        if not cls.__instance:  # if cls.__instance ==None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        print("初始化")


p1 = Person()
p2 = Person()
# 输出p1,p2变量的地址
print(p1, p2)
