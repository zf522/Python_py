# __slots__ 方法指明创建对象的时候只能是固定的属性，不能添加新的属性
class Person():
    # 这样的操作可以让对象的属性固定
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("初始化")


p = Person("张三", 22)
# p.sex = "男"    #报错，因为__slots__不允许添加新的属性
print(p.name, p.age)
# 允许修改原属性
p.name = 'wangwu'
print(p.name, p.age)
