import re
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.base import models
import requests
from utils.token import get_authorizer_access_token
from utils import return_code


class TemplateView(APIView):
    def get(self, request, *args, **kwargs):
        # 获取公众号ID
        pid = request.query_params.get("pid")

        # 检查此用户是否绑定该公众号
        pub_object = models.PublicNumbers.objects.filter(id=pid, mtb_user_id=request.user.user_id).first()
        if not pub_object:
            return Response({"code": return_code.VALIDATE_ERROR, 'detail': "公众号不存在"})

        # 获取模板列表
        access_token = get_authorizer_access_token(pub_object)
        res = requests.get(
            url="https://api.weixin.qq.com/cgi-bin/template/get_all_private_template",
            params={"access_token": access_token}
        )
        data_dict = res.json()
        template_list = data_dict.get("template_list")
        if not template_list:
            return Response({"code": return_code.VALIDATE_ERROR, 'detail': "未获取到模板"})


        result = {}
        for item in data_dict["template_list"]:
            # [result,withdrawMoney,cardInfo...]
            field_list = re.findall("{{(\w+)\.DATA}}", item["content"])
            # {"result":"", "withdrawMoney":"", ...}
            item["item_dict"] = {field: "" for field in field_list}
            result[item['template_id']] = item
        return Response({"code": return_code.SUCCESS, 'data': result})
