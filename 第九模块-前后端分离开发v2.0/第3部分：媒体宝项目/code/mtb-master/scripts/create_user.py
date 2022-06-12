import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mtb.settings")
django.setup()

from apps.task import models
#
# res = models.Activity.objects.filter(publics__public__authorizer_app_id="wx71bf291c758aaabf", poster__key="约吗")
# print(res)
