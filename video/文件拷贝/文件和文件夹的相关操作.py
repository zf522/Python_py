# file = open("a.txt", "w")
# file.write("abc")
# file.close()


# 导入os模块：文件和文件夹操作相关的模块
import os

# 文件删除的高级模块
import shutil

# 对文件重命名
# os.rename("c.txt","ccc")
# 1.指定路径创建文件夹
# file = open("ccc/c.txt","w",encoding="utf-8")
# file.close()

# 2.切换到指定某文件夹内创建
# 查看当前目录
# current_path = os.getcwd()
# print(current_path)
# # 切换到指定目录
# os.chdir("ccc")
# current_path = os.getcwd()
# print(current_path)
#
# file = open("d.txt", "w", encoding="utf-8")
# file.close()

# 创建文件夹
# os.mkdir("c.txt")

# renames可以将文件夹以及其中的文件同时重命名
# os.renames("a/a.txt","b/b.txt")
# 查看目录下的文件名列表信息
# print(os.listdir('ccc'))
# 删除文件
# os.remove("ccc/c.txt")
# 删除空文件夹
# os.rmdir("ccc")
# 删除目录树（即包含文件的目录）
# shutil.rmtree("ccc")

# 获取3.txt的绝对路径
# abs_path = os.path.abspath("3.txt")
# print(abs_path)
# #根据绝对路径获取路径中的文件名
# file_name = os.path.basename(abs_path)
# print(file_name)
#
# #获取文件名和文件后缀
# result = os.path.splitext(file_name)
# print(result)
