import pandas as pd
# print(pd.__version__)
# data1 = [10,20,30.0,40,50,60,70,80,'kabf']
# print(type(data1))
# data2 = pd.Series(data1)#数据方向上是纵向的
#
# print(type(data2))#dtype数据类型：int64,float61,bool,object,datatime64
#
# print(data2)#查看整体数据
#
# #查看某一项数据，利用下标值
# print(data2[0])
#
# #查看多个值，以区间的方式
# print(data2[0:3])#前闭后开
#
# #计算能力  矩阵型计算
# # print(data2+30)#每个值都加30
#
# # print(data2.sum())#针对整体求和
# # print(data2.mean())#求平均值
# # print(data2.median())#求中位数
# # print(data2.max())#求最大值
# # print(data2.min())#求最小值
#
# print(data2.dtype)#查看数据类型  Series没有dtypes属性 dtype关注的是单个数据类型，dtypes更多用于查看和处理多个数据类型的集合
# #Series混合数据类型的dtype确定原则是选择经量能兼容所有数据类型的最小公共类型
#
# print(data2.shape)#输出(9,)查看数据形状 元组 9行，此时一维数据没有列的存在， 加逗号是为了体现他是元组
# print(data2.size)#查看数据大小
# print(data2.head(5))#前5行数据
# print(data2.tail(5))#后五行数据
# # data3 = data2.astype('float')#会报错，无法将str强制转换成float
# data3 = data2.astype('object')

#DataFrame
dict1 = {
    "a":[1,2,3],
    "b":[4,None,6],
    "c":[7,8,9]
}
df = pd.DataFrame(dict1)
print(df.dtypes)
print(df.describe())#获取数据集中每列的一些基本统计信息count（计数）mean(均值) std(标准差)  min max 四分位数（25% 50% 75%）
print(df.info())#查看数据相关信息
# print(df.head(1))#查看第一行数据
# print(df.tail(1))#查看最后一行数据
print(df["a"])#查看具体某列数据

#替换某行数据
df["a"] = [100,200,300]
print(df)
print(df.size)#数据大小
print(df.shape)#数据形状

#数据的清洗
#表中有缺失值
print(df.isnull().sum())#查看是否有缺失值并统计缺失值个数
#填充缺失值
print(df.fillna(0))#将缺失值用传参代替
#删除缺失值所在的行
df = df.dropna()#调方法带括号
print(df)