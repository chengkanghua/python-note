from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.base_response import BaseResponse
from utils.redis_pool import POOL
from utils.my_auth import LoginAuth
from Course.models import Course
import json
import redis

# Create your views here.


# 前端传过来 course_id  price_policy_id
# 把购物车数据放入redis
"""
{
    SHOPPINGCAR_USERID_COURSE_ID: {
        "id", 
        "title",
        "course_img",
        "price_policy_dict": {
            price_policy_id: "{valid_period,  price}"
            price_policy_id2: "{valid_period,  price}"
            price_policy_id3: "{valid_period,  price}"

        },
        "default_price_policy_id": 1


    }


}
"""

SHOPPINGCAR_KEY = "SHOPPINGCAR_%s_%s"
CONN = redis.Redis(connection_pool=POOL)

class ShoppingCarView(APIView):
    authentication_classes = [LoginAuth, ]

    def post(self, request):
        res = BaseResponse()
        # 1, 获取前端传过来的数据以及user_id
        course_id = request.data.get("course_id", "")
        price_policy_id = request.data.get("price_policy_id", "")
        user_name = request.data.get("username","")
        # 2, 校验数据的合法性
        # 2.1 校验课程id合法性
        course_obj = Course.objects.filter(id=course_id).first()
        if not course_obj:
            res.code = 1040
            res.error = "课程id不合法"
            return Response(res.dict)
        # 2.2 校验价格策略id是否合法
        price_policy_queryset = course_obj.price_policy.all()
        price_policy_dict = {}
        for price_policy in price_policy_queryset:
            price_policy_dict[price_policy.id] = {
                "price": price_policy.price,
                "valid_period": price_policy.valid_period,
                "valid_period_display": price_policy.get_valid_period_display()
            }
        if price_policy_id not in price_policy_dict:
            res.code = 1041
            res.error = "价格策略id不合法"
            return Response(res.dict)
        # 3，构建redisKEY
        key = SHOPPINGCAR_KEY % (user_name, course_id)
        # 4，构建数据结构
        current_price_policy = price_policy_dict.get(price_policy_id)
        # print(current_price_policy)
        course_info = {
            "id": course_obj.id,
            "course_id":course_id,
            "title": course_obj.title,
            "course_img": str(course_obj.course_img),
            "price_policy_dict": json.dumps(price_policy_dict, ensure_ascii=False),
            "default_price_policy_id": price_policy_id,
            "coursePrice":current_price_policy.get("price"),
            "valid_period":current_price_policy.get("valid_period"),
            "valid_period_display":current_price_policy.get('valid_period_display'),
        }


        # print(course_info)

        # 5  写入redis
        if CONN.exists(key):
            res.data = "该套餐已更新"
        else:
            res.data = "加入购物车成功"

        CONN.hmset(key, course_info)
        return Response(res.dict)

    def get(self, request,username):
        res = BaseResponse()
        # 1, 拼接redis key
        # user_id = request.user.pk
        # print(username)
        shopping_car_key = SHOPPINGCAR_KEY % (username, "*")
        # 2, 去redis中读取数据
        # 2.1 匹配所有的keys
        # 3，构建数据结构展示
        all_keys = CONN.scan_iter(shopping_car_key)
        ret = []
        for key in all_keys:
            item = CONN.hgetall(key)
            str_dict = item.get('price_policy_dict')
            price_policy_dict = json.loads(str_dict)
            item['price_policy_dict'] = price_policy_dict
            ret.append(item)
            # print(item)
        res.data = ret
        return Response(res.dict)

    def put(self, request):
        # 前端 course_id  price_policy_id
        res = BaseResponse()
        # 1, 获取前端传过来的数据以及user_id
        course_id = request.data.get("course_id", "")
        price_policy_id = request.data.get("price_policy_id", "")
        user_id = request.user.pk
        # 2, 校验数据的合法性
        # 2.1 course_id是否合法
        key = SHOPPINGCAR_KEY % (user_id, course_id)
        if not CONN.exists(key):
            res.code = 1043
            res.error = "课程id不合法"
            return Response(res.dict)
        # 2,2 price_policy_id是否合法
        price_policy_dict = json.loads(CONN.hget(key, "price_policy_dict"))
        if str(price_policy_id) not in price_policy_dict:
            res.code = 1044
            res.error = "价格策略不合法"
            return Response(res.dict)
        # 3, 更新redis  default_price_policy_id
        CONN.hset(key, "default_price_policy_id", price_policy_id)
        res.data = "更新成功"
        return Response(res.dict)

    def delete(self, request):
        # course_list = [course_id, ]
        res = BaseResponse()
        # 1 获取前端传来的数据以及user_id
        username =  request.data.get("username", "")
        course_id = request.data.get("course_id", "")
        key = 'SHOPPINGCAR_%s_%s' %(username,course_id)
        print(key)

        # 3， 删除redis数据
        reply = CONN.delete(key)
        if reply:
            res.data = "删除成功"
        else:
            res.data = '不存在的购物车数据'
        return Response(res.dict)












