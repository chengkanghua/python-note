from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views import View
from .models import Book,Publisher
import json
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer

# Create your views here.
# class BookView(View):
#     publish_obj = Publisher.objects.get(id=1)
    # Book.objects.create(title='python图书',category='1',pub_time='2021-01-01',publisher=publish_obj)
    # Book.objects.create(title='python图书2',category='1',pub_time='2021-03-01',publisher=publish_obj)

    # 第一版 用.values JsonResponse实现序列化
    # def get(self,request):
    #     book_list = Book.objects.values('id','title','pub_time','publisher')
    #     # print(book_list,type(book_list))
    #     book_list=list(book_list)
    #     ret = []
    #     for book in book_list:
    #         publisher_id = book['publisher']
    #         publisher_obj = Publisher.objects.filter(id=publisher_id).first()
    #         book['publisher'] = {
    #             'id': publisher_id,
    #             'title': publisher_obj.title
    #         }
    #         ret.append(book)
    #
    #     # 这种方式没法转化时间格式 改用 JsonResponse
    #     # ret = json.dumps(book_list,ensure_ascii=False)
    #     # return HttpResponse(ret)
    #     # JsonResponse
    #     return  JsonResponse(ret,safe=False,json_dumps_params={'ensure_ascii':False})

    # 第二版 用django serializers实现序列化
    # def get(self,request):
    #     book_queryset = Book.objects.all()
    #     ret = serializers.serialize('json',book_queryset,ensure_ascii=False)
    #     return HttpResponse(ret)

class GenericAPIView(APIView):
    query_set = None
    serializer_class = None
    def get_queryset(self):
        return self.query_set
    def get_serializer(self,*args,**kwargs):
        return self.serializer_class(*args,**kwargs)

class ListModelMixin(object):
    def list(self, request):
        queryset = self.get_queryset()
        ret = self.get_serializer(queryset, many=True)
        return Response(ret.data)

class CreateModelMixin(object):
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
class RetrieveModelMixin(object):
    def retrieve(self, request, id):
        book_obj = self.get_queryset().filter(id=id).first()
        ret = self.get_serializer(book_obj)
        return Response(ret.data)

class UpdateModelMixin(object):
    def update(self, request, id):
        book_obj = self.get_queryset().filter(id=id).first()
        serializer = self.get_serializer(book_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class DestroyModelMixin(object):
    def destroy(self, request, id):
        book_obj = self.get_queryset().filter(id=id).first()
        book_obj.delete()
        return Response("")

class ListCreateAPIView(GenericAPIView,ListModelMixin,CreateModelMixin):
    pass

class RetrieveUpdateDestroyAPIView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    pass

class BookView(ListCreateAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer

    def get(self,request):
        # boo_obj = Book.objects.first()
        # ret = BookSerializer(book_obj)
        # 拿多个对象
        # book_list = Book.objects.all()
        # ret = BookSerializer(book_list,many=True)
        # return Response(ret.data)
        return self.list(request)

    def post(self,request):
        # print(request.data)
        # serializer = BookSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return serializer.data
        # else:
        #     return Response(serializer.errors)
        return self.create(request)

class BookEditView(RetrieveUpdateDestroyAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer

    def get(self,request,id):
        # book_obj = Book.objects.filter(id=id).first()
        # ret = BookSerializer(book_obj)
        # return Response(ret.data)
        return self.retrieve(request,id)

    def put(self,request,id):
        # book_obj = Book.objects.filter(id=id).first()
        # serializer = BookSerializer(book_obj,data=request.data,partial=True) # partial=True 允许部分更新
        # if serializer.is_valid():
        #     serializer.save()
        #     return  Response(request.data)
        # else:
        #     return Response(serializer.errors)
        return self.update(request,id)

    def delete(self,request,id):
        # book_obj = Book.objects.filter(id=id).first()
        # book_obj.delete()
        # return Response("")
        return self.destroy(request,id)


# 继承ViewSetMixin 既可以传参
from rest_framework.viewsets import ViewSetMixin

# class ModelViewSet(ViewSetMixin, GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     pass

from rest_framework.viewsets import ModelViewSet
class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


