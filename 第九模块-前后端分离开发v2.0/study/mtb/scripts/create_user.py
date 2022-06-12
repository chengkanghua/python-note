import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mtb.settings")
django.setup()

from apps.base import models
# 运行这个文件到数据库创建用户
# models.UserInfo.objects.create(
#     username="wupeiqi",
#     password="123123"
# )

