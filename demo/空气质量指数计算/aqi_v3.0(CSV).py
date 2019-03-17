import csv
import json

"""
1.以行为单位
2.每行表示一条记录
3.以英文逗号分割每列数据（如果数据为空，逗号也要保留）
4.列名通常放置在文件第一行
"""


def process_json_file(file_path):
    """
    解码json文件
    """
    f = open(file_path, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    file_path = input("请输入json文件名称：")
    city_list = process_json_file(file_path)
    city_list.sort(key=lambda city: city['aqi'])

    lines = []
    lines.append(list(city_list[0].key()))
    for city in city_list:
        lines.append(list(city.values()))

    f = open(file_path, "w", encoding="utf-8", newline=" ")
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)

    f.close()


if __name__ == '__main__':
    main()
