import requests


def main():
    print("*" * 100)
    print("使用字典存储url")
    print("*" * 100)
    url_dict = {"廖雪峰的网站": "http://www.liaoxuefeng.com/",
                "xyz": "www.baidu.com",
                "简书": "http://www.jianshu.com/",
                "网上书店": "http://www.phei.com.cn/module/goods/wssd_index.jsp",
                "简书2": "http://www.jianshu.com/"
                }
    get_url_dict = set()
    for ind, name in enumerate(url_dict.keys()):
        name_url = url_dict[name]
        if name_url in get_url_dict:
            print(ind, name, '已经抓取过了。')
        else:
            try:
                resp = requests.get(name_url)
            except Exception as e:  # 抛出异常
                print(ind, name, ':', str(e)[:50])
                continue
            content = resp.text
            get_url_dict.add(name_url)
            with open("get_dict" + name + ".html", "a", encoding="utf-8") as f:
                f.write(content)
                print("抓取完成：{} {}，内容长度为{}".format(ind, name, len(content)))

    for u in get_url_dict:
        print(u)

    print("*" * 100)
    print("使用列表存储url")
    print("*" * 100)
    url_list = [
        ("廖雪峰的网站", "https://www.liaoxuefeng.com/"),
        ("xyz", "www.baidu.com"),
        ("简书", "https://www.jianshu.com/")]
    get_url_list = set()
    for ind, tup in enumerate(url_list):
        name = tup[0]
        name_url = tup[1]
        if name_url in get_url_list:
            print(ind, name, '已经抓取过了。')
        else:
            try:
                resp = requests.get(name_url)
            except Exception as e:  # 抛出异常
                print(ind, name, ':', str(e)[:50])
                continue
            content = resp.text
            get_url_list.add(name_url)
            with open("get_dict" + name + ".html", "a", encoding="utf-8") as f:
                f.write(content)
                print("抓取完成：{} {}，内容长度为{}".format(ind, name, len(content)))

    for u in get_url_list:
        print(u)


if __name__ == '__main__':
    main()
