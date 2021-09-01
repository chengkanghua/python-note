class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
class Account:
    def __init__(self):
        # 用户列表，数据格式：[user对象，user对象，user对象]
        self.user_list = []
    def login(self):
        """
        用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
        :return:
        """
        while True:
            print('welcome login ')
            username = input('please username: Q/q quit')
            password = input('please password: ')
            if username.upper() == 'Q':
                break
            for i in self.user_list:
                if username == i.name and password== i.pwd:
                    print('登陆成功')
                    break
            else:
                print('账号或密码错误，请重试')
                continue
            # if username == self.user_list[username].name and password == self.user_list[username].pwd:
            #     print('登陆成功')
            #     break
            # else:
            #     print("账号或者密码错误，请重试")
            #     continue
    def register(self):
        """
        用户注册，每注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
        :return:
        """
        while True:
            print('welcome register')
            username = input('username:  Q/q quit ')
            password = input('password: ')
            if username.upper() == 'Q':
                break
            if username in self.user_list:
                print('用户已注册，重试：')
            username = User(username,password)
            self.user_list.append(username)
            print('注册成功')
            break
    def showinfo(self):
        # print(self.user_list)
        for i in self.user_list:
            print(i.name,i.pwd)

        # print(self.user_list[aa].name,self.user_list[aa].pwd)
        # print(type(self.user_list[aa].name),type(self.user_list[aa].pwd))
    def run(self):
        """
        主程序
        :return:
        """
        while True:
            print('welcome xxx system')
            print('1: login  2：register 3:showinfo')
            num = input('select num：Q/q quit')
            if num.upper() == 'Q':
                break
            if not num in {'1','2','3'}:
                print('error: not know ')
                continue
            if num == '1':
                self.login()
            if num == '2':
                self.register()
            if num == '3':
                self.showinfo()
if __name__ == '__main__':
    obj = Account()
    obj.run()