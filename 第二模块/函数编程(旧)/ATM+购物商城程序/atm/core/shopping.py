import json,os
from creditcard import link_creditcard
from auth import creditcard_auth
from log import get_logger
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''数据库文件相对路径'''

shopping_dic = BASE_DIR + r"/db/shopping_record"
shopping_lis = BASE_DIR + r"/db/shopping_list"
shopping_car = BASE_DIR + r"/db/shopping_car"
creditcard_dic = BASE_DIR + r"/db/creditcard_data"
user_dic = BASE_DIR + r"/db/user_data"
user_Water = BASE_DIR + r"/log/water_record"
logger = get_logger() #日志模块实例化对象


'''购物商城'''
def shopping_mall():
    shopping_list,pro_list  = [],[]
    with open(shopping_lis, "r", encoding="utf-8") as  f:
        for item in f:
            pro_list.append(item.strip("\n").split())
    def pro_inf():
        print("\t\t\t\t编号\t商品\t\t价格")
        for index, item in enumerate(pro_list):
            print("\t\t\t\t%s\t\t%s\t\t%s" % (index+1, item[0], item[1]))
    while True:
            print(("目前商城在售的商品信息").center(50, "-"))
            pro_inf()
            choice_id = input("选择要购买的商品编号 '购买 ID' 返回 'q'：")
            if choice_id.isdigit():
                choice_id = int(choice_id)
                if choice_id <= len(pro_list) and choice_id >=0:
                    pro_item = pro_list[choice_id-1]
                    print("商品 [ %s ] 加入购物车 价格 [ ￥%s ] "%(pro_item[0],pro_item[1]))
                    shopping_list.append(pro_item)
                    shopp_data = ["商品",str(pro_item[0]), "价格", str(pro_item[1])]
                    msg = "---".join(shopp_data)
                    logger.debug(msg)
                else:
                    print("没有相应的编号 请重新输入:")
            elif  choice_id == "q":
                with open(shopping_car, "r+") as f:
                    list = json.loads(f.read())
                    list.extend(shopping_list)
                    f.seek(0)
                    f.truncate(0)
                    list = json.dumps(list)
                    f.write(list)
                break
            else:
                 print("没有相应的编号 请重新输入:")

'''购物车'''
def Shopping_car():
    while True:
        with open(shopping_car, "r+") as f:
            list = json.loads(f.read())
            sum = 0
            print("购物车信息清单".center(40,"-"))
            print("id\t商品\t价格")
            for index,item in enumerate(list):

                print("%s\t%s\t%s"%(index+1,item[0],item[1]))
                sum +=int(item[1])

            print("商品总额共计： ￥%s"%(sum))
        choice = input("请选择要进行的操作 返回 'q' 清空'f':").strip()
        if choice == "q" :break
        if choice == "f":
            del_shopping_car()
            break

'''清空购物车'''
def del_shopping_car():
    while True:
        with open(shopping_car, "r+") as f:
            res = json.loads(f.read())
            if res != []:
                choice = input("是否清空购物车 确定 'y' 返回 'q' :").strip()
                print("购物车里的商品".center(50, "-"))
                print(res, "\n")
                if choice == "q":break
                if choice == "y":
                    list = json.dumps([])
                    f.seek(0)
                    f.truncate(0)
                    f.write(list)
                    print("购物车已清空")
                else:
                    print("请输入正确的指令： ‘y' 或 ’q' ")
            else:
                print("您还没有消费过，去商城花点钱把")
                break

'''购物结算'''
def shopping_pay():
    while True:
        print("购物结算".center(50, "-"),"\n")
        with open(shopping_car, "r+") as f:
            data = json.loads(f.read())
            if data != []:
                print("购物车信息清单".center(50, "-"))
                print("\t\t\t\t\tid\t商品\t价格")
                for index, item in enumerate(data):
                    print("\t\t\t\t\t%s\t%s\t%s" % (index + 1, item[0], item[1]))

                money = sum([int(i[1]) for i in data])
            else:
                print("您还没有消费过，去商城花点钱把")
                break
        choice = input("当前商品总额：[ ￥%s ] 是否进行支付 :确定 'y' 返回 'q':" % (money))
        if choice == "q": break
        if choice == "y":
            creditcard_auth()  # 信用卡认证模块
            #break
            user_name = input("请输入结算的用户账号:").strip()
            with open(user_dic, "r+") as f1:
                user_data = json.loads(f1.read())
                if user_name in user_data.keys():
                    user_creditcard = user_data[user_name]["creditcard"]
                    if user_creditcard == False:
                        print("账号 %s 未绑定信用卡，请先绑定信用卡" % (user_name))
                        link_creditcard()  #信用卡绑定模块
                    else:
                        with open(creditcard_dic, "r+") as f2:
                            creditcard_data = json.loads(f2.read())
                            pwd = input("请输入 信用卡[ %s ]支付密码 :" % (creditcard_data[user_creditcard]["creditcard"]))
                            if pwd == creditcard_data[user_creditcard]["password"]:
                                limit = creditcard_data[user_creditcard]["limit"]
                                limit_new = limit - money
                                limit_not = creditcard_data[user_creditcard]["limitcash"] - money // 2
                                if limit_new >= 0:
                                    creditcard_data[user_creditcard]["limit"] = limit_new
                                    creditcard_data[user_creditcard]["limitcash"] = limit_not
                                    shop_data = [user_name,str(creditcard_data[user_creditcard]["creditcard"]),
                                                 "信用卡结账", str(money)]

                                    msg = "---".join(shop_data)
                                    dict = json.dumps(creditcard_data)
                                    f2.seek(0)
                                    f2.truncate(0)
                                    f2.write(dict)
                                    logger.debug(msg)

                                    print("支付成功-->>>\t购物支付:[ ￥%s ]\t当前额度还剩 : [ ￥%s ]\n" % (money, limit_new))
                                    break

                                else:
                                    print("当前信用卡额度 %s元 不足矣支付购物款 可绑定其他信用卡支付\n" % (limit))
                            else:
                                print("密码错误，请重新输入！！！")
                                continue
                else:
                    print("您输入的用户不存在")

'''查看购物记录'''
def cat_shopp_record():
    while True:
        with open(user_dic) as f:
            user_data = json.loads(f.read())
            choice = input("请输入要查看购物记录的用户名:").strip()
            if choice in user_data.keys():
                print("用户 %s 购物记录".center(50, "-")%(choice))
                with open(user_Water) as f1:
                    for i in f1:
                        if choice in i:
                            print(i.strip())
                            #print("\33[31;0m用户 %s 还没有进行过消费\33[0m\n" % (choice))

                choice1 = input("返回 'q':")
                if choice1 == "q":
                    break
            else:
                print("您输入的用户名 [ %s ] 不存在"%(choice))

