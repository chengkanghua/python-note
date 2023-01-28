## linux 运维人员核心职责

-   网站数据不能丢
-   网站7*24小时运转
-   提供用户体验，访问速度要快。



## 常见的http响应状态码

-   404 40x系列  客户端的请求报错，请求的url不存在，或者过期了
-   302 30x系列， 客户端请求重定向，
-   503  50x系列 ， 指的是服务器代码出错，服务器端处理请求出问题了
-   200 20x系列， 请求正确的被响应了、



## 网络连接方式

桥接： 和宿主机共用一个网段

NAT：网络地址转换， 基于宿主机网卡，在机器内部生成一个私有的局域网

仅主机模式： 单击模式，，虚拟机只能和宿主机通信



## linux目录结构

```
linux一切皆文件
/   
/dev    存放抽象硬件
/boot   存放内核与启动文件
/lib    存放系统库文件
/bin    存放二进制文件（可执行命令）
/sbin   存放特权级二进制文件
/usr    存放安装程序 （软件默认目录）
/var    经常存放变化的文件
/mnt    文件挂载目录（u盘 光驱）
/home   普通用户目录
/root   root特权用户目录
/etc    存放配置文件目录
/opt    大型软件存放目录（非强制）
```



## 文件目录增删改查操作

修改linux 支持中文的命令

```
export LC_ALL=zh_CN.UTF-8
```



```
增
touch music.txt
mkdir  s25
mkdir -p /s25/ss/  #递归创建文件夹
mkdir -p /s25new/{1,2}   #创建了一个s25new文件夹，且2个平级的文件夹

删
rm 是remove的缩写，删除文件或者文件夹
rm test.txt 
rm -f test.txt #强制删除， 不需要确认
rm -r  文件夹名  # 递归删除文件夹，及内部的文件

改
cd /home
ls .  

查
# 查询当前目录的内容 ls   list的缩写
ls .    #当前目录
ls -a   # 查看文件夹所有内容，包括隐藏文件
ls -lht  # -h参数，是显示文件单位，以kb  mb gb大小为单位   -l是列表形式，列出文件夹中详细信息 -t 最新的文件排序



几个特殊的目录
.  代表当前的目录
..  代表上级目录
~   代表当前登录用户家目录
-   代表上一次的工作目录

绝对路径： 只要是从跟开始的目录的写法就是绝对路径
相对路径： 非从跟目录开始的写法，就是相对路径


```



## PATH 变量

```
which python #输出命令所在绝对路径

vim  /etc/profile #打开文件，在文件末尾，添加PATH值的修改
PATH="/opt/python36/bin/:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:"

source /etc/profile   # 生效


vim  /etc/profile   # 这个文件每次开机都会读取这个文件，让其生效
export LC_ALL=zh_CN.UTF-8  #打开注释，系统支持中文
#export LC_ALL=en_US.UTF-8  #打开注释，系统就支持英文了
```



linux 单引号和双引号区别

```
单引号中的内容，仅仅就是个字符串了，不识别任何其他的特殊符号

双引号中的内容，能够识别特殊符号，以及变量
```



### vim 使用流程

```
yum install vim -y #安装
#用vim写一个python脚本，
#vim的使用流程
第一步：vim  first.py  ，此时会进入命令模式，按下字母 a,i,o进入编辑模式
第二步：想要退出编辑模式，按下键盘的esc，回到命令模式
第三部：此时输入 shfit+冒号，输入一个英文的冒号，进入底线命令模式 
第四步：输入 :wq!  ，write写入内容，quit退出vim  ！ 强制性的操作
:wq!  强制保存写入退出vim
:q!  强制不保存内容，直接退出

命令模式下常用指令
$ 快速移动到行尾
0 行首
x 删除光标所在字符
g 移动到文件的第一行
G 移动到文件的最后一行

/string  从文件开头查找的内容， 按下n建 跳转下一个匹配的字符
?string  从文件第行， 向上搜索字符串信息
%  找到括号的另一半

yy 复制当前行
3yy  复制光标后3行
p    粘贴yy复制的内容
dd   删除当前行
4dd  删除光标向下的4行内容
dG   删除当前行到结尾的内容
u    撤销上一次的动作

底线命令模式下
：wq！ 保存退出
：q!  不保存退出
:数字  快速定位某一行
：set nu  显示行号
```

## linux 重定向符号

```
>   #重定向输出符号，  
>>  #重定向输出  追加符 ， 如同 a模式
<   #重定向写入符号符，   在mysql 数据导入时候用到
<<  #用在cat命令中
```



### top 命令

```
那么linux的资源管理器 就是top命令

第一行 (uptime)
系统时间 主机运行时间 用户连接数(who) 系统1，5，15分钟的平均负载

第二行:进程信息
进程总数 正在运行的进程数 睡眠的进程数 停止的进程数 僵尸进程数

第三行:cpu信息
1.5 us：用户空间所占CPU百分比
0.9 sy：内核空间占用CPU百分比
0.0 ni：用户进程空间内改变过优先级的进程占用CPU百分比
97.5 id：空闲CPU百分比
0.2 wa：等待输入输出的CPU时间百分比
0.0 hi：硬件CPU中断占用百分比
0.0 si：软中断占用百分比
0.0 st：虚拟机占用百分比

第四行：内存信息（与第五行的信息类似与free命令）
total：物理内存总量
used：已使用的内存总量
free：空闲的内存总量（free+used=total）
buffers：用作内核缓存的内存量

第五行：swap信息
total：交换分区总量
used：已使用的交换分区总量
free：空闲交换区总量
cached Mem：缓冲的交换区总量，内存中的内容被换出到交换区，然后又被换入到内存，但是使用过的交换区没有被覆盖，交换区的这些内容已存在于内存中的交换区的大小，相应的内存再次被换出时可不必再对交换区写入。
```

### ps 命令

```
用于查看linux进程信息的命令 
语法就是 
ps  -ef    # -ef，是一个组合参数，-e  -f 的缩写，默认显示linux所有的进程信息，以及pid，时间，进程名等信息 

#过滤系统有关vim的进程 
[root@s25linux ~]# ps -ef |  grep  "vim"
root      24277   7379  0 16:09 pts/1    00:00:00 vim ps是怎么用的.txt


kill 进程id
kill -9 pid # 卡死的进程 杀不掉 -9 强制的信号
```



# netstat

```
netstat -tunlp  # 显示所有的tcp udp的所有端口连接情况
netstat -tunlp |grep 80 # 查看80端口是否存在
netstat -tunlp | grep ssh

ssh  -p 22 root@192.168.178.134  # -p 指定连接端口



```



### 用户管理命令

```
id root  
id user # 查看用户的账户信息的命令

useradd eric  # 创建用户
passwd  eric   # 设置密码

userdel  eric     # 删除用户
userdel -rf eric  # 删除用户，且删除用户的家目录

su - root  切换用户

sudo  cd /root   # 临时使用root身份去执行命令

1 添加允许使用sudo 命令的配置文件 ，
visudo 
visudo  #打开文件后，找到大约在91行的内容，修改为如下
     91 ## Allow root to run any commands anywhere
     92 root    ALL=(ALL)       ALL
     93 eric    ALL=(ALL)       ALL  # 这是添加的
2 保存退出后，既可以使用sudo命令了
sudo ls /root



```



### Linux文件、目录权限管理

```
[root@bj1 ~]# ls -lh /opt
total 2.0M
drwxrwxr-x. 6 root root 4.0K Jan 22 00:27 redis-5.0.14
-rw-r--r--. 1 root root 2.0M Jan 21 16:13 redis5.0.tar.gz

说明 （第一行）
- 代表普通文件类型 d 代表目录类型
rwx（user的权限） rwx(group的权限) r-x(outher的权限) 
root（属主） root（属组）
4.0K  文件大小
Jan 22 00:27  最后一次修改时间
redis-5.0.14 文件名

对于文件的rwx
r   cat，more，less，head，等读取文件内容的操作
w    vim  ，echo，等写入内容的操作 
x   可以执行的脚本，例如bash，python等脚本，文件会变成绿色

对于文件夹的rwx
r  ls 查看文件夹内容
w   允许在文件夹中创建文件等操作
x    允许cd进入此文件夹

rwx 数字表示  421
chmod 更改权限  
chmod  u+r   file.txt  #给文件的user，添加读的权限
chmod  g-x  file.txt  #给文件的group组权限，去掉可执行
chmod o+r,o+w,o+x  file.txt  #给文件的other身份，最大的权限，读写执行
chmod 000 file.txt  # 给文件最低权限， 任何不可读写执行
chmod 644 file.txt  #


chown  # change owner 缩写  
chown 新的属主 file.txt

chgrp  # change group 缩写
chgrp 新的组名 file.txt


软链接： window的快捷方式
ln -s /opt/redis/bin/redis-server  /usr/bin/redis-server  

```



### 打包、压缩、解压缩

```
tar 命令 功能参数
-z  调用gzip命令， 对文件压缩
-x   解包，拆快递
-v    显示整个过程
-f    必须写在参数结尾，指定压缩文件的名字 
-c    打包，收拾快递

压缩文件的后缀，本没有意义，只是告诉别人，这个文件是用什么命令压缩/解压缩

*.gz   gzip命令解压缩
*.tar   用tar命令解压缩
*.xz   用xz命令解压
*.zip   用unzip命令解压

tar -zcvf etc.tar.gz /etc
tar -zxvf etc.tar.gz /
```



### 防火墙

```
用于控制服务器的出/入流量
防止恶意流量攻击服务器，保护服务器的端口等服务。
在学习阶段是直接关闭的，专业的运维人员需要学习iptables软件的一些指令

1 清空防火墙规则
iptables -F
2 关闭防火墙服务
systemctl stop firewalld
systemctl disable firewalld



```

### DNS域名解析

```
域名和ip的对应关系

# cat /etc/resolv.conf
# Generated by NetworkManager
#search localdomain
nameserver 119.29.29.29
nameserver 223.5.5.5

# cat  /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

127.0.0.1  pythonav.cn

nslookup 命令 查看域名的dns信息
yum provides nslookup #查找nslookup这个命令是哪个软件包提供的
yum install bind-utils
[root@bj1 ~]# nslookup www.baidu.com  
Server:		10.211.55.1
Address:	10.211.55.1#53

Non-authoritative answer:
www.baidu.com	canonical name = www.a.shifen.com.
Name:	www.a.shifen.com
Address: 14.215.177.38
Name:	www.a.shifen.com
Address: 14.215.177.39

yum install traceroute # 追踪网络数据包的路由途径
[root@bj1 ~]# traceroute www.baidu.com

```

浏览器里面输入 www.baidu.com 发生了什么

```
1 浏览器进行dns查找， 解析域名对应的ip机器，找到之后浏览器访问此ip地址
2 用户请求，发送到服务器之后， 优先是发给了nginx（web服务器），用户请求的是静态资源（jpg，html，css，jquery），nginx直接从磁盘上找到资料返回给用户的浏览器
	如果nginx监测到用户请求是一个动态请求，登陆，注册 读取数据库，例如.php .aspx 通过url 匹配发现是动态请求， 转发给后端的应用服务器（php tomcat django）
3 django 处理完用户的动态请求后，如果发现需要读取数据库，再通过pymysql 向mysql读取数据
4 如果django处理请求，发现读取的是redis，再通过pyredis向redis拿数据
5 django处理完毕之后，返回给nginx
6 nginx返回给用户浏览器
7 浏览器渲染数据之后给用户查看页面

推荐书籍  大型网站技术架构

```

### crontab 定时任务

```
crontab -e #编辑定时任务编辑文件
crontab -l #查看定时任务的规则
定时任务，注意的是 ，几号，和星期几不得共用

# 每分钟，讲一句话写入到一个文件中
第一步：crontab -e  #打开配置文件
写入如下内容，用的是vim编辑器命令
*  *  *  *  *  /usr/bin/echo  "有人问王思聪，钱是万能的吗？王思聪答：钱是万达的" >>  /tmp/wsc.txt

2.检查定时任务
crontab -l
-----------------------------------
定时任务的语法规则

*  *  *  *  *   命令的绝对路径
分 时  日 月 周  


3,5  *  *  *  *      #每小时的第3，第5分钟执行命令

15   2-5  *  *  *     ￥每天的2点一刻，3点一刻，4点一刻，5点一刻，执行命令

每天8.30上班
30 08 * * *  去上班

每天12下班回家睡觉
00 00 * * *   回家睡觉


```



### linux 软件包管理

```
linux平台的软件安装形式，有3个

- 源代码编译安装，此方式较为麻烦，但是可以自由选择软件的版本（因为是去官网下载最新版本代码），也可以扩展第三方额外的功能（五颗星）
    - 扩展第三方功能
    - 指定软件安装目录
- rpm包手动安装，此方式拒绝，需要手动解决依赖关系，贼恶心（两颗星）
- yum自动化安装软件，需要配置好yum源，能够自动搜索依赖关系，下载，安装，处理依赖关系（五颗星）
    - 不好的地方在于，yum源仓库的软件，版本可能较低
    - 无法指定安装路径，机器数量较多的时候，不容易控制
    


1.备份旧的yum仓库源
cd  /etc/yum.repos.d
mkdir  repobak
mv *.repo   repobak  #备份repo文件

2.下载新的阿里的yum源仓库，阿里的开源镜像站https://developer.aliyun.com/mirror/
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo



```

### 编译安装python3

```
1.很重要，必须执行此操作，安装好编译环境，c语言也是编译后运行，需要gcc编译器golang，对代码先编译，再运行，python是直接运行
yum install gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel -y

curl -o Python-3.6.9.tgz https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
tar -zxvf Python-3.6.9.tgz -C /opt
cd /opt/Python-3.6.9/
mkdir /opt/python3
./configure --prefix=/opt/python3/ && make && make install

echo 'PATH="/opt/python3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin"' >> /etc/profile
source /etc/profile


```



### python virtualenv 虚拟环境工具

```
1.下载虚拟环境工具
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple virtualenv

# 这个命令如果你用相对路径，就得注意你在哪敲打的此命令
[root@s25linux opt]# virtualenv --python=python  venv1

3.创建好venv1之后，需要激活方可使用，这个激活其实就是在修改PATH而已
[root@s25linux bin]# source /opt/venv1/bin/activate

4.明确虚拟环境下venv1的解释器是干净隔离的
(venv1) [root@s25linux bin]# which python3
/opt/venv1/bin/python3
(venv1) [root@s25linux bin]# pip3 list
Package    Version
---------- -------
pip        20.0.2
setuptools 45.2.0
wheel      0.34.2

5.在venv1中安装django1
(venv1) [root@s25linux opt]# pip3 install -i https://pypi.douban.com/simple django==1.11.9
(venv1) [root@s25linux opt]# django-admin  startproject  venv1_dj119

8.deactivate  #直接执行此命令，退出虚拟环境，系统会自动删除venv的PATH，也就表示退出了


# ## 保证开发环境，生产环境python模块一致性
 #把你当前解释器所有用到的模块，信息导出到一个文件中
pip3 freeze  > requirements.txt 
2.把此文件发送给linux机器，或者直接拷贝其内容，也可以
在linux机器上，安装此文件即可，自动读取文件每一行的模块信息，自动安装
pip3 install -i https://pypi.douban.com/simple  -r  requirements.txt   



```





## linux基础命令

```
man ls   # man手册
mkdir --help # help参数，查看简短的帮助信息
3.在线的搜索一些命令查询网站
http://linux.51yip.com/


uptime  #查看服务器运行多久
su - root  # 切换root超级用户  需要输入root密码

yum install net-tools -y  # 安装net-tools 就可以输入ifconfig

ctrl + alt + f1~f7 # 代表linux默认的7个终端

# linux命令行 root用户名 @ 分隔符 bj1主机名 ~ 当前路径家目录
[root@bj1 ~]#   
# 查看命令 按最新的文件在最上面
ls -lht
whoami
pwd
rm -f

yum install tree -y 
tree # 树状图显示文件目录层级结构

name = ‘eric ’ # linux命令行变量赋值， 是临时生效的
echo $name

cat first.py  #查看文件内容
cat -n first.py #-n显示行号
cat >> second.py << EOF
> #!coding:utf-8
> print('ai')
> EOF


cp #拷贝
cp  木兰诗.txt     新_木兰诗.txt
# 复制文件夹，-r 递归复制参数
cp -r a new_a

mv 移动文件  文件夹的路径   也能重命名 
mv 木兰诗.txt     新_木兰诗.txt

# alias 别名命令
alias start="python3  /home/mysite/manager.py runserver  0.0.0.0:8000"


find #查找
语法
find 从哪找 -type 文件类型 -size 文件内容多大  -name 内容名字是什么
-type f 普通文本文件
-type d 文件夹类型
-name 指定文件的名字呢绒

find / -name "*.txt"
find /etc -type f -name "ifcfg*"

# 过滤 在文件内查找内容
grep
grep -i: 忽略大小写；不区分大小写；跳过大小写
grep -r: 搜寻子目录；递归查找字符串；遍历子目录
grep -e: 使用扩展的正则表达式；查找多个字符串的匹配；使用扩展正则表达式
grep -n： # -n 参数是显示行号

grep “^$” test.txt #过滤出空白行
grep -v “^$” test.txt # 找出空白行以外的内容

head 文件名  # 默认从文件的前10行看
head -3  /etc/passwd # 查看文件的前3行

tail -f log.txt  #实时查看文件末尾内容

scp   #两台机器之间传输文件 文件夹
scp root@ip:/opt/test.txt /tmp/
scp /opt/test.txt root@ip:/opt/

scp -r /opt root@ip:/tmp   # -r 递归拷贝参数
scp -r /opt/* root@ip:/tmp/backed/

# windows  xshell工具使用
yum install lrzsz
rz   # window 传给linux
sz   # 从linux中下载到windows

du -sh /*   #显示每个目录的容量大小





```













