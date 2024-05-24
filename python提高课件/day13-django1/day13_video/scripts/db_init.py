"""
web runtime
    1. 启动django程序（数据库连接 & settings ）
    2. 用户发送请求，django接收请求并交给视图函数处理。
    3. 视图函数里面进行数据库操作
        models.Users.object......

离线脚本：

    models.Users.object......

注意：数据库中表的初始化，为了简化开发，我就用脚本先来实现。
"""

import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day13_video.settings")
django.setup()  # 伪造让django启动

from django.db.models import F
from app01 import models

# 1. 创建管理员
"""
user_object = models.Administrator.objects.create(
    username="wupeiqi",
    password="12312312312312",
    mobile="15131255089"
)
"""

# 2. 创建客户
"""
user_object = models.Administrator.objects.filter(username="wupeiqi").first()
customer_object = models.Customer.objects.create(
    username="alex",
    password="123123",
    creator=user_object
)
"""
"""
customer_object = models.Customer.objects.create(
    username="alex",
    password="123123",
    creator_id=1
)
"""

# 3. 充值
"""
models.ChargeRecord.objects.create(
    amount=100000,
    customer_id=1,  # alex客户
    creator_id=1,  # wupeiqi管理员
)
# models.Customer.objects.filter(id=1).update(balance=原来的值+100000)
models.Customer.objects.filter(id=1).update(balance=F("balance") + 100000)
"""

# 4. 价格策略
"""
models.PricePolicy.objects.bulk_create([
    models.PricePolicy(count=10000, price=5),
    models.PricePolicy(count=20000, price=9),
    models.PricePolicy(count=30000, price=13),
])
"""

# 5. 创建订单并删除
"""
import datetime

# 创建订单
models.Order.objects.create(
    oid=datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"),
    url="http://www.luffycity.com",
    count=10000,
    price=5,
    customer_id=1  # 模拟的客户id=1
)
# 余额扣除
models.Customer.objects.filter(id=1).update(balance=F("balance") - 5)
"""
