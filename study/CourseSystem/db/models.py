"""
@FileName：models.py
@Author：chengkanghua
@Time：2022/8/14 8:52 下午
"""
from db import db_handler
'''
学校类  学员类 课程类 讲师类 管理员类
'''
# 基类 所有子类继承 select save
class Base(object):
    # 查看数据
    @classmethod
    def select(cls,username):
        obj = db_handler.select_data(cls,username)
        return obj
    # 保存数据
    def save(self):
        db_handler.save_data(self)


# 管理员类
class Admin(Base):
    def __init__(self,username=None,password=None):
        self.username = username
        self.password = password

    # create school
    def create_school(self,school_name,school_address):
        school_obj = School(school_name,school_address)
        school_obj.save()

    # create course
    def create_course(self,school_obj,course_name):
        course_obj = Course(course_name)
        course_obj.save()
        # 添加到学校的课程列表
        school_obj.course_list.append(course_obj)
        school_obj.save()

    # create teacher
    def create_teacher(self,teacher_name,teacher_pwd):
        teacher_obj = Teacher(teacher_name,teacher_pwd)
        teacher_obj.save()

class School(Base):
    def __init__(self,school_name,school_address):
        self.school_name = school_name
        self.school_address = school_address
        # 课程列表  每所学校对应的课程
        self.course_list = []

class Student(Base):
    pass

class Course(Base):
    def __init__(self,course_name):
        self.course_name = course_name
        # 每个课程对应的学生列表
        self.student_list = []


class Teacher(Base):
    def __init__(self,teacher_name,teacher_pwd):
        self.teacher_name = teacher_name
        self.teacher_pwd = teacher_pwd
        # 老师教课列表
        self.teacher_course_list = []








