
import json
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


# from django.views.decorators.csrf import csrf_exempt
#
# @csrf_exempt
def run_case(request, pk=0):  # ["11", "12"]
    """ 执行用例 """
    # 如何做判断 请求 是ajax类型
    # if request.method == "POST":
    if request.is_ajax():  # 批量执行
        chk_value = request.POST.get('chk_value')
        # 一定要记得反序列化回来
        chk_value = json.loads(chk_value)
        # 数据库取 pk 在 chk_value 中记录对象
        api_list = models.Api.objects.filter(pk__in=chk_value)
        # print(api_list)
        RequestHandler.run_case(api_list)
        return JsonResponse({"path": '/logs_list/'})
    else:
        case_obj = models.Api.objects.filter(pk=pk).first()
        # print(111111111, case_obj.api_data, type(case_obj.api_data))
        RequestHandler.run_case([case_obj])
        it_obj_pk = case_obj.api_sub_it_id
        return redirect('/logs_list/')


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





def logs_list(request):
    """ log日志主页 """
    if request.method == 'POST':
        return HttpResponse("ok")
    else:
        logs_obj = models.Logs.objects.all()
        return render(request, 'logs_list.html', {"logs_obj": logs_obj})


def preview(request, pk):
    """ 测试报告预览 , pk:logs记录的pk"""
    if request.method == "POST":
        report_pk = request.POST.get("report_pk")
        log_obj = models.Logs.objects.filter(pk=report_pk).first()
        # 下载
        response = FileResponse(log_obj.log_report)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}.{}"'.format(escape_uri_path(log_obj.log_sub_it.it_name),
                                                                               'html')
        return response
    log_obj = models.Logs.objects.filter(pk=pk).first()
    return render(request, 'preview.html', {"log_obj": log_obj})


from utils.ShowTabHandler import ShowTabOpt

def show_tab(request):
    """ 可视化 """
    if request.is_ajax():
        tab_obj = ShowTabOpt()
        data_dict = {}
        data_dict.update(tab_obj.pie())
        data_dict.update(tab_obj.line_simple())
        # print(data_dict)
        return JsonResponse(data_dict)
    else:
        return render(request, 'show_tab.html')








from dengxin import settings
from django.core.mail import send_mail, EmailMessage

def send_email(request):
    # 发送简单邮件
    # send_mail(
    #     subject='这里是邮件标题',
    #     message='这里是邮件内容',
    #     from_email='tingyuweilou@163.com',
    #     recipient_list=settings.EMAIL_TO_USER_LIST,
    #     fail_silently=False
    # )
    # return HttpResponse('OK')

    # 发送带附件的邮件
    msg = EmailMessage(
        subject='这是带附件的邮件标题',
        body='这是带附件的邮件内容',
        from_email=settings.EMAIL_HOST_USER,  # 也可以从settings中获取
        to=settings.EMAIL_TO_USER_LIST
    )
    msg.attach_file(r'D:\video\s28-testing-day16-接口自动化平台-实现-3\note\dengxin\sex.html')
    msg.send(fail_silently=False)
    return HttpResponse('OK')


import xlrd
from django.db import transaction
def upload(request, pk):
    """ 文件上传 """
    if request.is_ajax():
        # print(request.POST)
        # print(request.FILES)
        try:
            with transaction.atomic():
                file_obj = request.FILES.get("f1")
                it_obj_pk = request.POST.get("it_obj_pk")
                # print(it_obj_pk, file_obj)  # 6 接口测试示例-2.xlsx
                book_obj = xlrd.open_workbook(filename=None, file_contents=file_obj.read())
                sheet = book_obj.sheet_by_index(0)
                title = sheet.row_values(0)
                data_list = [dict(zip(title, sheet.row_values(item))) for item in range(1, sheet.nrows)]
                """
                [
                    {
                        'case_num': 'neeo_001', 
                        'title': '下单接口', 
                        'desc': 'neeo项目的下单接口', 
                        'url': 'http://www.neeo.cc:6002/pinter/com/buy', 
                        'method': 'post', 
                        'params': '', 
                        'data': '{"param":{"skuId":123,"num":10}}', 
                        'json': '', 
                        'cookies': '', 
                        'headers': '', 
                        'except': '{"code": "0", "message": "success"}'
                    }
                ]
                """
                for item in data_list:
                    models.Api.objects.create(
                        api_sub_it_id=it_obj_pk,
                        api_name=item['title'],
                        api_desc=item['desc'],
                        api_url=item['url'],
                        api_method=item['method'],
                        api_params=item['params'],
                        api_data=item['data']
                    )
            return JsonResponse({"status": 200, 'path': '/list_api/{}'.format(pk)})
        except Exception as e:
            return JsonResponse({
                "status": 500,
                'path': '/list_api/{}'.format(pk),
                "it_obj_pk": pk,
                "errors": "这里只能上传 [xls] or [xlsx] 类型的表格，并且表格的字段要符合要求， 错误详情:{}".format(e)
            })
    else:
        return render(request, 'upload.html', {"it_obj_pk": pk})














