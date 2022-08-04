#用户认证,信用卡认证，管理员认证模块
import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
user_dic = BASE_DIR + r"/db/user_data"
creditcard_dic = BASE_DIR + r"/db/creditcard_data"


'''认证装饰器'''
def auth(auth_type):
     def out_wrapper(func):
        if auth_type == "user_auth": #用户认证
            def wrapper():
                res = func
                user_name = input("请输入登录用户名 ：").strip()
                user_pwd = input("请输入登录密码 ：").strip()
                if len(user_name)>0:
                    with open(user_dic,"r") as f:
                        user_data = json.loads(f.read())
                        if user_name in user_data.keys() and user_pwd == user_data[user_name]["password"]:
                            if user_data[user_name]["locked"] == False:
                                print("[ %s ] 用户认证成功"%(user_name))
                                return  res,user_name
                            else:
                                print("[ %s ] 用户已经被锁定，认证失败"%(user_name))
                        else:
                            print("[ %s ] 用户或密码错误，认证失败"%(user_name))
                else:
                    print("[ %s ] 用户输入不能为空"%(user_name))
            return wrapper

        if auth_type == "creditcard_auth": #信用卡认证
            def wrapper():
                res = func()
                creditcard = input("请输入信用卡卡号(6位数字):").strip()
                password = input("请输入信用卡密码 : ").strip()
                if creditcard:
                    with open(creditcard_dic,"r") as f:
                        creditcard_data = json.loads(f.read())
                        if creditcard in creditcard_data.keys() and password == creditcard_data[creditcard]["password"]:
                            if creditcard_data[creditcard]["locked"] == False:
                                print("信用卡 [ %s ] 验证成功"%(creditcard))

                                return res,creditcard
                            else:
                                print("信用卡 [ %s ]已经被冻结，请使用其他信用卡"%(creditcard))

                        else:
                            print("信用卡卡账号或密码输入错误")
                else:
                    print("信用卡账号输入不能为空")
            return wrapper

        if auth_type == "admin_auth": #管理员认证
            def wrapper():
                res = func()
                admin_dic = {"admin":"admin","passwrod":"123"}
                admin_name = input("请输入管理员账号 :").strip()
                admin_pwd = input("请输入密码 :").strip()
                if admin_name:
                    if admin_name in admin_dic and admin_pwd == admin_dic["passwrod"]:
                        print("管理员账号[%s] 登陆成功。"%(admin_name))

                        return res,admin_name

                    else:
                        print("账号或密码错误")
                else:
                    print("管理员账号输入不能为空")
            return wrapper

     return out_wrapper

@auth(auth_type="user_auth")
def user_auth():
    print("用户登录认证".center(40,"-"))
    return "True"

@auth(auth_type="creditcard_auth")
def creditcard_auth():
    print("信用卡登录认证".center(40,"-"))
    return "True"

@auth(auth_type="admin_auth")
def admin_auth():
    print("管理员登录认证".center(40,"-"))
    return "True"
