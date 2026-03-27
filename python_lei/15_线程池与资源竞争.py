# from concurrent.futures import ThreadPoolExecutor#导入线程池执行器
# import time
# import threading
# def func1(n):#定义一个任务函数
#     print(f'任务{n}开始')
#     time.sleep(0.1)
#     print(f'任务{n}结束')
# with ThreadPoolExecutor(max_workers=5) as executor:#创建线程池，并规定最大线程数为5
#     futures = []
#     for i in range(100):
#         futures.append(executor.submit(func1, i))#提交任务给线程池，（任务函数，传参（可以多个））
#     for future in futures:#注意缩进问题，缩进错了变成了顺序执行！！！
#         future.result()#阻塞当前任务，等待所有任务的完成并获取返回值
# print('任务执行完毕')


# #守护线程：在主线程结束后，不再去保留其余子线程
# #默认情况下，主线程结束后，不会去结束未完成的子线程（非守护线程）
# import threading
# import time
# def func(content):
#     while True:
#         print(content,end = '',flush=True) # ,不换行，强制刷新缓冲区，确保数据立即写入目标位置
#         time.sleep(0.1)
# threading.Thread(target=func,args=("胡桃",)).start()
# threading.Thread(target=func,args=("申鹤",)).start()
# print('任务结束')#主线程结束，子线程仍在执行

# import threading
# import time
# def func(content):
#     while True:
#         print(content,end = '',flush=True) # ,不换行，强制刷新缓冲区，确保数据立即写入目标位置
#         time.sleep(0.1)
# threading.Thread(target=func,args=("胡桃",),daemon = True).start()
# threading.Thread(target=func,args=("申鹤",),daemon = True).start()
# print('任务结束')#主线程结束，子线程被终止

#资源竞争：在编写多线程任务时，不可避免的会出现多个线程竞争同一个资源的情况，可能使结果与预期不符
import threading
import time
from concurrent.futures import ThreadPoolExecutor#导入线程池执行器
# class Account:#创建一个账户类，模拟银行存款
#     def __init__(self):
#         self.balance = 0
#
#     def deposit(self,money):#模拟存钱
#         # self.balance += money    # 此方法得出的结果为100，没有受影响 第二段代码的复合操作在Python字节码层面是原子的（虽然文档不保证这一点）
#         new_balance = self.balance + money#第一段代码将操作拆分成多个步骤并加入了延迟，放大了竞争窗口
#         time.sleep(0.01) #模拟操作延时
#         self.balance = new_balance
#     def main(self):
#         with ThreadPoolExecutor(max_workers=30) as executor:
#             # excutors = []
#             for i in range(100):
#                 executor.submit(self.deposit,1)
#                 # excutors.append(executor.submit(self.deposit,1))
#         print(self.balance)
#
# acconut = Account()
# acconut.main()

#改进
'''
如果要确保线程安全，推荐的做法是：
使用threading.Lock进行显式同步
或者使用+=这类原子操作（在CPython中有效，但不是所有Python实现都保证）
避免在非原子操作中间插入可能引起线程切换的操作（如I/O、sleep等）
'''
# #锁机制
# #threading提供了相应锁机制 -----RLock
# import time
# from threading import RLock
# from concurrent.futures import ThreadPoolExecutor
# #面向对象
# class Account:
#     def __init__(self):
#         self.lock = RLock()
#         self.balance = 0
#     def deposit(self, money):
#         self.lock.acquire()#上锁，保护下面数据的线程安全
#         new_balance = self.balance + money
#         time.sleep(0.01)
#         self.balance = new_balance
#         self.lock.release()#释放锁，以便后续代码对数据进行操作
#     def main(self):
#         for i in range(100):
#             with ThreadPoolExecutor(max_workers=30) as executor:
#                 executor.submit(self.deposit, 1)
#         print(self.balance)
# account1 = Account()#创建实例
# account1.main()

#作业  多线程 线程池 的方式爬取豆瓣电影海报100部
# import threading
import requests as req
import pandas as pd

import json
from concurrent.futures import ThreadPoolExecutor
import threading
def download(n):#定义任务函数，来下载海报链接地址
    headers1 = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "priority": "u=1, i",
        "referer": "https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
        "x-requested-with": "XMLHttpRequest"
    }
    # list1 = [0,20,40,60,80]#  海报数据存储在列表中，数据类型为json数据 看似是列表，但类型却显示str
    # for n in list1:  n传参，代表不同页面开始的电影序号
    url1 = f'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={n}&limit=20'


    response = req.get(url =url1,headers = headers1)
    r = response.content.decode('utf-8')
    r1 = json.loads(r)#反序列化（json转python）    json.dumps(n)序列化（python 转 json)
    # print(type(r1)) #反序列化处理后，类型由 str 变为 list
    list2 = []
    list3 = []
    for i in r1:#因为列表里套字典，所以i代表的就是字典，不能作为索引！！！
        list2.append(i["cover_url"])#列表里套的字典,i此时就是字典
        list3.append(list2)
    r = pd.DataFrame(list3)
    r.to_excel('./img/豆瓣电影海报链接.xlsx')

#多线程同时写入同一个Excel文件会导致数据错乱
#线程池
with ThreadPoolExecutor(max_workers=10) as executor:#创建线程池
    list1 = [0,20,40,60,80]
    for n in list1:
     executor.submit(download,n)

#自己创建线程
# threads = []
# threads.append(threading.Thread(target=download,args=(0,)))
# threads.append(threading.Thread(target=download,args=(20,)))
# threads.append(threading.Thread(target=download,args=(40,)))
# threads.append(threading.Thread(target=download,args=(60,)))
# threads.append(threading.Thread(target=download,args=(80,)))
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
print('下载完毕')















