import requests

"""
通过网页链接获取网页内容
对网页内容进行处理
"""


def get_code_text(get_url):
    r = requests.get(get_url, timeout=30)
    print(r.status_code)
    return r.text


def main():
    input_pinyin = input("请输入拼音：")
    url = "http://pm25.in/" + input_pinyin
    code_text = get_code_text(url)
    print(code_text)

    aqi_div = """    <div class="span12 data">
        <div class="span1">
          <div class="value">
            """  # div一定要复制到数字的前面空格
    index = code_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_val = code_text[begin_index:end_index]
    print('空气质量为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()
