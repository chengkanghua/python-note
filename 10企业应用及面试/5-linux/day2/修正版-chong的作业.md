```
1.每个人安装好Linux，并且获取自己的ip地址，使用xshell连接上
已完成

2.服务器有哪些硬件?
cpu 内存条 硬盘 显卡 主板 网卡 电源

3.centos是什么？
centos是一个操作系统 是linux的一个免费发行版本

4.开源是什么意思？
开源就是开放源代码  让大家在原有的基础上进行扩展开发。注意是要遵循 GUN开源许可协议的

5.Linux作者是谁？
Linus Torvalds 林纳斯·本纳第克特·托瓦兹

6.常见Linux发行版，你们公司用什么？
常见的有：Centos，Redhat，ubuntu，suse,我们用的是Centos 7(因为docker容器技术，都得在7系列平台上运行)

7.Linux的特性？好处？
稳定 开源免费，安全性强可供的多用户同时操作
支持多用户，多任务的一个操作系统 

8.学习Linux是怎么安装的操作系统？
(个人学习版)通过VMware workstations Pro虚拟机，创建需要的Linux发行版操作系统
(企业级)针对服务器，安装vmware esxi vsphere 企业级虚拟化软件，安装相应的linux镜像
(购买云服务器)腾讯、阿里云、华为云，提供了学生使用的低配版服务器10/元 


9.通过何种方式登录Linux？
通过xshell，远程连接

如何连接公司的阿里云服务器  ，ip地址是 123.206.16.61

ssh   账户@123.206.16.61
#远程连接服务器，就是 用ssh命令  连接远程服务器地址即可




10.什么是Ip，什么是port? 0.0.0.0 和127.0.0.1区别?
ip:网络地址 port:端口 0.0.0.0代表一台机器的所有的网络地址  127.0.0.1是本地回环地址 不能和外界通信。
linux的端口范围： 0~65535  
系统不常用的，开发人员经常可以用更的 10000~50000 

11.如何查看自己的ip地址
在windows下ipconfig 
linux下ifconfig
（ifconfig需要单独安装第三方的软件包，叫做 net-tools ，yum install net-tools -y ）
(linux自带的ip命令查看网络：   ip  addr show  )

12.每个人安装好Linux，并且获取自己的ip地址，使用xshell连接上
已完成

13.什么是linux的命令提示符？
[root@VM_0_8_centos ~]# 就是命令提示符
root是当前登录用户，怎么查看当前登录的用户是？   whoami
VM_0_8_centos是主机名，hostname(查看主机名)
#更改主机名的命令
hostnamectl set-hostname   新的主机名 


~ 可以代表当前登录用户的家目录 


#是超级用户的提示符，$是普通用户的提示符

【知识点补充】
新建用户useradd  用户名
更改/设置用户密码  passwd   用户名
切换用户 su  -   新用户名



13.1知识点补充，tab键补全
linux下使用tab键，可以补全 文件路径，以及命令的路径
1.补充命令的路径
[root@bogon ~]# python
python     python2    python2.7

2.文件路径的补全
/etc/sysconfig/network-scripts/ifcfg-ens33 #这是linux网卡配置文件



14.linux的目录分隔符是？
分隔符是/  

15.用自己的语言描述下，linux的目录结构
所有的目录都是从/开始的 倒状树状结构
/

/root  /home   /tmp(系统会将产生的临时文件，放在这里，系统会定时清理这个文件夹，里面东西，都得是不重要的)  

/root/你瞅啥.txt   

/home/普通用户的家目录/  



16.linux的 opt、root、home、etc、var目录作用是？
opt是大型软件存放目录 ，例如 /opt/nginx    /opt/redis  /opt/python3  /opt/mongodb

root是超级用户的家目录 

home是普通用户的统一管理家目录

etc是配置文件存放的目录  

var是存放经常变化文件的目录 例如日志。

17.待在/home/pyyu目录下，创建/s25/男同学，文件夹，绝对相对路径两种命令

#这个是绝对路径
/s25/xx/

#这些就是相对路径
../25/xx	#上一级目录的相对

./25/xx  #当前目录的相对

25/xx  		#同上



绝对路径: mkdir -p /s25/男同学  #写的对吗，写的是对的！！！！



相对路径: mkdir -p ../../s25/男同学  #写的对吗？

18.待在/tmp目录下，创建文件first.py，绝对相对路径两种命令
绝对路径: touch /tmp/first.py  #写的是对的！！
相对路径: touch  ./frist.py   #写的也是对的

19.删除 /tmp下所有内容
rm -rf  /tmp/*  #写的对不对？删除地下所有的内容
rm -rf /tmp/  #写的对不对 ，错了！！这是删除这个文件夹！！！

20.待在 /etc/目录下，进入 /tmp目录下，用绝对、相对两种命令
绝对路径: cd /tmp/  #没毛病 
相对路径: cd  ../tmp	#没毛病 

21.解释下几个特殊目录的用法
. 当前目录
.. 上一级目录
~ 家目录，当前以登录的用户家目录  ，root就是 /root    pyyu就是 /home/pyyu  


```