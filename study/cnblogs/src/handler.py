from utils import validator
from utils import context
from src import account
from src.article import art



class Handler(object):
    LOCAL_USER_DICT = context.UserDict()
    Navigation = []

    # 导航闭包函数
    def wrapper(self,method):
        def inner(*args,**kwargs):
            print(' > '.join(self.Navigation).center(50,"*"))
            res = method(*args,**kwargs)
            self.Navigation.pop(-1)
            return res
        return inner
    # 登陆
    def login(self):
        while True:
            user = input('请输入用户名 (q/Q退出): ')
            if user.upper() == 'Q':
                return
            pwd  = input('请输入密码: ')
            user_dict = account.login(user,pwd)
            # print(user_dict)
            if not user_dict:
                print('用户或密码错误,请重试')
                continue
            print('登陆成功')
            self.LOCAL_USER_DICT.set_info(user_dict)
            self.Navigation.insert(0,self.LOCAL_USER_DICT.nickname)
            return

    # 注册
    def registry(self):
        pass

    # 发表文章
    def publish(self):
        pass

    # 博客列表
    def article_list(self):
        pass
    # 文章详情
    def get_article(self):
        pass

    # run
    def run(self):
        '''主入口'''
        self.Navigation.append('系统首页')
        mapping = {
            '1': context.Context('登陆',self.wrapper(self.login)),
            '2': context.Context('注册',self.wrapper(self.registry)),
            '3': context.Context('发布博客',self.wrapper(self.publish)),
            '4': context.Context('查看博客列表',self.wrapper(self.article_list))
        }

        message = '\n'.join(['{} {}'.format(k,v.title) for k,v in mapping.items()])
        while True:
            print(message)
            cmd = input('请输入序号, Q退出: ')
            if cmd.upper() == 'Q':
                break
            data = mapping.get(cmd)
            if not data:
                print('输入错误, 请重试')
                continue
            self.Navigation.append(data.title)
            data.method()


handler = Handler()
handler.run()