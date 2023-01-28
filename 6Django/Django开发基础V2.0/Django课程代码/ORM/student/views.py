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

    # INSERT INTO `db_student` (`name`, `age`, `sex`, `birthday`, `classmate`, `description`, `chinese_score`, `math_score`) VALUES ('王五', 30, 1, '1998-03-12', '一班', '知识就是力量', 80, 60);
    # Student.objects.create(name='王五',age=30,sex=1,birthday='1998-3-12',description='知识就是力量',chinese_score=80,math_score=60,classmate='一班')
    # Student.objects.create(name='赵柳',age=26,sex=1,birthday='1998-5-12',chinese_score=78,math_score=50,classmate='一班')
    # Student.objects.create(name='王二',age=18,sex=0,birthday='1998-1-12',chinese_score=90,math_score=80,classmate='二班')
    # Student.objects.create(name='马原',age=18,sex=0,birthday='1998-8-12',chinese_score=98,math_score=90,classmate='三班')
    # Student.objects.create(name='赵六',age=34,sex=1,birthday='1995-3-12',chinese_score=67,math_score=90,classmate='三班')
    # Student.objects.create(name='马力',age=19,sex=0,birthday='1999-1-12',chinese_score=96,math_score=59,classmate='二班')
    # Student.objects.create(name='马媛',age=30,sex=1,birthday='2000-2-12',chinese_score=78,math_score=89,classmate='二班')
    # Student.objects.create(name='小媛',age=30,sex=1,birthday='2000-2-12',chinese_score=78,math_score=89,classmate='一班')
    # Student.objects.create(name='马小',age=30,sex=1,birthday='2000-2-12',chinese_score=78,math_score=89,classmate='二班')
    # Student.objects.create(name='王小于',age=30,sex=1,birthday='2000-2-12',chinese_score=78,math_score=89,classmate='三班')

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
    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` LIMIT 21;
    # student_list = Student.objects.all()
    # print("student_list",student_list)

    # （2）first()  last() : 返回模型类对象
    # 查询第一个学生
    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` LIMIT 1;
    # stu = Student.objects.all()[0]
    # print(stu.name)
    # print(stu.age)
    # print(student_list.name)

    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` ORDER BY `db_student`.`id` ASC LIMIT 1;
    # stu = Student.objects.first()
    # print(stu.name)
    # print(stu.age)
    #SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` ORDER BY `db_student`.`id` DESC LIMIT 1;
    # stu = Student.objects.last()
    # print(stu.name)
    # print(stu.age)

    # （3）filter方法：where语句： 返回时一个queryset对象

    # 查询所有的女生
    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` WHERE `db_student`.`sex` = 0 LIMIT 21;
    # student_list = Student.objects.filter(sex=0)
    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` WHERE (`db_student`.`age` = 28 AND `db_student`.`sex` = 0) LIMIT 21;
    # student_list = Student.objects.filter(sex=0,age=28) # 逻辑与
    # print("student_list", student_list) # <QuerySet [<Student: 小阳 28>]>

    # (4) exclude:排除符合条件的记录： 返回时一个queryset对象

    # 查询除了张三以外的所有学生记录
    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` WHERE NOT (`db_student`.`name` = '张三') LIMIT 21;
    # student_list = Student.objects.exclude(name="张三")
    # print("student_list",student_list)

    # (5) get方法: 有且只有一条符合条件的记录:返回一个查询到的模型类对象

    # stu = Student.objects.get(sex=0)
    # stu = Student.objects.get(sex=2)

    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` WHERE `db_student`.`id` = 7 LIMIT 21;
    # stu = Student.objects.get(id=7)
    # print(stu.name)
    # print(stu.age)

    # (6) order_by() : 是queryset类型的一个内置方法，返回时一个queryset对象

    #  将所有的学生按着年龄从高到低排序   如何age年龄相同,按id降序
    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` ORDER BY `db_student`.`age` DESC, `db_student`.`id` DESC LIMIT 21;
    # student_list = Student.objects.all().order_by("-age","-id")
    # print("student_list",student_list)

    # (7) count() :是queryset类型的一个内置方法，返回int对象

    # 查询学生个数
    # SELECT COUNT(*) AS `__count` FROM `db_student`;
    # count = Student.objects.all().count()
    # print("count",count)
    # 查询女生的个数
    # SELECT COUNT(*) AS `__count` FROM `db_student` WHERE `db_student`.`sex` = 0;
    # count = Student.objects.filter(sex=0).count()
    # print("count", count)

    # (8) exist: 是queryset类型的一个内置方法，判断是否存在记录，返回一个布尔值

    # 查询学生表中是否存在记录
    # SELECT (1) AS `a` FROM `db_student` LIMIT 1;
    # print(Student.objects.exists())

    # (9) values和values_list: 翻译的是select语句: 返回时一个queryset对象
    # SELECT `db_student`.`name`, `db_student`.`age` FROM `db_student` LIMIT 21;
    # student_list = Student.objects.all().values("name","age")
    # print(student_list)
    # import json
    # print(json.dumps(list(student_list),ensure_ascii=False)) # [{"name": "王五", "age": 30}, {"name": "赵柳", "age": 26}, ....]

    # SELECT `db_student`.`name`, `db_student`.`age` FROM `db_student` LIMIT 21;
    # student_list = Student.objects.all().values_list("name", "age")
    # print(student_list) # <QuerySet [('张三', 22), ('李四', 32)]>
    # 扩展 查询所有男生的姓名和年龄
    # SELECT `db_student`.`name`, `db_student`.`age` FROM `db_student` WHERE `db_student`.`sex` = 1 LIMIT 21;
    # student_list = Student.objects.filter(sex=1).values("name","age")
    # print(student_list) # <QuerySet [{'name': '张三', 'age': 22}, {'name': '李四', 'age': 32}, {'name': '王五', 'age': 34}]>

    # (10) distinct: 去重,是queryset类型的一个内置方法

    # Student.objects.all().distinct() # 无法去重 等于针对主键去重, 主键唯一等于没有去重
    # SELECT DISTINCT `db_student`.`age` FROM `db_student` LIMIT 21;
    # print(Student.objects.values("age").distinct())

    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` LIMIT 21;
    # print(Student.objects.filter())

    return HttpResponse("查询成功")


def select2_student(request):
    '''
    二、模糊查询
    :param request:
    :return:
    '''

    # 查询所有名字中小开头的学生
    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` WHERE `db_student`.`name` LIKE BINARY '小%' LIMIT 21;
    # stu_list = Student.objects.filter(name__startswith="小")

    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` WHERE `db_student`.`name` LIKE BINARY '%小' LIMIT 21;
    # stu_list = Student.objects.filter(name__endswith="小")

    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` WHERE `db_student`.`name` LIKE BINARY '%小%' LIMIT 21;
    # stu_list = Student.objects.filter(name__contains="小")
    # print("stu_list",stu_list)

    # 查询description不为空的所有的记录
    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` WHERE `db_student`.`description` IS NOT NULL LIMIT 21;
    # stu_list = Student.objects.filter(description__isnull=False)
    # print(stu_list)

    # gt lt gte lte
    # 查询所有年龄大于30的学生
    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` WHERE `db_student`.`age` > 30 LIMIT 21; args=(30,)
    # stu_list = Student.objects.filter(age__gt=30)
    # print(stu_list)

    # 查询年龄在20-30之间的学生
    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` WHERE `db_student`.`age` BETWEEN 20 AND 30 LIMIT 21;
    # stu_list = Student.objects.filter(age__range=(20,30))
    # print(stu_list )

    # 查询年龄是22,32,34的所有学生
    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` WHERE `db_student`.`age` IN (22, 32, 34) LIMIT 21;
    # stu_list = Student.objects.filter(age__in=[22,32,34])
    # print(stu_list)

    # 查询出生1998年的学生
    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` WHERE (EXTRACT(MONTH FROM `db_student`.`birthday`) = 5 AND `db_student`.`birthday` BETWEEN '1998-01-01' AND '1998-12-31') LIMIT 21;
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
    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` WHERE `db_student`.`chinese_score` > `db_student`.`math_score` LIMIT 21;
    # stu_list = Student.objects.filter(chinese_score__gt = F("math_score"))
    # print(stu_list)

    # (2) Q函数

    # Student.objects.filter(sex=0,age=22)
    # Student.objects.filter(sex=0).filter(age=22)

    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` WHERE (`db_student`.`age` > 30 OR `db_student`.`sex` = 0) LIMIT 21;
    # stu_list = Student.objects.filter(Q(age__gt=30)|Q(sex=0))
    # SELECT `db_student`.`id`, `db_student`.`name`, `db_student`.`age`, `db_student`.`sex`, `db_student`.`birthday`, `db_student`.`classmate`, `db_student`.`description`, `db_student`.`chinese_score`, `db_student`.`math_score` FROM `db_student` WHERE (`db_student`.`age` > 30 AND NOT (`db_student`.`sex` = 0)) LIMIT 21;
    # stu_list = Student.objects.filter(Q(age__gt=30)&~Q(sex=0))

    # stu_list = Student.objects.filter(Q(Q(age__gt=30)&Q(sex=0))&Q())
    # print(stu_list)

    # (3) 聚合函数：aggregate()

    from django.db.models import Sum, Count, Avg, Max, Min
    # 查询所有学生的平均年龄
    # SELECT AVG(`db_student`.`age`) AS `avg_age` FROM `db_student`;
    # ret = Student.objects.aggregate(avg_age = Avg("age"))
    # print(ret)

    # SELECT MAX(`db_student`.`chinese_score`) AS `max_chi_score` FROM `db_student`;
    # ret = Student.objects.aggregate(max_chi_score = Max("chinese_score"))
    # print(ret) # {'max_chi_score': 100}

    # (4) 分组统计函数：annotate(): group by values()对应的是group by的字段

    # 查询不同性别学生的语文平均成绩
    # SELECT `db_student`.`sex`, AVG(`db_student`.`chinese_score`) AS `avg_chi` FROM `db_student` GROUP BY `db_student`.`sex` ORDER BY NULL LIMIT 21;
    # ret = Student.objects.values("sex").annotate(avg_chi = Avg("chinese_score"))
    # print(ret) # <QuerySet [{'sex': 1, 'avg_chi': 92.0}, {'sex': 0, 'avg_chi': 95.3333}]>

    # 查询每个班级的数学的平均成绩
    # SELECT `db_student`.`classmate`, AVG(`db_student`.`math_score`) AS `avg_math` FROM `db_student` GROUP BY `db_student`.`classmate` ORDER BY NULL LIMIT 21;
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
    # UPDATE `db_student` SET `chinese_score` = 100, `math_score` = 100 WHERE `db_student`.`age` > 30;
    # Student.objects.filter(age__gt=30).update(chinese_score=100,math_score=100)

    # 将年龄小于30岁的学生的语文成绩降低20分

    from django.db.models import F
    # UPDATE `db_student` SET `chinese_score` = (`db_student`.`chinese_score` - 20) WHERE `db_student`.`age` < 30;
    # Student.objects.filter(age__lt=30).update(chinese_score=F("chinese_score")-20)

    return HttpResponse("修改成功")


def delete_student(request):

    # 方式1：基于模型类对象删除
    # DELETE FROM `db_student` WHERE `db_student`.`id` IN (11);
    # Student.objects.get(pk=11).delete()

    # 方式2：基于queryset删除
    # DELETE FROM `db_student` WHERE `db_student`.`chinese_score` < 60;
    # Student.objects.filter(chinese_score__lt=60).delete()

    return HttpResponse("删除成功")
