import time
import pandas as pd
from playwright.sync_api import sync_playwright#局部调用
goods_infor_lists = []
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)#默认是无头模式，即后台运行，输入False使网页显示
    page = browser.new_page()
    page.goto("https://ads.taobao.com/sem?bc_fl_src=tbsite_PpawhTGY&channelSrp=tbsy-lianxiang&commend=all&ie=utf8&initiative_id=tbindexz_20170306&localImgKey=&page=1&q=%E8%83%A1%E6%A1%83&search_type=item&sourceId=tb.index&spm=tbpc.pc_sem%2Fa.201856.d13_manual&ssid=s5-e&tab=all")
    for i in range (15):
        page.mouse.wheel(0,500)
        time.sleep(0.3)
    goods = page.locator('.doubleCard--U4iHXoyX').all()



    # good = goods[0]
    for good in goods:
        good_png = good.locator('.mainPic--CuSfUC4j').get_attribute('src')
        # print(good_png)
        good_name = good.locator('.title--F6pvp_RZ').inner_text()
        # print(good_name)

        good_price1 = good.locator('.priceInt--j47mhkXk').inner_text()
        good_price2 = good.locator('.priceFloat--zPTqSZZJ').inner_text()
        good_price = good_price1 + good_price2
        # print(good_price)
        good_address = good.locator('.procity--QyzqB59i').all()  # 类的定位要加  . !!
        good_address1 = good_address[0].inner_text()
        try:
            good_address2 = good_address[1].inner_text()
        except:
            good_address2 = ""
        # print(good_address1,good_address2)
        good_title = good.locator('.subIconWrapper--KnkgUW0R').inner_text()
        # print(good_title)
        good_seller = good.locator('.shopName--bg5aFTrf').inner_text()
        # print(good_seller)
        good_information = {
            '商品图片': good_png,
            '商品名称': good_name,
            '商品价格': good_price,
            '商品发货地址': good_address,
            '商品标题': good_title,
            '商品供货方': good_seller
        }
    # print(good_information)
        goods_infor_lists.append(good_information)
    print('爬取完毕！')
    # for info in goods_infor_lists:#缩进问题导致无法遍历
    #     print(info)

    df = pd.DataFrame(goods_infor_lists)
    df.to_excel("商品数据.xlsx")
    # print("数据保存完毕！")



    # print(len(goods))
    time.sleep(10000)
