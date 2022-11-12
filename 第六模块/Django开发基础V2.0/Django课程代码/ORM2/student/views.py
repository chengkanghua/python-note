from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import Student, StudentDetail, Course, Clas


def add_student(request):
    # ********************* 一对多,一对一的关联属性

    # stu = Student.objects.create(name="王五", age=23, sex=1, birthday="1991-11-12", clas_id=9, stu_detail_id=6)
    # print(stu.name)
    # print(stu.age)
    # print(stu.sex)
    # print(stu.clas_id)  # 6
    # print(stu.stu_detail_id)  # 5
    # print(stu.clas)  # 模型类对象
    # print(stu.stu_detail)  # 模型类对象
    #
    # 查询stu这个学生的班级名称
    # print(stu.clas.name)
    # 查询stu这个学生的手机号
    # print(stu.stu_detail.tel)

    # lisi = Student.objects.get(name="李四")
    # print(lisi.name)
    # print(lisi.age)
    # print(lisi.sex)
    # print(lisi.clas_id)
    # print(lisi.clas.name)
    # print(lisi.stu_detail.addr)
    # print(lisi.stu_detail.tel)

    # *********************  多对多的关联记录的增删改查

    # stu = Student.objects.create(name="rain", age=33, sex=1, birthday="1996-11-12", clas_id=9, stu_detail_id=7)

    # (1) 添加多对多的数据

    # 添加多对多方式1
    # c1 = Course.objects.get(title="思修")
    # c2 = Course.objects.get(title="逻辑学")
    # stu.courses.add(c1,c2)

    # 添加多对多方式2
    # stu = Student.objects.get(name="张三")
    # stu.courses.add(5,7)

    # 添加多对多方式3
    # stu = Student.objects.get(name="李四")
    # stu.courses.add(*[6,7])

    # (2) 删除多对多记录

    # stu = Student.objects.get(name="李四")
    # stu.courses.remove(7)

    # (3) 清空多对多记录：clear方法

    # stu = Student.objects.get(name="rain")
    # stu.courses.clear()

    # (4) 重置多对多记录：set方法

    # stu = Student.objects.get(name="李四")
    # stu.courses.set([5,8])

    # (5) 多对多记录查询： all

    # 查询李四所报课程的名称
    # stu = Student.objects.get(name="李四")
    # courses = stu.courses.all()
    # courses = stu.courses.all().values("title")
    # print(courses)  # <QuerySet [<Course: Course object (5)>, <Course: Course object (8)>]>

    return HttpResponse("添加关联记录成功")


def select_student(request):
    '''
    正向查询：通过关联属性查询属于正向查询，反之则称为反向查询


    基于对象的关联查询(子查询)

    '''
    # **********************************  一对多查询
    # 查询张三所在班级的名称
    # stu = Student.objects.get(name="张三")
    # print(stu.clas.name)

    # 查询计算机科学与技术2班有哪些学生

    # clas = Clas.objects.get(name="计算机科学与技术2班")
    # 反向查询方式1：
    # ret = clas.student_set.all()  # 反向查询按表名小写_set
    # print(ret) # <QuerySet [<Student: 张三>, <Student: 李四>]>
    # 反向查询方2：

    # print(clas.student_list.all())  # <QuerySet [<Student: 张三>, <Student: 李四>]>

    # **********************************  一对一查询

    # 查询李四的手机号
    # stu = Student.objects.get(name="李四")
    # print(stu.stu_detail.tel)

    # 查询110手机号的学生姓名和年龄

    # stu_detail = StudentDetail.objects.get(tel="110")
    # 反向查询方式1： 表名小写
    # print(stu_detail.student.name)
    # print(stu_detail.student.age)
    # 反向查询方式2： related_name
    # print(stu_detail.stu.name)
    # print(stu_detail.stu.age)

    # **********************************  多对多查询

    # 查询张三所报课程的名称

    # stu = Student.objects.get(name="张三")
    # print(stu.courses.all())  # QuerySet [<Course: 近代史>, <Course: 篮球>]>

    # 查询选修了近代史这门课程学生的姓名和年龄
    # course = Course.objects.get(title="近代史")
    # 反向查询方式1： 表名小写_set
    # print(course.student_set.all()) # <QuerySet [<Student: 张三>, <Student: 李四>]>

    # 反向查询方式2：related_name
    # print(course.students.all())
    # print(course.students.all().values("name","age")) # <QuerySet [{'name': '张三', 'age': 22}, {'name': '李四', 'age': 24}]>

    return HttpResponse("关联子查询成功")


def select2_student(request):
    '''
    基于双下划线跨表查询(join查询)
    '''

    # 查询张三的年龄
    # ret = Student.objects.filter(name="张三").values("age")
    # print(ret) # <QuerySet [{'age': 22}]>

    # (1) 查询年龄大于22的学生的姓名以及所在名称班级
    # select db_student.name,db_class.name from db_student inner join db_class on db_student.clas_id = db_class.id where db_student.age>22;

    # 方式1 ： Student作为基表
    # ret = Student.objects.filter(age__gt=22).values("name","clas__name")
    # print(ret)
    # 方式2 ：Clas表作为基表
    # ret = Clas.objects.filter(student_list__age__gt=22).values("student_list__name","name")
    # print(ret)

    # (2) 查询计算机科学与技术2班有哪些学生

    # ret = Clas.objects.filter(name="计算机科学与技术2班").values("student_list__name")
    # print(ret)  #<QuerySet [{'student_list__name': '张三'}, {'student_list__name': '李四'}]>

    # (3) 查询张三所报课程的名称

    # ret = Student.objects.filter(name="张三").values("courses__title")
    # print(ret) # <QuerySet [{'courses__title': '近代史'}, {'courses__title': '篮球'}]>

    # (4) 查询选修了近代史这门课程学生的姓名和年龄

    # ret = Course.objects.filter(title="近代史").values("students__name","students__age")
    # print(ret) # <QuerySet [{'students__name': '张三', 'students__age': 22}, {'students__name': '李四', 'students__age': 24}]>

    # (5) 查询李四的手机号

    # ret = Student.objects.filter(name='李四').values("stu_detail__tel")
    # print(ret)  # <QuerySet [{'stu_detail__tel': '911'}]>

    # (6) 查询手机号是110的学生的姓名和所在班级名称

    # 方式1
    # ret = StudentDetail.objects.filter(tel="110").values("stu__name","stu__clas__name")
    # print(ret) # <QuerySet [{'stu__name': '张三', 'stu__clas__name': '计算机科学与技术2班'}]>

    # 方式2：
    # ret = Student.objects.filter(stu_detail__tel="110").values("name","clas__name")
    # print(ret) # <QuerySet [{'name': '张三', 'clas__name': '计算机科学与技术2班'}]>

    # 分组查询
    # from django.db.models import Avg, Count, Max, Min
    # ret = Student.objects.values("sex").annotate(c = Count("name"))
    # print(ret) # <QuerySet [{'sex': 0, 'c': 1}, {'sex': 1, 'c': 3}]>

    # （1）查询每一个班级的名称以及学生个数

    # ret = Clas.objects.values("name").annotate(c = Count("student_list__name"))
    # print(ret) # <QuerySet [{'name': '网络工程1班', 'c': 0}, {'name': '网络工程2班', 'c': 0}, {'name': '计算机科学与技术1班', 'c': 0}, {'name': '计算机科学与技术2班', 'c': 1}, {'name': '软件1班', 'c': 3}]>

    # （2）查询每一个学生的姓名,年龄以及选修课程的个数

    # ret = Student.objects.values("name","age").annotate(c=Count("courses__title"))
    # print(ret) # <QuerySet [{'name': 'rain', 'c': 0}, {'name': '张三', 'c': 2}, {'name': '李四', 'c': 2}, {'name': '王五', 'c': 0}]>

    # ret = Student.objects.all().annotate(c=Count("courses__title")).values("name","age","sex","c")
    # print(ret)

    # (3) 每一个课程名称以及选修学生的个数
    # ret = Course.objects.all().annotate(c = Count("students__name")).values("title","c")
    # print(ret) # <QuerySet [{'title': '近代史', 'c': 2}, {'title': '思修', 'c': 0}, {'title': '篮球', 'c': 1}, {'title': '逻辑学', 'c': 1}, {'title': '轮滑', 'c': 0}]>

    # (4)  查询选修课程个数大于1的学生姓名以及选修课程个数
    # ret = Student.objects.all().annotate(c=Count("courses__title")).filter(c__gt=1).values("name","c")
    # print(ret) # <QuerySet [{'name': '张三', 'c': 2}, {'name': '李四', 'c': 2}]>

    # (5) 查询每一个学生的姓名以及选修课程个数并按着选修的课程个数进行从低到高排序
    # ret = Student.objects.all().annotate(c=Count("courses__title")).order_by("c").values("name","c")
    # print(ret)

    return HttpResponse("关联join查询成功")



