import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('./工作簿1.xlsx')
#解决画布中文问题
plt.rcParams['font.sans-serif'] = ['SimHei']
dt1 = df.groupby(by=['班级','科目'])['分数'].agg(['sum','mean']).unstack()#agg是一个用于数据聚合的函数可以对数据框或分组后的数据进行多种聚合操作
print(dt1)

dt1.plot(kind='bar',width=0.6)#bar为柱状图
# plt.title('各班各成绩总和')
plt.xlabel('班级')
plt.tight_layout()#图形尺寸过小，或者matplotlib自动布局时因空间不足舍弃了部份下标显示，调用该方法可调整布局
plt.show()