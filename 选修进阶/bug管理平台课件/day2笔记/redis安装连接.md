相信大家曾经都有过这样的经历：注册某个网站时，通过点击获取短信验证码，而验证码会一般会有60秒的超时时间限制，即：60s之后短信验证码失效，需重新获取验证码。

刚才说的短信验证码失效的事 和 今天的话题redis有什么关系呢？

redis是一个软件，他恰好提供了一个可以设置值并允许设定超时时间的功能，例如：

> 例如：我在redis中设置一个 键 值 并指定超时时间为 10 秒，简化之后可以这样实现 `conn.set("15131255089",9871,10)`，之后还可以根据 键 再可以去获取对应的值 `value = conn.get("15131255089")`，如果已超时则获取的值为空。

so，今天要给大家先聊聊redis，这样以后在项目中我们就可以用上他了。

**声明**：redis中要学的知识点非常多，而这些redis专项内容会在咱们之后的Linux架构的课程中详细讲解，本节主要以“短信超时”功能为目的来讲解。

## 1. 什么是redis？

官方：Redis是一个使用 C语言 编写的开源、支持网络、基于内存、可选持久性的键值对存储数据库。
白话：Redis是一个软件，这个软件可以帮助我们维护一部分内存，让我们往那块内存中进行存取值。如果数据在内存中存储，遇到宕机那么数据就会丢失，而redis解决了这个问题，他可以将内存中的数据以某种策略存储到硬盘，以保证宕机数据不丢失。

Redis和MySQL数据库的比较？

```
redis，直接在内存中进行存取数据，速度非常快；由于在内存，所以存储的数据不能太多，内存一般8G/16G；对数据可以设置自动超时时间；mysql，通过SQL语句操作的数据都在硬盘上，速度相对慢；由于存储在硬盘，所以存储的数据可以非常多，硬盘一般500G/1T；数据不能自动超时，想超时需要自定写SQL处理；
```

## 2. 安装redis

由于目前同学们还未接触过 Linux 操作系统，所以大家可以先安装到windows系统上来进行学习。

注意：以后在工作中使用到redis时，都是需要安装在Linux操作系统上，咱们后期Linux架构课程会单独讲解Linux并带着大家手把手搭建redis和高可用及集群等。

### 2.1 下载redis

选择最新稳定版安装，地址：https://github.com/microsoftarchive/redis/releases

<img src="redis%E5%AE%89%E8%A3%85%E8%BF%9E%E6%8E%A5.assets/download-redis.png" alt="示例图片" style="zoom:50%;" />

提醒：截止目前redis稳定版本已到 5.0 ，由于windows实际应用不多，所以版本就比较滞后。

### 2.2 安装redis

找到已下载好的安装包，根据下图的提示按步骤点击执行即可。

<img src="redis%E5%AE%89%E8%A3%85%E8%BF%9E%E6%8E%A5.assets/r1.png" alt="img" style="zoom: 50%;" />

<img src="redis%E5%AE%89%E8%A3%85%E8%BF%9E%E6%8E%A5.assets/r2.png" alt="img" style="zoom:50%;" />

<img src="redis%E5%AE%89%E8%A3%85%E8%BF%9E%E6%8E%A5.assets/r3.png" alt="img" style="zoom:50%;" />

<img src="redis%E5%AE%89%E8%A3%85%E8%BF%9E%E6%8E%A5.assets/r4.png" alt="img" style="zoom:50%;" />

<img src="redis%E5%AE%89%E8%A3%85%E8%BF%9E%E6%8E%A5.assets/r5.png" alt="img" style="zoom:50%;" />

最后点击next就开始安装，直至安装成功，成功之后所有redis相关安装的窗口都会自动关闭。

### 2.3 修改配置

redis这个软件安装上之后，需要对他进行一些基本设置，以便于我们以后可以通过python代码来对redis中的数据进行操作。

- 打开配置文件，redis安装的目录下的 `redis.windows-service.conf` 文件

  <img src="redis%E5%AE%89%E8%A3%85%E8%BF%9E%E6%8E%A5.assets/r6.png" alt="img" style="zoom:50%;" />

- 修改配置

  - 设置绑定IP，如果想要让局域网内其他主机访问自己的redis，需要设置 `bind 0.0.0.0`

    <img src="redis%E5%AE%89%E8%A3%85%E8%BF%9E%E6%8E%A5.assets/c1.png" alt="img" style="zoom:50%;" />

  - 设置redis密码，如果想需要提供密码再登录redis，需要设置 `requirepass 密码`

    <img src="redis%E5%AE%89%E8%A3%85%E8%BF%9E%E6%8E%A5.assets/c2.png" alt="img" style="zoom:50%;" />

### 2.4 启动redis

安装和配置完成之后，需要启动redis。

- 打开电脑的【控制面板】，然后选择【管理工具】，在选择【服务】

  <img src="redis%E5%AE%89%E8%A3%85%E8%BF%9E%E6%8E%A5.assets/r7.png" alt="img" style="zoom:50%;" />

- 启动 或 关闭，在右边找到并选中redis服务，然后点击 重启动 或 关闭

  <img src="redis%E5%AE%89%E8%A3%85%E8%BF%9E%E6%8E%A5.assets/r8.png" alt="img" style="zoom:50%;" />

## 3. redis-cli连接redis

redis安装并启动之后，就可以通过各种客户端连接redis并做各种操作。

redis-cli是安装上redis之后自带的客户端工具，他可以让我们快速通过命令对redis操作。

在windows中打开终端，输入 redis-cli 就可以使用这个客户端了。例如：

<img src="redis%E5%AE%89%E8%A3%85%E8%BF%9E%E6%8E%A5.assets/client.png" alt="img" style="zoom:50%;" />

## 4. python连接redis

python代码也可以实现连接redis并对redis中进行各种操作。python代码想要操作redis必须先安装相关模块。

![img](redis%E5%AE%89%E8%A3%85%E8%BF%9E%E6%8E%A5.assets/p1.png)

提示：在安装redis的主机上执行 ipconfig 获取redis的IP（windows系统）
<img src="redis%E5%AE%89%E8%A3%85%E8%BF%9E%E6%8E%A5.assets/ip.png" alt="img" style="zoom:50%;" />

**第一步**：安装python操作redis模块

```
pip3 install redis
```

**第二步**：写代码去操作redis

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
# 直接连接redis
conn = redis.Redis(host='10.211.55.28', port=6379, password='foobared', encoding='utf-8')
# 设置键值：15131255089="9999" 且超时时间为10秒（值写入到redis时会自动转字符串）
conn.set('15131255089', 9999, ex=10)
# 根据键获取值：如果存在获取值（获取到的是字节类型）；不存在则返回None
value = conn.get('15131255089')
print(value)
```

上面python操作redis的示例是以直接创建连接的方式实现，每次操作redis如果都重新连接一次效率会比较低，建议使用redis连接池来替换，例如：

```python
import redis
# 创建redis连接池（默认连接池最大连接数 2**31=2147483648）
pool = redis.ConnectionPool(host='10.211.55.28', port=6379, password='foobared', encoding='utf-8', max_connections=1000)
# 去连接池中获取一个连接
conn = redis.Redis(connection_pool=pool)
# 设置键值：15131255089="9999" 且超时时间为10秒（值写入到redis时会自动转字符串）
conn.set('name', "武沛齐", ex=10)
# 根据键获取值：如果存在获取值（获取到的是字节类型）；不存在则返回None
value = conn.get('name')
print(value)
```

## 5. django连接redis

按理说搞定上一步python代码操作redis之后，在django中应用只需要把上面的代码写到django就可以了。

例如：django的视图函数中操作redis

```python
import redis
from django.shortcuts import HttpResponse
# 创建redis连接池
POOL = redis.ConnectionPool(host='10.211.55.28', port=6379, password='foobared', encoding='utf-8', max_connections=1000)
def index(request):
    # 去连接池中获取一个连接
    conn = redis.Redis(connection_pool=POOL)
    conn.set('name', "武沛齐", ex=10)
    value = conn.get('name')
    print(value)
    return HttpResponse("ok")
```

上述可以实现在django中操作redis。**但是**，这种形式有点非主流，因为在django中一般不这么干，而是用另一种更加简便的的方式。

**第一步**：安装django-redis模块（内部依赖redis模块）

```
pip3 install django-redis
```

**第二步**：在django项目的settings.py中添加相关配置

```python
# 上面是django项目settings中的其他配置....
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://10.211.55.28:6379", # 安装redis的主机的 IP 和 端口
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                "encoding": 'utf-8'
            },
            "PASSWORD": "foobared" # redis密码
        }
    }
}
```

**第三步**：在django的视图中操作redis

```python
from django.shortcuts import HttpResponse
from django_redis import get_redis_connection
def index(request):
    # 去连接池中获取一个连接
    conn = get_redis_connection("default")
    conn.set('nickname', "武沛齐", ex=10)
    value = conn.get('nickname')
    print(value)
    return HttpResponse("OK")
```

## 写在最后

至此，就是本节的所有内容，大家可以在django中通过redis进行存取值，在后续的项目开发中可以用他来完成短信验证码过期的功能。

以后关于redis还会讲很多其他高级的知识点，参见：

- https://pythonav.com/wiki/detail/3/33/
- https://www.cnblogs.com/wupeiqi/articles/5132791.html
- http://www.redis.cn/