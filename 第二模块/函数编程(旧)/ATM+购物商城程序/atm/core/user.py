import json,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''数据库文件相对路径'''
user_dic = BASE_DIR + r"/db/user_data"
user_Blacklist = BASE_DIR + r"/db/Blacklist_user"

'''创建用户'''
def new_user(address="None", locked=False, creditcard=False):
    while True:
        print("开始创建用户".center(50, "-"))
        with open(user_dic, "r+") as f:
            user_data = json.loads(f.read())
            for key in user_data:
                print("系统已有用户 [ %s ]" % (key))
            choice = input("是否创建新的用户 确定'y'/返回'q':")
            if choice == "q": break
            if choice == "y":
                user_name = input("请输入要创建的用户名:").strip()
                user_pwd = input("请输入创建用户的密码 :").strip()
                if user_name not in user_data.keys():
                    if len(user_name) > 0 and len(user_pwd) > 0:
                        user_data[user_name] = {"username": user_name, "password": user_pwd, "creditcard": creditcard,
                                                "address": address,"status":False,"locked": locked}
                        dic = json.dumps(user_data)
                        f.seek(0)
                        f.truncate(0)
                        f.write(dic)
                        print("用户 %s 创建成功\n" % (user_name))
                    else:
                        print("输入的用户或密码不能密码为空")

                else:
                    print("用户 %s 已经存在\n" % (user_name))

'''解锁用户'''
def unlock_user():
    while True:
        print("解锁用户".center(50, "-"))
        with open(user_dic, "r+") as f:
            user_data = json.loads(f.read())
            for key in user_data:
                if user_data[key]["locked"] == False:
                    print("用户 [ %s ]\t\t锁定状态：[未锁定]" % (key))
                else:
                    print("用户 [ %s ]\t\t锁定状态：[已锁定]" % (key))
            choice = input("是否进行用户解锁 : 确定 'y' 返回 'q' :").strip()
            if choice == "q":break
            if choice == "y":
                unlock_user = input("请输入要解锁的用户名:").strip()
                if unlock_user in user_data.keys():
                    if user_data[unlock_user]["locked"] == True:
                        user_data[unlock_user]["locked"] = False
                        dict = json.dumps(user_data)
                        f.seek(0)
                        f.truncate(0)
                        f.write(dict)
                        print("\33[31;1m用户 %s 解锁成功\33[0m\n" % (unlock_user))
                    else:
                        print("用户 %s 解锁失败 用户未被锁定" % (unlock_user))
                else:
                    print("用户 %s 不存在"%(unlock_user))

'''锁定用户'''
def lock_user():
    while True:
        print("锁定用户".center(50, "-"))
        with open(user_dic, "r+") as f:
            user_data = json.loads(f.read())
            for key in user_data:
                if user_data[key]["locked"] == False:
                    print("用户 [ %s ]\t\t锁定状态：[未锁定]"%(key))
                else:
                    print("用户 [ %s ]\t\t锁定状态：[已锁定]" % (key))
            choice = input("是否进行用户锁定 : 确定'y' 返回'q' :")
            if choice == "q":break
            if choice == "y":
                lock_user = input("请输入要锁定的用户名 :")
                if lock_user in user_data.keys():
                    if user_data[lock_user]["locked"] == False:
                        user_data[lock_user]["locked"] = True
                        dic = json.dumps(user_data)
                        f.seek(0)
                        f.truncate(0)
                        f.write(dic)
                        print("\33[31;1m用户 %s 锁定成功\33[0m\n" % (lock_user))
                    else:
                        print("用户 %s 已经锁定\n" % (lock_user))
                else:
                    print("用户 %s 不存在\n"%(lock_user))

'''三次锁定'''
def lock():
    while True:
        with open(user_Blacklist,"r+") as f:
            blacklist_data = json.loads(f.read())
            print("blacklist_data:",blacklist_data)
            user_name = input("请输入登录的用户名 : ").strip()
            if user_name in blacklist_data.keys():
                if blacklist_data[user_name] == 3 :
                    print("您的 %s 用户已经在黑名单中 ！！" %(user_name))
                    continue

            with open(user_dic,"r+") as f1:
                user_data = json.loads(f1.read())
                print("user_data:",user_data)
                if user_name in user_data.keys():
                    if user_data[user_name]["status"] == False:

                        if blacklist_data[user_name] != 3:
                            user_pwd = input("请输入用户 [ %s ] 的登录密码: "%(user_name)).strip()

                            if user_pwd and user_pwd == user_data[user_name]["password"]:
                                print("用户 [ %s ] 登陆成功"%(user_name))
                                user_data[user_name]["status"] = True
                                data = json.dumps(user_data)
                                f1.seek(0)
                                f1.truncate(0)
                                f1.write(data)
                                break
                            else:
                                print("用户 [ %s ] 密码输入错误:"%(user_name))
                                blacklist_data[user_name] += 1
                                data = json.dumps(blacklist_data)
                                #print(blacklist_data)
                                f.seek(0)
                                f.truncate(0)
                                f.write(data)

                        else:
                            print("用户 [ %s ] 已被加入黑名单" % (user_name))
                            data = json.dumps(blacklist_data)
                            f.seek(0)
                            f.truncate(0)
                            f.write(data)
                    else:
                        print("用户 [ %s ] 已经在登录状态" % (user_name))
                else:
                    print("用户 [ %s ] 不存在，请重新输入：" % (user_name))

