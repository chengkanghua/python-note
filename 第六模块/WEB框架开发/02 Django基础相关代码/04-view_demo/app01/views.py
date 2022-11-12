from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


from django.shortcuts import HttpResponse

'''
http://127.0.0.1:8000/index/
url:协议://IP:port/路径?get请求数据

'''


def index(request):
    # print("method", request.method)  # "GET
    #
    # print(request.GET)
    # print(request.GET.get("name"))
    # print(request.POST)
    #
    # print(request.path)
    # print(request.get_full_path())

    print(request.body)
    print(request.path_info)
    print(request.method)
    print(request.encoding)
    print(request.META)
    print(request.session)
    print(request.user)
    print(request.is_ajax())
    import time

    ctime = time.time()

    # return HttpResponse("<h1>OK</h1>")

    return render(request, "index.html", {"timer": ctime})  # index.html 模板文件


def login(request):
    if request.method == "POST":

        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        if user == "alex" and pwd == "123":
            # return HttpResponse("success!")

            return redirect("/index/")

    return render(request, "login.html")


'''
# print(request.META)
{
'PATH': '/usr/local/bin:/usr/local/sbin:/Library/Frameworks/Python.framework/Versions/3.9/bin:/usr/local/mysql/support-files/:/usr/local/mysql/bin/:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin', 
'MANPATH': '/usr/local/share/man:', 
'HOMEBREW_PREFIX': '/usr/local', 
'VERSIONER_PYTHON_VERSION': '2.7', 
'LOGNAME': 'kanghua', 
'HOMEBREW_REPOSITORY': '/usr/local/Homebrew', 
'XPC_SERVICE_NAME': 'com.jetbrains.pycharm.4444',
'PWD': '/Users/kanghua/PycharmProjects/python-note/第六模块-WEB框架开发/02 Django基础相关代码/04-view_demo', 
'PYCHARM_HOSTED': '1', 
'INFOPATH': '/usr/local/share/info:', 
'PYCHARM_DISPLAY_PORT': '63342', 
'PYTHONPATH': '/Users/kanghua/PycharmProjects/python-note/第六模块-WEB框架开发/02 Django基础相关代码/04-view_demo:/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend:/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display', 
'SHELL': '/bin/bash',
'PYTHONIOENCODING': 'UTF-8', 
'HOMEBREW_BOTTLE_DOMAIN': 'https://mirrors.aliyun.com/homebrew/homebrew-bottles',
'HOMEBREW_CELLAR': '/usr/local/Cellar', 
'VERSIONER_PYTHON_PREFER_32_BIT': 'no', 
'USER': 'kanghua', 
'TMPDIR': '/var/folders/s9/qr1tfvss2yxf97638lb27b400000gn/T/',
'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.ZT4rPtjZ3f/Listeners',
'DJANGO_SETTINGS_MODULE': 'view_demo.settings', 
'XPC_FLAGS': '0x0',
'PYTHONUNBUFFERED': '1', 
'__CF_USER_TEXT_ENCODING': '0x1F5:0x19:0x34', 
'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.SxKEiZ1Swq/Render', 
'LC_CTYPE': 'zh_CN.UTF-8', 
'HOME': '/Users/kanghua', 
'TZ': 'UTC', 
'RUN_MAIN': 'true', 
'SERVER_NAME': '1.0.0.127.in-addr.arpa',
'GATEWAY_INTERFACE': 'CGI/1.1', 
'SERVER_PORT': '8000', 
'REMOTE_HOST': '',
'CONTENT_LENGTH': '14', 
'SCRIPT_NAME': '', 
'SERVER_PROTOCOL': 'HTTP/1.1',
'SERVER_SOFTWARE': 'WSGIServer/0.2',
'REQUEST_METHOD': 'POST',
'PATH_INFO': '/index/', 
'QUERY_STRING': '', 
'REMOTE_ADDR': '127.0.0.1', 
'CONTENT_TYPE': 'application/x-www-form-urlencoded',
'HTTP_HOST': '127.0.0.1:8000', 
'HTTP_CONNECTION': 'keep-alive', 
'HTTP_CACHE_CONTROL': 'max-age=0', 
'HTTP_SEC_CH_UA': '"Microsoft Edge";v="95", 
"Chromium";v="95", ";Not A Brand";v="99"',
'HTTP_SEC_CH_UA_MOBILE': '?0',
'HTTP_SEC_CH_UA_PLATFORM': '"macOS"',
'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 
'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.40 Safari/537.36 Edg/95.0.1020.20',
'HTTP_ORIGIN': 'http://127.0.0.1:8000',
'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
'HTTP_SEC_FETCH_SITE': 'same-origin', 'HTTP_SEC_FETCH_MODE': 'navigate', 'HTTP_SEC_FETCH_USER': '?1', 
'HTTP_SEC_FETCH_DEST': 'document', 
'HTTP_REFERER': 'http://127.0.0.1:8000/index/',
'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 
'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'wsgi.input': <_io.BufferedReader name=6>, 
'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>, 
'wsgi.version': (1, 0),
'wsgi.run_once': False,
'wsgi.url_scheme': 'http',
'wsgi.multithread': True,
'wsgi.multiprocess': False,
'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>
}

'''
