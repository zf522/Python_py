import io

str_io = io.StringIO()
# 向内存中写入字符串数据
str_io.write("Hello")
# 从内存中读取
content = str_io.getvalue()
print(content)

# 设置光标的位置
str_io.seek(0)
# 从光标的位置开始读取数据
# read()默认全部读取出来，可以指定读取的长度
result = str_io.read(2)
print(result)
