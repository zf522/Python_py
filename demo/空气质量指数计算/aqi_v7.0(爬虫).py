from bs4 import BeautifulSoup
import requests

"""
通过网页链接获取网页内容
对网页内容进行处理
获取所有城市
"""


def get_city_aqi(city_pinyin):
    url = "http://pm25.in/" + city_pinyin
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


def get_city():
    """
    用来获取所有城市名
    :return:
    """
    city_list = []
    url = "http://pm25.in/"
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    # 先找到"bottom"的节点，取第一节点
    city_div = soup.find_all("div", {"class": "bottom"})[1]
    # 再从节点中找到"a"的一行存入列表中
    city_link_list = city_div.find_all("a")
    # 循环得到其中的name和pinyin，最后添加到之前建立好的空列表汇中，返回空列表
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link["href"][1:]
        city_list.append((city_name, city_pinyin))
    return city_list


def main():
    # 将获得的数据存到列表中
    city_list = get_city()
    # 循环遍历，取出列表中name和pinyin，将pinyin传给get_city_aqi函数获得city_aqi，最后输出name和aqi
    for city in city_list:
        city_name = city[0]
        city_pinyin = city[1]
        city_aqi = get_city_aqi(city_pinyin)
        print(city_name, city_aqi)


if __name__ == '__main__':
    main()
