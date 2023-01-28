from urllib.request import urlopen
from django.conf import settings
from urllib.parse import urlencode, parse_qs
import logging
import json

logger =logging.getLogger("django")

class OAuthQQError(Exception):
    pass

class OAuthQQ(object):
    """QQ第三方登录的辅助类"""
    def __init__(self, app_id=None, app_key=None, redirect_uri=None, state=None):
        self.app_id = app_id or settings.QQ_APP_ID     # 应用ID
        self.app_key = app_key or settings.QQ_APP_KEY  #　应用秘钥　
        self.redirect_url = redirect_uri or settings.QQ_REDIRECT_URL # 回调域名
        self.state = state or settings.QQ_STATE  # 用于保存登录成功后的跳转页面路径

    def get_auth_url(self):
        """生成QQ第三方登录的链接"""
        params = {
            'response_type': 'code', # 授权类型
            'client_id': self.app_id,
            'redirect_uri': self.redirect_url, # 回调域名
            'state': self.state,     # 自定义状态
            'scope': 'get_user_info', # 可选，可以不填
        }

        url = 'https://graph.qq.com/oauth2.0/authorize?' + urlencode(params)

        return url

    def get_access_token(self,code):
        """通过授权码获取临时票据access_token"""
        params = {
            'grant_type': 'authorization_code',
            'client_id': self.app_id,
            'client_secret': self.app_key,
            'redirect_uri': self.redirect_url,
            'code': code,
        }
        # urlencode 把字典转换成查询字符串的格式
        url = 'https://graph.qq.com/oauth2.0/token?' + urlencode(params)
        try:
            response = urlopen(url)
            response_data = response.read().decode()
            # parse_qs　把查询字符串格式的内容转换成字典[注意：转换后的字典，值是列表格式]
            data = parse_qs(response_data)
            access_token = data.get('access_token')[0]
        except:
            logger.error('code=%s msg=%s' % (data.get('code'), data.get('msg')))
            raise OAuthQQError

        return access_token

    def get_open_id(self,access_token):
        """根据access_token获取openID"""
        url = 'https://graph.qq.com/oauth2.0/me?access_token=' + access_token
        try:
            response = urlopen(url)
            response_data = response.read().decode()
            data = json.loads(response_data[10:-4])
            openid = data.get('openid')
        except:
            logger.error('code=%s msg=%s' % (data.get('code'), data.get('msg')))
            raise OAuthQQError

        return openid

    def get_qq_user_info(self, access_token, openid):
        params = {
            'access_token': access_token,
            'oauth_consumer_key': self.app_id,
            'openid': openid,
        }
        url = 'https://graph.qq.com/user/get_user_info?' + urlencode(params)
        try:
            response = urlopen(url)
            response_data = response.read().decode()
            data = json.loads(response_data)
            return data
        except:
            logger.error('code=%s msg=%s' % (data.get('code'), data.get('msg')))
            raise OAuthQQError