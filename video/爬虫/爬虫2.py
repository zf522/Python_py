import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json

commenturl = 'http://comment5.news.sina.com.cn/page/info?\
version=1&format=js&channel=gn&newsid=comos-{}&\
group=&compress=0&ie=utf-8&oe=utf-8&page=1&\
page_size=20'


def getCommentCounts(newsurl):
    m = re.search('doc-i(.*).shtml', newsurl)
    newsid = m.group(1)
    comments = requests.get(commenturl.format(newsid))
    jd = json.loads(comments.text.strip('var data='))
    return jd['result']['count']['total']


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

newsurl = 'https://news.baidu.com/mil' #只要这条代码中的newsurl具体赋值就可以了
print(getNewsDetail(newsurl))