import time
from playwright.sync_api import sync_playwright


# with sync_playwright() as p:#完成初始化并返回一个包含浏览器操作相关功能的对象（赋值给p）,离开with代码块时会释放playwright相关资源，关闭浏览器
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.baidu.com")
#
#     input_item = page.locator('#kw')#定位页面元素，返回一个locator对象
#     src_item = page.locator('#su')
#     input_item.fill('全国有多少个名字叫张嘉辉的')
#     src_item.click()
#     for i in range(0,11):
#         page.mouse.wheel(0,200)
#         time.sleep(0.5)
#
#
#     time.sleep(10)



# import pyautogui as pg
# import time
# import pyperclip as pc
# pg.PAUSE = 0.1
# pg.press('win')
# pc.copy('百度一下')
# pg.hotkey('ctrl', 'v')
# pg.press('enter',1)#不加次数默认1次
# time.sleep(1)
# pc.copy('全国有多少个名字叫张嘉辉的')
# pg.hotkey('ctrl', 'v')
# pg.press('enter')
# for i in range(4):
#     pg.scroll(-500)
#     time.sleep(1)

from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.baidu.com")
    title_item = page.locator(".title-content-title").all()#获取所有匹配元素并将他们以列表的形式返回
    for title in title_item:
        print(title.inner_text())#元素的一个方法，获取元素内部的文本内容,<>xxxxx</>（不包含子元素的标签，但包含子元素的文本）



    time.sleep(10000)#不能顶格，要被with模块包裹，注意缩进