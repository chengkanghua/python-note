from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from SerDemo.models import Book
from SerDemo.serializers import BookSerializer
from utils.pagination import MyPagination
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework import pagination
# Create your views here.


# 自己实现分页视图
# class BookView(APIView):
#     def get(self,request):
#         queryset = Book.objects.all()
#         # 1 实例化分页器对象
#         page_obj = MyPagination()
#         # 2调用分页器方法分页
#         page_queryset = page_obj.paginate_queryset(queryset,request,view=self)
#         # 3，把分页好的数据序列化返回
#         # 4, 带着上一页下一页连接的响应
#         ser_obj = BookSerializer(page_queryset, many=True)
#
#         return page_obj.get_paginated_response(ser_obj.data)


# 效果和自己实现一样
class BookView(GenericAPIView,ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = MyPagination

    def get(self,request):
        return self.list(request)