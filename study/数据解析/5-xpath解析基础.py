from lxml import etree

tree = etree.parse('test.html')
# r = tree.xpath('/html/body/div')
# r = tree.xpath('/html//div')
# r = tree.xpath('//div[@class="song"]')
# r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')[0]
# r = tree.xpath('//li[7]//text()')
r = tree.xpath('//div[@class="song"]//img/@src')[0]

print(r)









