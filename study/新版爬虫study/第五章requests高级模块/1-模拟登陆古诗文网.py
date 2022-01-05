import requests
from lxml import etree
from hashlib import md5
# 超级鹰
class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

#1.对验证码图片进行捕获和识别
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

#https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx
#模拟登录：验证码的识别，动态参数的处理，cookie相关的操作处理
s = requests.Session()
#1.验证码图片爬取到本地进行存储
url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
page_text = s.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
img_src = 'https://so.gushiwen.org'+tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = s.get(url=img_src,headers=headers).content
with open('./gushiwen.jpg','wb') as fp:
    fp.write(img_data)

#解析动态参数
__VIEWSTATE = tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
__VIEWSTATEGENERATOR = tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]

#将验证码图片提交给打码平台进行识别
chaojiying = Chaojiying_Client('user', 'pwd', 'software_id')
im = open('gushiwen.jpg', 'rb').read()
code_text = chaojiying.PostPic(im, 1902)
print(code_text)

#模拟登录
post_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
data = {
    #前两个参数是动态参数
    '__VIEWSTATE': __VIEWSTATE,
    '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.org/user/collect.aspx',
    'email': '18679816495',
    'pwd': 'ckh1234561112',
    'code': code_text['pic_str'],
    'denglu': '登录',
}
#s表示的session中已经存储了相关的cookie
response = s.post(url=post_url,data=data,headers=headers)
page_text = response.text
print(response.status_code)
with open('./gushiwenwang.html','w',encoding='utf-8') as fp:
    fp.write(page_text)