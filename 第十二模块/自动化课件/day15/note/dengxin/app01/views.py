from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from app01 import models
from utils.MyModelForm import ItModelForm, ApiModelForm
from utils import RequestHandler


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



def list_api(request, pk):
    """
        思考：要不要有 pk ?
        pk:项目的pk
        查看某一个项目下的用例列表
    """
    api_obj = models.Api.objects.filter(api_sub_it_id=pk)
    it_obj = models.It.objects.filter(pk=pk).first()
    # print(1111111, it_obj.it_name)
    return render(request, 'list_api.html', {"api_obj": api_obj, 'it_obj': it_obj})






def add_api(request, pk):
    """ 添加用例, pk:所属项目的pk """

    if request.method == "POST":
        form_data = ApiModelForm(request.POST)
        if form_data.is_valid():

            form_data.instance.__dict__['api_sub_it_id'] = pk
            # form_data.instance.api_sub_it = it_obj
            form_data.save()
            return redirect('/index/')
        else:
            return render(request, 'add_api.html', {"api_form_obj": form_data})
    else:
        api_form_obj = ApiModelForm()
        it_obj = models.It.objects.filter(pk=pk).first()
        return render(request, 'add_api.html', {"api_form_obj": api_form_obj, "it_obj": it_obj})

def edit_api(request, pk):
    """ 编辑用例, pk:api的pk """
    api_obj = models.Api.objects.filter(pk=pk).first()
    if request.method == "POST":
        form_data = ApiModelForm(request.POST, instance=api_obj)
        if form_data.is_valid():
            # print(111111111, form_data.instance.__dict__)
            form_data.instance.__dict__['api_pass_status'] = 0
            form_data.instance.__dict__['api_run_status'] = 0
            form_data.instance.__dict__['api_report'] = ""
            form_data.save()
            return redirect('/list_api/{}'.format(api_obj.api_sub_it_id))  # 用例列表接口需要所属项目的pk值
        else:
            return render(request, 'edit_api.html', {"api_form_obj": form_data})
    else:
        api_form_obj = ApiModelForm(instance=api_obj)
        return render(request, 'edit_api.html', {"api_form_obj": api_form_obj, "it_obj": api_obj.api_sub_it})

def delete_api(request, pk):
    """ 删除用例, pk:用例的pk """
    # 由于返回时，需要项目的pk值，这里不能直接删除
    api_obj = models.Api.objects.filter(pk=pk).first()
    # 获取所属项目的pk
    it_obj_pk = api_obj.api_sub_it_id
    api_obj.delete()
    return redirect('/list_api/{}'.format(it_obj_pk))



def run_case(request, pk=0):  # ["11", "12"]
    """ 执行用例 """
    case_obj = models.Api.objects.filter(pk=pk).first()
    # print(111111111, case_obj.api_data, type(case_obj.api_data))
    RequestHandler.run_case(case_obj)
    it_obj_pk = case_obj.api_sub_it_id
    return redirect('/list_api/{}'.format(it_obj_pk))

from django.http import FileResponse
from django.utils.encoding import escape_uri_path   # 导入这个家伙
def download_case_report(request, pk):
    """ 下载用例的执行报告，pk:用例的pk """
    api_obj = models.Api.objects.filter(pk=pk).first()
    # 下载
    response = FileResponse(api_obj.api_report)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}.{}"'.format(escape_uri_path(api_obj.api_name), 'html')
    return response









































