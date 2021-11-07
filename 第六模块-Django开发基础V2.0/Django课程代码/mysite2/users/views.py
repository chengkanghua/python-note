from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
from django.http import JsonResponse

'''

POST / HTTP/1.1
...

请求体   urlencoded : a=1&b=2&c=3    json: {"a":1,"b":2,"c":3}

'''


def index(request):
    # ************************************* 请求对象 *************************************

    # 获取请求方式
    # print(request.method) # POST

    # 发送POST请求时获取数据的方式
    # print(request.body) #
    # print(request.POST) # 只有数据格式是 urlencoded
    # user = request.POST.get("user")
    # pwd = request.POST.get("pwd")
    # hobby = request.POST.getlist("hobby")
    # print(user,pwd,hobby)

    # 发送GET请求获取数据

    # print(request.GET) # <QueryDict: {'a': ['1'], 'b': ['2']}>

    # 获取请求路径
    # print(request.path)  # /users
    # print(request.get_full_path()) # /users?a=1

    # 获取请求头数据
    # print(request.META)
    # print(request.META.get("HTTP_HOST"))
    # print(request.META.get("HTTP_XXX"))

    # ************************************* 响应对象 *************************************

    # return HttpResponse("OK")
    # return HttpResponse("您访问的资源不存在",status=404)
    # return HttpResponse("<h1>OK</h1>",content_type="text/plain")

    # 自定义响应头
    # res = HttpResponse("OK")
    # res["user"] = "yuan"
    # return res

    # 响应json数据

    # book = {"title":"金瓶梅","price":199}
    # import json
    # return HttpResponse(json.dumps(book,ensure_ascii=False),content_type="application/json")
    # 序列化一个字典数据
    # return JsonResponse(book)

    # 序列化一个列表数据
    # books = [{"title": "金瓶梅", "price": 199}, {"title": "水浒传", "price": 299}]
    # return JsonResponse(books, safe=False)
    print(request.META)
    remote_addr = request.META.get("REMOTE_ADDR")


    return render(request,"users/index.html",{"ip":remote_addr})




def login(request):

    return render(request,"users/login.html")


def auth(request):

    #  获取数据
    print("request.POST:",request.POST)

    user = request.POST.get("user")
    pwd = request.POST.get("pwd")

    # 模拟数据校验
    if user == "rain" and pwd == "123":
        # return HttpResponse("验证通过")
        return redirect("/users/")
    else:
        # return HttpResponse("用户名或者密码错误")
        # return redirect("/users/login")
        msg = "用户名或者密码错误"
        return render(request,"users/login.html",{"msg":msg})




