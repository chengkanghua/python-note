from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r'./chromedriver')

driver.get('http://www.baidu.com')

driver.find_elements_by_xpath('//*[@id="s-usersetting-top"]')[0].click()
sleep(2)
# 点击搜索设置
driver.find_elements_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]')[0].click()
sleep(2)
# 选中每页显示50条
driver.find_elements_by_xpath('//*[@id="nr_3"]')[0].click()
# 确定
driver.find_elements_by_xpath('//*[@id="se-setting-7"]/a[2]')[0].click()

# 处理弹出的警告页面   确定accept() 和 取消dismiss()
# driver.switch_to_alert().accept()
driver.switch_to.alert.accept()

# 找到百度的输入框，并输入 美女
driver.find_element_by_id('kw').send_keys('美女')
sleep(2)
# 点击搜索按钮
driver.find_element_by_id('su').click()
sleep(2)
# 在打开的页面中找到“Selenium - 开源中国社区”，并打开这个页面
driver.find_elements_by_link_text('美女 - 百度图片')[0].click()
sleep(3)
# 关闭浏览器
driver.quit()