# 如果不在一个包中，可以：
# from 包名 import 模块名 ||   from 包名.模块名 import *
# import first_module
# from first_module import *
# from 模块名 import 功能模块名 as 设置别名
import first_module as first  # as设置模块别名

print(first.num)
stu = first.Student("李四", 22)
stu.show()

first.show_msg()
