from django.shortcuts import render

# Create your views here.

def index(request):
    import datetime
    now= datetime.datetime.now()
    ctime = now.strftime("%Y-%m-%d %x")
    return render(request,"index.html",{"ctime":ctime})


