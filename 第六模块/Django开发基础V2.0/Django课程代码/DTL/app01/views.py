from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
from django.template.loader import get_template


class Book(object):
    def __init__(self, title, price, publish):
        self.title = title
        self.price = price
        self.publish = publish

    def __str__(self):
        return self.title


def index(request):
    '''
    # (1) 获取模板文件
    template = get_template("index.html")

    # (2) 获取数据

    context = {"name": "rain"}

    # (3) 渲染
    html = template.render(context,request)

    print(":::",html)

    return HttpResponse(html,content_type="text/html")

    '''

    name = "root"
    name = None
    age = 21
    score = 78
    is_married = False

    book_list = ["三国演义", "水浒传", "西游记", "金瓶梅"]

    zhangsan = {"name": "张三", "age": 33}

    book01 = Book("三体", 199, "苹果出版社")
    book02 = Book("飘", 299, "苹果出版社")
    book03 = Book("乱世佳人", 99, "西瓜出版社")
    book04 = Book("放风筝的人", 199, "苹果出版社")

    books = [book01,book02, book03, book04]

    books2 = ["AAA"]

    import datetime
    now = datetime.datetime.now()

    fileSize = 122324789

    content = "i am rain,AAA BBB CCC"

    link = "<a href = 'http://www.baidu.com'>baidu</a>"

    comment = "<script>alert(123)</script>"

    my_tel = "13653268428"

    return render(request, "index.html", locals())

# 反向解析
from django.urls import reverse

def order(request):

    order_list = ["订单1","订单2","订单3"]

    print("反向解析：：：",reverse("ind"))   # 反向解析：：： /index/

    return render(request,"order.html",{"order_list":order_list})





