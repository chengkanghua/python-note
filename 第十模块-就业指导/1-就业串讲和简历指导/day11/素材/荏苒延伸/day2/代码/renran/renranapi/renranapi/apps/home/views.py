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

            # 查询当前用户关注的作者是否有新的推送[查询同步库]
            # 先到未读池中提取当前访问用户上一次读取Feed的最大主键
            start_sequence_id = self.get_start_sequence_id(user.id)
            # 然后根据主键到同步库中查看数据
            message_id_list = self.get_feed_message(user.id, start_sequence_id)
            if len(message_id_list)>=10:
                """如果未读池存在10条以上的推送内容"""
                queryset = queryset.filter(id__in=message_id_list)

            else:
                # 基于物品进行协同过滤推荐文章
                message_id_list = self.get_message_by_itemCF(user.id)

                # 判断tablestore中是否曾经推送过当前当前文章给用户
                queryset = self.check_user_message_log(user, queryset)

            # 更新推送日志
            if len(queryset)>0:
                article_id_list = []
                for item in queryset:
                    article_id_list.append(item.id)
                self.push_log(user.id, article_id_list)

        return queryset

    def get_message_by_itemCF(self,user_id):
        """基于物品的协同过滤获取Feed内容"""
        pass

    def get_feed_message(self,user_id, start_sequence_id):
        """获取同步库中的数据"""
        table_name = "user_message_table"

        # 范围查询的起始主键
        inclusive_start_primary_key = [
            ('user_id', user_id),
            ('sequence_id', start_sequence_id),
            ('sender_id', INF_MIN),
            ('message_id', INF_MIN)
        ]

        # 范围查询的结束主键
        exclusive_end_primary_key = [
            ('user_id', user_id),
            ('sequence_id', INF_MAX),
            ('sender_id', INF_MAX),
            ('message_id', INF_MAX),
        ]

        columns_to_get = [] # 表示返回所有列
        limit = 10

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name, # 操作表明
            Direction.FORWARD, # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
            inclusive_start_primary_key, exclusive_end_primary_key, # 取值范围
            columns_to_get, # 返回字段列
            limit, #　结果数量
            max_version=1         # 返回版本数量
        )

        message_id_list = []
        for item in row_list:
            message_id_list.append( item.primary_key[3][1] )

        # 下一次读取同步库的开始主键
        try:
            self.set_start_sequence_id(user_id, start_sequence_id, next_start_primary_key[1][1])
        except:
            pass

        return message_id_list

    def set_start_sequence_id(self, user_id,old_start_sequence_id, next_start_primary_key):
        table_name = "user_message_session_table"
        try:
            primary_key = [('user_id', user_id), ('last_sequence_id', old_start_sequence_id)]
            row = Row(primary_key)
            consumed, return_row = self.client.delete_row(table_name, row, None)
        except:
            pass

        primary_key = [('user_id', user_id), ('last_sequence_id', next_start_primary_key)]
        attribute_columns = []
        row = Row(primary_key, attribute_columns)
        consumed, return_row = self.client.put_row(table_name, row)
        print(return_row)
        return return_row

    def get_start_sequence_id(self,user_id):
        """获取最后读取的Feed流id"""
        table_name = "user_message_session_table"

        # 范围查询的起始主键
        inclusive_start_primary_key = [
            ('user_id', user_id),
            ('last_sequence_id', INF_MIN)
        ]

        # 范围查询的结束主键
        exclusive_end_primary_key = [
            ('user_id', user_id),
            ('last_sequence_id', INF_MAX)
        ]

        columns_to_get = [] # 表示返回所有列
        limit = 1

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name, # 操作表明
            Direction.FORWARD, # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
            inclusive_start_primary_key, exclusive_end_primary_key, # 取值范围
            columns_to_get, # 返回字段列
            limit, #　结果数量
            # column_filter=cond, # 条件
            max_version=1         # 返回版本数量
        )

        if len(row_list) < 1:
            # 之前没有读取过推送内容
            return INF_MIN
        else:
            return row_list[0].primary_key[1][1]


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