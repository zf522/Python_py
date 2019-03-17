import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json
import pandas
import sqlite3

commenturl = 'http://comment5.news.sina.com.cn/page/info?\version=1&format=js&channel=gn&newsid=comos-{}&\group=&compress=0&ie=utf-8&oe=utf-8&page=1&\page_size=20'

#获取评论数量
def getCommentCounts(newsurl):
    m = re.search('doc-i(.*).shtml', newsurl)
    newsid = m.group(1)
    comments = requests.get(commenturl.format(newsid))
    jd = json.loads(comments.text.strip('var data='))
    return jd['result']['count']['total']

#获取新闻详情
def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    result['title'] = soup.select('#artibodyTitle')[0].text
    result['newssource'] = soup.select('.time-source span a')[0].text
    timesource = soup.select('.time-source')[0].contents[0].strip()
    result['dt'] = datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
    result['article'] = '@'.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
    result['editor'] = soup.select('.article-editor')[0].text.strip('责任编辑：')
    result['comments'] = getCommentCounts(newsurl)
    return result

#解析分页连接
def parseListLinks(url):
    newsdetails = []
    res = requests.get(url)
    jd = json.loads(res.text.rstrip(');').lstrip(' newsloadercallback('))
    for ent in jd['result']['data']:
        newsdetails.append(getNewsDetail(ent['url']))
    return newsdetails

#url为分页链接，关键参数page
url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1509779364426'
news_total = []

#抓取1，2两页新闻信息
for i in range(1,3):
    newsurl = url.format(i)
    newsary = parseListLinks(newsurl)
    news_total.extend(newsary)

#使用sqlite存储数据，pandas清晰展示数据
df = pandas.DataFrame(news_total)
with sqlite3.connect('news.sqlite') as db:
    df2 = pandas.read_sql_query('select * from news', con = db)
df2