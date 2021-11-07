from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def get_timer(request):
    '''
    :param request:
    :return: HttpResponse对象
    '''
    # 获取数据

    nowStr = datetime.datetime.now().strftime("%Y-%m-%d %X")


    return render(request,"app01/timer.html",{"now":nowStr})


def index(request):

    # 返回给客户端一个简单字符串
    # return HttpResponse("index...")
    # 返回给客户端一个页面字符串

    return render(request, "app01/index.html")



def show(request,m):

    print("mobile:",m,type(m))

    return HttpResponse(f"hi,{m}用户")




