# 1.打开原文件
src_file = open("3.txt", "rb")
# 可以指定拷贝后的文件路径
aim_file = open("/Users/16681/Desktop/4.txt", "wb")
while True:
    print(src_file.tell())
    file_data = src_file.read(1024)     # 一次性读出1024个字节
    if file_data:       # 判断二进制变量类型是否有数据
        file_new_data = aim_file.write(file_data)
    else:
        print("文件读取完毕！")
        break
# 5.关闭文件
aim_file.close()
src_file.close()
