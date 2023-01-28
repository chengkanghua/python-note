# Create your views here.

from .models import ArticleImage
from rest_framework.generics import CreateAPIView
from .serializers import ArticleImageModelSerializer
class ImageAPIView(CreateAPIView):
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageModelSerializer


from .models import ArticleCollection
from .serializers import ArticleCollectionModelSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class CollecionAPIView(CreateAPIView, ListAPIView):
    """文集的视图接口"""
    queryset = ArticleCollection.objects.all()
    serializer_class = ArticleCollectionModelSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = self.filter_queryset(self.get_queryset().filter(user=user))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

from rest_framework.generics import UpdateAPIView
from .serializers import ArticleCollectionDetailModelSerializer
class CollecionDetailAPIView(UpdateAPIView):
    """文集的视图接口"""
    queryset = ArticleCollection.objects.all()
    serializer_class = ArticleCollectionDetailModelSerializer
    permission_classes = [IsAuthenticated]


from rest_framework.viewsets import ModelViewSet
from .models import Article
from .serializers import ArticleModelSerializer
from rest_framework.decorators import action
from rest_framework import status
from django_redis import get_redis_connection
from datetime import datetime
from django.db import transaction

class ArticleAPIView(ModelViewSet):
    """文章的视图集接口"""
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    permission_classes = [IsAuthenticated]

    @property
    def client(self):
        return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    @action(methods=["PUT"], detail=True)
    def save_article(self,request,pk):
        # 接收文章内容，标题，编辑次数，文章ID
        content = request.data.get("content")
        title = request.data.get("title")
        save_id = int( request.data.get("save_id") )
        collection_id = request.data.get("collection_id")
        user = request.user
        if save_id is None:
            save_id = 1
        else:
            save_id += 1

        # 验证文章是否存在
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response({"message":"当前文章不存在！"}, status=status.HTTP_400_BAD_REQUEST)

        # 写入到redis中[先配置redis库]
        redis_conn = get_redis_connection("article")
        """
        article_<user_id>_<article>_<save_id>:{
            "title":   title,
            "content": content,
            "update_time": 1929293,
            "collection_id":collection_id,
        }
        """
        new_timestamp = datetime.now().timestamp()
        data = {
            "title": title,
            "content": content,
            "updated_time": new_timestamp,
            "collection_id": collection_id,
        }
        redis_conn.hmset("article_%s_%s_%s" % (user.id, pk, save_id), data)
        # 把用户针对当前文章的最新编辑记录ID保存起来
        redis_conn.hset("article_history_%s" % (user.id), pk, save_id )
        # 实现查看当前文章的编辑历史的思路：
        # article_edit_history = redis_conn.keys("article_%s_%s*" % (user.id, pk) )
        # data_list = []
        # for item in article_edit_history:
        #     ret = redis_conn.hgetall(item)
        #     data_list.append({
        #         "title": ret.get("title".encode()).decode(),
        #         "content": ret.get("content".encode()).decode(),
        #         "updated_time": ret.get("updated_time".encode()).decode(),
        #     })
        # print(data_list)
        # 返回结果
        return Response({"message":"保存成功！","save_id": save_id})

    def list(self, request, *args, **kwargs):
        user = request.user
        collection_id = request.query_params.get("collection")
        try:
            ArticleCollection.objects.get(pk=collection_id)
        except ArticleCollection.DoesNotExist:
            return Response({"message":"对不起，当前文集不存在！"})

        # 先到redis中查询
        redis_conn = get_redis_connection("article")
        history_dist = redis_conn.hgetall("article_history_%s" % (user.id) )
        data = []
        exclude_id = []
        if history_dist is not None:
            for article_id, save_id in history_dist.items():
                article_id = article_id.decode()
                save_id = save_id.decode()
                article_data_byte = redis_conn.hgetall("article_%s_%s_%s" % (user.id, article_id, save_id) )
                if article_data_byte["collection_id".encode()].decode() == collection_id:
                    data.append({
                        "id": article_id,
                        "title": article_data_byte["title".encode()].decode(),
                        "content": article_data_byte["content".encode()].decode(),
                        "save_id": save_id,
                        "collection": collection_id,
                    })
                    exclude_id.append(article_id)

        # 然后把redis中已经编辑过的内容结果排除出来，然后到MySQL中查询

        queryset = self.filter_queryset(self.get_queryset().filter(user=user, collection_id=collection_id).exclude(id__in=exclude_id) )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        data +=serializer.data

        return Response(data)

    @action(methods=["patch"],detail=True)
    def pub_article(self,request,pk):
        """发布文章"""
        user    = request.user
        status  = request.data.get("is_pub")

        with transaction.atomic():
            save_id = transaction.savepoint()
            try:
                article = Article.objects.get(user=user, pk=pk)
            except:
                transaction.savepoint_rollback(save_id)
                return Response({"message":"当前文章不存在或者您没有修改的权限！"})

            if status:
                """发布文章"""
                article.pub_date = datetime.now()

                # 先查询到当前作者的粉丝 user_relation_table中查询　
                fens_list = self.get_fens(user.id)

                # 循环结果，把Feed进行推送
                if len(fens_list) > 0:
                    ret = self.push_feed(fens_list, user.id, article.id)
                    if not ret:
                        transaction.savepoint_rollback(save_id)
                        message = {"message": "发布文章失败！"}
                    else:
                        message = {"message": "发布文章成功！"}
                else:
                    message = {"message":"发布文章成功"}
            else:
                """私密文章，取消发布"""
                article.pub_date = None
                message = {"message":"取消发布成功"}

            # 从redis的编辑记录中提取当前文章的最新记录
            redis_conn = get_redis_connection("article")
            user_history_dist = redis_conn.hgetall("article_history_%s" % user.id)
            save_id = user_history_dist.get(pk.encode()).decode()
            article_dict = redis_conn.hgetall("article_%s_%s_%s" % (user.id, pk, save_id) )
            if article_dict is not None:
                article.title = article_dict["title".encode()].decode()
                article.content = article_dict["content".encode()].decode()
                timestamp = datetime.fromtimestamp(int(float(article_dict["updated_time".encode()].decode())))
                article.updated_time = timestamp
                article.save_id = save_id
            article.save()

            return Response(message)

    def push_feed(self, fens_list,author_id, article_id):
        """推送Feed给粉丝"""
        table_name = "user_message_table"

        put_row_items = []

        for i in fens_list:
            # 主键列
            primary_key = [  # ('主键名', 值),
                ('user_id', i),  # 接收Feed的用户ID
                ('sequence_id', PK_AUTO_INCR),  # 如果是自增主键，则值就是 PK_AUTO_INCR
                ("sender_id", author_id),  # 发布Feed的用户ID
                ("message_id", article_id),  # 文章ID
            ]

            attribute_columns = [('recevice_time', datetime.now().timestamp()), ('read_status', False)]
            row = Row(primary_key, attribute_columns)
            condition = Condition(RowExistenceExpectation.IGNORE)
            item = PutRowItem(row, condition)
            put_row_items.append(item)

        request = BatchWriteRowRequest()
        request.add(TableInBatchWriteRowItem(table_name, put_row_items))
        result = self.client.batch_write_row(request)

        return result.is_all_succeed()

    def get_fens(self, user_id):
        """获取当前用户的所有粉丝，后面自己整理下这个方法到工具库中"""
        table_name = "user_relation_table"

        # 范围查询的起始主键
        inclusive_start_primary_key = [
            ('user_id', user_id),
            ('follow_user_id', INF_MIN)
        ]

        # 范围查询的结束主键
        exclusive_end_primary_key = [
            ('user_id', user_id),
            ('follow_user_id', INF_MAX)
        ]

        # 查询所有列
        columns_to_get = [] # 表示返回所有列

        # 范围查询接口
        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            table_name,  # 操作表明
            Direction.FORWARD,  # 范围的方向，字符串格式，取值包括'FORWARD'和'BACKWARD'。
            inclusive_start_primary_key, exclusive_end_primary_key,  # 取值范围
            columns_to_get,  # 返回字段列
            max_version=1  # 返回版本数量
        )

        fens_list = []
        for row in row_list:
            fens_list.append( row.primary_key[1][1] )

        return fens_list

    @action(methods=["patch"], detail=True)
    def change_collection(self, request, pk):
        """切换当前文章的文集ID"""
        user = request.user
        collection_id = request.data.get("collection_id")
        try:
            article = Article.objects.get(user=user, pk=pk)
        except:
            return Response({"message": "当前文章不存在或者您没有修改的权限！"})

        try:
            ArticleCollection.objects.get(user=user, pk=collection_id)
        except:
            return Response({"message": "当前文集不存在或者您没有修改的权限！"})

        # 当前文章如果之前有曾经被编辑，则需要修改redis中的缓存
        redis_conn = get_redis_connection("article")
        save_id_bytes = redis_conn.hget("article_history_%s" % (user.id),pk)
        if save_id_bytes is not None:
            save_id = save_id_bytes.decode()
            redis_conn.hset("article_%s_%s_%s" % (user.id, pk, save_id ), "collection_id", collection_id )
        article.collection_id = collection_id
        article.save()

        return Response({"message":"切换文章的文集成功！"})

from .models import Special,SpecialArticle
from .serializers import SpecialModelSerializer
class SpecialListAPIView(ListAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialModelSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        ret = self.get_queryset().filter(mymanager__user=user)
        article_id = request.query_params.get("article_id")
        # 验证文章

        queryset = self.filter_queryset(ret)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        # 返回专题对于当前文章的收录状态
        data = []
        for special in serializer.data:
            try:
                SpecialArticle.objects.get(article_id=article_id, special_id=special.get("id"))
                special["post_status"] = True # 表示当前文章已经被专题收录了
            except SpecialArticle.DoesNotExist:
                special["post_status"] = False  # 表示当前文章已经被专题收录了
            data.append(special)
        return Response(data)

class ArticlePostSpecialAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        """收录到我管理的专题"""
        article_id = request.data.get("article_id")
        special_id = request.data.get("special_id")
        user = request.user
        try:
            Article.objects.get(user=user, pk=article_id)
        except Article.DoesNotExist:
            return Response({"message": "当前文章不存在或者您没有操作的权限！"})

        try:
            Special.objects.get(mymanager__user=user, pk=special_id)
        except Article.DoesNotExist:
            return Response({"message": "当前专题不存在或者您没有操作的权限！"})

        SpecialArticle.objects.create(article_id=article_id,special_id=special_id)

        return Response({"message":"收录成功！"})

from rest_framework.generics import RetrieveAPIView
from .serializers import ArticleInfoModelSerializer
from users.models import User
from tablestore import *
from django.conf import settings

class ArticleInfoAPIView(RetrieveAPIView):
    """文章详情"""
    serializer_class = ArticleInfoModelSerializer
    queryset = Article.objects.exclude(pub_date=None)
    @property
    def client(self):
        return OTSClient(settings.OTS_ENDPOINT, settings.OTS_ID, settings.OTS_SECRET, settings.OTS_INSTANCE)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        if isinstance(request.user, User):
            """用户登录了"""
            user = request.user                                    # 访问者
            author_id = response.data.get("user").get("id")        # 文章作者

            # 用户对文章的阅读记录
            article_id = kwargs.get("pk")
            self.read_log(user.id, article_id)

            if author_id != user.id:
                # 到tablestore里面查询当前访问者是否关注了文章作者
                table_name = "user_relation_table"

                primary_key = [('user_id', author_id), ('follow_user_id', user.id)]

                columns_to_get = []

                consumed, return_row, next_token = self.client.get_row(table_name, primary_key, columns_to_get)

                if return_row is None:
                    """没有关注"""
                    is_follow = 1
                else:
                    """已经关注了"""
                    is_follow = 2

            else:
                is_follow = 3 # 当前用户就是作者

        else:
            """用户未登录"""
            is_follow = 0  # 当前访问者未登录


        response.data["is_follow"] = is_follow
        return response

    def read_log(self,user_id, article_id):
        """更新用户对文章的阅读记录"""
        table_name = "user_message_log_table"
        primary_key = [('user_id', int(user_id)), ('message_id', int(article_id))]
        update_of_attribute_columns = {
            'PUT': [('is_read', True)],
        }
        row = Row(primary_key, update_of_attribute_columns)
        condition = Condition(RowExistenceExpectation.IGNORE,
                              SingleColumnCondition("is_read", False, ComparatorType.EQUAL))  # update row on\
        consumed, return_row = self.client.update_row(table_name, row, condition)


from drf_haystack.viewsets import HaystackViewSet
from .serializers import ArticleIndexSerializer
from .paginations import ArticleSearchPageNumberPagination
class ArticleSearchViewSet(HaystackViewSet):
    """
    文章搜索
    """
    index_models = [Article]
    serializer_class = ArticleIndexSerializer
    pagination_class = ArticleSearchPageNumberPagination