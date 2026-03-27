import random
import pyautogui as pag
import pyperclip as pc #输入中文
pag.PAUSE=0.5
class Wx:
    def __init__(self):
        # self.position =(500,500)#初始位置
        # self.check_msg()#检测消息图标
        # self.click_msg()#点进输入框
        # self.send_msg()#发送消息
        # self.auto_msg()
        self.messages=['在忙！','实验成功！','在学习，勿扰！','在打游戏，勿扰！','稍后回复']
        self.text=''
    def auto_msg(self):
        while True:
            if self.check_msg():#检测新消息
                self.click_msg()
                self.send_msg()
                print('有新消息')
            else:
                print('没有新消息')
                pag.sleep(1)
    def check_msg(self):
        try:
            self.position = pag.locateCenterOnScreen('img/img_2.png', confidence=0.7)
            return True
        except pag.ImageNotFoundException:
            return False
    def click_msg(self):
        pag.moveTo(self.position)
        pag.click()
        pag.sleep(1)
        position2 = pag.locateCenterOnScreen('img/img_1.png', confidence=0.8)
        pag.moveTo(position2)
        pag.click()
    def send_msg(self):
        self.text = random.choice(self.messages)
        pc.copy(self.text)
        pag.hotkey('ctrl','v')
        pag.hotkey('Alt','s')

wx=Wx()
wx.auto_msg()

# import pyautogui as pg
# class Douy():
#     def __init__(self):
#         self.position=(0,0)
#
#
#
#
#     def move(self):
#         position = pg.locateCenterOnScreen('./img/img.png',confidence=0.8)#文件相对位置
#         pg.PAUSE = 1
#         pg.moveTo(position)
#         pg.click(clicks=2)
#         pg.sleep(1)
#         position2 = pg.locateCenterOnScreen('./img/img_3.png', confidence=0.8)
#         pg.moveTo(position2)
#         pg.click(clicks=1)
#
#
#
#
# WX = Douy()
# WX.move()