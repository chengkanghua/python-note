from django.shortcuts import render, HttpResponse, redirect
from blog.utils import validCode
from django.contrib import auth
from django.http import JsonResponse
from blog import models
from blog.Myform import UserForm
from blog.models import UserInfo,Article
from django.db.models import Count,F
from django.db import transaction
from django.core.mail import send_mail
from cnblog import settings
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
import threading
import json,os
# Create your views here.

def login(request):
    if request.method == 'POST':
        response = {'user': None, 'msg': None}
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        valid_code = request.POST.get('valid_code')
        valid_code_str = request.session.get('valid_code_str')
        # print(valid_code,valid_code_str)
        # print(type(valid_code),type(valid_code_str))
        if valid_code.upper() == valid_code_str.upper():
            user = auth.authenticate(username=user, password=pwd)
            if user:
                auth.login(request, user)
                response['user'] = user.username
            else:
                response['msg'] = '用户名或密码错误!'
        else:
            response['msg'] = '验证码错误'
        return JsonResponse(response)

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/login/')

def register(request):
    if request.is_ajax():
        print(request.POST)
        form = UserForm(request.POST)
        response = {'user':None,'msg':None}
        if form.is_valid():
            response['user'] = form.cleaned_data.get('user')

            #生成一条用户数据
            user = form.cleaned_data.get('user')
            pwd = form.cleaned_data.get('pwd')
            email = form.cleaned_data.get('email')
            avatar_obj = request.FILES.get('avatar')
            extra = {}
            if avatar_obj:
                extra['avatar'] = avatar_obj
            UserInfo.objects.create_user(username=user,password=pwd,email=email,**extra)
        else:
            print(form.cleaned_data)  # 校验通过的数据
            print(form.errors)        # 校验错误的数据 <ul class="errorlist"><li>pwd<ul class="errorlist"><li>This field is required.</li></ul>
            response['msg'] = form.errors
        return JsonResponse(response)

    form = UserForm()
    return render(request,'register.html',{'form':form})

def get_validCode_img(request):
    img_data = validCode.get_valid_code_img(request)
    return HttpResponse(img_data)

def index(request):
    article_list = models.Article.objects.all()
    return render(request,'index.html',{'article_list':article_list})

def home_site(request,username,**kwargs):
    print('kwargs:' ,kwargs)
    print('username:', username)
    user = UserInfo.objects.filter(username=username).first()
    if not user:
        return render(request,'not_found.html')

    blog = user.blog  # 查询当前站点对象
    # article_list = user.article_set.all()
    article_list = models.Article.objects.filter(user=user)
    if kwargs:
        condition = kwargs.get("condition")
        param = kwargs.get("param")  # 2012-12

        if condition == "category":
            article_list = article_list.filter(category__title=param)
        elif condition == "tag":
            article_list = article_list.filter(tags__title=param)
        else:
            year, month = param.split("/")
            article_list = article_list.filter(create_time__year=year, create_time__month=month)

    # 每一个分类对应的文章数
    # ret = models.Category.objects.values('pk').annotate(c=Count("article__title")).values('title','c')
    # 当前站点每一个分类的文章数
    # ret  =  models.Category.objects.filter(blog=blog).values('pk').annotate(c=Count('article__title')).values('title','c')
    # 查询当前站点的每一个标签名称以及对应的文章数
    ret = models.Tag.objects.filter(blog=blog).values('pk').annotate(c=Count('article__title')).values('title','c')
    print(ret)


    return render(request,'home_site.html',{'username':username,'blog':blog,'article_list':article_list})

def article_detail(request,username,article_id):
    # print('username:',username)
    # print('article_id:',article_id)
    user = UserInfo.objects.all().filter(username=username).first()
    # print('user: ',user)
    blog = user.blog
    article_obj = models.Article.objects.filter(pk=article_id).first()
    # print('article_obj:',article_obj)
    comment_list = models.Comment.objects.filter(article_id=article_id)
    # print(comment_list)

    return render(request,'article_detail.html',locals())


def digg(request):
    """
    点赞功能
    :param request:
    :return:
    """
    print(request.POST)
    is_up = request.POST.get('is_up')   # 接收到的是一个字符串
    is_up = json.loads(is_up)
    article_id = request.POST.get('article_id')
    user_id = request.user.pk   #点赞人即登陆人
    obj = models.ArticleUpDown.objects.filter(user_id=user_id,article_id=article_id).first()

    response = {'state': True}
    if not obj:
        ard = models.ArticleUpDown.objects.create(user_id=user_id,article_id=article_id,is_up=is_up)
        queryset = models.Article.objects.filter(pk=article_id)
        if is_up:
            queryset.update(up_count=F("up_count") + 1)
        else:
            queryset.update(down_count=F("down_count") + 1)
    else:
        response['state'] = False        # 表示已经做过赞或者踩了,
        response['handled'] = obj.is_up  # 取赞还是踩
    return JsonResponse(response)

def comment(request):
    print(request.POST)
    user_id = request.user.pk
    article_id = request.POST.get('article_id')
    pid = request.POST.get('pid')
    content  = request.POST.get('content')

    article_obj = models.Article.objects.filter(pk=article_id).first()
    # 事务操作
    with transaction.atomic():
        comment_obj = models.Comment.objects.create(article_id=article_id,user_id=user_id,content=content,parent_comment_id=pid)
        models.Article.objects.all().filter(pk=article_id).update(comment_count=F("comment_count")+1) # 文章的评论数+1

    response = {}
    response['create_time'] = comment_obj.create_time.strftime('%Y-%m-%d %X')
    response['username'] = request.user.username
    response['content'] = comment_obj.content
    if pid:  # 父评论的姓名和内容
        pidcomment_obj = models.Comment.objects.filter(pk=pid).first()
        response['pidname'] = pidcomment_obj.user.username
        response['pidcontent'] = pidcomment_obj.content
        # print(response)

    # 发送邮件
    # send_mail(
    #     "您的文章%s新增了一条评论内容"%article_obj.title,  邮件标题
    #     content,       // 内容
    #     settings.EMAIL_HOST_USER,   # 发送方
    #     ["916852314@qq.com"]   #  接收方邮箱地址
    # )
    t = threading.Thread(target=send_mail, args=("您的文章%s新增了一条评论内容"%article_obj.title,
                                                 content,
                                                 settings.EMAIL_HOST_USER,
                                                 ["81422463@qq.com","343264992@163.com","916852314@qq.com"])
                         )
    t.start()

    return JsonResponse(response)

def get_comment_tree(request):
    article_id = request.GET.get('article_id')
    response = list(models.Comment.objects.filter(article_id=article_id).order_by('pk').values('pk','content','parent_comment_id'))
    # print(response,type(response))
    return JsonResponse(response,safe=False)

@login_required
def cn_backend(request):
    '''
    后台管理页面
    :param request:
    :return:
    '''

    article_list = models.Article.objects.filter(user=request.user)
    return render(request,'backend/backend.html',{'article_list': article_list})

@login_required
def add_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # 防止xss攻击 去除 scripts 标签
        soup = BeautifulSoup(content,"html.parser")
        for tag in soup.find_all():
            # print(tag.name)
            if tag.name == 'script':
                soup.decompose()

        # 构建摘要数据,获取标签字符串的文本前150个符号
        desc = soup.text[0:150]+'...'
        models.Article.objects.create(title=title,desc=desc,content=str(soup),user=request.user)
        return redirect('/cn_backend')
    return render(request,'backend/add_article.html')

@login_required
def edit_article(request,id):
    article_obj = Article.objects.filter(pk=id).first()
    if request.method == 'POST':
        # print(request.POST)
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 防止xss攻击 去除 scripts 标签
        soup = BeautifulSoup(content,"html.parser")
        for tag in soup.find_all():
            # print(tag.name)
            if tag.name == 'script':
                soup.decompose()

        # 构建摘要数据,获取标签字符串的文本前150个符号
        desc = soup.text[0:150]+'...'
        reply = Article.objects.filter(pk=id).update(title=title,desc=desc,content=content)
        if reply:
            return redirect('/cn_backend/')
    return render(request,"backend/edit_article.html",{"article_obj":article_obj})

@login_required
def del_article(request,id):
    reply = Article.objects.filter(pk=id).delete()
    print(reply)
    if reply:
        return redirect('/cn_backend/')


def upload(request):
    # print(request.FILES)
    img_obj = request.FILES.get('upload_img')
    # print(img_obj.name)

    path = os.path.join(settings.MEDIA_ROOT,'add_article_img',img_obj.name)
    with open(path,'wb') as f:
        for line in img_obj:
            f.write(line)
    response = {
        'error':0,
        'url':'/media/add_article_img/%s'%img_obj.name
    }
    return HttpResponse(json.dumps(response))