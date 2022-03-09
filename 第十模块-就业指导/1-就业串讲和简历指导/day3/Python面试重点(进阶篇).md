# Python面试重点（进阶篇）

注意：只有必答题部分计算分值，补充题不计算分值。

## 第一部分 必答题

1.   简述OSI 7层模型及其作用？

     应用层 表示层 会话层 传输层  网络层 数据链路层 物理层

     一般在开发中应用层 表示层 会话层会合并成表示层

     我们开发中的网路通信都是基于socket来完成的，它封装了传输层 网络层 数据链路层 物理层各层的功能

     大概包括：

     ​	应用层  在两个应用能够通信的基础上又封装了一些应用独有的关心的内容http协议 https协议 ftp协议

     ​	传输层 选择具体的传输协议，tcp/udp 以及封装应用的端口

     ​	网络层 封装了ip协议 ipv4 ipv6

     ​	数据链路层。封装了mac地址 并且 arp和rarp协议

     ​	物理层 将上述内容进行转换在网线上进行数据传输

2.   简述tcp三次握手、四次挥手的流程。

https://www.cnblogs.com/clschao/articles/9578922.html

3.   TCP和UDP的区别？

     tcp 面向连接 传输可靠  速度慢

     udp 面向报文 可靠性差 速度快

4.   神木市黏包？

     tcp协议数据无边界的特点 导致了多条分散发送的数据黏合在一起变成了一条数据

5.   什么 B/S和C/S架构？

     web项目  B/S

     C/S  桌面端

6.   请实现一个简单的socket编程 （客户端和服务端可以进行收发消息）

7.   简述进程、线程、协程的区别？

     进程：开销大 数据隔离 子进程中有一个挂了不影响其他的 cpython可以利用多核 高计算型

     线程：开销小 数据共享 子进程中挂了一个会影响其他 cpython不能利用多核 高IO型(文件操作/网络操作)

     协程：只能针对高IO型 且是网络IO才能有并发作用 用户级别  开销更小

8.   什么是GIL锁？

9.   进程之间如何通信？

     IPC：基于第三方工具（redis）基于管道 队列

10.   Python如何使用线程池、进程池？

      concurrent.futures.ThreadPoolExecutor

      Concurrent.futures.ProcessPoolExecutor

11.   请通过yield关键字实现一个协程？

      ```python
      任务切换+保存状态
      
      def consumer():
          while True:
              n = yield
              print('处理数据%s' % n)
            
      def producer():
          cg = consumer()
          next(cg)
          for i in range(100):
              print('生成了一个%s' %i）
              # yield i    # 每生产一个数据就停止
              cg.send(i)
                
      producer()
      ```

12.   什么是异步非阻塞？

      同步join input   异步： terminate

      阻塞不占用cpu     非阻塞：占用cpu

      同步阻塞： name = input();  pwd = input()

      同步非阻塞： say(); say2()

      异步阻塞：比如启动多线程和多个客户端进行tcp通信

      ​					可以同时和多个人通信，但是每个人的通信中recv 仍然会发生阻塞

      异步非阻塞：可以启动多线程 设置setblocking(False)

      ​					可以同时和多个人通信，并且在过程中没有阻塞

13. 什么是死锁？如何避免？
    
    用一把锁：一把锁递归/一把互斥锁
    
14.   程序从flag a执行到falg b的时间大致是多少秒？

      ```python
      import threading
      import time
      def _wait():
          time.sleep(60)
      # flag a
      t = threading.Thread(target=_wait)
      t.setDeamon(False)
      t.start()
      # flag b
      ```

15.   程序从flag a 执行到falg b的时间大致是多少秒？

      ```python
      import threading
      import time
      def _wait():
          time.sleep(60)
      # flag a
      t = threading.Thread(target=_wait)
      t.setDeamon(True)
      t.start()
      # flag b
      ```

16.   程序从flag a执行到falg b的时间大致是多少秒？    60

      ```python
      import threading
      import time
      def _wait():
          time.sleep(60)
      # flag a
      t = threading.Thread(target=_wait)
      t.start()
      t.join()
      # flag b
      ```

17.   读程序，请确认执行到最后number是否为0？   一定

      ```python
      import threading
      loop = int(1E7)
      def _add(loop:int = 1):
          global number
          for _ in range(loop):
              number += 1
      def _sub(loop:int = 1):
          global number
          for _ in range(loop):
              number -= 1
      number = 0
      ta = threading.Thread(target=_add,args=(loop,))
      ts = threading.Thread(target=_sub,args=(loop,))
      ta.start()
      ta.join()
      ts.start()
      ts.join()
      
      ```

18.   读程序，请确认执行到最后number是否一定为0 ？   不一定

      ```
      import threading
      loop = int(1E7)
      def _add(loop:int = 1):
      	global number
      	for _ in range(loop):
      		number += 1
      def _sub(loop:int = 1):
      	global number
      	for _ in range(loop):
      		number -= 1
      number = 0
      ta = threading.Thread(target=_add,args=(loop,))
      ts = threading.Thread(target=_sub,args=(loop,))
      ta.start()
      ts.start()
      ta.join()
      ts.join()
      ```

19.   MySQL常见数据引擎区别？

      innodb 5.6之后的默认：支持行级锁 事务 外键

      ​	开启事务 查询这个用户换是不是一个公户+锁，如果是改成私户 提交事务

      ​	select xxx from 表 where id = 1 for update

      myisam 5.5 之前的默认  只支持表锁

      memory  内存

      blackhole  黑洞

      ​	create table 表名() charset=utf8 engine=blackhole;

20.   简述事务及其特性？

      一致性  原子性 隔离性  持久性

21.   事务的隔离级别？

      脏读，幻读，不可重复读

      未提交读\已提交读\可重复读\串行化

22.   char和varchar的区别？

      定长255  高效 浪费空间

      变长 65535 低效  节省空间

23.   mysql中varchar与char的区别以及varchar(50)中的50代表的含义？  最长50个字符

24.   MySQL中的delete和truncate的区别？

      delete： 可以删除部分数据 auto_incement清除不掉。

      truncate： 清空表 并且重置auto_increment为0

25.   where子句中有a,b,c三个查询条件，创建一个组合索引abc(a,b,c),以下哪种会命中索引。

      ```
      （a）  这个
      （b）
       (c)  
      (a,b) 这个
      (b,c)
      (a,c) 这个
      (a,b,c) 这个
      
      ```

26.   组合索引遵循什么原则才能命中索引？

      最左前缀原则 不能用范围 只能用and

27.   列举MySQL常见的函数？

      count sum  avg max min now year month day hour minute second week sub_date

      concat group_count concat_ws user password database

28.   MySQL 数据库 导入 导出命令有哪些？

      mysqldump

      mysqldump -database

      source

29.   什么是sql注入？

      通过一些输入的内容绕过sql的判断机制

30.   简述left join和 inner join 的区别？

31.   SQL语句中having的作用？

      以聚合函数作为条件过滤分组

32.   MySQL数据中varchar和text最多能存储多少个字符？  65535

33.   MySQL的索引方式有几种？

      主键索引 唯一索引 普通索引 联合主键 联合唯一 联合普通

      b+树（innodb） hash索引(memory) 全文索引(Full-text)

      b+树(聚合索引  辅助索引)

34.   什么时候索引会失效？ （有索引但无法命中索引）

35.   数据库优化方案？

      读写分离  主从复制 binlog日志

      分库分表

      用定长字段代替变长字段

      建表的时候把短的 固定长度的字段放在左边

36.   什么是MySQL慢日志？

37.   设计表，关系如下：教师teacher ，班级class，学生student，科室post。

      科室与教师为一对多关系，教师和班级为多对多关系，班级和学生为一对多关系，科室中需体现层级关系。

      ```
      1. 写出各张表的逻辑字段
      2. 根据上述关系表
      	a. 查询教师id=1的学生数
      	b. 查询科室id=3的下级部门数
      	c. 查询所带学生最多的教师的id
      ```

      select count(*) from student s, class c,teacher t where 

      s.cid=c.cid and c.cid = t.cid 

      and tid=1;

      select count(*) from post where parent_id=3;

       Select tid,count(*) as p from student s ,class c ,teacher t where

      s.cid=c.cid and c.cid=t.cid group by tid order by p limit 1;

38.   有staff表，字段为主键Sid，姓名Sname，性别Sex（值为男或者女），课程表Course，字段为主键Cid，课程名称Cname，关系表SC_Relation，字段为Student表主键Sid和Course表主键Cid，组成联合主键，请SQL查询语句写出查询所有选“计算机”课程的男士的姓名。

39.   根据表关系写SQL语句

      图片未显示

。查询所有同学的学号、姓名、选课数、总成绩；

。查询姓“李”的老师的个数；
。查询平均成绩大于60分的同学的学号和平均成绩；。

查询有课程成绩小于60分的同学的学号、姓名。

删除学习“叶平”老师课的score表记录；
。查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；。

查询每门课程被选修的学生数；
。查询出只选修了一门课程的全部学生的学号和姓名；
。查询选修“杨艳”老师所授课程的学生中，成绩最高的学生姓名及其成绩；

查询两门以上不及格课程的同学的学号及其平均成绩；

## 第二步 补充题

1.   什么是IO多路复用？
     网络数据传输监控机制 - 多个网络连接复用一个监听机制

     select模块、selectors模块
     操作系统提供的io多路复用的机制 select poll epoll

     epoll最好用的是回调函数的机制
     select poll 的内部机制 是轮询

2. async/await关键字的作用？
  async用来定义一个协程函数的
  await用来控制一个可能发生io阻塞的任务的切入和切出

  ```python
  async def func ():pass
  await asyncio.sleep(2) 
  import asyncio
  loop = asyncio.get_event_loop()
  loop.run_until_complete(func) 
  ```

  

3.  MySQL的执行计划的作用？
  不执行sql，在之前先查看以下sql的顺序 索引的使用情况从而去推测 优化sql语句

4. 简述MySQL触发器、函数、视图、存储过程？

  触发器 trigger：在用户对某张表做完某个固定的操作（insert update delete）会自动在数据库中触发另一个动作insert 一条数据 苹果手机
  往对应的统计表中  把苹果这条数据+1
  函数（function）：根据参数进行判断循环得出一个结果 并返回，通过select 函数名（参数）来调用并查看结果

  视图（view）：帮助我简化查询部分的连表操作
  存储过程（procedure）：可以实现非常负责的sql逻辑并对数据进行增删改查且可以返回多个结果call 名字（参数）调用

5. 数据库中有表：t_tade_date 

  ```
  id tade_date 
  1 2018-1-2 
  2 2018-1-26 
  3 2018-2-8 
  4 2018-5-6
  ...
  输出每个月最后一天的ID
  ```

  select last_day(tade_date) from t_tade_date group by month(tade_date);
  select id from t_tade_date where tade_date in (select last_day(tade_date) from t_tade_date group by month(tade_date));



​      select id,max(tade_date) from t.table_date group by month(tade_date)

















​		