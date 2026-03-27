import requests as req
import json
import pandas as pd
list1 = []
r = req.get(url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20',headers ={
    'user-agent':'Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.2081 SLBChan/112 SLBVPV/64-bit'
})
res = r.content.decode('utf-8')
d = json.loads(res)
print(d)
for data in d :
    list1.append(data['cover_url'])
df = pd.DataFrame(list1)
df.to_excel("./img/1.xlsx")



#     with open('./img/img_5.str','w',encoding='utf-8') as f:
#
#         f.write(p)
# print('爬取完成')
#

# html文档  抖音  未成功
# import requests as req
# r = req.get(url=
# 'https://www.douyin.com/?recommend=1',headers={
# 'User-Agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.4011 SLBChan/ SLBVPV/64-bit'
# })#U-A校验   复制请求接口地址时要复制完整，另外要注意所获取的数据的 格式 以及 数据形式
# res = r.content.decode('utf-8')
# with open('./img/抖音.html','w',encoding='utf-8') as f:
#     f.write(res)
# print('爬取完毕')

#照片 抖音 火舞
# import requests as req
# r = req.get(url='https://p3-pc-sign.douyinpic.com/tos-cn-i-0813c001/osABFNOlAc72EeoBFuABoEIDRAwGoAJEf4f1b5~tplv-dy-cropcenter:323:430.jpeg?biz_tag=pcweb_cover&from=327834062&lk3s=138a59ce&s=PackSourceEnum_FAVORITE&sc=cover&se=true&sh=323_430&x-expires=2061597600&x-signature=7Nv2lkyXaRL%2FQO2aWvls7zXIXT8%3D',headers={
#     'User-Agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.4011 SLBChan/ SLBVPV/64-bit'
# })#U-A校验   复制请求接口地址时要复制完整，另外要注意所获取的数据的 格式 以及 数据形式
# res = r.content
# with open('./img/img_4.png','wb') as f:#图片格式的数据写入时用wb，是字节流数据
#     f.write(res)
#     print('爬取完毕')
#百度 html 成功
# import requests as req
# r = req.get(url=
# 'https://www.baidu.com/index.htm',headers={
# 'User-Agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.4011 SLBChan/ SLBVPV/64-bit'
# })#U-A校验   复制请求接口地址时要复制完整，另外要注意所获取的数据的 格式 以及 数据形式
# res = r.content.decode('utf-8')
# with open('./img/百度.html','w',encoding='utf-8') as f:
#     f.write(res)
# print('爬取完毕')




