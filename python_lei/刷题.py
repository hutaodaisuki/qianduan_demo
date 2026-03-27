# import math
# r = float(input('半径为:'))
# s = math.pi * r ** 2
# print(f'圆的面积为：{s}')



# x = input('请输入：')
# list2 = list(x)
# list1 = list2[::-1]
# print(list1)



# for x in range(1,10):
#     for y in range(1,x+1):
#         print(f"{y}*{x}={x*y}",end="\t")
#     print()#在内层循环结束后执行这行代码进行换行



# list1 = [10,20,30,40,50]
# x = eval(input('请输入：'))
#
# if x in list1:
#     print('在')
# else:
#     print('不在')

#计算自幂数（五角星数
# for n in range (10000,100000):
#     a = n//10000
#     b = (n-a*10000)//1000
#     c = (n-a*10000-b*1000)//100
#     d = (n-a*10000-b*1000-c*100)//10
#     e = (n-a*10000-b*1000-c*100-d*10)
#     if n == a ** 5 + b ** 5 + c ** 5 + d ** 5 + e ** 5:
#         print(n)
#改进
# for i in range(10000,100000):
#     n = str(i)
#     x = [int(a)**5 for a in n]
#     if i == sum(x):
#         print(i)
#推广
# def Num(w):
#     for i in range(10**(w-1),10**w):
#         s = str(i)
#         x = [int(a)**w for a in s]
#         if i == sum(x):
#             yield i  #关键字，用于生成器函数，yield会暂停函数执行，保存函数状态，下次调用从暂停处执行，返回值会被传递给迭代的上下文，如for中的i
#             # print(f'{w}位自幂数是：{i}')
# print(list(Num(3)))
# print(list(Num(4)))
# print(list(Num(5)))

# num1 =Num(3)
# num2 =Num(4)
# num3 =Num(5)

# import time as ti
# import turtle as t
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.lt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.lt(180)
# t.up()
# t.fd(20)
#
# ti.sleep(10000)
s = ['python']
print(s[0:3])#输出结果为['python']，因为列表里'python'为一个元素
print(s[0][0:3])#输出为pyt,涉及两层操作，外层与内层   [start:stop:step]


'''
字符串的格式化   %s字符串占位   %d整数占位   %f浮点数占位
%m.nf    m为宽度，  .n为小数位数，会对相应位数四舍五入 最后f表示浮点数
字符串类型之间才能拼接
字符串的快速格式化：f"{变量}" #不限制类型 

'''
