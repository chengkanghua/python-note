"""
@FileName：admin.py
@Author：chengkanghua
@Time：2022/8/14 8:50 下午
"""

'''admin_view'''
from interface import admin_interface
from interface import common_interface
from lib import common

admin_info = {
    'user': None
}

def register():
    while True:
        username = input('Enter username:>').strip()
        password = input('Enter password:>').strip()
        re_password = input('Enter confirm password:>').strip()
        if password == re_password and password != '':
            # 调用接口层注册用户
            flag , msg = admin_interface.register(username, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('password is incorrect.')

def login():
    while True:
        username = input('Enter username:>').strip()
        password = input('Enter password:>').strip()
        flag,msg = admin_interface.login(username,password)
        if flag:
            print(msg)
            admin_info['user'] = username
            break
        else:
            print(msg)

@common.auth('admin')
def create_shool():
    while True:
        school_name = input('Enter school_name:>').strip()
        school_address = input('Enter school_address:>').strip()
        flag , msg = admin_interface.create_school(school_name,school_address,admin_info.get('user'))
        if flag:
            print(msg)
            break
        else:
            print(msg)

@common.auth('admin')
def create_course():
    while True:
        # 1.让管理员先选择学校
        # 1.1 调用接口，获取所有学校的名称并打印
        flag , school_list = common_interface.get_all_school()
        if not flag:
            print(school_list)
            break
        for index,school_name in enumerate(school_list):
            print(index, school_name)
        choice = input("please enter a school number: ")
        if not choice.isdigit():
            print("please enter a number: ")
            continue
        choice = int(choice)
        if choice not in range(len(school_list)):
            print(f"please enter a number between 0 and {len(school_list) - 1}")
            continue
        school_name = school_list[choice]
        course_name = input("Please enter a course_name: ")
        flag,msg = admin_interface.create_course(school_name,course_name,admin_info.get('suer'))
        if flag:
            print(msg)
            break
        else:
            print(msg)

@common.auth('admin')
def create_teacher():
    while True:
        # 1.让管理员输入创建的老师名字
        teacher_name = input('please enter a teacher name:: ').strip()
        # 2.调用接口创建老师
        flag, msg = admin_interface.create_teacher(teacher_name, admin_info.get('user'))
        if flag:
            print(msg)
            break

        else:
            print(msg)


func_dict = {
    '1':register,
    '2':login,
    '3':create_shool,
    '4':create_course,
    '5':create_teacher
}
def admin_view():
    while True:
        print('''
            - 1.register 
            - 2.login 
            - 3.create_shool
            - 4.create_course
            - 5.create_teacher
        ''')
        choice = input("please enter your select number: ").strip()
        if choice == 'q':
            break
        if choice not in func_dict:
            print("error : enter your select number and try again ")
            continue

        func_dict.get(choice)()