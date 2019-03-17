from bs4 import BeautifulSoup
import requests

"""
通过网页链接获取网页内容
对网页内容进行处理
"""


def get_city_aqi(input_pinyin):
    url = "http://pm25.in/" + input_pinyin
    r = requests.get(url, timeout=30)
    # 获取html代码以文本格式
    soup = BeautifulSoup(r.text, 'lxml')
    # 以关键字从中找到并存入列表中:可以使用字典：
    # city_list = soup.find_all("div", {"class":"span1"})
    city_list = soup.find_all("div", class_="span1")  # 注意是class_
    # 建立一个空列表
    content_list = []

    # 需要几项就循环几次
    for i in range(8):
        # 从列表中逐次循环赋值
        city_content = city_list[i]
        # 再按关键字查找得到节点，然后拿到节点的内容（text)，再去掉空格（即取到字符串strip())
        aqi_caption = city_content.find('div', class_="caption").text.strip()
        aqi_value = city_content.find('div', class_="value").text.strip()

        # 存入列表中,使用append方法，一次只能加入一个值，可以使用元组添加
        content_list.append((aqi_caption, aqi_value))

        # 返回列表
    return content_list


def main():
    input_pinyin = input("请输入拼音：")
    city_aqi = get_city_aqi(input_pinyin)
    print(city_aqi)


if __name__ == '__main__':
    main()
