from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from app01 import models
from utils.MyModelForm import ItModelForm



def index(request):
    """ 项目主页 """
    if request.method == "POST":
        return JsonResponse({"code": 0, "message": "项目主页的post请求，非法"})
    else:
        it_obj = models.It.objects.all()
        # print(1111111, it_obj)
        return render(request, 'index.html', {"it_obj": it_obj})

def add_it(request):
    """ 添加项目 """
    if request.method == "POST":
        form_data = ItModelForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('/index/')
        else:
            return render(request, 'add_it.html', {"it_form_obj": form_data})
    else:
        it_form_obj = ItModelForm()
        return render(request, 'add_it.html', {"it_form_obj": it_form_obj})

def edit_it(request, pk):
    """ 编辑项目， pk:项目的pk """
    it_obj = models.It.objects.filter(pk=pk).first()
    if request.method == "POST":
        form_data = ItModelForm(request.POST, instance=it_obj)
        if form_data.is_valid():
            form_data.save()
            return redirect('/index/')
        else:
            return render(request, 'add_it.html', {"it_form_obj": form_data})
    else:
        it_form_obj = ItModelForm(instance=it_obj)
        return render(request, 'edit_it.html', {"it_form_obj": it_form_obj})


def delete_it(request, pk):
    """ 删除项目表记录，pk:项目的pk """
    models.It.objects.filter(pk=pk).delete()
    return redirect('/index/')








