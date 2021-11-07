from django.shortcuts import render, HttpResponse


# Create your views here.


def index(request):
    print("index函数执行...")
    return HttpResponse("<h1>hello world</h1>")



def timer(request):

    return HttpResponse("<h3>当前时间：2012-12-12</h3>")