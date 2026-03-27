'''
import requests as rq
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor
import time
session = rq.Session()#每次requests.get()新建连接，TCP握手耗时。全局使用requests.Session()

def download(n):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        # "cache-control": "max-age=0",#缓存时间，不要
        # "if-modified-since": "Wed, 25 Jun 2025 11:17:22 +0000",#请求头里有日期有时会有阻碍
        "priority": "u=0, i",
        "referer": "https://www.b31fa.icu/index/44045/",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
    }
    cookies = {
        "Hm_lvt_9c5f07b6ce20e3782eac91ed47d1421c": "1750995146",
        "HMACCOUNT": "C218DBB9B5B973C2",
        "Hm_lpvt_9c5f07b6ce20e3782eac91ed47d1421c": "1750996034"
    }
    response = session.get(url = f'https://www.b31fa.icu/index/44045/{n}.html',headers = headers,cookies = cookies)
    r = response.content.decode("utf-8")
    soup = bs(r,"html.parser")#创建BeautifulSoup对象，   指定一个解析器
    r1 = soup.select_one("#chaptercontent").decode_contents()#获取全部内容   #select 返回的是一个列表     soup.select_one("#chaptercontent") - 使用CSS选择器语法选取文档中第一个id为"chaptercontent"的元素
    #                                                                       .text - 获取该元素及其所有子元素的纯文本内容
    r1 = r1.replace('<br/>','\n')

    with open(f'万相之王/第{n}章.txt','w',encoding='utf-8') as f:# 'w'模式：写入模式（会覆盖已存在文件）
        f.write(r1)
start = time.time()
with ThreadPoolExecutor(max_workers=64) as executor:#100线程：160s  300线程: 50s 1000线程：43s 800线程：29s 一章：1.4s
    # excutor = []
    for n in range(1,1688):
        executor.submit(download,n)
end = time.time()
print(f"下载完成，共用时{end-start}s")
'''


#改进
import requests as rq
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor
import time
session = rq.Session()#每次requests.get()新建连接，TCP握手耗时。全局使用requests.Session()
urls = []
def url_s():#搞定链接地址
    for i in range(1,1689):
        url = f'https://www.b31fa.icu/index/44045/{i}.html'
        urls.append(url)

def download(a_url,n):#
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        # "cache-control": "max-age=0",#缓存时间，不要
        # "if-modified-since": "Wed, 25 Jun 2025 11:17:22 +0000",#请求头里有日期有时会有阻碍
        "priority": "u=0, i",
        "referer": "https://www.b31fa.icu/index/44045/",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
    }
    cookies = {
        "Hm_lvt_9c5f07b6ce20e3782eac91ed47d1421c": "1750995146",
        "HMACCOUNT": "C218DBB9B5B973C2",
        "Hm_lpvt_9c5f07b6ce20e3782eac91ed47d1421c": "1750996034"
    }
    response = session.get(url = a_url,headers = headers,cookies = cookies)
    r = response.content.decode("utf-8")
    soup = bs(r,"html.parser")#创建BeautifulSoup对象，   指定一个解析器
    texts = soup.select_one("#chaptercontent").decode_contents()#获取小说内容，以元素形式，包含页面所有内容 #  .decode_contents()适合单元素用法
    texts = texts.replace('<br/>','\n')
    with open(f'万相之王/第{n}.txt','w',encoding='utf-8') as f:
        f.write(texts)
def main():#定义主函数
    start = time.time()
    url_s()
    with ThreadPoolExecutor(max_workers=200) as executor:
        n = 1
        for a_url in urls:
            executor.submit(download,a_url,n)
            n += 1
    end = time.time()
    print(f'下载用时{end-start}s')
main()


