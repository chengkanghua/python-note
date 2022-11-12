from django.shortcuts import render, HttpResponse, redirect
from blog import forms, models
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from geetest import GeetestLib
from django.db.models import F
from django.db import transaction
import os
from mybbs import settings
import json
# Create your views here.


# 注册
def reg(request):
    if request.method == "POST":
        ret = {"status": 0, "msg": ""}
        valid_code = request.session.get("valid_code", "")
        valid_code_user = request.POST.get("valid_code")
        if valid_code.upper() == valid_code_user.upper():
            # 验证码相同
            print(request.POST)
            form_obj = forms.RegForm(request.POST)
            if form_obj.is_valid():
                # 将头像文件加载
                print(form_obj.cleaned_data)
                username = form_obj.cleaned_data.get("username")
                password = form_obj.cleaned_data.get("password")
                phone = form_obj.cleaned_data.get("phone")
                avatar = request.FILES.get("avatar")
                print(avatar)
                user = models.UserInfo.objects.create_user(
                    username=username,
                    password=password,
                    phone=phone,
                    avatar=avatar,
                )
                # 登录
                auth.login(request, user)
                ret["status"] = 0
                ret["msg"] = "/index/"
            else:
                ret["status"] = 1
                ret["msg"] = form_obj.errors
        else:
            ret["status"] = 1
            ret["msg"] = {"valid_code": ["验证码错误", ]}
        return JsonResponse(ret)

    form_obj = forms.RegForm()
    return render(request, "register.html", {"form_obj": form_obj})


# 登录
# def login(request):
#     if request.method == "POST":
#         ret = {"status": 0, "msg": ""}
#         if request.POST.get("valid_code").upper() == request.session.get("valid_code").upper():
#             username = request.POST.get("username")
#             pwd = request.POST.get("password")
#             user = auth.authenticate(username=username, password=pwd)
#             if user:
#                 # 登录成功
#                 auth.login(request, user=user)
#             else:
#                 ret["status"] = 1
#                 ret["msg"] = "用户名或密码错误"
#         else:
#             ret["status"] = 1
#             ret["msg"] = "验证码错误"
#         return JsonResponse(ret)
#
#     form_obj = forms.LoginForm()
#     return render(request, "login.html", {"form_obj": form_obj})

pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"


def pc_get_captcha(request):
    user_id = 'test'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)


# 滑动验证码
def login2(request):
    if request.method == "POST":
        ret = {"status": 0, "msg": ""}
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]
        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        if result:
            username = request.POST.get("username")
            pwd = request.POST.get("password")
            user = auth.authenticate(username=username, password=pwd)
            if user:
                # 登录成功
                auth.login(request, user=user)
            else:
                ret["status"] = 1
                ret["msg"] = "用户名或密码错误"
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"
        return JsonResponse(ret)

    form_obj = forms.LoginForm()
    return render(request, "login2.html", {"form_obj": form_obj})

'''
def get_valid_pic(request):
    # with open("xx.png", "rb") as f:
    #     data = f.read()
    from PIL import Image
    import random

    def get_random_color():
        """
        随机生成颜色代码
        :return:
        """
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    img_obj = Image.new(
        "RGB",
        (250, 35),
        get_random_color()
    )
    # 保存在磁盘上
    # f = open("valid_code.png", "wb")
    # img_obj.save(f, "png")
    # f = open("valid_code.png", "rb")
    # data = f.read()
    # f.close()
    # 内存操作
    from io import BytesIO
    f = BytesIO()
    img_obj.save(f, "png")
    data = f.getvalue()
    return HttpResponse(data)
'''


def login(request):
    if request.method == "POST":
        ret = {"status": 0, "msg": ""}
        v_code = request.POST.get("valid_code", "")
        if v_code and v_code.upper() == request.session.get("valid_code", ""):
            username = request.POST.get("username")
            pwd = request.POST.get("password")
            user = auth.authenticate(username=username, password=pwd)
            if user:
                # 登录成功
                auth.login(request, user=user)
            else:
                ret["status"] = 1
                ret["msg"] = "用户名或密码错误"
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"
        return JsonResponse(ret)

    form_obj = forms.LoginForm()
    return render(request, "login.html", {"form_obj": form_obj})


# 第二步给验证图片加字母
def get_valid_pic(request):
    # with open("xx.png", "rb") as f:
    #     data = f.read()
    from PIL import Image, ImageDraw, ImageFont
    import random

    def get_random_color():
        """
        随机生成颜色代码
        :return:
        """
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    img_obj = Image.new(
        "RGB",
        (250, 35),
        get_random_color()
    )
    # 在图片上生成一个画笔对象
    draw_obj = ImageDraw.Draw(img_obj)
    # 画线draw_obj.line() 画点 draw_obj.point() 写字 draw_obj.text()
    # 加载字体文件，注意路径是从项目的根目录下开始找
    font_obj = ImageFont.truetype("static/font/kumo.ttf", 28)
    # 循环五次添加随机字符
    valid_code_tmp = []
    for i in range(5):
        n = str(random.randint(0, 9))
        l = chr(random.randint(97, 122))
        u = chr(random.randint(65, 90))
        r = random.choice([n, l, u])
        valid_code_tmp.append(r)
        draw_obj.text((i*40+20, 0), r, fill=get_random_color(), font=font_obj)

    # 加干扰线
    # width = 250  # 图片宽度（防止越界）
    # height = 35
    # for i in range(5):
    #     x1 = random.randint(0, width)
    #     x2 = random.randint(0, width)
    #     y1 = random.randint(0, height)
    #     y2 = random.randint(0, height)
    #     draw_obj.line((x1, y1, x2, y2), fill=get_random_color())
    #
    # # 加干扰点
    # for i in range(40):
    #     draw_obj.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw_obj.arc((x, y, x+4, y+4), 0, 90, fill=get_random_color())
    # 内存操作
    from io import BytesIO
    f = BytesIO()
    img_obj.save(f, "png")
    data = f.getvalue()

    # 将验证码保存在session中
    valid_code = "".join(valid_code_tmp)
    request.session["valid_code"] = valid_code.upper()
    return HttpResponse(data, content_type="image/png")


@login_required
def index(request):
    # 取出所有的文章
    article_list = models.Article.objects.all()

    return render(request, "index.html", {"article_list": article_list})


def logout(request):
    auth.logout(request)
    return redirect("/login/")


def test(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)

        file_obj = request.FILES.get("avatar")
        with open(file_obj.name, "wb") as f:
            for i in file_obj:
                f.write(i)

    return render(request, "test.html")


def home(request, username, *args):
    user = models.UserInfo.objects.filter(username=username).first()
    if not user:
        return HttpResponse("404")
    # 拿到当前用户的博客对象
    blog = user.blog
    if args and len(args) == 2:
        if args[0] == "category":
            article_list = models.Article.objects.filter(user=user).filter(category__title=args[1])
        elif args[0] == "tag":
            article_list = models.Article.objects.filter(user=user).filter(tags__title=args[1])
        elif args[0] == "archive":
            try:
                year, month = args[1].split("-")
                article_list = models.Article.objects.filter(user=user).filter(create_time__year=year, create_time__month=month)
            except Exception as e:
                article_list = []
        else:
            article_list = []
    else:
        # 查询当前站点的所有文章
        # user.article_set.all()
        article_list = models.Article.objects.filter(user=user)
        print(article_list)

    return render(
        request,
        "home.html",
        {
            "username": username,
            "article_list": article_list,
            "blog": blog,
        }
    )


# 文章详情
def article_detail(request, username, article_id):
    user = models.UserInfo.objects.filter(username=username).first()
    blog = user.blog
    article_obj = models.Article.objects.filter(pk=article_id).first()
    print(article_obj)
    # 该文章的所有评论
    comment_list = models.Comment.objects.filter(article_id=article_id)
    return render(request, "article_detail.html", {
        "blog": blog,
        "username": username,
        "article": article_obj,
        "comment_list": comment_list
    })


# 点赞
def poll(request):
    if request.method == "POST":
        print(request.POST)
        print("=" * 120)
        ret = {"code": 0, "data": ""}
        is_up = True if request.POST.get("is_up").upper() == "TRUE" else False  # 这TM是个字符串
        article_id = request.POST.get("article_id ")
        user_id = request.POST.get("user_id")
        is_exist = models.ArticleUpDown.objects.filter(article_id=article_id, user_id=user_id)
        print(is_exist, is_up)
        print("-" * 120)
        if is_exist:
            ret["code"] = 1
            ret["data"] = "你已经赞过了！" if is_exist.first().is_up else "你已经踩过了！"
        else:
            with transaction.atomic():
                models.ArticleUpDown.objects.create(is_up=is_up, article_id=article_id, user_id=user_id)
                # 更新文章表里的点赞数或踩数
                if is_up:
                    print("up+1")
                    models.Article.objects.filter(pk=article_id).update(up_count=F("up_count")+1)
                else:
                    models.Article.objects.filter(pk=article_id).update(down_count=F("down_count")+1)
                    print("down+1")
                ret["data"] = "赞！！！" if is_up else "踩！！！"

        return JsonResponse(ret)


# 评论
def comment(request):
    ret = {"code": 0, "data": ""}
    print(request.POST)
    article_id = request.POST.get("article_id")
    content = request.POST.get("content")
    pid = request.POST.get("pid")
    user_id = request.user.pk
    with transaction.atomic():
        # 根评论
        # 提交子评论
        obj = models.Comment.objects.create(
            user_id=user_id,
            article_id=article_id,
            content=content,
            parent_comment_id=pid
        )
        # 更新文章的评论数
        models.Article.objects.filter(pk=article_id).update(comment_count=F("comment_count") + 1)
        ret["data"] = {
            "pk": obj.pk,
            "time": obj.create_time.strftime("%Y-%m-%d %H:%M"),
            "content": obj.content
        }

    return JsonResponse(ret)


def backend(request):
    article_list = models.Article.objects.filter(user=request.user)
    return render(request, "backend.html", {"article_list": article_list})


def add_article(request):
    if request.method == "POST":
        article_title = request.POST.get("title")
        article_content = request.POST.get("content")

        # 需要对提交的内容做处理，去除掉特殊的标签，防止XSS攻击
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(article_content, 'html.parser')
        for tag in soup.select('script'):
            tag.decompose()
        with transaction.atomic():
            # 创建文章
            obj = models.Article.objects.create(
                title=article_title,
                user=request.user,
                desc=soup.text[0:150]  # 截取文本内容的前150个自字符
            )
            # 创建文章内容
            models.ArticleDetail.objects.create(
                content=soup.prettify(),  # 保存格式化的文本内容
                article=obj
            )
        return redirect("/blog/backend/")
    return render(request, "add_article.html")


def clean_content(content):
    # 需要对提交的内容做处理，去除掉特殊的标签，防止XSS攻击
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    for tag in soup.select('script'):
        tag.decompose()
    return soup


# 个人管理后台编辑或删除文章
def op_article(request, op, pk):
    article_obj = models.Article.objects.filter(pk=pk).first()

    if op == "add":
        if request.method == "POST":
            article_title = request.POST.get("title")
            article_content = request.POST.get("content")
            soup = clean_content(article_content)

            with transaction.atomic():
                # 创建文章
                obj = models.Article.objects.create(
                    title=article_title,
                    user=request.user,
                    desc=soup.text[0:150]  # 截取文本内容的前150个自字符
                )
                # 创建文章内容
                models.ArticleDetail.objects.create(
                    content=soup.prettify(),  # 保存格式化的文本内容
                    article=obj
                )
            return redirect("/blog/backend/")
        return render(request, "op_article.html")
    elif article_obj and op == "delete":
        article_obj.delete()
        return redirect("/blog/backend/")
    elif article_obj and op == "edit":
        article_detail = models.ArticleDetail.objects.filter(article=article_obj).first()
        tags = json.dumps([i[0] for i in article_obj.tags.values_list("title")])
        print(tags)
        print("=" * 120)

        if request.method == "POST":
            title = request.POST.get('title')
            article_content = request.POST.get('content')
            user = request.user
            soup = clean_content(article_content)
            with transaction.atomic():
                article_obj.title = title
                article_obj.user = user
                article_obj.desc = soup.text[0:150]
                article_obj.save()
                article_detail.content = soup.prettify()
                article_detail.save()
                return redirect("/blog/backend/")
        return render(request, "op_article.html", {"article": article_obj, "article_detail": article_detail, "tags": tags})
    else:
        return HttpResponse("404")


def upload_img(request):
    ret = {"error": 0, "url": ""}

    img_obj = request.FILES.get("img")

    file_path = os.path.join(settings.MEDIA_ROOT, "article_img", img_obj.name)
    print(file_path)
    with open(file_path, "wb") as f:
        for chunk in img_obj.chunks():
            f.write(chunk)

    ret["url"] = "/media/article_img/" + img_obj.name
    return JsonResponse(ret)


def tags(request):

    category_id = request.GET.get("category")
    if category_id:
        data = models.Tag.objects.filter(article=category_id).values("nid", "title")
    else:
        key = request.GET.get("name_contains")
        print(key)
        data = models.Tag.objects.filter(blog=request.user.blog, title__icontains=key).values("nid", "title")
        print(data)
    ret = {"code": 0, "data": list(data)} if data else {"code": 1}
    print(ret)
    return JsonResponse(ret)


def demo(request):
    return render(request, "tagsinput_demo.html")
