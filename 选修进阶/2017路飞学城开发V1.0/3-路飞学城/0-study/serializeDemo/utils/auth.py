from rest_framework.exceptions import AuthenticationFailed
from authDemo.models import User
from rest_framework.authentication import BaseAuthentication

# http://127.0.0.1:8000/auth/test?token=160b85f738ca4869bc9ac2ec41e07709
class MyAuth(BaseAuthentication):
    def authenticate(self,request):
        token = request.query_params.get("token","")
        if not token:
            raise AuthenticationFailed("没有携带token")
        user_obj = User.objects.filter(token=token).first()
        if not user_obj:
            raise AuthenticationFailed("token不合法")
        return (user_obj,token)