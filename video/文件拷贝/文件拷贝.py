# 1.打开原文件
src_file = open("3.txt", "rb")
# 2.读取数据
file_data = src_file.read()
# 3.打开目标文件
# 可以指定拷贝后的文件路径
aim_file = open("/Users/16681/Desktop/4.txt", "wb")
# 4.写入目标文件
file_new_data = aim_file.write(file_data)
# 5.关闭文件
aim_file.close()
src_file.close()
