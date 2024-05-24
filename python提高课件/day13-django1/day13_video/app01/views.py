from django.shortcuts import render, redirect
from django.db.models import F
from app01 import models
import datetime
from django_redis import get_redis_connection
from django.conf import settings


def order_list(request):
    """ 订单列表 """
    customer_id = 1  # 按理说这个值应该是当前登录用户
    result = models.Order.objects.filter(customer_id=customer_id).order_by('-id')
    return render(request, 'order_list.html', {"result": result})


def order_add(request):
    """ 添加订单 """
    # 获取所有的价格策略
    price_list = models.PricePolicy.objects.all()

    if request.method == "GET":
        return render(request, "order_add.html", {'price_list': price_list})
    else:
        # 提交过来的数据
        policy_id = request.POST.get("policy")
        url = request.POST.get("url")
        print(policy_id, url)

        # 根据这些数据在数据库表中创建一条记录
        # 0.根据policy_id获取个数和数量
        policy_object = models.PricePolicy.objects.filter(id=policy_id).first()

        # 1.创建订单
        oid = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        models.Order.objects.create(
            oid=oid,
            url=url,
            count=policy_object.count,
            price=policy_object.price,
            customer_id=1  # 模拟的客户id=1
        )
        # 2. 余额扣除
        models.Customer.objects.filter(id=1).update(balance=F("balance") - policy_object.price)

        # 3. 在redis中添加记录（稍后），只存放订单号
        #   3.1 安装并启动redis
        #   3.2 在django中安装 pip install django-redis
        #   3.3 配置django-redis
        #   3.4 写入到redis中
        conn = get_redis_connection("default")
        conn.lpush(settings.REDIS_QUEUE_NAME, oid)

        return redirect("/order/list/")
