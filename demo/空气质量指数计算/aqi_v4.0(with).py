import csv
import json
import os

"""

判断文件后缀名（使用os模块中的方法）
用with语句进行文件的读写，省去了”关闭文件“这一步骤
"""


def process_json_file(file_path):
    """
    解码json文件
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)

    # f = open(file_path, mode='r', encoding='utf-8')
    # city_list = json.load(f)
    # return city_list


def process_csv_file(file_path):
    with open(file_path, "w", encoding="utf-8", newline=" ") as f:
        reader = csv.reader(f)
        for line in reader:
            print(','.join(line))


def main():
    file_path = input("请输入json文件名称：")
    file_name, file_ext = os.path.splitext(file_path)
    if file_ext == '.json':
        process_json_file(file_path)
    elif file_ext == '.csv':
        process_csv_file(file_path)
    else:
        print("不支持的文件格式！")


if __name__ == '__main__':
    main()
