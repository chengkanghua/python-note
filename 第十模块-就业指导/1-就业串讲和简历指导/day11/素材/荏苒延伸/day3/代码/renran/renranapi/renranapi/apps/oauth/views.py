from rest_framework.views import APIView
from .utils import OAuthQQ,OAuthQQError
from rest_framework.response import Response
from .models import OAuthUser

class OAuthQQAPIView(APIView):
    def get(self, request):
        """生成QQ登录的地址"""
        state = request.query_params.get('state') # 客户端指定的状态
        oauth = OAuthQQ(state=state)
        url = oauth.get_auth_url()
        print(url)
        return Response(url)

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadData
from django.conf import settings
from renranapi.settings import constants
class QQInfoAPIView(APIView):
    def get(self,request):
        """获取QQ用户的信息"""
        # 1. 获取客户端转发过来的QQ登录授权码
        code = request.query_params.get("code")
        state = request.query_params.get('state')  # 客户端指定的状态
        if not code:
            return Response("QQ登录异常！请重新尝试登录！")

        oauth = OAuthQQ(state=state)
        try:
            # 2. 根据授权码到QQ服务器获取access_token
            access_token = oauth.get_access_token(code)
            # 3. 根据access_token获取用户信息[openID]
            openid = oauth.get_open_id(access_token)
            # 3.1 获取用户信息
            user_info = oauth.get_qq_user_info(access_token,openid)
            print(user_info)
            # 4F65D2442D41B0D1639FD7FC14123B11

        except OAuthQQError:
            return Response("QQ登录异常！获取授权信息失败！请重新尝试登录！")

        # 4. 根据openID到数据库中查询用户判断是否属于第一次使用QQ登录
        try:
            oauth_qq_user = OAuthUser.objects.get(openid=openid)
            # 查找到对应的用户记录，证明用户创建我们网站的账号并且已经关联了QQ的openID
            user = oauth_qq_user.user
            # 生成jwt登录token
            from rest_framework_jwt.settings import api_settings
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            user_info = {
                "token":token,
                "id":user.id,
                "username":user.username,
                "avatar":user.avatar.url if user.avatar else "",
                "nickname":user.nickname,
            }
            return Response({"user_info": user_info,"status": 1})
        except OAuthUser.DoesNotExist:
            # 查找不到对应的用户记录，用户属于第一次使用QQ登录
            # 使用itsdangrous对数据进行加密
            serializer = Serializer(settings.SECRET_KEY, constants.DATA_SIGNATURE_EXPIRE)
            data = serializer.dumps({"openid": openid}).decode()
            return Response({
                "avatar": user_info.get("figureurl_qq_1"),
                "nickname": user_info.get("nickname"),
                "data": data,
                "status": 0,
            })


from rest_framework import status as http_status
from users.utils import UsernameMobileAuthBackend
from .models import OAuthUser
from users.models import User

class BindQQUserAPIView(APIView):
    def post(self,request):
        """绑定QQ用户账号"""
        status = request.data.get("status")
        if status != 1 and status != 2:
            return Response("绑定账号数据出错！", status=http_status.HTTP_400_BAD_REQUEST)

        if status == 1:
            """已有账号绑定QQ"""
            username = request.data.get("username")
            password = request.data.get("password")

            # 账号密码校验
            Authbackend = UsernameMobileAuthBackend()
            user = Authbackend.authenticate(request, username, password)
            if user is None:
                return Response("账号或密码错误！", status=http_status.HTTP_400_BAD_REQUEST)

            try:
                data = request.data.get("openid")
                serializer = Serializer(settings.SECRET_KEY, constants.DATA_SIGNATURE_EXPIRE)
                ret = serializer.loads(data)
                openid = ret.get("openid")
                OAuthUser.objects.create(user=user,openid=openid)
            except:
                return Response("账号绑定超时，请重新登录绑定！", status=http_status.HTTP_400_BAD_REQUEST)

        else:
            """注册账号后绑定QQ"""
            """
              "password":this.password,
              "openid": this.openid,
              "mobile": this.mobile,
              "sms_code": this.sms_code,
              "nickname": this.qq_nickname,
              "avatar": this.qq_avatar,
            """
            password = request.data.get("password")
            openid_data = request.data.get("openid")
            mobile = request.data.get("mobile")
            sms_code = request.data.get("sms_code")
            nickname = request.data.get("nickname")
            avatar = request.data.get("avatar")
            # 判断数据是否完整
            if len(password) > 16 and len(password)<6:
                return Response("密码长度有误！", status=http_status.HTTP_400_BAD_REQUEST)

            # todo 判断手机格式是否正确
            # todo 判断手机验证码是否正确

            # 判断 昵称是否被占用
            try:
                User.objects.get(nickname=nickname)
                return Response("当前昵称已经被使用！", status=http_status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                pass

            # todo 判断 手机是否被占用
            try:
                User.objects.get(mobile=mobile)
                return Response("当前手机已经被使用！", status=http_status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                pass

            # 判断openid是否超时或者被篡改
            try:
                serializer = Serializer(settings.SECRET_KEY, constants.DATA_SIGNATURE_EXPIRE)
                ret = serializer.loads(openid_data)
                openid = ret.get("openid")
            except:
                return Response("账号绑定超时，请重新登录绑定！", status=http_status.HTTP_400_BAD_REQUEST)

            # 判断openid是否绑定了别的账户
            try:
                OAuthUser.objects.get(openid=openid)
                return Response("当前QQ已经绑定别的账号，请使用账号进行登录！", status=http_status.HTTP_400_BAD_REQUEST)
            except OAuthUser.DoesNotExist:
                pass

            # 注册用户信息
            user = User.objects.create_user(username=mobile, mobile=mobile, nickname=nickname, password=password)
            # 新用户绑定QQ账号
            OAuthUser.objects.create(user=user, openid=openid)

        # 生成jwt登录token
        from rest_framework_jwt.settings import api_settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user_info = {
            "token": token,
            "id": user.id,
            "username": user.username,
            "avatar": user.avatar.url if user.avatar.url else "",
            "nickname": user.nickname,
        }
        return Response({"user_info": user_info, "status": 1})