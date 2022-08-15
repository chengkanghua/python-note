"""
@FileName：src.py
@Author：chengkanghua
@Time：2022/8/14 8:50 下午
"""

'''用户视图层'''
from core import admin
from core import student
from core import teacher
func_dict = {
    '1': admin.admin_view,
    '2': student.student_view,
    '3': teacher.teacher_view,
}

def run():
    while True:
        print('''
        =====================欢迎来到选课系统================
                      1.管理员功能
                      2.学生功能
                      3.老师功能
        =========================end=======================
        ''')
        choice = input("please enter your number:").strip()
        if choice not in func_dict:
            print("error enter")
            continue

        func_dict.get(choice)()


