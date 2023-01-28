# 编程题
# 1
# 请使用socket模块实现一个简单的web服务器，当用户在浏览器地址栏
# 输入"http://127.0.0.1:8000"，返回"welcome to index page"
# 输入"http://127.0.0.1:8000/login"，返回"welcome to login page"
# 输入其他非法路径返回"404 not found"

# 2
# 使用命令，创建一个Django项目，然后请写一个基于class的视图，返回字符串"Hello World"给客户端

# 3
# kanghuadeMacBook-Pro:study kanghua$ django-admin.py startproject djpro
# kanghuadeMacBook-Pro:study kanghua$ cd djpro/
# kanghuadeMacBook-Pro:djpro kanghua$ django-admin.py startapp hello
# 使用Django，写一个登录页面，基于form表单完成。
# 使用bootstrap为form表单添加样式，不许使用cdn的方式引入bootstrap，而是要本地以静态文件的方式引入。
# 创建user表，只需要name和password两个字段即可。然后数据库可以使用sqlite3或者MySQL都行；用户数据自行填充。
# 在页面中，如果输入的用户名或者密码错误时，提示"user or password error!"，并且在3秒后消除。
# 登录成功，跳转到主页，主页只需要h1标签，写上"欢迎来到主页"即可。


# 问答题
# Web框架的本质是什么？为什么要有Web框架？
# socket 请求响应 ,  # 节省时间,提高效率,去掉重复造轮子的工作, 底层的工作都交给web框架做了, 开发只需要聚焦在业务代码上
'''
标准答案: web框架本质上就是一个socket server.
在没有web框架的情况下,程序员需要自己处理客户单的请求,
包括解析客户端请求,获取请求的所有数据,封装数据,封装响应数据并返回客户端,
这些重复的工作,会大大降低程序员的工作效率.从另一个层面看,web框架就是一套处理客户端请求,分发请求,最后封装响应数据并返回给客户端的一套系统.
有了web框架,程序员不在需要重复这些工作,大大提升工作效率,能将所有精力集中在业务功能的实现上.
'''
# Django请求的生命周期(即从浏览器向Django后台发送一个请求并得到返回，Django都做了哪些事儿情)？
# 客户端请求----> wsgi-->中间件---> url路由 --> views --> model --> databases
#                                   |--> template -->中间件 ---> wsgi
#                                                返回客户端   <----|
'''
标准答案:
1. 用户输入网址,浏览器发起请求
2. WSGI(服务器网关接口) 创建socket服务端,接受请求
3. 中间件处理请求
4. url路由,根据当前请求的url找到相应的视图函数
5. 进入view,进行业务处理,执行类或者函数,   <---> model <----> databases
5.1 渲染对应template模板, 返回字符串
6. 再次通过中间件处理
7. WSGI返回响应
8. 浏览器渲染
'''


# Django的视图，有几种处理请求的方式？
#  FBV 函数视图    CBV 类视图

# 类视图
'''
# urls.py
from django.contrib import admin
from django.urls import path
from app01 import views    # 导入views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.Hello.as_view()),  # as_view() 固定写法
]

# views.py
from django.shortcuts import render, HttpResponse
from django.views import View
class Hello(View):   # 类视图继承 View类
    def get(self, request):   # get方法关键字方法名称 还有post
        return HttpResponse("Hello World")

'''

# 如何判断查询集正是否有数据？
#   reply = model_obj.objects.filter().exists()

# Django中间件的使用，Django在中间件中，预留了几个方法？每个方法的作用？
'''
对输入或输出进行干预，方法如下：
1. 初始化：无需任何参数，服务器响应第一个请求的时候调用一次，用于确定是否启用当前中间件。
def init(): pass

2. 处理请求前：在每个请求上调用，返回 None 或 HttpResponse 对象。
def process_request(request): pass

3. 处理视图前：在每个请求上调用，返回 None 或 HttpResponse 对象。
def process_view(request, view_func, view_args, view_kwargs): pass

4. 处理模板响应前：在每个请求上调用，返回实现了 render 方法的响应对象。
def process_template_responose(request, response): pass

5. 处理响应后：所有响应返回浏览器之前被调用，在每个请求上调用，返回 HttpResponse 对象。
def process_response(request, response): pass

6. 异常处理：当视图抛出异常时调用，在每个请求上调用，返回一个 HttpResponse 对象。
def process_exception(request, exception): pass
'''
