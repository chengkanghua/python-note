from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from .models import Student, StudentDetail, Course, Clas


def index(request):
    # 获取所有的学生数据
    student_list = Student.objects.all()

    return render(request, "student/index.html", {"student_list": student_list})


def add_student(request):
    if request.method == "GET":

        class_list = Clas.objects.all()
        course_list = Course.objects.all()
        return render(request, "student/add_stu.html", {"class_list": class_list, "course_list": course_list})

    else:
        # 获取客户端数据
        # <QueryDict: {'name': ['alvin'], 'age': ['22'], 'sex': ['2'], 'birthday': ['2021-10-26'], 'clas_id': ['8']}>
        print(request.POST)
        # 添加数据到数据库
        # 方式1
        # name = request.POST.get("user")
        # age = request.POST.get("age")
        # sex = request.POST.get("sex")
        # birthday = request.POST.get("birthday")
        # clas_id = request.POST.get("clas_id")
        #
        # Student.objects.create(name=name,age=age,sex=sex,birthday=birthday,clas_id=clas_id)
        # 方式2
        # 前提： 客户端form表单的name值要与models中的字段保持一致
        stu = Student.objects.create(**request.POST.dict())

        return redirect("/student/")


def delete_student(request, del_id):
    student = Student.objects.get(pk=del_id)

    if request.method == "GET":
        return render(request, "student/delete_stu.html", {"student": student})

    else:
        student.delete()
        return redirect("/student/")


def edit_student(request,edit_id):
    edit_stu = Student.objects.get(pk=edit_id)
    if request.method == "GET":

        class_list = Clas.objects.all()
        course_list = Course.objects.all()
        return render(request, "student/edit_stu.html", {"edit_stu": edit_stu, "class_list": class_list,"course_list":course_list})
    else:
        print("request.POST",request.POST)
        course_id_list = request.POST.getlist("course_id_list")
        # 获取客户端数据
        data = request.POST.dict()
        print("data",data)
        # 删除并获取课程id列表
        data.pop("course_id_list")
        # 更新除了多对多以外的数据
        Student.objects.filter(pk=edit_id).update(**data)
        # 多对多关系的重置
        edit_stu.courses.set(course_id_list)
        return redirect("/student/")





def elective(request):

    if request.method == "GET":
        course_list = Course.objects.all()
        return render(request,"student/course.html",{"course_list":course_list})

    else:
        print(request.POST)
        course_id_list =request.POST.getlist("course_id_list")
        stu_id = 14
        stu = Student.objects.get(pk=stu_id)
        stu.courses.set(course_id_list)

        return redirect("/student/")