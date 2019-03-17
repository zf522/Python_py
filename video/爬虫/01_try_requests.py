import requests

"""
获取网页的HTML字符串
"""

# 发送get请求
# url = "http://www.baidu.com/basetrans"
#
# response = requests.get(url)
#
# print(response)

# 发送post请求
url = "https://fanyi.baidu.com"

query_str = {"from": "zh",
             "to": "en",
             "query": "人生苦短，我用python"}

# 为了模拟浏览器，获取和浏览器一模一样的内容
# 如果服务器检测到是爬虫，就多加些headers的键值对
header ={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
           "Referer": "https: // fanyi.baidu.com /?aldtype = 16047"}

response = requests.post(url, data=query_str, headers = header)

# 进行解码的方法一：
# response.encoding = "utf-8"
# print(response.text)

# 方法二：
print(response.content.decode())

# 方法三：
# print(response.content.decode("utf-8"))
