'''
编写登陆接口
基础需求：
● 让用户输入用户名密码
● 认证成功后显示欢迎信息
● 输错三次后退出程序
升级需求：
● 可以支持多个用户登录 (提示，通过列表存多个账户信息)
● 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）


'''

# 用户数据一般是提前建立好的，如果没有提前创建好。需要执行上一步。
f = open("account.txt", 'r')
account = eval(f.read())
f.close()
count = 0  # 计数器
last_input = None
flag = True
global user
while count < 3:
    user = input("Username:").strip()  # 去掉用户字符串两边的空格
    password = input("Password:").strip()
    if last_input is None:  # 第一次输入
        last_input = user
    if last_input != user:  # 上一次与此次输入的用户不相等
        flag = False
    if user in account:
        if account[user][1] == 1:  # 用户状态是否锁定
            exit("用户已锁定，请联系管理员")
        elif password == account[user][0]:  # 用户没有锁定
            print('Welcome to %s' % user)
            break
        else:
            print('Wrong username or password')
    else:
        print('用户不存在')
    count += 1
else:
    print('输入的次数太多了')
    if flag is True:
        account[user][1] = 1  # 3次一致，锁定
        f = open("account.txt", 'w')
        f.write(str(account))
        f.close()
