# from bs4 import BeautifulSoup as bs
# import requests as req
# headers = {
#     'User-Agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.4011 SLBChan/ SLBVPV/64-bit'
# }
# res = req.get("https://www.baidu.com/?tn=15007414_3_pg", headers=headers)
# html_doc = res.content.decode('utf-8')
# soup = bs(html_doc, 'html.parser')# 创建BeautifulSoup对象   'html.parser'或'lxml', 'html5lib'指定一个解析器
# spans = soup.find_all('span',class_="title-content-title")#还有一种方法：spans = soup.select('.title-content-title') class下划线容易漏
# print(len(spans))
# with open("./img/百度头条.txt","w",encoding="utf-8") as f:#凡事有长度的对象都可以被遍历
#     for span in spans:
#         f.write(span.text+'\n')#  +'\n' 实现换行，通过字符串的拼接




import requests as req
import json
import pprint#实现列表中字典的换行


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Referer": "https://www.weather.com.cn/",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b": "1746415057",
    "HMACCOUNT": "C218DBB9B5B973C2",
    "f_city": "%E8%BF%9E%E4%BA%91%E6%B8%AF%7C101191001%7C",
    "Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b": "1746415464"
}
url = "https://d1.weather.com.cn/weather_index/101191001.html"
params = {
    "_": "1746415463712"
}
response = req.get(url, headers=headers, cookies=cookies, params=params)
data = response.content.decode('utf-8')
# data = json.loads(data)   text/html不符合json数据格式，只是字符串，非json数据格式，无法用json.loads()来解析
data = data.split('=')[5]
# for i in data:
#     print(i)
data = json.loads(data)
datas = data['f']
list1 = []
for data in datas:
    dict0 ={
        "日期":data['fj'],
        "最高温":data['fc'],
        "最低温":data['fd'],
        "风向":data['fe'],
        "风速":data['fg'],
    }
    list1.append(dict0)
# list1 = pprint.pprint(list1)#该函数不返回任何内容
# list1 = json.dumps(list1)
with open('./img/爬虫天气.txt', 'w',encoding = 'utf=8') as f:
    f.write(str(list1))

print('爬取完毕')
