import requests

url = "http://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
cookie = "IKUT=7042; BAIDUID=4519F85EEDBB7CE677A2C69C3B5CAFFD:FG=1; BIDUPSID=4519F85EEDBB7CE677A2C69C3B5CAFFD; PSTM=1547720614; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; pgv_pvi=4714108928; SE_LAUNCH=5%3A25862788_0%3A25862788_3%3A25862788; BD_BOXFO=_avOi_aj2YoaC; H_WISE_SIDS=125703_128066_129326_129554_120181_118890_118868_118847_118826_118800_107315_129387_129087_129558_117327_129751_117433_128790_128402_129652_128246_124629_129621_129009_128968_129642_129294_129394_129518_129374_129288_129836_127761_129480_129644_129506_124030_110085_123289_129811_128195_129251_128960; rsv_i=8c0dpSM%2BA85GRHLxfhj5X1SpbAx%2BsSUuqCOymjmn9eOSkgDe2m2IyMBb7qENY87vpTtAk4TEA0%2BWCACTPRjb6dVfEVgkUe8; FEED_SIDS=480279_0305_14; ZD_ENTRY=empty; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1551686306,1551706103,1551709483,1551771558; BDUSS=GlwQnVTd0lQSXJjcXl6QUFCRn5ZSFlWZmQzNTFNU2NIaU9jUGJTQUoxckF0S1ZjQUFBQUFBJCQAAAAAAAAAAAEAAAADacc5SGVsbG~VxbfJAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAnflzAJ35cc; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1551771737"
# 获取cookie字典cookie_dict
cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in cookie.split("; ")}
print(cookie_dict)
# cookie_dict传给cookies参数
response = requests.get(url, headers=headers, cookies=cookie_dict)

# 爬取整个html并保存为loginup.html文件
with open('loginup.html', "w", encoding="utf-8") as f:
    f.write(response.content.decode())
