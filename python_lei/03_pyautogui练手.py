import pyautogui as pag

pag.moveTo(x=30,y=800)
pag.click(clicks=2)
pag.sleep(2)
pag.write('doyin')
pag.press('1')
pag.press('enter')
pag.moveTo(x=500,y=550)
pag.sleep(1)
pag.click(clicks=1)
pag.sleep(2)
# pag.moveRel(x=500,y=500)#代码无效果，可能是小窗口坐标错乱
pag.moveTo(x=450,y=300)
pag.click(clicks=1)
pag.press('backspace')
pag.press('backspace')
pag.write('ABCD')
pag.sleep(1)
pag.press('enter')
pag.press('enter')
pag.sleep(1)
pag.moveTo(x=500,y=700)
pag.sleep(1)
pag.click(clicks=2)



