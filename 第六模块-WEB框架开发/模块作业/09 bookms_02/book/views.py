from django.shortcuts import render, HttpResponse, redirect
from .models import Publish, Author, Book
from book.Myforms import UserForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.

# 登陆
def login(request):
    if request.method == 'POST':
        print(request.POST)
        response = {'user': None, 'msg': None}
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = auth.authenticate(username=user, password=pwd)
        if user:
            auth.login(request, user)
            response['user'] = user.username
        else:
            response['msg'] = '用户名或者密码错误'
        return JsonResponse(response)

    form = UserForm()
    return render(request, 'login.html', {'form': form})


# 注册用户
def register(request):
    """
    注册视图函数:
       get请求响应注册页面
       post(Ajax)请求,校验字段,响应字典
    :param request:
    :return:
    """
    if request.is_ajax():
        # print(request.POST)
        form = UserForm(request.POST)  # 校验字段

        response = {"user": None, "msg": None}
        if form.is_valid():
            response["user"] = form.cleaned_data.get("user")

            # 生成一条用户纪录
            user = form.cleaned_data.get("user")
            print("user", user)
            pwd = form.cleaned_data.get("pwd")

            User.objects.create_user(username=user, password=pwd, )
        else:
            print(form.cleaned_data)
            print(form.errors)
            response["msg"] = form.errors
    return JsonResponse(response)


def publish(request):
    publish_list = Publish.objects.all()
    books = Book.objects.all()

    return render(request, 'publish.html', {'publish_list': publish_list})


def del_publish(request, id):
    Publish.objects.filter(pk=id).delete()

    return redirect('/publish/')


def authors(request):
    author_list = Author.objects.all()
    return render(request, 'authors.html', {'author_list': author_list})


def del_author(request, id):
    Author.objects.filter(pk=id).delete()
    return redirect('/authors/')


@login_required
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish_id = request.POST.get("publish_id")
        authors_id_list = request.POST.getlist("authors_id_list")  # checkbox,select

        book_obj = Book.objects.create(title=title, price=price, publishDate=pub_date, publish_id=publish_id)
        print(authors_id_list)  # ['2', '3']

        book_obj.authors.add(*authors_id_list)

        return redirect('/books/')

    publish_list = Publish.objects.all()
    author_list = Author.objects.all()

    return render(request, "addbook.html", {"author_list": author_list, "publish_list": publish_list})


@login_required
def books(request, **kwargs):
    print(kwargs)
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    if kwargs:
        condition = kwargs.get('condition')
        param = kwargs.get('param')
        if condition == 'publish':
            book_list = Book.objects.all().filter(publish=param)
        elif condition == 'author':
            book_list = Book.objects.filter(authors=param)
    else:
        book_list = Book.objects.all()

    return render(request, "books.html", {"book_list": book_list, 'publish_list': publish_list,'author_list': author_list})


@login_required
def change_book(request, edit_book_id):
    edit_book_obj = Book.objects.filter(pk=edit_book_id).first()

    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish_id = request.POST.get("publish_id")
        authors_id_list = request.POST.getlist("authors_id_list")  # checkbox,select

        Book.objects.filter(pk=edit_book_id).update(title=title, price=price, publishDate=pub_date,
                                                    publish_id=publish_id)
        # edit_book_obj.authors.clear()
        # edit_book_obj.authors.add(*authors_id_list)
        # set 等于以上两条语句
        edit_book_obj.authors.set(authors_id_list)

        return redirect("/books/")

    publish_list = Publish.objects.all()
    author_list = Author.objects.all()

    return render(request, "editbook.html",
                  {"edit_book_obj": edit_book_obj, "publish_list": publish_list, "author_list": author_list})

def book_edit(request):
    if request.is_ajax():
        # print(request.POST)
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_pk = request.POST.get('publish_pk')
        author_list = request.POST.get('author_list')
        print(title,pub_date,publish_pk,author_list)

    return redirect('/books/')

def change_book2(request):
    if request.is_ajax():
        book_pk = request.POST.get('book_pk')
        book_obj = Book.objects.filter(nid=book_pk).first()
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()

        print(request.POST)

        response = {'title':'aa','data':'1330-123','publish': '华夏出版社','publish_list':['北京出版社','华夏出版社']}
    return JsonResponse(response)

@login_required
def delete_book(request, delete_book_id):
    Book.objects.filter(pk=delete_book_id).delete()

    return redirect("/books/")


def logout(request):
    auth.logout(request)

    return redirect('/login/')
