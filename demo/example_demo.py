# str1 = "10ze"
# print(str1[0:-1])


# import turtle
# """
# 绘制一个包含9个同心圆的靶盘
# 问题：怎样确定画笔的坐标
# """
# turtle.speed(10)
# turtle.circle(20, 360)
# turtle.penup()
# turtle.forward(10)
# turtle.pendown()
# turtle.circle(30, 360)
#
# turtle.done()


# name_list = ["zhangsan", "lisi", "wangwu","zhangsan"]
# print(name_list.count("zhangsan"))
# print(len(name_list))
# name_list.remove("zhangsan")
# print(name_list)


"""
字典
"""


# charactor_directory = {"name": "小明",
#                        "age": 22,
#                        "gentle": "男",
#                        "tall": 1.75}
# for key in charactor_directory:
#     print("%s - %s" % (key, charactor_directory[key]))


# name = "python语言程序设计"
# print(name[2:8])


# 不可变类型，内存中的数据不允许被修改，会报错。若是重新赋值，内存地址也会改变：
# 数字类型：int,bool,float……
# 字符串:str
# 元组：tuple

# 可变类型，内存中的数据可以被修改，但是内存地址不变：
# 列表：list
# 字典：dict
# 如果传入参数是可变类型
# 在函数内部使用方法修改数据的内容，同样会影响到外部数据
# 若是在函数中重新给变量赋值，不会影响外部数据
# def demo(num_list):
#     num_list.append(9)
#     print(num_list)
#
#
# gl_list = [1,2,3]
# demo(gl_list)
# print(gl_list)


# 一般在给多值参数命名时，习惯使用以下方式：
# *args       存放元组参数
# **kwargs    存放字典参数

# 将传入的所有数字累加并返回求和结果
# def sum_nums(*args):
#     num = 0
#     for n in args:
#         num += n
#     return num
#
# print(sum_nums(2,3))

# def num_value(num1):
#     num1 = 2
#     return num1
#
# num1 = 1
# # num_value(num1)
# print(num_value(num1))


# global可以对全局变量进行改变
# def num_value():
#     global num1
#     num1 = 2
#
#
# num1 = 1
# num_value()
# print(num1)

import requests
from threading import Thread
import re
import time
import hashlib

class BaiDu:
    """
    爬取百度图片
    """
    def __init__(self, name, page):
        self.start_time = time.time()
        self.name = name
        self.page = page
        #self.url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&rn=60&'
        self.url = 'https://image.baidu.com/search/acjson'
        self.header = {}# 添加为自己的
        self.num = 0

    def queryset(self):
        """
        将字符串转换为查询字符串形式
        """
        pn = 0
        for i in range(int(self.page)):
            pn += 60 * i
            name = {'word': self.name, 'pn': pn, 'tn':'resultjson_com', 'ipn':'rj', 'rn':60}
            url = self.url
            self.getrequest(url, name)

    def getrequest(self, url, data):
        """
        发送请求
        """
        print('[INFO]: 开始发送请求：' + url)
        ret = requests.get(url, headers=self.header, params=data)

        if str(ret.status_code) == '200':
            print('[INFO]: request 200 ok :' + ret.url)
        else:
            print('[INFO]: request {}, {}'.format(ret.status_code, ret.url))

        response = ret.content.decode()
        img_links = re.findall(r'thumbURL.*?\.jpg', response)
        links = []
        # 提取url
        for link in img_links:

            links.append(link[11:])

        self.thread(links)

    def saveimage(self, link):
        """
        保存图片
        """
        print('[INFO]:正在保存图片：' + link)
        m = hashlib.md5()
        m.update(link.encode())
        name = m.hexdigest()
        ret = requests.get(link, headers = self.header)
        image_content = ret.content
        filename = './image/' + name + '.jpg'

        with open(filename, 'wb') as f:
            f.write(image_content)

        print('[INFO]:保存成功，图片名为：{}.jpg'.format(name))

    def thread(self, links):
        """多线程"""
        self.num +=1
        for i, link in enumerate(links):
            print('*'*50)
            print(link)
            print('*' * 50)
            if link:
                # time.sleep(0.5)
                t = Thread(target=self.saveimage, args=(link,))
                t.start()
                # t.join()
            self.num += 1
        print('一共进行了{}次请求'.format(self.num))

    def __del__(self):

        end_time = time.time()
        print('一共花费时间:{}(单位秒)'.format(end_time - self.start_time))

def main():
    name = input('请输入你要爬取的图片类型: ')
    page = input('请输入你要爬取图片的页数(60张一页):')
    baidu = BaiDu(name, page)
    baidu.queryset()


if __name__ == '__main__':


    main()

