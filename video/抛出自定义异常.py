# 自定义异常类，必须继承Exceptoin类
class CustomException(Exception):
    def __init__(self, content):
        self.content = content

    # 表示抛出异常显示的异常描述信息
    def __str__(self):
        return "出现异常！因为数据不是a,而是%s" % self.content


content = input("请输入数据：")
if content != 'a':
    # 抛出自定义异常
    raise CustomException(content)
