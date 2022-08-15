"""
@FileName：admin_interface.py
@Author：chengkanghua
@Time：2022/8/14 8:51 下午
"""
'''管理员接口'''
from db import models

def register(username, password):
    admin_obj = models.Admin.select(username)
    if admin_obj is None:
    # if not admin_obj:
        admin_obj = models.Admin(username, password)
        admin_obj.save()
        return True,'register success'
    else:
        return False,'register failure'


def login(username, password):
    # 判断用户是否存在
    admin_obj = models.Admin.select(username)
    if admin_obj is None:
        return False,'username not exists'
    # 校验密码
    if password == admin_obj.password:
        return True,'login success'
    else:
        return False,'password is incorrect'

def create_school(school_name, school_address, admin_name):
    school_obj = models.School.select(school_name)
    if school_obj:
        return False,'school_name already exists'
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_school(school_name, school_address)
    return True,f'{school_name}create School successed'

def create_course(school_name,course_name,admin_name):
    # check if course_name already exists
    school_obj = models.Course.select(school_name)
    if course_name in school_obj.course_list:
        return False,'course_name already exists'
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(course_name, school_name)
    return True,f'{course_name} create successed and banding {school_name} successed'

def create_teacher(teacher_name,admin_name,teacher_pwd='123'):
    teacher_name = models.Teacher.select(teacher_name)
    if teacher_name:
        return False,'teacher_name already exists'
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name, teacher_pwd)
    return True,f'{teacher_name} create successed'



