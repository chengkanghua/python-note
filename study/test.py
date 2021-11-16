import re

if re.match('^/customer/edit/(?P<cid>\d+)/$','/customer/edit/20/'): # 匹配成功
    print('匹配成功')
else:
    print('匹配失败')
# if re.match('^/payment/edit/(<?P<pid>\d+)/$','/payment/edit/13/'): # 匹配失败
#     print('匹配成功')
# else:
#     print('匹配失败')