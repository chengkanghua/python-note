import requests
from lxml import etree

# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
# }
# url = 'https://bj.58.com/ershoufang/'

# path_text = requests.get(url=url,headers=headers).text
# # tree = etree.HTML(path_text)
# fp = open('58.html','w',encoding='utf-8')
# fp.write(path_text)
# fp.close()


tree = etree.parse('58.html',etree.HTMLParser())

# 存储的就是li标签对象
li_list = tree.xpath('//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')

# strTitle = etree.tostring(tree, encoding = "utf-8").decode("utf-8") # encoding和decode一个都不能少。
# print(strTitle)

fp = open('58.txt', 'w', encoding='utf-8')
for li in li_list:
    # 局部解析
    title = li.xpath('./a/div[2]/div[1]/div[1]/h3/text()')[0]
    print(title)
    # title = etree.tostring(title, encoding="utf-8").decode("utf-8")  # encoding和decode一个都不能少。
    # print(title)
    fp.write(title + '\n')
