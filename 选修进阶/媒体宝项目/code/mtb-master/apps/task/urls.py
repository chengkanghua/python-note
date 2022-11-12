from django.urls import path
from rest_framework import routers
from .views import activity
from .views import wx
from .views import promo
from .views import fans
from .views import stat

router = routers.SimpleRouter()

router.register(r'activity', activity.ActivityView)
router.register(r'promo', promo.PromoView)
router.register(r'total/promo', promo.TotalPromoView)

router.register(r'fans', fans.FansView)

urlpatterns = [
    # 活动 APIView
    # /task/activity/  POST
    # /task/activity/  GET
    path('to/black/', fans.ToBlackView.as_view()),
    path('out/black/', fans.OutBlackView.as_view()),
    path('export/', fans.ExportBlackView.as_view()),
    path('stat/', stat.StatView.as_view()),
    path('oauth/', wx.oauth),
]

urlpatterns += router.urls
