from io import BytesIO

byte_io = BytesIO()
# 向内存中写入二进制数据
byte_io.write("哈哈".encode("utf-8"))
# 获取二进制数据
data = byte_io.getvalue()
print(data)
# 对二进制数据解码
content = data.decode("utf-8")
print(content)
