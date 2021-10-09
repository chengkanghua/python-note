# 1 web应用

Web应用程序是一种可以通过Web访问的应用程序，程序的最大好处是用户很容易访问应用程序，用户只需要有浏览器即可，不需要再安装其他软件。应用程序有两种模式C/S、B/S。C/S是客户端/服务器端程序，也就是说这类程序一般独立运行。而B/S就是浏览器端/服务器端应用程序，这类应用程序一般借助谷歌，火狐等浏览器来运行。WEB应用程序一般是B/S模式。Web应用程序首先是“应用程序”，和用标准的程序语言，如java，python等编写出来的程序没有什么本质上的不同。在网络编程的意义下，浏览器是一个socket客户端，服务器是一个socket服务端。

```python
import socket

def handle_request(client):

    request_data = client.recv(1024)
    print("request_data: ",request_data)

    client.send("HTTP/1.1 200 OK\r\nstatus: 200\r\nContent-Type:text/html\r\n\r\n".encode("utf8"))
    client.send("<h1>Hello, luffycity!</h1><img src=''>".encode("utf8"))

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',8812))
    sock.listen(5)

    while True:
        print("the server is waiting for client-connection....")
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':

    main()
```


# 2 http协议

## http协议简介

HTTP协议是Hyper Text  Transfer Protocol（超文本传输协议）的缩写,是用于万维网（WWW:World Wide Web ）服务器与本地浏览器之间传输超文本的传送协议。

HTTP是一个属于应用层的面向对象的协议，由于其简捷、快速的方式，适用于分布式超媒体信息系统。它于1990年提出，经过几年的使用与发展，得到不断地完善和扩展。HTTP协议工作于客户端-服务端架构为上。浏览器作为HTTP客户端通过URL向HTTP服务端即WEB服务器发送所有请求。Web服务器根据接收到的请求后，向客户端发送响应信息。

![img](assets/877318-20180418160227278-698810818.png)

## http协议特性

 

### (1) 基于TCP/IP

http协议是基于TCP/IP协议之上的应用层协议。

### (2) 基于请求－响应模式

HTTP协议规定,请求从客户端发出,最后服务器端响应该请求并 返回。换句话说,肯定是先从客户端开始建立通信的,服务器端在没有 接收到请求之前不会发送响应

![img](assets/877318-20180418160433297-1726664935.png)

### (3) 无状态保存

HTTP是一种不保存状态,即无状态(stateless)协议。HTTP协议 自身不对请求和响应之间的通信状态进行保存。也就是说在HTTP这个 级别,协议对于发送过的请求或响应都不做持久化处理。

1.  1.  1.  1.  ![img](assets/877318-20180418160546133-1479186889.png)

使用HTTP协议,每当有新的请求发送时,就会有对应的新响应产 生。协议本身并不保留之前一切的请求或响应报文的信息。这是为了更快地处理大量事务,确保协议的可伸缩性,而特意把HTTP协议设计成 如此简单的。可是,随着Web的不断发展,因无状态而导致业务处理变得棘手 的情况增多了。比如,用户登录到一家购物网站,即使他跳转到该站的 其他页面后,也需要能继续保持登录状态。针对这个实例,网站为了能 够掌握是谁送出的请求,需要保存用户的状态。HTTP/1.1虽然是无状态协议,但为了实现期望的保持状态功能, 于是引入了Cookie技术。有了Cookie再用HTTP协议通信,就可以管 理状态了。有关Cookie的详细内容稍后讲解。

### 无连接

无连接的含义是限制每次连接只处理一个请求。服务器处理完客户的请求，并收到客户的应答后，即断开连接。采用这种方式可以节省传输时间。

## http请求协议与响应协议

http协议包含由浏览器发送数据到服务器需要遵循的请求协议与服务器发送数据到浏览器需要遵循的请求协议。用于HTTP协议交互的信被为HTTP报文。请求端(客户端)的HTTP报文 做请求报文,响应端(服务器端)的 做响应报文。HTTP报文本身是由多行数据构成的字 文本。 

![img](assets/877318-20180418160732113-669528378.png)

### 请求协议

#### 请求格式

![img](assets/877318-20180418160914403-902015370.png)

#### 请求方式: get与post请求

-   GET提交的数据会放在URL之后，以?分割URL和传输数据，参数之间以&相连，如EditBook?name=test1&id=123456. POST方法是把提交的数据放在HTTP包的请求体中.
-   GET提交的数据大小有限制（因为浏览器对URL的长度有限制），而POST方法提交的数据没有限制.
-   GET与POST请求在服务端获取请求数据方式不同。

### 响应协议

#### 响应格式

![img](assets/877318-20180418161014087-738990087.png)

#### 响应状态码

状态码的职 是当客户端向服务器端发送请求时, 返回的请求 结果。借助状态码,用户可以知道服务器端是正常 理了请求,还是出 现了 。状态码如200 OK,以3位数字和原因 成。数字中的 一位指定了响应 别,后两位无分 。响应 别有以5种。

![img](assets/877318-20180418161321986-304902913.png)

```python
import socket


sock=socket.socket()
sock.bind(("127.0.0.1",8808))
sock.listen(5)

while 1:
    print("server waiting.....")
    conn,addr=sock.accept()
    data=conn.recv(1024)
    print("data",data)

    # 读取html文件
    with open("login.html","rb") as f:
        data=f.read()

    conn.send((b"HTTP/1.1 200 OK\r\n\r\n%s"%data))
    conn.close()
```

login.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<form action="" method="post">
    用户名 <input type="text" name="user">
    密码 <input type="password" name="pwd">
    <input type="submit">
</form>

</body>
</html>
```

# 3 web框架

Web框架（Web framework）是一种开发框架，用来支持动态网站、网络应用和网络服务的开发。这大多数的web框架提供了一套开发和部署网站的方式，也为web行为提供了一套通用的方法。web框架已经实现了很多功能，开发人员使用框架提供的方法并且完成自己的业务逻辑，就能快速开发web应用了。浏览器和服务器的是基于HTTP协议进行通信的。也可以说web框架就是在以上十几行代码基础张扩展出来的，有很多简单方便使用的方法，大大提高了开发的效率。

### wsgiref模块

最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。

如果要动态生成HTML，就需要把上述步骤自己来实现。不过，接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，还没开始写动态HTML呢，就得花个把月去读HTTP规范。

正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口协议来实现这样的服务器软件，让我们专心用Python编写Web业务。这个接口就是WSGI：Web Server Gateway Interface。而wsgiref模块就是python基于wsgi协议开发的服务模块。

```python
from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


httpd = make_server('', 8080, application)

print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
```

### DIY一个web框架

![img](assets/877318-20180425174338237-444563046.png)

models.py

```python
import pymysql
#连接数据库
conn = pymysql.connect(host='127.0.0.1',port= 3306,user = 'root',passwd='',db='web') #db：库名
#创建游标
cur = conn.cursor()

sql='''
create table userinfo(
        id INT PRIMARY KEY ,
        name VARCHAR(32) ,
        password VARCHAR(32)
)

'''

cur.execute(sql)

#提交
conn.commit()
#关闭指针对象
cur.close()
#关闭连接对象
conn.close()
```

启动文件manage.py

```python
from wsgiref.simple_server import make_server

from app01.views import *
import urls


def routers():

    URLpattern=urls.URLpattern
    return URLpattern


def applications(environ,start_response):

    path=environ.get("PATH_INFO")
    start_response('200 OK', [('Content-Type', 'text/html'),('Charset', 'utf8')])
    urlpattern=routers()
    func=None
    for item in urlpattern:
        if path==item[0]:
            func=item[1]
            break
    if func:
        return [func(environ)]
    else:
        return [b"<h1>404!<h1>"]

if __name__ == '__main__':

    server=make_server("",8889,applications)
    print("server is working...")
    server.serve_forever()
```

urls.py

```python
from app01.views import *


URLpattern = (
    ("/login/", login),
)
```

views

```python
import pymysql

from urllib.parse import parse_qs


def login(request):

    if request.get("REQUEST_METHOD")=="POST":

        try:
            request_body_size = int(request.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0

        request_body = request['wsgi.input'].read(request_body_size)
        data = parse_qs(request_body)


        user=data.get(b"user")[0].decode("utf8")
        pwd=data.get(b"pwd")[0].decode("utf8")

        #连接数据库
        conn = pymysql.connect(host='127.0.0.1',port= 3306,user = 'root',passwd='',db='web') # db：库名
        #创建游标
        cur = conn.cursor()
        SQL="select * from userinfo WHERE NAME ='%s' AND PASSWORD ='%s'"%(user,pwd)
        cur.execute(SQL)

        if cur.fetchone():

            f=open("templates/backend.html","rb")
            data=f.read()
            data=data.decode("utf8")
            return data.encode("utf8")

        else:
             print("OK456")
             return b"user or pwd is wrong"

    else:
        f = open("templates/login.html", "rb")
        data = f.read()
        f.close()
        return data
```

login.html

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h4>登录页面</h4>
<form action="" method="post">
     用户名 <input type="text" name="user">
     密码 <input type="text" name="pwd">
    <input type="submit">
</form>

</body>
</html>
```

backend.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h4>welcome to oldboy!</h4>
</body>
</html>
```

yuan这个package就是一个web框架，下载这个web框架就可以快速实现一些简单的web功能，比如查看时间。

# 4 Django简介



## MVC与MTV模型

## MVC

Web服务器开发领域里著名的MVC模式，所谓MVC就是把Web应用分为模型(M)，控制器(C)和视图(V)三层，他们之间以一种插件式的、松耦合的方式连接在一起，模型负责业务对象与数据库的映射(ORM)，视图负责与用户的交互(页面)，控制器接受用户的输入调用模型和视图完成用户的请求，其示意图如下所示：

![img](assets/877318-20180418162558974-92667466.png)

## MTV

Django的MTV模式本质上和MVC是一样的，也是为了各组件间保持松耦合关系，只是定义上有些许不同，Django的MTV分别是值：

-   M 代表模型（Model）： 负责业务对象和数据库的关系映射(ORM)。
-   T 代表模板 (Template)：负责如何把页面展示给用户(html)。
-   V 代表视图（View）：  负责业务逻辑，并在适当时候调用Model和Template。

除了以上三层之外，还需要一个URL分发器，它的作用是将一个个URL的页面请求分发给不同的View处理，View再调用相应的Model和Template，MTV的响应模式如下所示：

![img](assets/877318-20180418162350672-193671507.png)

一般是用户通过浏览器向我们的服务器发起一个请求(request)，这个请求回去访问视图函数，（如果不涉及到数据调用，那么这个时候视图函数返回一个模板也就是一个网页给用户），视图函数调用模型，模型去数据库查找数据，然后逐级返回，视图函数把返回的数据填充到模板中空格中，最后返回网页给用户。



# Django的下载与基本命令

### 1、下载Django：

```
pip3 install django
pip3 install django=2.0.1
```

### 2、创建一个django project

```
django_admin.py startproject mysite
```

 当前目录下会生成mysite的工程，目录结构如下：

​    ![img](assets/877318-20160724114201404-1121087959.png)

-   manage.py ----- Django项目里面的工具，通过它可以调用django shell和数据库等。
-   settings.py ---- 包含了项目的默认设置，包括数据库信息，调试标志以及其他一些工作的变量。
-   urls.py ----- 负责把URL模式映射到应用程序。

### 3、在mysite目录下创建应用

```
python manage.py startapp blog
```

​    ![img](assets/877318-20160724114930826-472002646.png)

### 4、启动django项目

```
python manage.py runserver ``8080
```

​    这样我们的django就启动起来了！当我们访问：http://127.0.0.1:8080/时就可以看到：

​    ![img](assets/877318-20160724120547497-22629173.png)

[回到顶部](https://www.cnblogs.com/yuanchenqi/articles/8875659.html#_labelTop)

# 基于Django实现的一个简单示例

###  url控制器

```
from django.contrib import admin
from django.urls import path


from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
]
```



### 视图



```
from django.shortcuts import render

# Create your views here.



def index(request):

    import datetime
    now=datetime.datetime.now()
    ctime=now.strftime("%Y-%m-%d %X")

    return render(request,"index.html",{"ctime":ctime})
```



### 模板

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h4>当前时间:{{ ctime }}</h4>

</body>
</html>
```



执行效果如下：

 ![img](assets/877318-20180423153419047-864210640.png)

 

# 5 Django-2的路由层(URLconf)



URL配置(URLconf)就像Django 所支撑网站的目录。它的本质是URL与要为该URL调用的视图函数之间的映射表；你就是以这种方式告诉Django，对于客户端发来的某个URL调用哪一段逻辑代码对应执行。

##  简单的路由配置



```
from django.urls import path,re_path

from app01 import views

urlpatterns = [
    re_path(r'^articles/2003/$', views.special_case_2003),
    re_path(r'^articles/([0-9]{4})/$', views.year_archive),
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
]
```



注意：

-   若要从URL 中捕获一个值，只需要在它周围放置一对圆括号。
-   不需要添加一个前导的反斜杠，因为每个URL 都有。例如，应该是`^articles` 而不是 `^/articles`。
-   每个正则表达式前面的'r' 是可选的但是建议加上。它告诉Python 这个字符串是“原始的” —— 字符串中任何字符都不应该转义

示例：



```
    '''
 一些请求的例子：

/articles/2005/03/ 请求将匹配列表中的第三个模式。Django 将调用函数views.month_archive(request, '2005', '03')。
/articles/2005/3/ 不匹配任何URL 模式，因为列表中的第三个模式要求月份应该是两个数字。
/articles/2003/ 将匹配列表中的第一个模式不是第二个，因为模式按顺序匹配，第一个会首先测试是否匹配。请像这样自由插入一些特殊的情况来探测匹配的次序。
/articles/2003 不匹配任何一个模式，因为每个模式要求URL 以一个反斜线结尾。
/articles/2003/03/03/ 将匹配最后一个模式。Django 将调用函数views.article_detail(request, '2003', '03', '03')。
   
    '''
```



## 有名分组

上面的示例使用简单的、没有命名的正则表达式组（通过圆括号）来捕获URL 中的值并以位置 参数传递给视图。在更高级的用法中，可以使用命名的正则表达式组来捕获URL 中的值并以关键字 参数传递给视图。

在Python 正则表达式中，命名正则表达式组的语法是`(?P<name>pattern)`，其中`name` 是组的名称，`pattern` 是要匹配的模式。

下面是以上URLconf 使用命名组的重写：



```
from django.urls import path,re_path

from app01 import views

urlpatterns = [
    re_path(r'^articles/2003/$', views.special_case_2003),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
]
```



这个实现与前面的示例完全相同，只有一个细微的差别：捕获的值作为关键字参数而不是位置参数传递给视图函数。例如：

```
    '''
    /articles/2005/03/ 请求将调用views.month_archive(request, year='2005', month='03')函数，而不是views.month_archive(request, '2005', '03')。
    /articles/2003/03/03/ 请求将调用函数views.article_detail(request, year='2003', month='03', day='03')。

    '''
```

在实际应用中，这意味你的URLconf 会更加明晰且不容易产生参数顺序问题的错误 —— 你可以在你的视图函数定义中重新安排参数的顺序。当然，这些好处是以简洁为代价；

## 分发



```
'''
At any point, your urlpatterns can “include” other URLconf modules. This
essentially “roots” a set of URLs below other ones.

'''

from django.urls import path,re_path,include
from app01 import views

urlpatterns = [
   re_path(r'^admin/', admin.site.urls),
   re_path(r'^blog/', include('blog.urls')),
]
```



## 反向解析

在使用Django 项目时，一个常见的需求是获得URL 的最终形式，以用于嵌入到生成的内容中（视图中和显示给用户的URL等）或者用于处理服务器端的导航（重定向等）。人们强烈希望不要硬编码这些URL（费力、不可扩展且容易产生错误）或者设计一种与URLconf 毫不相关的专门的URL 生成机制，因为这样容易导致一定程度上产生过期的URL。

在需要URL 的地方，对于不同层级，Django 提供不同的工具用于URL 反查：

-   在模板中：使用url 模板标签。
-   在Python 代码中：使用`from django.urls import reverse()函数` 

urls.py:



```
from django.conf.urls import url

from . import views

urlpatterns = [
    #...
    re_path(r'^articles/([0-9]{4})/$', views.year_archive, name='news-year-archive'),
    #...
]
```



在模板中：

```
<a href="{% url 'news-year-archive' 2012 %}">2012 Archive</a>

<ul>
{% for yearvar in year_list %}
<li><a href="{% url 'news-year-archive' yearvar %}">{{ yearvar }} Archive</a></li>
{% endfor %}
</ul>
```



在python中：

```
from django.urls import reverse
from django.http import HttpResponseRedirect

def redirect_to_year(request):
    # ...
    year = 2006
    # ...
    return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))   # 同redirect("/path/")
```



当命名你的URL 模式时，请确保使用的名称不会与其它应用中名称冲突。如果你的URL 模式叫做`comment`，而另外一个应用中也有一个同样的名称，当你在模板中使用这个名称的时候不能保证将插入哪个URL。在URL 名称中加上一个前缀，比如应用的名称，将减少冲突的可能。我们建议使用`myapp-comment` 而不是`comment`。

## 名称空间

命名空间（英语：Namespace）是表示标识符的可见范围。一个标识符可在多个命名空间中定义，它在不同命名空间中的含义是互不相干的。这样，在一个新的命名空间中可定义任何标识符，它们不会与任何已有的标识符发生冲突，因为已有的定义都处于其它命名空间中。

由于name没有作用域，Django在反解URL时，会在项目全局顺序搜索，当查找到第一个name指定URL时，立即返回

我们在开发项目时，会经常使用name属性反解出URL，当不小心在不同的app的urls中定义相同的name时，可能会导致URL反解错误，为了避免这种事情发生，引入了命名空间。

#### **project的urls.py:**

```
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^app01/', include("app01.urls",namespace="app01")),
    re_path(r'^app02/', include("app02.urls",namespace="app02")),
]
```

#### **app01.urls:**

```
urlpatterns = [
    re_path(r'^index/', index,name="index"),
]
```

#### **app02.urls:**

```
urlpatterns = [
    re_path(r'^index/', index,name="index"),
]
```

#### **app01.views** 

```
from django.core.urlresolvers import reverse

def index(request):

    return  HttpResponse(reverse("app01:index"))
```

#### app02.views

```
from django.core.urlresolvers import reverse

def index(request):

    return  HttpResponse(reverse("app02:index"))
```

## django2.0版的path

思考情况如下：

```
urlpatterns = [  
    re_path('articles/(?P<year>[0-9]{4})/', year_archive),  
    re_path('article/(?P<article_id>[a-zA-Z0-9]+)/detail/', detail_view),  
    re_path('articles/(?P<article_id>[a-zA-Z0-9]+)/edit/', edit_view),  
    re_path('articles/(?P<article_id>[a-zA-Z0-9]+)/delete/', delete_view),  
]
```

考虑下这样的两个问题：

第一个问题，函数 `year_archive` 中year参数是字符串类型的，因此需要先转化为整数类型的变量值，当然`year=int(year)` 不会有诸如如TypeError或者ValueError的异常。那么有没有一种方法，在url中，使得这一转化步骤可以由Django自动完成？

第二个问题，三个路由中article_id都是同样的正则表达式，但是你需要写三遍，当之后article_id规则改变后，需要同时修改三处代码，那么有没有一种方法，只需修改一处即可？

在Django2.0中，可以使用 `path` 解决以上的两个问题。

### 基本示例

这是一个简单的例子：

```
from django.urls import path  
from . import views  
urlpatterns = [  
    path('articles/2003/', views.special_case_2003),  
    path('articles/<int:year>/', views.year_archive),  
    path('articles/<int:year>/<int:month>/', views.month_archive),  
    path('articles/<int:year>/<int:month>/<slug>/', views.article_detail),  
]  
```



基本规则：

-   使用尖括号(`<>`)从url中捕获值。
-   捕获值中可以包含一个转化器类型（converter type），比如使用 `<int:name>` 捕获一个整数变量。若果没有转化器，将匹配任何字符串，当然也包括了 `/` 字符。
-   无需添加前导斜杠。

以下是根据 [2.0官方文档](https://docs.djangoproject.com/en/2.0/topics/http/urls/#example) 而整理的示例分析表：

![img](assets/877318-20180424163727952-1649289117.png)

### path转化器

>   文档原文是Path converters，暂且翻译为转化器。

Django默认支持以下5个转化器：

-   str,匹配除了路径分隔符（`/`）之外的非空字符串，这是默认的形式
-   int,匹配正整数，包含0。
-   slug,匹配字母、数字以及横杠、下划线组成的字符串。
-   uuid,匹配格式化的uuid，如 075194d3-6885-417e-a8a8-6c931e272f00。
-   path,匹配任何非空字符串，包含了路径分隔符

### 注册自定义转化器

对于一些复杂或者复用的需要，可以定义自己的转化器。转化器是一个类或接口，它的要求有三点：

-   `regex` 类属性，字符串类型

-   `to_python(self, value)` 方法，value是由类属性 `regex` 所匹配到的字符串，返回具体的Python变量值，以供Django传递到对应的视图函数中。
-   `to_url(self, value)` 方法，和 `to_python` 相反，value是一个具体的Python变量值，返回其字符串，通常用于url反向引用。

例子：

```
class FourDigitYearConverter:  
    regex = '[0-9]{4}'  
    def to_python(self, value):  
        return int(value)  
    def to_url(self, value):  
        return '%04d' % value  
```

使用`register_converter` 将其注册到URL配置中：

```
from django.urls import register_converter, path  
from . import converters, views  
register_converter(converters.FourDigitYearConverter, 'yyyy')  
urlpatterns = [  
    path('articles/2003/', views.special_case_2003),  
    path('articles/<yyyy:year>/', views.year_archive),  
    ...  
]  
```



# [6 Django的视图层](https://www.cnblogs.com/yuanchenqi/articles/8876856.html)

 

## 视图函数

一个视图函数，简称视图，是一个简单的Python 函数，它接受Web请求并且返回Web响应。响应可以是一张网页的HTML内容，一个重定向，一个404错误，一个XML文档，或者一张图片. . . 是任何东西都可以。无论视图本身包含什么逻辑，都要返回响应。代码写在哪里也无所谓，只要它在你的Python目录下面。除此之外没有更多的要求了——可以说“没有什么神奇的地方”。为了将代码放在某处，约定是将视图放置在项目或应用程序目录中的名为`views.py`的文件中。

下面是一个返回当前日期和时间作为HTML文档的视图：

```
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
```

让我们逐行阅读上面的代码：

-   首先，我们从 `django.shortcuts`模块导入了`HttpResponse`类，以及Python的`datetime`库。

-   接着，我们定义了`current_datetime`函数。它就是视图函数。每个视图函数都使用`HttpRequest`对象作为第一个参数，并且通常称之为`request`。

    注意,视图函数的名称并不重要；不需要用一个统一的命名方式来命名，以便让Django识别它。我们将其命名为`current_datetime`，是因为这个名称能够精确地反映出它的功能。

-   这个视图会返回一个`HttpResponse`对象，其中包含生成的响应。每个视图函数都负责返回一个`HttpResponse`对象。

#### ![img](assets/877318-20160725101445044-1768854009.jpg)

视图层，熟练掌握两个对象即可：请求对象(request)和响应对象(HttpResponse)

## HttpRequest对象

### request属性 　　

django将请求报文中的请求行、首部信息、内容主体封装成 HttpRequest 类中的属性。 除了特殊说明的之外，其他均为只读的。

```
/*

1.HttpRequest.GET

　　一个类似于字典的对象，包含 HTTP GET 的所有参数。详情请参考 QueryDict 对象。

2.HttpRequest.POST

　　一个类似于字典的对象，如果请求中包含表单数据，则将这些数据封装成 QueryDict 对象。

　　POST 请求可以带有空的 POST 字典 —— 如果通过 HTTP POST 方法发送一个表单，但是表单中没有任何的数据，QueryDict 对象依然会被创建。
   因此，不应该使用 if request.POST  来检查使用的是否是POST 方法；应该使用 if request.method == "POST"
　　另外：如果使用 POST 上传文件的话，文件信息将包含在 FILES 属性中。
   
   注意：键值对的值是多个的时候,比如checkbox类型的input标签，select标签，需要用：
        request.POST.getlist("hobby")

3.HttpRequest.body

　　一个字符串，代表请求报文的主体。在处理非 HTTP 形式的报文时非常有用，例如：二进制图片、XML,Json等。
　　但是，如果要处理表单数据的时候，推荐还是使用 HttpRequest.POST 。


4.HttpRequest.path

　　一个字符串，表示请求的路径组件（不含域名）。
　　例如："/music/bands/the_beatles/"

5.HttpRequest.method

　　一个字符串，表示请求使用的HTTP 方法。必须使用大写。
　　例如："GET"、"POST"


6.HttpRequest.encoding

　　一个字符串，表示提交的数据的编码方式（如果为 None 则表示使用 DEFAULT_CHARSET 的设置，默认为 'utf-8'）。
   这个属性是可写的，你可以修改它来修改访问表单数据使用的编码。
   接下来对属性的任何访问（例如从 GET 或 POST 中读取数据）将使用新的 encoding 值。
   如果你知道表单数据的编码不是 DEFAULT_CHARSET ，则使用它。


7.HttpRequest.META

 　　一个标准的Python 字典，包含所有的HTTP 首部。具体的头部信息取决于客户端和服务器，下面是一些示例：

    CONTENT_LENGTH —— 请求的正文的长度（是一个字符串）。
    CONTENT_TYPE —— 请求的正文的MIME 类型。
    HTTP_ACCEPT —— 响应可接收的Content-Type。
    HTTP_ACCEPT_ENCODING —— 响应可接收的编码。
    HTTP_ACCEPT_LANGUAGE —— 响应可接收的语言。
    HTTP_HOST —— 客服端发送的HTTP Host 头部。
    HTTP_REFERER —— Referring 页面。
    HTTP_USER_AGENT —— 客户端的user-agent 字符串。
    QUERY_STRING —— 单个字符串形式的查询字符串（未解析过的形式）。
    REMOTE_ADDR —— 客户端的IP 地址。
    REMOTE_HOST —— 客户端的主机名。
    REMOTE_USER —— 服务器认证后的用户。
    REQUEST_METHOD —— 一个字符串，例如"GET" 或"POST"。
    SERVER_NAME —— 服务器的主机名。
    SERVER_PORT —— 服务器的端口（是一个字符串）。
 　　从上面可以看到，除 CONTENT_LENGTH 和 CONTENT_TYPE 之外，请求中的任何 HTTP 首部转换为 META 的键时，
    都会将所有字母大写并将连接符替换为下划线最后加上 HTTP_  前缀。
    所以，一个叫做 X-Bender 的头部将转换成 META 中的 HTTP_X_BENDER 键。

8.HttpRequest.FILES

　　一个类似于字典的对象，包含所有的上传文件信息。
   FILES 中的每个键为<input type="file" name="" /> 中的name，值则为对应的数据。
　　注意，FILES 只有在请求的方法为POST 且提交的<form> 带有enctype="multipart/form-data" 的情况下才会
   包含数据。否则，FILES 将为一个空的类似于字典的对象。


9.HttpRequest.COOKIES

　　一个标准的Python 字典，包含所有的cookie。键和值都为字符串。



10.HttpRequest.session

 　　一个既可读又可写的类似于字典的对象，表示当前的会话。只有当Django 启用会话的支持时才可用。
    完整的细节参见会话的文档。


11.HttpRequest.user(用户认证组件下使用)

　　一个 AUTH_USER_MODEL 类型的对象，表示当前登录的用户。

　　如果用户当前没有登录，user 将设置为 django.contrib.auth.models.AnonymousUser 的一个实例。你可以通过 is_authenticated() 区分它们。

    例如：

    if request.user.is_authenticated():
        # Do something for logged-in users.
    else:
        # Do something for anonymous users.


     　　user 只有当Django 启用 AuthenticationMiddleware 中间件时才可用。

     -------------------------------------------------------------------------------------

    匿名用户
    class models.AnonymousUser

    django.contrib.auth.models.AnonymousUser 类实现了django.contrib.auth.models.User 接口，但具有下面几个不同点：

    id 永远为None。
    username 永远为空字符串。
    get_username() 永远返回空字符串。
    is_staff 和 is_superuser 永远为False。
    is_active 永远为 False。
    groups 和 user_permissions 永远为空。
    is_anonymous() 返回True 而不是False。
    is_authenticated() 返回False 而不是True。
    set_password()、check_password()、save() 和delete() 引发 NotImplementedError。
    New in Django 1.8:
    新增 AnonymousUser.get_username() 以更好地模拟 django.contrib.auth.models.User。

*/
```



### request常用方法



```
/*

1.HttpRequest.get_full_path()

　　返回 path，如果可以将加上查询字符串。

　　例如："/music/bands/the_beatles/?print=true"


2.HttpRequest.is_ajax()

　　如果请求是通过XMLHttpRequest 发起的，则返回True，方法是检查 HTTP_X_REQUESTED_WITH 相应的首部是否是字符串'XMLHttpRequest'。

　　大部分现代的 JavaScript 库都会发送这个头部。如果你编写自己的 XMLHttpRequest 调用（在浏览器端），你必须手工设置这个值来让 is_ajax() 可以工作。

　　如果一个响应需要根据请求是否是通过AJAX 发起的，并且你正在使用某种形式的缓存例如Django 的 cache middleware，
   你应该使用 vary_on_headers('HTTP_X_REQUESTED_WITH') 装饰你的视图以让响应能够正确地缓存。

*/
```



## HttpResponse对象

响应对象主要有三种形式：

-   HttpResponse()
-   render()
-   redirect()

HttpResponse()括号内直接跟一个具体的字符串作为响应体，比较直接很简单，所以这里主要介绍后面两种形式。

### render()

```
render(request, template_name[, context]）` `结合一个给定的模板和一个给定的上下文字典，并返回一个渲染后的 HttpResponse 对象。
参数：
     request： 用于生成响应的请求对象。

     template_name：要使用的模板的完整名称，可选的参数

     context：添加到模板上下文的一个字典。默认是一个空字典。如果字典中的某个值是可调用的，视图将在渲染模板之前调用它。

render方法就是将一个模板页面中的模板语法进行渲染，最终渲染成一个html页面作为响应体。
```

### redirect()

传递要重定向的一个硬编码的URL

```
def` `my_view(request):``  ``...``  ``return` `redirect(``'/some/url/'``)
```

也可以是一个完整的URL：

```
def` `my_view(request):``  ``...``  ``return` `redirect(``'http://example.com/'``)　
```

key：两次请求　

```
1）301和302的区别。

　　301和302状态码都表示重定向，就是说浏览器在拿到服务器返回的这个状态码后会自动跳转到一个新的URL地址，这个地址可以从响应的Location首部中获取
  （用户看到的效果就是他输入的地址A瞬间变成了另一个地址B）——这是它们的共同点。

　　他们的不同在于。301表示旧地址A的资源已经被永久地移除了（这个资源不可访问了），搜索引擎在抓取新内容的同时也将旧的网址交换为重定向之后的网址；

　　302表示旧地址A的资源还在（仍然可以访问），这个重定向只是临时地从旧地址A跳转到地址B，搜索引擎会抓取新的内容而保存旧的网址。 SEO302好于301

 

2）重定向原因：
（1）网站调整（如改变网页目录结构）；
（2）网页被移到一个新地址；
（3）网页扩展名改变(如应用需要把.php改成.Html或.shtml)。
        这种情况下，如果不做重定向，则用户收藏夹或搜索引擎数据库中旧地址只能让访问客户得到一个404页面错误信息，访问流量白白丧失；再者某些注册了多个域名的
    网站，也需要通过重定向让访问这些域名的用户自动跳转到主站点等。
```



用redirect可以解释APPEND_SLASH的用法！

 # [7 Django的模板层](https://www.cnblogs.com/yuanchenqi/articles/8876892.html)

你可能已经注意到我们在例子视图中返回文本的方式有点特别。 也就是说，HTML被直接硬编码在 Python代码之中。

```
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
```

尽管这种技术便于解释视图是如何工作的，但直接将HTML硬编码到你的视图里却并不是一个好主意。 让我们来看一下为什么：

-   对页面设计进行的任何改变都必须对 Python 代码进行相应的修改。 站点设计的修改往往比底层 Python 代码的修改要频繁得多，因此如果可以在不进行 Python 代码修改的情况下变更设计，那将会方便得多。

-   Python 代码编写和 HTML 设计是两项不同的工作，大多数专业的网站开发环境都将他们分配给不同的人员（甚至不同部门）来完成。 设计者和HTML/CSS的编码人员不应该被要求去编辑Python的代码来完成他们的工作。

-   程序员编写 Python代码和设计人员制作模板两项工作同时进行的效率是最高的，远胜于让一个人等待另一个人完成对某个既包含 Python又包含 HTML 的文件的编辑工作。

基于这些原因，将页面的设计和Python的代码分离开会更干净简洁更容易维护。 我们可以使用 Django的 *模板系统* (Template System)来实现这种模式，这就是本章要具体讨论的问题。

```
python的模板：HTML代码＋模板语法
```

[![复制代码](assets/copycode-20211009142828435.gif)](javascript:void(0);)

```
def current_time(req):
    # ================================原始的视图函数
    # import datetime
    # now=datetime.datetime.now()
    # html="<html><body>现在时刻：<h1>%s.</h1></body></html>" %now


    # ================================django模板修改的视图函数
    # from django.template import Template,Context
    # now=datetime.datetime.now()
    # t=Template('<html><body>现在时刻是:<h1>{{current_date}}</h1></body></html>')
    # #t=get_template('current_datetime.html')
    # c=Context({'current_date':str(now)})
    # html=t.render(c)
    #
    # return HttpResponse(html)


    #另一种写法(推荐)
    import datetime
    now=datetime.datetime.now()
    return render(req, 'current_datetime.html', {'current_date':str(now)[:19]})
```

[![复制代码](assets/copycode-20211009142828435.gif)](javascript:void(0);)

## 1 模板语法之变量

在 Django 模板中遍历复杂数据结构的关键是句点字符, 语法： 

```
{{var_name}}
```

***views.py：\***

[![复制代码](assets/copycode-20211009142828435.gif)](javascript:void(0);)

```
def index(request):
    import datetime
    s="hello"
    l=[111,222,333]    # 列表
    dic={"name":"yuan","age":18}  # 字典
    date = datetime.date(1993, 5, 2)   # 日期对象
 
    class Person(object):
        def __init__(self,name):
            self.name=name
 
    person_yuan=Person("yuan")  # 自定义类对象
    person_egon=Person("egon")
    person_alex=Person("alex")
 
    person_list=[person_yuan,person_egon,person_alex]
 
 
    return render(request,"index.html",{"l":l,"dic":dic,"date":date,"person_list":person_list})　
```

[![复制代码](assets/copycode-20211009142828435.gif)](javascript:void(0);)

***template：\*** 

```
<h4>{{s}}</h4>
<h4>列表:{{ l.0 }}</h4>
<h4>列表:{{ l.2 }}</h4>
<h4>字典:{{ dic.name }}</h4>
<h4>日期:{{ date.year }}</h4>
<h4>类对象列表:{{ person_list.0.name }}</h4>
```

注意：句点符也可以用来引用对象的方法(无参数方法):

```
<h4>字典:{{ dic.name.upper }}<``/``h4>
```

## 2 模板之过滤器

语法：

```
{{obj|filter__name:param}}
```

### `default`

如果一个变量是false或者为空，使用给定的默认值。否则，使用变量的值。例如：

```
{{ value|default:"nothing" }}

```

### length

返回值的长度。它对字符串和列表都起作用。例如：

```
{{ value|length }}
```

如果 value 是 ['a', 'b', 'c', 'd']，那么输出是 4。

### `filesizeformat`

将值格式化为一个 “人类可读的” 文件尺寸 （例如 `'13 KB'`, `'4.1 MB'`, `'102 bytes'`, 等等）。例如：

```
{{ value|filesizeformat }}

```

如果 `value` 是 123456789，输出将会是 `117.7 MB`。　　

### date

如果 value=datetime.datetime.now()

```
{{ value|date:"Y-m-d" }}　　
```

### slice

如果 value="hello world"

```
{{ value|slice:"2:-1" }}
```

### truncatechars[ ](http://python.usyiyi.cn/documents/django_182/ref/templates/builtins.html#truncatechars)

如果字符串字符多于指定的字符数量，那么会被截断。截断的字符串将以可翻译的省略号序列（“...”）结尾。

**参数：**要截断的字符数

例如：

```
{{ value|truncatechars:9 }}
```

### safe

Django的模板中会对HTML标签和JS等语法标签进行自动转义，原因显而易见，这样是为了安全。但是有的时候我们可能不希望这些HTML元素被转义，比如我们做一个内容管理系统，后台添加的文章中是经过修饰的，这些修饰可能是通过一个类似于FCKeditor编辑加注了HTML修饰符的文本，如果自动转义的话显示的就是保护HTML标签的源文件。为了在Django中关闭HTML的自动转义有两种方式，如果是一个单独的变量我们可以通过过滤器“|safe”的方式告诉Django这段代码是安全的不必转义。比如：

```
value="<a href="">点击</a>"

{{ value|safe}}
```

这里简单介绍一些常用的模板的过滤器，[更多详见](http://python.usyiyi.cn/translate/django_182/ref/templates/builtins.html#ref-templates-builtins-tags)

## 3 模板之标签　

标签看起来像是这样的： `{% tag %}`。标签比变量更加复杂：一些在输出中创建文本，一些通过循环或逻辑来控制流程，一些加载其后的变量将使用到的额外信息到模版中。一些标签需要开始和结束标签 （例如`{% tag %} ...`标签 内容 ... {% endtag %}）。

### **for标签**

遍历每一个元素：

```
{% for person in person_list %}
    <p>{{ person.name }}</p>
{% endfor %}
```

可以利用`{% for obj in list reversed %}`反向完成循环。

遍历一个字典：

```
{% for key,val in dic.items %}
    <p>{{ key }}:{{ val }}</p>
{% endfor %}
```

注：循环序号可以通过｛｛forloop｝｝显示　　

```
forloop.counter            The current iteration of the loop (1-indexed)
forloop.counter0           The current iteration of the loop (0-indexed)
forloop.revcounter         The number of iterations from the end of the loop (1-indexed)
forloop.revcounter0        The number of iterations from the end of the loop (0-indexed)
forloop.first              True if this is the first time through the loop
forloop.last               True if this is the last time through the loop
```

### for ... empty[ ](http://python.usyiyi.cn/documents/django_182/ref/templates/builtins.html#for-empty)

`for` 标签带有一个可选的`{% empty %}` 从句，以便在给出的组是空的或者没有被找到时，可以有所操作。

```
{% for person in person_list %}
    <p>{{ person.name }}</p>

{% empty %}
    <p>sorry,no person here</p>
{% endfor %}
```

### if 标签

`{% if %}`会对一个变量求值，如果它的值是“True”（存在、不为空、且不是boolean类型的false值），对应的内容块会输出。

[![复制代码](assets/copycode-20211009142828435.gif)](javascript:void(0);)

```
{% if num > 100 or num < 0 %}
    <p>无效</p>
{% elif num > 80 and num < 100 %}
    <p>优秀</p>
{% else %}
    <p>凑活吧</p>
{% endif %}
```

[![复制代码](assets/copycode-20211009142828435.gif)](javascript:void(0);)

### with[ ](http://python.usyiyi.cn/documents/django_182/ref/templates/builtins.html#with)

使用一个简单地名字缓存一个复杂的变量，当你需要使用一个“昂贵的”方法（比如访问数据库）很多次的时候是非常有用的

例如：

```
{% with total=business.employees.count %}
    {{ total }} employee{{ total|pluralize }}
{% endwith %}
```

### csrf_token[ ](http://python.usyiyi.cn/documents/django_182/ref/templates/builtins.html#csrf-token)

这个标签用于跨站请求伪造保护

## 4 自定义标签和过滤器

1、在settings中的INSTALLED_APPS配置当前app，不然django无法找到自定义的simple_tag.

2、在app中创建templatetags模块(模块名只能是templatetags)

3、创建任意 .py 文件，如：my_tags.py

```python
from django import template
from django.utils.safestring import mark_safe
 
register = template.Library()   #register的名字是固定的,不可改变
 
 
@register.filter
def filter_multi(v1,v2):
    return  v1 * v2
<br>
@register.simple_tag
def simple_tag_multi(v1,v2):
    return  v1 * v2
<br>
@register.simple_tag
def my_input(id,arg):
    result = "<input type='text' id='%s' class='%s' />" %(id,arg,)
    return mark_safe(result)
```



**4、在使用自定义simple_tag和filter的html文件中导入之前创建的 my_tags.py**

```
{% load my_tags %}　

```

**5、使用simple_tag和filter（如何调用）**

```
-------------------------------.html
{% load xxx %}  
      
# num=12
{{ num|filter_multi:2 }} #24
 
{{ num|filter_multi:"[22,333,4444]" }}
 
{% simple_tag_multi 2 5 %}  参数不限,但不能放在if for语句中
{% simple_tag_multi num 5 %}
```

注意：filter可以用在if等语句后，simple_tag不可以

```
{% if num|filter_multi:30 > 100 %}
    {{ num|filter_multi:30 }}
{% endif %}
```

## 5 模板继承 (extend)

Django模版引擎中最强大也是最复杂的部分就是模版继承了。模版继承可以让您创建一个基本的“骨架”模版，它包含您站点中的全部元素，并且可以定义能够被子模版覆盖的 blocks 。

通过从下面这个例子开始，可以容易的理解模版继承：

[![复制代码](assets/copycode-20211009142828435.gif)](javascript:void(0);)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css" />
    <title>{% block title %}My amazing site{%/span> endblock %}</title>
</head>

<body>
    <div id="sidebar">
        {% block sidebar %}
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/blog/">Blog</a></li>
        </ul>
        {% endblock %}
    </div>

    <div id="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

[![复制代码](assets/copycode-20211009142828435.gif)](javascript:void(0);)

这个模版，我们把它叫作 `base.html`， 它定义了一个可以用于两列排版页面的简单HTML骨架。“子模版”的工作是用它们的内容填充空的blocks。

在这个例子中， `block` 标签定义了三个可以被子模版内容填充的block。 `block` 告诉模版引擎： 子模版可能会覆盖掉模版中的这些位置。

子模版可能看起来是这样的：

```
{% extends "base.html" %}
 
{% block title %}My amazing blog{% endblock %}
 
{% block content %}
{% for entry in blog_entries %}
    <h2>{{ entry.title }}</h2>
    <p>{{ entry.body }}</p>
{% endfor %}
{% endblock %}
```

`extends` 标签是这里的关键。它告诉模版引擎，这个模版“继承”了另一个模版。当模版系统处理这个模版时，首先，它将定位父模版——在此例中，就是“base.html”。

那时，模版引擎将注意到 `base.html` 中的三个 `block` 标签，并用子模版中的内容来替换这些block。根据 `blog_entries` 的值，输出可能看起来是这样的：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css" />
    <title>My amazing blog</title>
</head>
 
<body>
    <div id="sidebar">
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/blog/">Blog</a></li>
        </ul>
    </div>
 
    <div id="content">
        <h2>Entry one</h2>
        <p>This is my first entry.</p>
 
        <h2>Entry two</h2>
        <p>This is my second entry.</p>
    </div>
</body>
</html>
```

请注意，子模版并没有定义 `sidebar` block，所以系统使用了父模版中的值。父模版的 `{% block %}` 标签中的内容总是被用作备选内容（fallback）。

这种方式使代码得到最大程度的复用，并且使得添加内容到共享的内容区域更加简单，例如，部分范围内的导航。

这里是使用继承的一些提示：

-   如果你在模版中使用 `{% extends %}` 标签，它必须是模版中的第一个标签。其他的任何情况下，模版继承都将无法工作。

-   在base模版中设置越多的 `{% block %}` 标签越好。请记住，子模版不必定义全部父模版中的blocks，所以，你可以在大多数blocks中填充合理的默认内容，然后，只定义你需要的那一个。多一点钩子总比少一点好。

-   如果你发现你自己在大量的模版中复制内容，那可能意味着你应该把内容移动到父模版中的一个 `{% block %}` 中。

-   If you need to get the content of the block from the parent template, the `{{ block.super }}` variable will do the trick. This is useful if you want to add to the contents of a parent block instead of completely overriding it. Data inserted using `{{ block.super }}` will not be automatically escaped (see the next section), since it was already escaped, if necessary, in the parent template.

-   为了更好的可读性，你也可以给你的 `{% endblock %}` 标签一个 *名字* 。例如：

    ```python
    {% block content %}
    ...
    {% endblock content %}　　
    ```

    在大型模版中，这个方法帮你清楚的看到哪一个　 `{% block %}` 标签被关闭了。

-   不能在一个模版中定义多个相同名字的 `block` 标签。
