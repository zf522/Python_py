import requests

# 获取数据
r = requests.get("http://www.pptok.com/wp-content/uploads/2012/08/xunguang-4.jpg")

# 接收数据
my_content = r.content

# 把图片保存到本地
f = open("tupian.png", "wb")

# 把文件存起来
f.write(my_content)

# 关闭文件
f.close()

