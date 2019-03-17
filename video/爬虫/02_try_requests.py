import requests
from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

# 进行异常捕获
@retry(stop_max_attempt_number=3)
# 让被装饰的函数反复执行三次，三次全部报错才会报错，只要有一次没有报错，程序就继续向下执行
def _parse_url(url):
    print("*"*100)
    response = requests.get(url, headers=headers, timeout=5)
    return response.content.decode()


def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str


if __name__ == "__main__":
    url = "www.baidu.com"
    url1 = "http://www.baidu.com"
    print(parse_url(url1)[:100])

