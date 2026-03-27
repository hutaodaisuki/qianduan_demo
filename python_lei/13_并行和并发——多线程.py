import threading
import time
import random
def download(filename):
    start = time.time()
    print(f'开始打印{filename}')
    time.sleep(random.randint(1, 3))
    end = time.time()
    print(f"{filename}打印完毕")
    print(f"用时{end - start}s")
# 单线程 用时5s
def main():
    etart1 = time.time()
    download('makama')
    download('makaa')
    download('makaa')
    end1 = time.time()
    print(f"共用时{end1 - etart1}s")
main()
#多线程 用时3s
# def main():
#     threads = [#创建列表用于存放后续创建的线程单元
#         threading.Thread(target = download,args = ('filename1',)),#args是元祖，要加,!!!!
#         threading.Thread(target = download,args = ('filename2',)),
#         threading.Thread(target = download,args = ('filename3',))
#     ]
#     start = time.time()
#     for t in threads:
#         t.start()#开始线程
#     for t in threads:#将完成的线程加入等待，好捕捉总用时，实际操作时不用加
#         t.join()
#     end = time.time()
#     print(f"花费总时间{end - start}s")
# main()
