'''信用卡信息，'''
from log import get_logger
import json,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''数据库文件相对路径'''
user_dic = BASE_DIR + r"/db/user_data"
creditcard_dic = BASE_DIR + r"/db/creditcard_data"
creditcard_record = BASE_DIR + r"/db/creditcard_record"
user_Water = BASE_DIR + r"/log/water_record"
logger = get_logger()  #日志实例化对象

'''信用卡信息'''
def creditcard_data():

    while True:
        with open(creditcard_dic,"r") as f:
            creditcard_data = json.loads(f.read())
            choice = input("请输入要查看信息的信用卡账号 '6位数字' :").strip()
            if choice in creditcard_data.keys():
                print("我的信用卡信息".center(50,"-"))
                print("持卡人:\t[ %s ]\n卡号:\t[ %s ]\n额度:\t[ ￥%s ]\n可用额度:\t[ ￥%s ]\n取现额度:\t[ ￥%s ]"
                      %(creditcard_data[choice]["personinfo"],
                        choice,
                        creditcard_data[choice]["deflimit"],
                        creditcard_data[choice]["limit"],
                        creditcard_data[choice]["limitcash"]))

            else:
                print("您输入的信用卡，不存在。")
            choice = input("返回输入’q':")
            if choice == "q":
                break

'''查看信用卡流水'''
def cat_cred_record():
    while True:
        choice = input("请输入要查看流水记录的信用卡账号:").strip()
        with open(creditcard_dic) as f1:
            cred_record = json.loads(f1.read())
            if choice:
                if choice in cred_record.keys():
                    print("信用卡 [ %s ] 流水记录".center(50, "-") % (choice))
                    with open(user_Water) as f:
                        for i in f:
                            if choice in i:
                                #print("\33[31;0m信用卡 [ %s ] 还没有进行过消费,去商城买点东西吧\33[0m\n" % (choice))
                                print(i.strip())
                else:
                    print("您输入的信用卡 [ %s ] 不存在"%(choice))
            else:
                print("您输入的信用卡 [ %s ] 不存在"%(choice))

        choice = input("返回 'q':")
        if choice == "q":
            break

'''信用卡还款'''
def repayment():
    while True:
        print(" 还款 ".center(40, "-"))
        with open(creditcard_dic, "r+") as f:
            creditcard_data = json.loads(f.read())
            choice = input("请输入还款的信用卡账号, 返回'q' :").strip()
            if choice == 'q': break
            if choice in creditcard_data:
                money = input("请输入还款金额:").strip()
                pwd = input("请输入还款密码 :").strip()
                if pwd == creditcard_data[choice]["password"]:
                    if money.isdigit():
                        money = int(money)
                        with open(creditcard_dic, "r+") as f:
                            creditcard_data = json.loads(f.read())
                            limit = creditcard_data[choice]["limit"]
                            limitcash = creditcard_data[choice]["limitcash"]
                            limit += money
                            limitcash += (money//2)
                            creditcard_data[choice]["limit"]=limit
                            creditcard_data[choice]["limitcash"] = limitcash
                            dic = json.dumps(creditcard_data)
                            rapayment_data = [str(choice), "信用卡还款", str(money)]
                            msg = "---".join(rapayment_data)
                            f.seek(0)
                            f.truncate(0)
                            f.write(dic)
                            f.flush()
                            logger.debug(msg)  #日志模块
                            print("信用卡 [ %s ] 还款金额 [ ￥%s ] 还款成功" % (choice, money))
                            print("信用卡\t[ %s ]\n可用额度:\t[ ￥%s ]\n取现额度:\t[ ￥%s ] "
                                  %(choice,
                                    creditcard_data[choice]["limit"],
                                    creditcard_data[choice]["limitcash"]))
                    else:
                        print("输入金额格式有误")
                else:
                    print("密码输入错误")
            else:
                print("您输入的信用卡不存在")

'''信用卡取现'''
def takenow():
    while True:
        print(" 取现 ".center(40, "-"))
        with open(creditcard_dic, "r+") as f:
            creditcard_data = json.loads(f.read())
            choice = input("请输入取现的信用卡账号, 返回'q' :").strip()
            if choice == 'q': break
            if choice in creditcard_data:
                #print(creditcard_data)
                limit = creditcard_data[choice]["limit"]
                limitcash = creditcard_data[choice]["limitcash"]
                takenow = limit // 2
                print("信用卡卡号:\t[ %s ]\n信用卡额度:\t[ ￥ %s ]\n取现额度:\t[ ￥ %s ]"
                      % (choice,limit,takenow))
                if limit >= limitcash:
                    print("可取现金额为:\t [ ￥%s ]\n" % (limitcash))
                    cash = input("请输入要取现的金额，收取%5手续费 :").strip()
                    if cash.isdigit():
                        cash = int(cash)
                        if cash <= limitcash:
                            if cash > 0 :
                                password = input("请输入信用卡[ %s ] 的密码 :"
                                            % (choice)).strip()
                                if password and password == creditcard_data[choice]["password"]:
                                    limitcash = int(limitcash - (cash * 0.05 + cash))
                                    limit = int(limit - (cash * 0.05 + cash))
                                    creditcard_data[choice]["limit"] = limit
                                    creditcard_data[choice]["limitcash"] = limitcash
                                    f.seek(0)
                                    f.truncate(0)
                                    dic = json.dumps(creditcard_data)
                                    f.write(dic)
                                    takenow_data = [str(choice),"信用卡取现",str(cash),"手续费",str(int(cash*0.05))]
                                    msg = "---".join(takenow_data)
                                    logger.debug(msg)
                                    print("取现成功".center(40,"-"))
                                    print("取现金额:\t[%s]\n手续费:\t[%s]" % (cash, cash * 0.05))

                                else:
                                    print("密码输入错误\n")
                            else:
                                print("金额不能为0")
                        else:
                            print("您的取现金额已经超出取现额度了。")
                else:
                    print("您的信用额度已经小于取现额度，不能取现了")
            else:
                print("您输入的信用卡账号 [ %s ] 错误"%(choice))

'''信用卡转账'''
def transfer():
    while True:
        print(" 转账 ".center(40, "-"))
        with open(creditcard_dic, "r+") as f:
            creditcard_data = json.loads(f.read())
            choice = input("请输入信用卡账号, 返回'q' :").strip()
            if choice == 'q': break
            if choice in creditcard_data:
                current_limit = creditcard_data[choice]["limit"]
                transfer_account = input("请输入转账账号:").strip()
                if transfer_account.isdigit():
                    #print("----------")
                    if len(transfer_account) == 6 :
                        if transfer_account in creditcard_data.keys():
                            money = input("请输入转账金额:").strip()
                            if money.isdigit():
                                money = int(money)
                                creditcard_pwd = input("请输入信用卡账号密码:")
                                if creditcard_pwd == creditcard_data[choice]["password"]:
                                    if money <= current_limit:
                                        creditcard_data[choice]["limit"] -= money
                                        creditcard_data[choice]["limitcash"] -= money//2
                                        creditcard_data[transfer_account]["limit"] += money
                                        creditcard_data[transfer_account]["limitcash"] += money//2
                                        print("转账成功".center(40,"-"))
                                        print("转账卡号:\t[ %s ]\n转账金额:\t[ ￥%s ]"%(transfer_account,money))
                                        print("信用卡:\t[ %s ]\t可用额度还剩:\t[ ￥%s ]\n"%(creditcard_data[choice]["creditcard"],
                                                                       creditcard_data[choice]["limit"]))


                                        transfer_data = [str(choice), "信用卡转账", str(money)]
                                        msg = "---".join(transfer_data)
                                        logger.debug(msg)
                                        f.seek(0)
                                        f.truncate(0)
                                        dic = json.dumps(creditcard_data)
                                        f.write(dic)


                                    else:
                                        print("转账金额不能超过信用额度")
                                else:
                                    print("密码输入错误")
                            else:
                                print("请输入数字的金额")
                        else:
                            print("您输入的卡号不存在")
                    else:
                        print("您输入的卡号不存在")
                else:
                    print("请输入正确的卡号")
            else:
                print("您输入的信用卡不存在")

'''冻结信用卡'''
def lock_creditcard():
    while True:
        print("冻结信用卡".center(50, "-"))
        with open(creditcard_dic, "r+") as f:
            creditcard_data = json.loads(f.read())
            for key in creditcard_data:
                if creditcard_data[key]["locked"] == False:
                    print("信用卡 [ %s ]\t\t冻结状态：[未冻结]" % (key))
                else:
                    print("信用卡 [ %s ]\t\t冻结状态：[已冻结]" % (key))
            choice = input("是否进行信用卡冻结 : 确定 'y' 返回 'q' :").strip()
            if choice == "q":break
            if choice == "y":
                lock_creditcard = input("请输入要冻结的信用卡卡号:").strip()
                if lock_creditcard in creditcard_data.keys():
                    if creditcard_data[lock_creditcard]["locked"] == False:
                        creditcard_data[lock_creditcard]["locked"] = True
                        dic = json.dumps(creditcard_data)
                        f.seek(0)
                        f.truncate(0)
                        f.write(dic)
                        print("信用卡 %s 冻结成功\n" % (lock_creditcard))
                    else:
                        print("信用卡 %s 已经被冻结\n" % (lock_creditcard))
                else:
                    print("信用卡 %s 不存在\n" %(lock_creditcard))

'''解除冻结信用卡'''
def unlock_creditcard():
    while True:
        print("解冻结信用卡".center(50, "-"))
        with open(creditcard_dic, "r+") as f:
            creditcard_data = json.loads(f.read())
            for key in creditcard_data:
                if creditcard_data[key]["locked"] == False:
                    print("信用卡 [ %s ]\t\t冻结状态：[未冻结]" % (key))
                else:
                    print("信用卡 [ %s ]\t\t冻结状态：[已冻结]" % (key))
            choice = input("是否进行解除信用卡冻结 : 确定 'y' 返回 'q' :").strip()
            if choice == "q":break
            if choice == "y":
                lock_creditcard = input("请输入要冻结的信用卡卡号:").strip()
                if lock_creditcard in creditcard_data.keys():
                    if creditcard_data[lock_creditcard]["locked"] == True:
                        creditcard_data[lock_creditcard]["locked"] = False
                        dic = json.dumps(creditcard_data)
                        f.seek(0)
                        f.truncate(0)
                        f.write(dic)
                        print("信用卡 %s 解除冻结成功\n" % (lock_creditcard))
                    else:
                        print("信用卡 %s 已经解除冻结\n" % (lock_creditcard))
                else:
                    print("信用卡 %s 不存在\n" %(lock_creditcard))

'''申请信用卡'''
def new_creditcard(limit=15000,locked=False):

    while True:
        print("申请信用卡".center(50, "-"))
        with open(creditcard_dic, "r+") as f:
            creditcard_data = json.loads(f.read())
            for key in creditcard_data:
                print("系统已有信用卡 【%s】 \t持卡人 【%s】" % (key,creditcard_data[key]["personinfo"]))
            choice = input("\n\33[34;0m是否申请新的信用卡 确定'y' 返回'q'\33[0m:").strip()
            if choice == "q":break
            if choice == "y":
                creditcard = input("\33[34;0m输入要申请的信用卡卡号(6位数字)：\33[0m").strip()
                if creditcard not in creditcard_data.keys():
                    if creditcard.isdigit() and len(creditcard) == 6:
                        password = input("\33[34;0m请输入申请的信用卡密码：\33[0m").strip()
                        if len(password) > 0:
                            personinfo = input("\33[34;0m请输入信用卡申请人：\33[0m").strip()
                            if len(personinfo) > 0:
                                creditcard_data[creditcard] = {"creditcard":creditcard, "password":password, "personinfo":personinfo,
                                                        "limit":limit,"limitcash":limit//2,"locked":locked,"deflimit":limit,}
                                dict = json.dumps(creditcard_data)
                                f.seek(0)
                                f.truncate(0)
                                f.write(dict)
                                print("信用卡:\t[ %s ] 申请成功\n持卡人:\t[ %s ]\n额度:\t[ ￥%s ]\n取现额度:\t[ ￥%s ]"%(creditcard,
                                                                                          personinfo,
                                                                                          limit,
                                                                                          creditcard_data[creditcard]["limitcash"]))
                            else:
                                print("信用卡申请人不能为空\n")
                        else:
                            print("输入的密码不正确\n")
                    else:
                        print("信用卡 %s 卡号不符合规范\n" % (creditcard))
                else:
                    print("信用卡 %s 已经存在\n" % (creditcard))

'''信用卡绑定'''
def link_creditcard():
    while True:
        print("\33[32;0m修改信用卡绑定\33[0m".center(40, "-"))

        with open(user_dic, "r+") as f:
            user_data = json.loads(f.read())
            user_name = input("请输入绑定信用卡的用户名  返回 'q' :").strip()
            if user_name == "q":break
            if user_name in user_data.keys():
                creditcard = user_data[user_name]["creditcard"]
                if creditcard == 0 :
                    print("当前账号： \t%s"%(user_name))
                    print("信用卡绑定：\33[31;0m未绑定\33[0m\n")
                else:
                    print("当前账号： \t%s" %(user_name))
                    print("绑定的信用卡： %s\n"%(creditcard))
                choice = input("\33[34;0m是否要修改信用卡绑定 确定 'y' 返回'q' \33[0m:")
                if choice == "q":break
                if choice == "y":
                    creditcard_new = input("\33[34;0m输入新的信用卡卡号(6位数字)\33[0m:").strip()
                    if creditcard_new.isdigit() and len(creditcard_new) ==6:
                        with open(creditcard_dic, "r+") as f1:
                            creditcard_data = json.loads(f1.read())
                            if creditcard_new in creditcard_data.keys():
                                user_data[user_name]["creditcard"]=creditcard_new
                                dict = json.dumps(user_data)
                                f.seek(0)
                                f.truncate(0)
                                f.write(dict)
                                print("\33[31;1m信用卡绑定成功\33[0m\n")
                            else:
                                print("\33[31;0m输入信用卡卡号不存在(未发行)\33[0m\n")
                    else:
                        print("\33[31;0m输入信用卡格式错误\33[0m\n")
                else:
                    print("请选择 ’y‘ 或 ’q‘ ")
            else:
                print("您输入的用户 [ %s ] 不存在 ")

