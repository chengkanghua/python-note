import jwt

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.exceptions import NotAuthenticated
from django.conf import settings
from .. import return_code

from corsheaders.middleware import CorsMiddleware


class CurrentUser(object):
    def __init__(self, user_id, username, exp):
        self.user_id = user_id
        self.username = username
        self.exp = exp


class MtbAuthenticationFailed(AuthenticationFailed):
    status_code = 200


class JwtTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # OPTIONS
        # 读取用户提交的jwt token
        # token = request.query_params.get("token")
        # 去请求头获取 Authorization: 401f7ac837da42b97f613d789819ff93537bee6a
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            # 状态码=>401 ，内容=>{code:2000,error:"认证失败"}
            raise AuthenticationFailed({"code": return_code.AUTH_FAILED, "error": "认证失败"})

            # 状态码=>200 ，内容=>{code:2000,error:"认证失败"}
            # raise MtbAuthenticationFailed({"code": return_code.AUTH_FAILED, "error": "认证失败"})

        # jwt token校验
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, ["HS256"])
            # {'user_id': 1, 'username': 'wupeiqi', 'exp': 1648309198}
            # print(payload, type(payload))
            return CurrentUser(**payload), token
        except Exception as e:
            # 状态码=>200 ，内容=>{code:2000,error:"认证失败"}
            raise MtbAuthenticationFailed({"code": return_code.AUTH_FAILED, "error": "认证失败"})

    def authenticate_header(self, request):
        return 'Bearer realm="API"'


class ParamsJwtTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        if not token:
            # 状态码=>401 ，内容=>{code:2000,error:"认证失败"}
            raise AuthenticationFailed({"code": return_code.AUTH_FAILED, "error": "认证失败"})

            # 状态码=>200 ，内容=>{code:2000,error:"认证失败"}
            # raise MtbAuthenticationFailed({"code": return_code.AUTH_FAILED, "error": "认证失败"})

        # jwt token校验
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, ["HS256"])
            # {'user_id': 1, 'username': 'wupeiqi', 'exp': 1648309198}
            # print(payload, type(payload))
            return CurrentUser(**payload), token
        except Exception as e:
            # 状态码=>200 ，内容=>{code:2000,error:"认证失败"}
            raise MtbAuthenticationFailed({"code": return_code.AUTH_FAILED, "error": "认证失败"})

    def authenticate_header(self, request):
        return 'Bearer realm="API"'
