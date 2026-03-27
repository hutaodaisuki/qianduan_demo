import pandas as pd
import matplotlib.pyplot as plt
#链式调用
#数据处理   数据分析（价值）  通过数据分析的结果，将结果展示（数据可视化）
#加载数据源
df = pd.read_excel('./工作簿1.xlsx')#  ./表示当前目录
print(df.describe())#调方法，查看基础信息
#查看数据情况以及类型
print(df.dtypes)
print(type(df))
#为了性能，可查看数据的前后几行
print(df.head(5))
print(df.tail(5))
print(df.info())#查看数据表的整体信息
#查看数据缺失值
print(df.isnull().sum())#查看缺失值并统计
print(df.shape)#14行4列
print(df.size)#56个有效数据

#对分数的大小排序
print(df.sort_values(by = '分数',ascending=False))#对指定字段排序，默认升序，加参数ascending = False 则为降序
#取最高分
print(df.sort_values(by = '分数',ascending=False).head(1))
#最低分
print(df.sort_values(by = '分数',ascending=False).tail(1))
#query 条件查询
print(df.query('分数>=60').sort_values(by = '分数',ascending=False))
#语文最高分
print(df.query('分数>=60 and 科目 == "语文"').sort_values(by = ['分数','班级'],ascending=False))#by值后面可以跟列表，以多个字段排序
#计算一班语文总分
print(df.query('班级 == "一班" and 科目 == "语文"')['分数'].sum())


#分组和聚合运算
#分组  将一张完整的表数据进行分组分类 划分出子表
#聚合运算 分别再去统计子表的数据  最终汇总得到数据分析统计的结果
#求各班语文成绩总分
print(df.query('科目 == "语文"').groupby(by='班级')['分数'].sum())

#各科目总分
print(df.groupby(by='科目')['分数'].sum())

#数据可视化
dt1 = df.groupby(by='科目')['分数'].sum()#各科总分
plt.rcParams['font.sans-serif'] = ['SimHei']#解决画布支持中文问题
dt1.plot(kind='bar')#bar是柱状图
#完善绘图信息
plt.title('各科目总分')
plt.xlabel('科目')
plt.ylabel('分数')
plt.show()