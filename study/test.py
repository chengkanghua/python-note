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
            if username.upper() == 'Q':
                break
            password = input('please password: ')
            for i in self.user_list:
                if username == i.name and password== i.pwd:
                    print('登陆成功')
                    return
            else:
                print('账号或密码错误，请重试')
                continue
    def register(self):
        """
        用户注册，每注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
        :return:
        """
        while True:
            print('welcome register')
            username = input('username:  Q/q quit ')
            if username.upper() == 'Q':
                break
            password = input('password: ')
            user_object = User(username,password)
            self.user_list.append(user_object)
            print('注册成功')
            break
    def showinfo(self):
        for i in self.user_list:
            print(i.name,i.pwd)
    def run(self):
        """
        主程序
        :return:
        """
        method_dict = {
            '1':{'title':'登陆','method':self.login},
            '2':{'title':'注册','method':self.register},
            '3':{'title':'显示','method':self.showinfo}
        }
        message = '\n'.join(['{}:{}'.format(k,v['title']) for k,v in method_dict.items()])
        while True:
            print(message)
            select_num = input('请选择功能： Q/q退出 》')
            if select_num.upper() == 'Q':
                break
            info = method_dict.get(select_num)['method']
            if not info:
                print('选择错误， 请重新选择。')
                continue
            info()


if __name__ == '__main__':
    obj = Account()
    obj.run()