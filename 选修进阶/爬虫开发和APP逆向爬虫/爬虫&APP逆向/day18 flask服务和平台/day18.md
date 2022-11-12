# day18 Flask服务和平台

今日概要：

- 服务（解决so文件加密）

  - 硬核破解，难度大。

  - frida-rpc，不再破解而是调用。

  - 开发一个app，加载so文件并调用so文件中的函数直接加密。【B站】

    ```
    内部依赖少，加密结果直接拿到。
    内部依赖多，补充很多代码（繁琐）。
    ```

- 平台

  - 下单
  - 程序自动去执行
  - 修改订单状态



## 1.app调用so

- JNI开发，自己写so文件，自己调用。
- 别人给我一个so文件，安卓开发中调用他so文件。



### 1.1 标准步骤

- 创建安卓应用

- 引入别人的so文件
  ![image-20211123201612598](assets/image-20211123201612598-7669774.png)

- 配置，安卓程序去指定的目录中寻找so文件。
  ![image-20211123201826368](assets/image-20211123201826368.png)

- 写类 + native方法，调用so文件（仿照你逆向的app）。

  ```java
  package com.bilibili.nativelibrary;
  import com.bilibili.nativelibrary.SignedQuery;
  
  import java.security.InvalidKeyException;
  import java.util.Map;
  import java.util.SortedMap;
  import java.util.TreeMap;
  
  import javax.crypto.spec.IvParameterSpec;
  
  public class LibBili {
      public static final int a = 0;
      public static final int b = 1;
      public static final int c = 0;
      public static final int d = 1;
      public static final int e = 2;
      public static final int f = 3;
  
      static {
          System.loadLibrary("bili");
      }
  	
      public static SignedQuery g(Map arg1) {
          TreeMap v1 = arg1 == null ? new TreeMap() : new TreeMap(arg1);
          return LibBili.s(((SortedMap) v1));
      }
      
      static native SignedQuery s(SortedMap arg0);
      
      ...
  }
  ```

- 使用类去调用方法进行加密

  ```java
  SignedQuery query = LibBili.g(参数)
  ```

- 编写哪些加密过程中依赖的所有的类。

  ```java
  ...
  ...
  ```

  注意：都依赖哪些类，你是无法直接找出来。

  



### 1.2 B站

day18【源码】



至此，写死了的URL参数，加密并获取sign，不能对外提供服务。



## 2.Flask服务

![image-20211123204629734](assets/image-20211123204629734.png)



### 2.1 Flask部分

```python
import uuid
from queue import Queue, Empty
from flask import Flask, request, jsonify

app = Flask(__name__)

# 签名 任务队列
TASK_QUEUE = Queue()

# 结果队列
SIGN_DICT = {}


@app.route("/sign/task/", methods=["POST", "GET"])
def sign_task():
    if request.method == "POST":
        # ################ 第一步：客户端发送签名任务 ##############
        # 获取待签名字符串
        # 例如："abi=x86&appid=tv.danmaku.bili&appkey=1d8b6e7d45233436&brand=HUAWEI.."
        param_string = request.form.get('param_string')
        # sign_type=1，算法1加密 Libbili.g
        # sign_type=2，算法2加密 Libbili.h
        sign_type = request.form.get('sign_type')

        uid = str(uuid.uuid4())
        info = {"uid": uid, 'param_string': param_string, 'sign_type': sign_type}
        TASK_QUEUE.put(info)
        SIGN_DICT[uid] = Queue()
        return uid
    try:
        # ################ 第二步：app获取签名任务 ##############
        print("app取任务")
        task = TASK_QUEUE.get(block=True, timeout=8)
        res = jsonify(task)
    except Empty as e:
        res = "error"
    return res


@app.route("/sign/", methods=["POST", "GET"])
def sign():
    if request.method == "POST":
        # ################ 第三步：app签名后，签名的结果发送回来。 ##############
        print("app计算好并发送结果")
        info = request.json
        print('json--->', info)
        SIGN_DICT[info['uid']].put(info['total_string'])
        return "success"

    # ################ 第四步：客户端获取签名的结果 ##############
    print("等待获取 total string")
    uid = request.args.get('uid')
    total_string = SIGN_DICT[uid].get(block=True)
    del SIGN_DICT[uid]
    return total_string


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
```



### 2.2 APP签名部分

见源码：hook



### 2.3 客户端部分

在B站中找了好几个请求，包含：LibBili.g 或 LibBili.h 。

见代码：v3.py



## 3.平台（x视频）

![image-20211123214318315](assets/image-20211123214318315.png)

### 3.1 下单

- 大致框架

- 前端：HTML、CSS、JavaScript（模板BootStrap开发）

  - 使用BootStrap

    ```
    - 下载
    - 引入页面
    - 学习标签怎么编写，根据标签页面编写
    ```

  - BootStrap动态效果，依赖jQuery.js 



见代码：day18_chongming









































