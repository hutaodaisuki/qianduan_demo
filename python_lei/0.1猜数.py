# import random
# number=random.randint(1,100)
# guess=None
# tries=0
# print("欢迎来到猜数游戏，1到100之间，你不会不行吧?不会吧不会吧？")
# while guess != number:
#     try:
#         guess=int(input("请输入你的猜测，天才："))
#         tries +=1
#         if guess < number:
#          print("你猜的数跟你一样小，小笨蛋")
#         elif guess > number:
#           print("太大了，受不了的")
#         else:
#             print(f"你一定偷看答案了，竟然被你蒙对了,你一共猜了{tries}次")
#     except ValueError:
#         print("要的是整数哦，小笨蛋！")
#
# def fun(a,b):
#     sum = a+b
#     return sum    #将代码运算的值返回给外界       return还能够中断函数  return与break都是在循环里使用
# print(fun(2,3))

#while 循环
# i = 0
# while i < 10:
#     if i == 2 :
#
#         i += 1     #避免i一直等于2而陷入死循环
#         continue
#     print(i)
#     i += 1

#for循环
# for i in range(10):
#     if i == 2:
#         i+=1       #避免i=2而一直陷入死循环
#         continue
#     print(i)


dict1 = {
    '姓名':'zhangsan','年龄':'18'
}

print(dict1['姓名'],dict1['年龄'])
dict1['姓名'] = 'zhazhahui'#ctl+shift+上下键实现代码的换行
print(dict1['姓名'])






