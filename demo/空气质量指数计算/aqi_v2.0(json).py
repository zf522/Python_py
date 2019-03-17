import json
"""
需要在文件夹里添加json文件
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
    top_list = city_list[:5]

    f = open('top_json_list', 'w', encoding='utf-8')
    json.dump(top_list, f, ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    main()
