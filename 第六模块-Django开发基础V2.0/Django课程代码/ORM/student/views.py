from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import Student


def add_student(request):
    # 添加记录

    # （1）方式：实例化+save()    模型类对象映射表记录
    # import datetime
    # birth = datetime.date(2012,12,12)
    # Student(name="张三",age=22,sex=1,birthday=birth)
    # stu = Student(name="李四", age=32, sex=1, birthday="2001-12-12")
    # stu.save() # 创建对应的sql语句并执行
    # print(stu.id)
    # print(stu.name)
    # print(stu.age)

    # 方式2： create方法：返回了创建的模型类对象

    # stu = Student.objects.create(name="王五", age=34, sex=1, birthday="1998-3-12")
    # print(stu.id)
    # print(stu.name)
    # print(stu.age)

    return HttpResponse("添加记录成功！")


def select_student(request):
    '''
    一、查询API
    :param request:
    :return:
    '''

    # （1）all函数：返回的一个Queryset
    # about Queryset: Queryset（查询集）是一个类似于list的数据类型，里面的元素是统一类型，比如模型类对象或者字典

    # 查询所有的学生
    # student_list = Student.objects.all()
    # print("student_list",student_list)

    # （2）first()  last() : 返回模型类对象
    # 查询第一个学生
    # stu = Student.objects.all()[0]
    # print(stu.name)
    # print(stu.age)
    # print(student_list.name)

    # stu = Student.objects.first()
    # print(stu.name)
    # print(stu.age)
    # stu = Student.objects.last()
    # print(stu.name)
    # print(stu.age)

    # （3）filter方法：where语句： 返回时一个queryset对象

    # 查询所有的女生
    # student_list = Student.objects.filter(sex=0)
    # student_list = Student.objects.filter(sex=0,age=28) # 逻辑与
    # print("student_list", student_list) # <QuerySet [<Student: 小阳 28>]>

    # (4) exclude:排除符合条件的记录： 返回时一个queryset对象

    # 查询除了张三以外的所有学生记录
    # student_list = Student.objects.exclude(name="张三")
    # print("student_list",student_list)

    # (5) get方法: 有且只有一条符合条件的记录:返回一个查询到的模型类对象

    # stu = Student.objects.get(sex=0)
    # stu = Student.objects.get(sex=2)
    # stu = Student.objects.get(id=19)
    # print(stu.name)
    # print(stu.age)

    # (6) order_by() : 是queryset类型的一个内置方法，返回时一个queryset对象

    #  将所有的学生按着年龄从高到低排序
    # student_list = Student.objects.all().order_by("-age","-id")
    # print("student_list",student_list)

    # (7) count() :是queryset类型的一个内置方法，返回int对象

    # 查询学生个数
    # count = Student.objects.all().count()
    # print("count",count)
    # 查询女生的个数
    # count = Student.objects.filter(sex=0).count()
    # print("count", count)

    # (8) exist: 是queryset类型的一个内置方法，判断是否存在记录，返回一个布尔值

    # 查询学生表中是否存在记录
    # print(Student.objects.exists())

    # (9) values和values_list: 翻译的是select语句: 返回时一个queryset对象

    # student_list = Student.objects.all().values("name","age")
    # print(student_list)
    # import json
    # print(json.dumps(list(student_list),ensure_ascii=False))
    # student_list = Student.objects.all().values_list("name", "age")
    # print(student_list) # <QuerySet [('张三', 22), ('李四', 32), ('王五', 34), ('小雨', 22), ('小阳', 28), ('小茜', 31)]>
    # 扩展 查询所有男生的姓名和年龄

    # student_list = Student.objects.filter(sex=1).values("name","age")
    # print(student_list) # <QuerySet [{'name': '张三', 'age': 22}, {'name': '李四', 'age': 32}, {'name': '王五', 'age': 34}]>

    # (10) distinct: 去重,是queryset类型的一个内置方法

    # Student.objects.all().distinct() # 无法去重
    # print(Student.objects.values("age").distinct())

    print(Student.objects.filter())

    return HttpResponse("查询成功")


def select2_student(request):
    '''
    二、模糊查询
    :param request:
    :return:
    '''

    # 查询所有名字中小开头的学生
    # stu_list = Student.objects.filter(name__startswith="小")
    # stu_list = Student.objects.filter(name__endswith="小")
    # stu_list = Student.objects.filter(name__contains="小")
    # print("stu_list",stu_list)

    # 查询description不为空的所有的记录
    # stu_list = Student.objects.filter(description__isnull=False)
    # print(stu_list)

    # gt lt gte lte
    # 查询所有年龄大于30的学生
    # stu_list = Student.objects.filter(age__gt=30)
    # print(stu_list)

    # 查询年龄在20-30之间的学生
    # stu_list = Student.objects.filter(age__range=(20,30))
    # print(stu_list )

    # 查询年龄是22,32,34的所有学生
    # stu_list = Student.objects.filter(age__in=[22,32,34])
    # print(stu_list)

    # 查询出生1998年的学生
    # stu_list = Student.objects.filter(birthday__year=1998,birthday__month=5)
    # print(stu_list)

    return HttpResponse("模糊查询成功")


def select3_student(request):
    '''

    三、高阶查询
    :param request:
    :return:
    '''
    from django.db.models import F, Q

    # (1) F函数: 两个属性比较使用F对象.
    # 查询语文成绩大于数学成绩的学生
    # stu_list = Student.objects.filter(chinese_score__gt = F("math_score"))
    # print(stu_list)

    # (2) Q函数

    # Student.objects.filter(sex=0,age=22)
    # Student.objects.filter(sex=0).filter(age=22)

    # stu_list = Student.objects.filter(Q(age__gt=30)|Q(sex=0))
    # stu_list = Student.objects.filter(Q(age__gt=30)&~Q(sex=0))
    # stu_list = Student.objects.filter(Q(Q(age__gt=30)&Q(sex=0))&Q())
    # print(stu_list)

    # (3) 聚合函数：aggregate()

    from django.db.models import Sum, Count, Avg, Max, Min
    # 查询所有学生的平均年龄
    # ret = Student.objects.aggregate(avg_age = Avg("age"))
    # print(ret)

    # ret = Student.objects.aggregate(max_chi_score = Max("chinese_score"))
    # print(ret) # {'max_chi_score': 100}

    # (4) 分组统计函数：annotate(): group by  values()对应的是group by的字段

    # 查询不同性别学生的语文平均成绩

    # ret = Student.objects.values("sex").annotate(avg_chi = Avg("chinese_score"))
    # print(ret) # <QuerySet [{'sex': 1, 'avg_chi': 92.0}, {'sex': 0, 'avg_chi': 95.3333}]>

    # 查询每个班级的数学的平均成绩

    # ret = Student.objects.values("classmate").annotate(avg_math = Avg("math_score")) 
    # print(ret)

    # 思考：
    # Student.objects.all().annotate(avg_math = Avg("math_score"))

    # （5）原生sql

    # ret = Student.objects.raw("SELECT id,name,age FROM db_student")  # student 可以是任意一个模型
    # # 这样执行获取的结果无法通过QuerySet进行操作读取,只能循环提取
    # print(ret, type(ret))
    # for stu in ret:
    #      print(stu, type(stu),stu.name,stu.age)

    return HttpResponse("高阶查询成功")


def update_student(request):
    # 方式1：基于模型对象save

    # stu = Student.objects.get(name="李四")
    # print(stu.name)
    # print(stu.age)
    # stu.chinese_score = 88
    # stu.save()  # 创建对应的sql语句并执行

    # 方式2：queryset对象的update方法

    # Student.objects.filter(age__gt=30).update(chinese_score=100,math_score=100)

    # 将年龄小于30岁的学生的语文成绩降低20分

    # from django.db.models import F
    # Student.objects.filter(age__lt=30).update(chinese_score=F("chinese_score")-20)

    return HttpResponse("修改成功")


def delete_student(request):

    # 方式1：基于模型类对象删除

    # Student.objects.get(pk=15).delete()

    # 方式2：基于queryset删除

    # Student.objects.filter(chinese_score__lt=60).delete()

    return HttpResponse("删除成功")
