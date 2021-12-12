from selenium import webdriver
from time import sleep
#导入动作链对应的类
from selenium.webdriver import ActionChains
bro = webdriver.Chrome(executable_path=r'./chromedriver')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

#如果定位的标签是存在于iframe标签之中的则必须通过如下操作在进行标签定位
bro.switch_to.frame('iframeResult')#切换浏览器标签定位的作用域   # iframeResult 是iframe框架的id
div1 = bro.find_element_by_id('draggable')
div2 = bro.find_element_by_id('droppable')
#动作链
action = ActionChains(bro)
#点击长按指定的标签
# action.click_and_hold(div)
action.drag_and_drop(div1, div2).perform()  # 从div1 拖动到div2 位置执行

sleep(2)
bro.switch_to.alert.accept()
# for i in range(5):
#     #perform()立即执行动作链操作
#     #move_by_offset(x,y):x水平方向 y竖直方向
#     action.move_by_offset(17,0).perform()
#     sleep(0.5)
#
#
# #释放动作链
# action.release()