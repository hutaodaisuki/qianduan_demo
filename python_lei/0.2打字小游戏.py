import time
import random
# class Game:
#     def __init__(self,words):#words:从外部传入参数，下面的则是程序运行过程中程序自身产生的！所以加入  words是传递实际参数的，self是
#         #形式参数
#         self.words = words
#         self.gameword=''
#         self.userword = ''
#         self.start_time =0
#         self.over_time =0
#         self.spend_time =0
#         self.acc =0
#         self.speed=0
# #上面是属性，下面是行为，方法
#
#     def show(self):#show 是方法
#         self.gameword=random.choice(self.words)
#         print(f'game starting,the password is: {self.gameword}')#f加{}可以在字符串中插入参数
#     def play(self):
#         self.start_time = int(time.time())
#         self.userword = input('enter your word:')
#         self.over_time = int(time.time())
#         self.spend_time = self.over_time - self.start_time
#         # return self.spend_time#代码实际运行时不显示花费时间，原因是没有变量接受返回值，返回值没有被存储
#         print(f'打字速度{self.spend_time}s')
#         # for i in range(len(self.)):
#     def eval (self):
#         true_num = 0
#         for i in range(len(self.userword)):    #字符串下标从0开始
#             if i < len(self.userword):
#                 if self.userword[i] == self.gameword[i]:   #计算正确字母个数
#                     true_num += 1
#             else:
#                 break   #退出for循环
#         self.acc = round (true_num / len(self.userword),2)
#         self.speed = len(self.userword)/self.spend_time
#         print(f'准确率{self.acc}')
#     def over (self):
#         print(f'game starting,the password is: {self.gameword}')
#         print(f'花费时间{self.spend_time}s')
#         print(f'准确率{self.acc}')
#         print(f'打字速度{self.speed}/s')
#
#
#
# #调用 类
# Play = Game(['Gay','Sex','Jocker','Passenger','Tower','Tokyohot'])
# Play.show()
# Play.play()
# Play.eval()
# Play.over()
import time
import random
class Game:
    def __init__(self):
        self.score = 0
        self.starttime = 0
        self.overtime = 0
        self.gameword = ''
        self.guessword = ''
        self.usetime = 0


    def show(self):
        gameword1 = ['sex','bitch','Fuck','stupid cunt','silly dog']
        self.gameword = random.choice(gameword1)
        print(f'本局游戏单词为:{self.gameword}')
        self.starttime = time.time()
        self.guessword = input('请输入：')
        self.overtime = time.time()
        use_time = self.overtime - self.starttime
        self.usetime = int(use_time)
        print(f'花费时间:{self.usetime}s')

    def num(self):
        try:
            if len(self.guessword) <= len(self.gameword):
                for i in range(len(self.guessword)):
                    if self.guessword[i] == self.gameword[i]:
                        self.score += 1
                        score = (self.score / len(self.gameword)) * 100
            print(f'得分为:{score}')  # 缩进不同影响print执行次数
        except:
            print('作弊可耻!!!!!!')




























Game1 = Game()#调用类不能把类的实例方法当成普通函数调用，需要先创建类的实例，再通过实例调用方法！！！
Game1.show()
Game1.num()
