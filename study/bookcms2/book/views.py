from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        publishDate = request.POST.get("publishDate")
        price = request.POST.get("price")
        publish_id = request.POST.get("publish_id")
        authors_id_list = request.POST.getlist("authors_id_list")
        print(authors_id_list)
        print(request.POST)
        book_obj = Book.objects.create(title=title,publishDate=publishDate,price=price,publish_id=publish_id)
        print(book_obj)
        book_obj.authors.add(*authors_id_list)

        return HttpResponse("add ok")
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    return render(request,"add_book.html",{"publish_list":publish_list,"author_list":author_list})

def books(request):

    return render(request,"")


