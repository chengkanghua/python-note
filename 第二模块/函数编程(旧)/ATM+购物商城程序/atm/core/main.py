'''主逻辑交互程序'''

from auth import *
from user import *
from creditcard import *
from shopping import *

'''主页面列表'''


def main_list():
    msg = ["  ATM  ",
           "购物商城",
           "管理系统",
           "退出程序 输入 q", ]

    index = 0
    for i in msg:
        print("\t\t\t\t", index + 1, "\t ", i)
        index += 1


'''ATM页面列表'''


def atm_list():
    msg = ["信用卡信息",
           "信用卡取现",
           "信用卡转账",
           "信用卡还款",
           "申请信用卡",
           "信用卡绑定",
           "信用卡流水",
           "返回上一层 输入 q",
           "退出程序 输入 exit"]

    index = 0
    for i in msg:
        print("\t\t\t\t", index + 1, "\t ", i)
        index += 1


'''购物车页面列表'''


def shopp_list():
    msg = ["购物",
           "购物车",
           "购物结算",
           "购物记录",
           "清空购物车",
           "返回上一层 输入 q",
           "退出程序 输入  exit"]

    index = 0
    for i in msg:
        print("\t\t\t\t", index + 1, "\t ", i)
        index += 1


'''管理员页面列表'''


def admin_list():
    msg = ["冻结信用卡",
           "解冻信用卡",
           "创建用户",
           "锁定用户",
           "解锁用户",
           "返回上一层 输入 q",
           "退出程序  输入 exit"]

    index = 0
    for i in msg:
        print("\t\t\t\t", index + 1, "\t ", i)
        index += 1


'''主函数'''


def main():
    print("购物商城ATM系统".center(40, "-"))
    lock()  # 三次锁定模块
    while True:
        print("欢迎来到购物商城ATM系统".center(40, "-"))
        print(" \t\t\t\t ID\t\t信息")
        main_list()
        choice = input("请选择 ID :").strip()
        if choice == "q":
            print(" bye bye ".center(50, "-"))
            exit()
        if choice.isdigit():
            choice = int(choice)
            if choice >= 1 and choice <= 4:
                if choice == "q": break
                while True:
                    if choice == 1:
                        print("欢迎来到信用卡中心".center(50, "-"))
                        print(" \t\t\t\t ID\t\tATM信息")
                        atm_list()  # 信用卡列表
                        atm_choice = input("请选择 ATM ID :").strip()
                        if atm_choice == "q": break
                        if atm_choice == "exit": exit()
                        if atm_choice.isdigit():
                            atm_choice = int(atm_choice)
                            if atm_choice >= 1 and atm_choice <= 7:
                                while True:
                                    if atm_choice == 1:
                                        creditcard_data()  # 信用卡信息模块
                                        break
                                    elif atm_choice == 2:
                                        creditcard_auth()  # 信用卡认证模块
                                        takenow()  # 信用卡取现模块
                                        break
                                    elif atm_choice == 3:
                                        creditcard_auth()  # 信用卡认证模块
                                        transfer()  # 信用卡转账模块
                                        break
                                    elif atm_choice == 4:
                                        creditcard_auth()  # 信用卡认证模块
                                        repayment()  # 信用卡还款模块
                                        break
                                    elif atm_choice == 5:
                                        new_creditcard(limit=15000, locked=False)  # 申请信用卡模块
                                        break
                                    elif atm_choice == 6:
                                        link_creditcard()  # 用户绑定信用卡模块
                                        break
                                    elif atm_choice == 7:
                                        cat_cred_record()  # 查看信用卡流水模块
                                        break
                            else:
                                print("请输入正确的 ID ")
                        else:
                            print("请输入正确的 ID ")

                    elif choice == 2:
                        print("欢迎来到购物中心".center(50, "-"))
                        print(" \t\t\t\t ID\t\t商城信息")
                        shopp_list()  # 商城列表
                        shopp_choice = input("请选择 商城 ID :").strip()
                        if shopp_choice == "q": break
                        if shopp_choice == "exit": exit()
                        if shopp_choice.isdigit():
                            shopp_choice = int(shopp_choice)
                            if shopp_choice >= 1 and shopp_choice <= 5:
                                while True:
                                    if shopp_choice == 1:
                                        shopping_mall()  # 购物商城模块
                                        break
                                    elif shopp_choice == 2:
                                        Shopping_car()  # 购物车模块
                                        break
                                    elif shopp_choice == 3:
                                        shopping_pay()  # 购物结算模块
                                        break
                                    elif shopp_choice == 4:
                                        cat_shopp_record()  # 查看购物记录模块
                                        break
                                    elif shopp_choice == 5:
                                        del_shopping_car()  # 清空购物车模块
                                        break
                            else:
                                print("请输入正确的 ID ")
                        else:
                            print("请输入正确的 ID ")

                    elif choice == 3:
                        print("欢迎来到管理中心".center(50, "-"))
                        print(" \t\t\t\t ID\t\t操作信息")
                        admin_list()  # 管理中心列表
                        admin_choice = input("请选择 信息 ID :").strip()
                        if admin_choice == "q": break
                        if admin_choice == "exit": exit()
                        if admin_choice.isdigit():
                            admin_choice = int(admin_choice)
                            if admin_choice >= 1 and admin_choice <= 5:
                                while True:
                                    if admin_choice == 1:
                                        admin_auth()  # 管理员用户验证模块
                                        lock_creditcard()  # 冻结信用卡模块
                                        break
                                    elif admin_choice == 2:
                                        admin_auth()  # 管理员用户验证模块
                                        unlock_creditcard()  # 解冻信用卡模块
                                        break
                                    elif admin_choice == 3:
                                        admin_auth()  # 管理员用户验证模块
                                        # 创建用户模块
                                        new_user(address="None", locked=False, creditcard=False)
                                        break
                                    elif admin_choice == 4:
                                        admin_auth()  # 管理员用户验证模块
                                        lock_user()  # 锁定用户模块
                                        break
                                    elif admin_choice == 5:
                                        admin_auth()  # 管理员用户验证模块
                                        unlock_user()  # 解锁用户模块
                                        break

                    elif choice == 4:
                        exit()

