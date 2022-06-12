from rest_framework.views import APIView
from rest_framework.response import Response
from utils import return_code
from .. import models
import datetime


class StatView(APIView):
    def get(self, request, *args, **kwargs):
        activity_id = request.query_params.get('activity')
        if not activity_id:
            return Response({"code": return_code.ERROR})


        # 获取当前活动近7天数据
        today = datetime.date.today()
        start_date = today - datetime.timedelta(days=7)
        queryset = models.TakePartIn.objects.filter(
            ctime__gt=start_date,
            activity_id=activity_id,
            public_number__mtb_user=request.user.user_id
        )

        yesterday = today - datetime.timedelta(days=1)

        """
        total_dict = {
            "11-11":{
                total:0,
                valid:0,
                cancel:0,
                "join":0
            },
            "11-12":{
                total:0,
                valid:0,
                cancel:0,
                "join":0
            },
        }
        """
        total_dict = {}
        for i in range(7, -1, -1):
            date = today - datetime.timedelta(days=i)
            date_string = date.strftime("%m-%d")
            total_dict[date_string] = {
                "total": 0,  # 总数
                "valid": 0,  # 净增（关注中）
                "cancel": 0,  # 取关
                "join": 0,  # 参与
            }

        for item in queryset:
            ctime_string = item.ctime.strftime("%m-%d")
            total_dict[ctime_string]['total'] += 1
            if item.looking == 0:
                total_dict[ctime_string]['valid'] += 1
            else:
                total_dict[ctime_string]['cancel'] += 1

            if item.part_in == 0:
                total_dict[ctime_string]['join'] += 1

        info = {
            "total": {
                "name": "总数量",
                "data": [item['total'] for item in total_dict.values()],
            },
            "valid": {
                "name": "净增",
                "data": [item['valid'] for item in total_dict.values()],
            },
            "cancel": {
                "name": "取关",
                "data": [item['cancel'] for item in total_dict.values()],
            },
            "join": {
                "name": "参与",
                "data": [item['join'] for item in total_dict.values()],
            }
        }
        context = {
            "name": [item for item in total_dict.keys()],  # ["4-03",4-5]
            "series": info.values(),
            "today": total_dict[today.strftime("%m-%d")],
            "yesterday": total_dict[yesterday.strftime("%m-%d")],
        }
        # print(context)
        return Response({"code": return_code.SUCCESS, "data": context})
