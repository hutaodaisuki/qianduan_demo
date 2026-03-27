# #模拟单线程  顺序执行
# import time
# import random
# #创建一个任务
# def download(filename):#传入形参  下载的文件名
#     start = time.time()
#     print(f"文件{filename}下载完成"  )
#     t = random.randint(1,3)
#     time.sleep(t)
#     end = time.time()
#     print(f'花费时间{round(end-start)}s')
# def main():#创建实例
#     start = time.time()
#     download('胡桃1')
#     download('胡桃2')
#     download('胡桃3')
#     end = time.time()
#     spend = end - start
#     print('下载完成，共用时{}s'.format(spend))
# main()

# #模拟多线程
# import threading
# import time
# import random
# #创建一个可执行任务
# def download(filename):#传入形参  下载的文件名
#     start = time.time()
#     print(f"文件{filename}下载完成"  )
#     t = random.randint(1,3)
#     time.sleep(t)
#     end = time.time()
#     print(f'花费时间{round(end-start)}s')
# def main():
#     threadings = [
#         threading.Thread(target=download,args=('胡桃1',)),#args跟的是元组，可以传多个参数，要加逗号，跟括号区分开来
#         threading.Thread(target=download,args=('胡桃2',)),
#         threading.Thread(target=download,args=('胡桃3',))
#     ]
#     start = time.time()
#     for thread in threadings:
#
#         thread.start()
#     for thread in threadings:
#         thread.join()
#     end = time.time()
#     print(f'共用时{end - start}s')
# main()
#实例
#单线程
# import requests as rq
# import time
# #创建url列表
# urls = []
# for i in range(1,101):
#     urls.append(f'https://www.cnblogs.com/#p{i}')
# def download():
#     start = time.time()
#     for url in urls:
#         r = rq.get(url)
#         print(url,len(r.content))
#     end = time.time()
#     print(f"共用时{end-start}s")#19s
# download()
#多线程实例
import requests as rq
import time
import threading
#创建url列表
urls = []
for i in range(1,101):
    urls.append(f'https://www.cnblogs.com/#p{i}')
def download(url):

    r = rq.get(url)
    print(url,len(r.content))
threads = []
for url in urls:
    threads.append(threading.Thread(target=download, args=(url,)))



start = time.time()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
end = time.time()
print('下载完成，共用时{}'.format(end-start))#共用时5s
