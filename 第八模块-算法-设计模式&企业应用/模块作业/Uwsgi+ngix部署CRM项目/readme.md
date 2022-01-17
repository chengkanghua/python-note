1. 把之前的CRM项目通过Uwsgi+nginx部署
2. 通过压力测试工具，测试最大并发请求数
3. 并发测试结果请截图交作业
4. 写好readme，确保导师可以很简单的启动您的项目

环境说明:
```bash
(django3.2) [root@centos7-kh opt]# cat /etc/redhat-release
CentOS Linux release 7.6.1810 (Core)
(django3.2) [root@centos7-kh opt]# python3 -V
Python 3.6.1
(django3.2) [root@centos7-kh opt]# pip3 freeze > requirements.txt
(django3.2) [root@centos7-kh opt]# cat requirements.txt
asgiref==3.4.1
certifi==2021.10.8
charset-normalizer==2.0.7
Django==3.2
idna==3.3
PyMySQL==1.0.2
pytz==2021.3
requests==2.26.0
sqlparse==0.4.2
typing-extensions==3.10.0.2
urllib3==1.26.7
uWSGI==2.0.20
wincertstore==0.2
xlrd==2.0.1

```

服务器centos 最小精简化安装
# 操作系统优化:
```bash
//0.yum仓库配置
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo

//1.安装基础软件包
yum install net-tools vim tree htop iftop \
iotop lrzsz sl wget unzip telnet nmap nc psmisc \
dos2unix bash-completion iotop iftop sysstat -y
//2.关闭firewalld防火墙
systemctl disable firewalld
systemctl stop firewalld
systemctl status firewalld
//3.关闭selinux
# 方式一
sed -ri 's#(^SELINUX=).*#\1disabled#g' /etc/selinux/config
# 方式二
sed -i '/^SELINUX=/c SELINUX=disabled' /etc/selinux/config
# 方式三
vim /etc/selinux/config
# 临时生效
setenforce 0  
//4.优化ulimit
echo '* - nofile 65535' >> /etc/security/limits.conf
//临时生效
ulimit -n 65536
//5.重启并快照
```

# python3 编译安装
```bash
编译安装python3的步骤

1.安装python前的库环境,非常重要
yum install -y gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

2.获取python的源代码，下载且安装，

wget https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tar.xz
3.下载完源代码包之后，进行解压缩
tar -xvf Python-3.6.6.tgz  
4.解压缩完毕之后，生成了python369的源代码目录，进入源代码目录准备开始编译
cd  Python-3.6.6  # 进入源码包文件夹

5.此时准备编译三部曲 ，
mkdir /usr/local/python3
./configure --prefix=/usr/local/python3  

make && make install    

6 最后创建软链接
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3

---------------------------------
虚拟环境创建
pip3 install -i https://pypi.douban.com/simple virtualenv
mkdir /opt/virtualenv
cd /opt/virtualenv/
virtualenv --python=python3 django3.2
source /opt/virtualenv/django3.2/bin/activate

```

# nginx 编译安装
```bash

0.编译前的基础环境安装
yum install gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel openssl openssl-devel -y

1.在linux的opt目录下，下载nginx源代码
wget http://tengine.taobao.org/download/tengine-2.3.2.tar.gz

2.解压缩源代码，准备编译三部曲
tar -zxvf  tengine-2.3.2.tar.gz

3.进入源码目录，指定nginx的安装位置
./configure --prefix=/opt/tengine/

5.编译且编译安装，生成nginx的可执行命令目录
make && make install 

6.添加nginx到PATH中，可以快捷执行命令

永久修改PATH，开机就去读
vim /etc/profile  
写入PATH="/opt/tengine/sbin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:"

```

# Uwsgi django 等安装
```bash
# 复制第一步的环境说明requirements.txt 
pip3 install -r requirement.txt

```

# 配置启动CRM 项目
```bash
# uwsgi 配置
(django3.2) [root@centos7-kh opt]# cat /opt/uwsgi.ini
[uwsgi]
chdir           = /opt/pro_crm/
module          = pro_crm.wsgi
home            = /opt/virtualenv/django3.2
master          = true
processes       = 3
socket          = 0.0.0.0:8000
vacuum          = true

# nginx配置
(django3.2) [root@centos7-kh opt]# cat /opt/tengine/conf/nginx.conf
#user  nobody;
worker_processes  2;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    gzip  on;

    server {
        listen       80;
        server_name  localhost;

        charset utf-8;

        location / {
        uwsgi_pass 0.0.0.0:8000;
        include uwsgi_params;
        }
        location /static {
        alias /opt/static/;
	    }
        error_page  404              /404.html;
    }
}

# 将pro_crm 项目文件解压到/opt/目录下
tar xf crm.tar.gz

# 用命令收集静态文件
python3 manage.py collectstiac

# 启动 uwsig
(django3.2) [root@centos7-kh opt]# uwsgi --ini uwsgi.ini

# 启动nginx
(django3.2) [root@centos7-kh opt]# nginx

```









