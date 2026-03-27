#胎死腹中，因为有人机验证
from playwright.sync_api import sync_playwright as p
import time
with p() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()#确保page被正确初始化为playwright的page对象！！！
    page.goto("https://stuonline.zhihuishu.com/stuonline/teachMeeting/stuListV2?recruitId=304939")
    time.sleep(3)
    name_item = page.locator('#lUsername')
    name_item.fill('18606150867')
    password_item = page.locator('#lPassword')
    password_item.fill('Yyh12345678')
    # click_button = page.locator('.wall-sub-btn')
    # click_button.click()




    time.sleep(1000000000)



