from playwright.sync_api import sync_playwright
import time
import pandas as pd
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://uland.taobao.com/sem/tbsearch?bc_fl_src=tbsite_T9W2LtnM&channelSrp=bingSomama&clk1=de9c12796a13ee55931e0c5833c72b09&commend=all&ie=utf8&initiative_id=tbindexz_20170306&localImgKey=&msclkid=7cf5012276f61e88f9206931259aba56&page=1&q=%E8%83%A1%E6%A1%83%E6%89%8B%E5%8A%9E&refpid=mm_2898300158_3078300397_115665800437&search_type=item&sourceId=tb.index&spm=tbpc.pc_sem_alimama%2Fa.201856.d13&ssid=s5-e&tab=all")
    for i in range(15):
        page.mouse.wheel(0,500)
        time.sleep(0.3)
    goods = page.locator('.CardV2--doubleCard--_OJ1T8j').all()#要加括号，不加括号导致goods被赋值为方法对象而不是列表
    good_infor_list = []
    print(len(goods))

    # good = goods[12]
    for good in goods:
        good_img = good.locator('.MainPic--mainPic--aVle5J9').get_attribute('src')
        good_name = good.locator('.Title--title--wJY8TeA ').inner_text()
        try:#要多观察页面结构，有时会因为一个小的不同而导致程序出错，在可疑的地方多用try方法可以使程序更健康
            good_range = good.locator('.Abstract--text--HIuCbR0').inner_text()
        except:
            good_range = '无范围'
        good_sprice1 = good.locator('.Price--priceInt--BXYeCOI').inner_text()
        good_sprice2 = good.locator('.Price--priceFloat--rI_BYho').inner_text()
        good_price = good_sprice1 + good_sprice2
        good_locations = good.locator('.Price--procity--Na1DQVe').all()#定位元素要加点，
        try:
            good_location2 = good_locations[1].inner_text()
        except:
            good_location2 = ""

        good_location1= good_locations[0].inner_text()
        good_location = good_location1 + good_location2
        good_seller = good.locator('.ShopInfo--shopNameText--kxQC2cC').inner_text()

        good_information = {
            '商品图片':good_img,
            '商品名称':good_name,
            '商品对象年龄':good_range,
            '商品价格':good_price,
            '商品产地':good_location
        }
        good_infor_list.append(good_information)
    hutao = pd.DataFrame(good_infor_list)
    hutao.to_excel('胡桃手办商品数据.xlsx')

    print('爬取完成')







    time.sleep(10000)