from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from app01.models import Book, user


def registry(request):
    if request.method == 'POST':
        # print(request.POST)
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        user_obj = user.objects.create(username=uname, password=pwd)
        return HttpResponse('Ok')
    return render(request, 'registry.html')


def login(request):
    if request.method == 'POST':
        print(request.POST)
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        user_obj = user.objects.get(username=uname)
        if not user_obj:
            return HttpResponse("用户或密码错误")
        if pwd == user_obj.password:
            return HttpResponse("登陆成功")
        else:
            return HttpResponse("用户或密码错误")
    return render(request, 'login.html')


def books(request):
    book_list = Book.objects.all()
    # print(books)
    return render(request, "books.html", locals())


def authorlist(request, author):
    authorlist = Book.objects.filter(author=author)
    # print(authorlist)
    return render(request, "authorlist.html", locals())


def publishlist(request, publish):
    publishlist = Book.objects.filter(publish=publish)
    return render(request, "publishlist.html", locals())


def addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        author = request.POST.get("author")
        publish = request.POST.get("publish")
        print(request.POST)
        book_obj = Book.objects.create(title=title, price=price, pub_date=pub_date, author=author, publish=publish)
        return redirect('/books/')
    return render(request, "addbook.html")


def delbook(request, id):
    Book.objects.filter(id=id).delete()
    print(id)
    return redirect("/books/")


def editbook(request, id):
    book_obj = Book.objects.all().get(id=id)
    print(id,book_obj.pub_date)
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        author = request.POST.get("author")
        publish = request.POST.get("publish")
        Book.objects.filter(id=id).update(title=title, price=price, pub_date=pub_date, author=author, publish=publish)
        print(request.POST)
        return redirect("/books/")
    return render(request, 'editbook.html', locals())
