# 把方法改成对应的属性
class Student():
    def __init__(self):
        self.__score = 100

    # 获取值
    @property
    def get_score(self):
        return self.__score

    # 设置值
    @get_score.setter
    def set_score(self, score):
        self.__score = score


stu = Student()

score = stu.get_score  # 获取值
print(score)  # 打印值

stu.set_score = 20  # 用set_score设置值
score = stu.get_score  # 获取值
print(score)  # 打印值
