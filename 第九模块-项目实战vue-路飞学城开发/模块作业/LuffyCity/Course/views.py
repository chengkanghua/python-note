from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from .serializers import CategorySerializer,CourseSerializer,CourseDetailSerializer,CourseChapterSerializer,CourseCommentSerializer,QuestionSerializer


# Create your views here.

class CategoryView(APIView):
    def get(self, request):
        queryset = models.Category.objects.all()
        ser_obj = CategorySerializer(queryset, many=True)
        return Response(ser_obj.data)

class CourseView(APIView):
    def get(self,request):
        category_id = request.query_params.get("category",0)
        if category_id == '0':
            queryset = models.Course.objects.all().order_by("order")
        else:
            queryset = models.Course.objects.filter(category_id=category_id).all().order_by("order")
        ser_obj = CourseSerializer(queryset,many=True)
        return Response(ser_obj.data)

class CourseDetailView(APIView):
    def get(self,request,pk):
        # 根据pk获取课程详情
        course_detail_obj = models.CourseDetail.objects.filter(course_id=pk).first()
        if not course_detail_obj:
            return Response({"code":1001,"error":"查询的课程不存在"})

        ser_obj = CourseDetailSerializer(course_detail_obj)
        return Response(ser_obj.data)

class CourseChapterView(APIView):
    def get(self,request,pk):
        queryset = models.CourseChapter.objects.filter(course_id=pk).all().order_by("chapter")
        ser_obj = CourseChapterSerializer(queryset,many=True)
        return Response(ser_obj.data)

class CourseCommentView(APIView):
    def get(self, request, pk):
        # 通过课程id找到课程所有的评论
        queryset = models.Course.objects.filter(id=pk).first().course_comments.all()
        # 序列化
        ser_obj = CourseCommentSerializer(queryset, many=True)
        # 返回
        return Response(ser_obj.data)


class QuestionView(APIView):
    def get(self, request, pk):
        queryset = models.Course.objects.filter(id=pk).first().often_ask_questions.all()
        ser_obj = QuestionSerializer(queryset, many=True)
        return Response(ser_obj.data)



