from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from article.models import Article
from .serializers import ArticleListModelSerializer
from .paginations import HomeArticlePageNumberPagination
from tablestore import *
from django.conf import settings
from users.models import User
from datetime import datetime
class ArticleListAPIView(ListAPIView):
    serializer_class = ArticleListModelSerializer
    pagination_class = HomeArticlePageNumberPagination

    @property
    def client(self):
        return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    def get_queryset(self):
        week_timestamp = datetime.now().timestamp() - 7 * 86400
        week_date = datetime.fromtimestamp(week_timestamp) # 获取一周前的时间对象
        queryset = Article.objects.filter(pub_date__gte=week_date).exclude(pub_date=None,).order_by("-reward_count","-comment_count","-like_count","-id")

        # 记录本次给用户推送文章的记录
        user = self.request.user

        if isinstance(user, User):

            # 查询当前用户关注的作者是否有新的推送

            # 判断tablestore中是否曾经推送过当前当前文章给用户
            queryset = self.check_user_message_log(user, queryset)

            if len(queryset)>0:
                article_id_list = []
                for item in queryset:
                    article_id_list.append(item.id)
                self.push_log(user.id, article_id_list)

        return queryset

    def check_user_message_log(self, user, queryset):
        """判断系统是否曾经推送过文章给用户"""
        columns_to_get = []
        rows_to_get = []
        for article in queryset:
            primary_key = [('user_id', user.id), ('message_id', article.id)]
            rows_to_get.append(primary_key)
        request = BatchGetRowRequest()
        table_name = "user_message_log_table"

        cond = CompositeColumnCondition(LogicalOperator.OR)
        cond.add_sub_condition(SingleColumnCondition("is_read", True, ComparatorType.EQUAL))
        cond.add_sub_condition(SingleColumnCondition("is_like", True, ComparatorType.EQUAL))

        request.add(TableInBatchGetRowItem(table_name, rows_to_get, columns_to_get,column_filter=cond, max_version=1))
        result = self.client.batch_get_row(request)
        table_result = result.get_result_by_table(table_name)
        push_id_list = []
        for item in table_result:
            if item.row is not None:
                push_id_list.append(item.row.primary_key[1][1])

        return queryset.exclude(id__in=push_id_list)

    def push_log(self, user_id, article_id_list):
        """推送文章给用户的记录"""
        table_name = "user_message_log_table"

        put_row_items = []

        for i in article_id_list:
            # 主键列
            primary_key = [
                ('user_id', user_id),  # 用户ID
                ("message_id", i),  # 文章ID
            ]

            attribute_columns = [('is_push', True), ('is_read', False), ('is_like', False), ('is_reward',False), ('is_comment',False)]

            row = Row(primary_key, attribute_columns)
            condition = Condition(RowExistenceExpectation.IGNORE)
            item = PutRowItem(row, condition)
            put_row_items.append(item)

        request = BatchWriteRowRequest()
        request.add(TableInBatchWriteRowItem(table_name, put_row_items))
        result = self.client.batch_write_row(request)
        return result.is_all_succeed()