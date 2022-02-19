
from rest_framework import versioning

# 自定义的认证方法
class MyVersion(object):
    def determine_version(self,request,*args,**kwargs):
        version = request.query_params.get("version","v1")

        return version


