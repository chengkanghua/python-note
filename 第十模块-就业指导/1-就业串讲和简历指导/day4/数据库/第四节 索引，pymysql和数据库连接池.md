# 引入



今天我们来学习一下索引、pymysql的python连接mysql的客户端和数据库连接池DBUtils。





# 第一节 索引

## 1.1 为什么使用索引

​	一般的应用系统，读写比例在10:1左右，而且插入操作和一般的更新操作很少出现性能问题，在生产环境中，我们遇到最多的，也是最容易出问题的，还是一些复杂的查询操作，因此对查询语句的优化显然是重中之重。说起加速查询，就不得不提到索引了。

​	索引的目的在于提高查询效率，与我们查阅图书所用的目录是一个道理：先定位到章，然后定位到该章下的一个小节，然后找到页数。相似的例子还有：查字典，查火车车次，飞机航班等，下面内容看不懂的同学也没关系，能明白这个目录的道理就行了。 那么你想，书的目录占不占页数，这个页是不是也要存到硬盘里面，也占用硬盘空间。你再想，你在没有数据的情况下先建索引或者说目录快，还是已经存在好多的数据了，然后再去建索引，哪个快，肯定是没有数据的时候快，因为如果已经有了很多数据了，你再去根据这些数据建索引，是不是要将数据全部遍历一遍，然后根据数据建立索引。你再想，索引建立好之后再添加数据快，还是没有索引的时候添加数据快，索引是用来干什么的，是用来加速查询的，那对你写入数据会有什么影响，肯定是慢一些了，因为你但凡加入一些新的数据，都需要把索引或者说书的目录重新做一个，所以索引虽然会加快查询，但是会降低写入的效率。　　

​	**索引的影响**

​		1、在表中有大量数据的前提下，创建索引速度会很慢

​		2、在索引创建完毕后，对表的查询性能会发幅度提升，但是写性能会降低

​	**本质都是：通过不断地缩小想要获取数据的范围来筛选出最终想要的结果，同时把随机的事件变成顺序的事件，也就是说，有了这种索引机制，我们可以总是用同一种查找方式来锁定数据。**

​	数据库也是一样，但显然要复杂的多，因为不仅面临着等值查询，还有范围查询(>、<、between、in)、模糊查询(like)、并集查询(or)等等。数据库应该选择怎么样的方式来应对所有的问题呢？我们回想字典的例子，能不能把数据分成段，然后分段查询呢？最简单的如果1000条数据，1到100分成第一段，101到200分成第二段，201到300分成第三段......这样查第250条数据，只要找第三段就可以了，一下子去除了90%的无效数据。但如果是1千万的记录呢，分成几段比较好？稍有算法基础的同学会想到搜索树，其平均复杂度是lgN，具有不错的查询性能。但这里我们忽略了一个关键的问题，复杂度模型是基于每次相同的操作成本来考虑的。而数据库实现比较复杂，一方面数据是保存在磁盘上的，另外一方面为了提高性能，每次又可以把部分数据读入内存来计算，因为我们知道访问磁盘的成本大概是访问内存的十万倍左右，所以简单的搜索树难以满足复杂的应用场景。

​	前面提到了访问磁盘，那么这里先简单介绍一下磁盘IO和预读，磁盘读取数据靠的是机械运动，每次读取数据花费的时间可以分为寻道时间、旋转延迟、传输时间三个部分，寻道时间指的是磁臂移动到指定磁道所需要的时间，主流磁盘一般在5ms以下；旋转延迟就是我们经常听说的磁盘转速，比如一个磁盘7200转/min，表示每分钟能转7200次，也就是说1秒钟能转120次，旋转延迟就是1/120/2 = 4.17ms，也就是半圈的时间（这里有两个时间：平均寻道时间，受限于目前的物理水平，大概是5ms的时间，找到磁道了，还需要找到你数据存在的那个点，寻点时间，这寻点时间的一个平均值就是半圈的时间，这个半圈时间叫做平均延迟时间，那么平均延迟时间加上平均寻道时间就是你找到一个数据所消耗的平均时间，大概9ms，其实机械硬盘慢主要是慢在这两个时间上了，当找到数据然后把数据拷贝到内存的时间是非常短暂的，和光速差不多了）；传输时间指的是从磁盘读出或将数据写入磁盘的时间，一般在零点几毫秒，相对于前两个时间可以忽略不计。那么访问一次磁盘的时间，即一次磁盘IO的时间约等于5+4.17 = 9ms左右，听起来还挺不错的，但要知道一台500 -MIPS（Million Instructions Per Second）的机器每秒可以执行5亿条指令，因为指令依靠的是电的性质，换句话说执行一次IO的消耗的时间段下cpu可以执行约450万条指令，数据库动辄十万百万乃至千万级数据，每次9毫秒的时间，显然是个灾难，所以我们要想办法降低IO次数。



## 1.2 索引原理

​	前面讲了索引的基本原理，数据库的复杂性，又讲了操作系统的相关知识，目的就是让大家了解，现在我们来看看索引怎么做到减少IO，加速查询的。任何一种数据结构都不是凭空产生的，一定会有它的背景和使用场景，我们现在总结一下，我们需要这种数据结构能够做些什么，其实很简单，那就是：每次查找数据时把磁盘IO次数控制在一个很小的数量级，最好是常数数量级。那么我们就想到如果一个高度可控的多路搜索树是否能满足需求呢？就这样，b+树应运而生，看下图：

![img](https://images2017.cnblogs.com/blog/1036857/201709/1036857-20170912011123500-158121126.png)



​	如上图，是一颗b+树，最上层是树根，中间的是树枝，最下面是叶子节点，关于b+树的定义可以参见[B+树](http://zh.wikipedia.org/wiki/B%2B树)，这里只说一些重点，浅蓝色的块我们称之为一个磁盘块或者叫做一个block块，这是操作系统一次IO往内存中读的内容，一个块对应四个扇区，可以看到每个磁盘块包含几个数据项（深蓝色所示，一个磁盘块里面包含多少数据，一个深蓝色的块表示一个数据，其实不是数据，后面有解释）和指针（黄色所示，看最上面一个，p1表示比上面深蓝色的那个17小的数据的位置在哪，看它指针指向的左边那个块，里面的数据都比17小，p2指向的是比17大比35小的磁盘块），如磁盘块1包含数据项17和35，包含指针P1、P2、P3，P1表示小于17的磁盘块，P2表示在17和35之间的磁盘块，P3表示大于35的磁盘块。真实的数据存在于叶子节点即3、5、9、10、13、15、28、29、36、60、75、79、90、99。非叶子节点只不存储真实的数据，只存储指引搜索方向的数据项，如17、35并不真实存在于数据表中。

​	如果要查找数据项29，那么首先会把磁盘块1由磁盘加载到内存，此时发生一次IO，在内存中用二分查找确定29在17和35之间，锁定磁盘块1的P2指针，内存时间因为非常短（相比磁盘的IO）可以忽略不计，通过磁盘块1的P2指针的磁盘地址把磁盘块3由磁盘加载到内存，发生第二次IO，29在26和30之间，锁定磁盘块3的P2指针，通过指针加载磁盘块8到内存，发生第三次IO，同时内存中做二分查找找到29，结束查询，总计三次IO。真实的情况是，3层的b+树可以表示上百万的数据，如果上百万的数据查找只需要三次IO，性能提高将是巨大的，如果没有索引，每个数据项都要发生一次IO，那么总共需要百万次的IO，显然成本非常非常高。除了叶子节点，其他的树根啊树枝啊保存的就是数据的索引，他们是为你建立这种数据之间的关系而存在的。

​	**索引字段要尽量的小**：通过上面的分析，我们知道IO次数取决于b+数的高度h或者说层级，这个高度或者层级就是你每次查询数据的IO次数，假设当前数据表的数据为N，每个磁盘块的数据项的数量是m，则有h=㏒(m+1)N，当数据量N一定的情况下，m越大，h越小；而m = 磁盘块的大小 / 数据项的大小，磁盘块的大小也就是一个数据页的大小，是固定的，如果数据项占的空间越小，数据项的数量越多，树的高度越低。这就是为什么每个数据项，即索引字段要尽量的小，比如int占4字节，要比bigint8字节少一半。这也是为什么b+树要求把真实的数据放到叶子节点而不是内层节点，一旦放到内层节点，磁盘块的数据项会大幅度下降，导致树增高。当数据项等于1时将会退化成线性表

## 1.3 MySQL的常用索引

1.3.1 常用索引

```
主键索引PRIMARY：又称为聚集索引，每张表有且只能有一个，主键索引PRIMARY KEY：加速查找+约束（不为空、不能重复）

普通索引INDEX：加速查找，可以有多个

唯一索引：主键索引PRIMARY KEY：加速查找+约束（不为空、不能重复）
   

联合索引：多个字段联合起来作为索引
    -PRIMARY KEY(id,name):联合主键索引
    -UNIQUE(id,name):联合唯一索引
    -INDEX(id,name):联合普通索引
```

​	**使用InnoDB存储引擎的时候，每建一个表，就需要给一个主键，是因为这个主键是InnoDB存储引擎的.idb文件来组织存储数据的依据或者说方式，也就是说InnoDB存储引擎在存储数据的时候默认就按照索引的那种树形结构来帮你存。这种索引，我们就称为聚集索引，也就是在聚集数据组织数据的时候，就用这种索引。InnoDB这么做就是为了加速查询效率，因为你经常会遇到基于主键来查询数据的情况，并且通常我们把id字段作为主键，第一点是因为id占用的数据空间不大，第二点是你经常会用到id来查数据。如果你的表有两个字段，一个id一个name，id为主键，当你查询的时候如果where后面的条件是name=多少多少，那么你就没有用到主键给你带来的加速查询的效果（需要主键之外的辅助索引），如果你用where id=多少多少，就会按照我们刚才上面说的哪种树形结构来给你找寻数据了（当然不仅仅有这种树形结构的数据结构类型），能够快速的帮你定位到数据块。这种聚集索引的特点是它会以id字段作为依据，去建立树形结构，但是叶子节点存的是你表中的一条完整记录，一条完整的数据。**



## 1.4 索引操作



```
主键索引:
  创建的时候添加:  
    Create table t1(
      Id int primary key,
    )
    Create table t1(
      Id int,
      Primary key(id)
    )

表创建完了之后添加
	Alter table 表名 add primary key(id)
删除主键索引:
	Alter table 表名 drop primary key;


唯一索引:
  Create table t1(
  	Id int unique,
  )

  Create table t1(
    Id int,
    Unique key uni_name (id)
  )

show create table t1;

表创建好之后添加唯一索引:
	alter table t1 add unique key  uni_name(id);
删除唯一索引:
	Alter table t1 drop index uni_name;

普通索引:
创建:
  Create table t1(
    Id int,
    Index index_name(id)
  )
表创建好之后添加普通索引:  
	Alter table t1 add index index_name(id);
	Create index index_name on t1(id);

删除普通索引:
	Alter table t1 drop index u_name;
	DROP INDEX 索引名 ON 表名字;
```

将上面添加索引的字段变为多个就成了联合索引，例如：

```
联合主键索引
	Create table t1(
      Id int,
      name char(10),
      Primary key(id，name)
    )
联合唯一索引
	Create table t1(
    Id int,
    name char(10),
    Unique key uni_name (id，name)
  )
联合普通索引
	Create table t1(
    Id int,
    name char(10),
    Index index_name(id，name)
  )

创建表完成之后，再添加联合索引的方式和上面的给单个字段添加索引的方式相同。
```



## 1.5 测试索引

### 1.5.1 数据准备



```
#1. 准备表
create table s1(
  id int,
  name varchar(20),
  gender char(6),
  email varchar(50)
);

#2. 创建存储过程，实现批量插入记录，存储过程没什么特别的，将下面的代码到mysql中运行一下就可以了，注意，可能会花费挺长时间，因为数据量比较大，有300万条数据。
delimiter $$ #声明存储过程的结束符号为$$
create procedure auto_insert1()
BEGIN
    declare i int default 1;
    while(i<3000000)do
        insert into s1 values(i,'egon','male',concat('egon',i,'@oldboy'));
        set i=i+1;
    end while;
END$$ #$$结束
delimiter ; #重新声明分号为结束符号

#3. 查看存储过程
show create procedure auto_insert1\G 

#4. 调用存储过程
call auto_insert1();
```



### 1.5.2 测试示例

1. 在没有索引的前提下测试查询速度。

```
mysql> select * from s1 where id=333333333;
Empty set (0.33 sec)
```



​	在表中已经存在大量数据的前提下，为某个字段段建立索引，建立速度会很慢



​	或者用alter table s1 add primary key(id);加主键，建索引很慢的。

![img](https://images2017.cnblogs.com/blog/1036857/201709/1036857-20170913163337125-480382090.png)

​	在索引建立完毕后，以该字段为查询条件时，查询速度提升明显

　　　　![img](https://images2017.cnblogs.com/blog/1036857/201709/1036857-20170913171928047-457783306.png)



### 1.5.3 正确命中索引

​	并不是说我们创建了索引就一定会加快查询速度，若想利用索引达到预想的提高查询速度的效果，我们在添加索引时，必须遵循以下问题

1. 范围问题，或者说条件不明确，条件中出现这些符号或关键字：>、>=、<、<=、!= 、between...and...、like

   **![img](https://images2017.cnblogs.com/blog/1036857/201709/1036857-20170913173142047-877845727.png)**

​	如果你写where id >1 and id <1000000;你会发现，随着你范围的增大，速度会越来越慢，会成倍的体现出来。

2. 尽量选择区分度高的列作为索引,区分度的公式是count(distinct col)/count(\*)，表示字段不重复的比例，比例越大我们扫描的记录数越少，唯一键的区分度是1，而一些状态、性别字段可能在大数据面前区分度就是0。

3. =和in可以乱序，比如a = 1 and b = 2 and c = 3 建立(a,b,c)索引可以任意顺序，mysql的查询优化器会帮你优化成索引可以识别的形式

   ```
   #1、and与or的逻辑
       条件1 and 条件2:所有条件都成立才算成立，但凡要有一个条件不成立则最终结果不成立
       条件1 or 条件2:只要有一个条件成立则最终结果就成立
   
   #2、and的工作原理
       条件：
           a = 10 and b = 'xxx' and c > 3 and d =4
       索引：
           制作联合索引(d,a,b,c)
       工作原理:  #如果是你找的话，你会怎么找，是不是从左到右一个一个的比较啊，首先你不能确定a这个字段是不是有索引，即便是有索引，也不一定能确保命中索引了（所谓命中索引，就是应用上了索引），mysql不会这么笨的，看下面mysql是怎么找的：
           索引的本质原理就是先不断的把查找范围缩小下来，然后再进行处理，对于连续多个and：mysql会按照联合索引，从左到右的顺序找一个区分度高的索引字段(这样便可以快速锁定很小的范围)，加速查询，即按照d—>a->b->c的顺序
   
   #3、or的工作原理
       条件：
           a = 10 or b = 'xxx' or c > 3 or d =4
       索引：
           制作联合索引(d,a,b,c)
           
       工作原理:
           只要一个匹配成功就行，所以对于连续多个or：mysql会按照条件的顺序，从左到右依次判断，即a->b->c->d
   ```

   

4. 索引列不能参与计算，保持列“干净”，比如from_unixtime(create_time) = ’2014-05-29’就不能使用到索引，原因很简单，b+树中存的都是数据表中的字段值，但进行检索时，需要把所有元素都应用函数才能比较，显然成本太大。所以语句应该写成create_time = unix_timestamp(’2014-05-29’)



5. 最左匹配特性(针对联合索引的)

   最左前缀：顾名思义，就是最左优先，上一个博客中数据库我们创建了UNIQUE KEY `uk_device` (`device_id`,`user_id`,`token`)多列索引,相当于创建了(device_id)单列索引，(device_id,user_id)组合索引以及(device_id,user_id,token)组合索引。

   结论是索引键是（a_b_c）seclect * from table where a=' ';以下情况：

   ​	1：a=  可以命中索引，b=  不可以命中索引，c=  不可以命中索引。

   ​	2：a=‘’ and b=‘’可以命中，a=‘’ and c=‘’  可以命中索引。

   ​	3：b=’‘and a=’‘可以命中索引， b=‘‘ and c=’‘  不可以命中索引。

   ​	4：c=’‘ and a=’‘ 可以命中 索引，c=’‘ and  b=’‘不可命中索引。



# 第二节 pymysql

​	我们要学的pymysql就是用来在python程序中如何操作mysql，本质上就是一个套接字客户端，只不过这个套接字客户端是在python程序中用的，既然是客户端套接字，应该怎么用，是不是要连接服务端，并且和服务端进行通信啊，让我们来学习一下pymysql这个模块

## 2.1 安装

```
pip3 install pymysql
```

## 2.2 使用

我们通过一个登陆认证，也就是验证用户名和密码是否在用户表中存在来使用一下pymysql

首先我们创建一个用户表，名为userinfo表，其中有用户名(name)和密码字段(password)，然后在表中存放一些数据。

然后在我们的python脚本中写上以下内容，就可以完成我们的登陆认证了

```
import pymysql
user=input('用户名: ').strip()
pwd=input('密码: ').strip()

#链接，指定ip地址和端口，本机上测试时ip地址可以写localhost或者自己的ip地址或者127.0.0.1，然后你操作数据库的时候的用户名，密码，要指定你操作的是哪个数据库，指定库名，还要指定字符集。不然会出现乱码
conn=pymysql.connect(host='localhost',port=3306,user='root',password='123',database='student',charset='utf8') 

cursor=conn.cursor() #这就想到于mysql自带的那个客户端的游标mysql> 在这后面输入指令，回车执行

sql='select * from userinfo where name="%s" and password="%s"' %(user,pwd) 

res=cursor.execute(sql) #执行sql语句，返回sql查询成功的记录数目，是个数字，是受sql语句影响到的记录行数
#all_data=cursor.fetchall()  #获取返回的所有数据，注意凡是取数据，取过的数据就没有了，结果都是元祖格式的
#many_data=cursor.fetchmany(3) #一下取出3条数据，
#one_data=cursor.fetchone()  #按照数据的顺序，一次只拿一个数据，下次再去就从第二个取了，因为第一个被取出去了，取一次就没有了，结果也都是元祖格式的
if res:
    print('登录成功')
else:
    print('登录失败')

cursor.close() #关闭游标
conn.close()   #关闭连接
```



## 2.3 sql注入

所谓sql注入，就是通过将一些特殊符号写入到我们的sql语句中，使我们的sql语句失去了原有的作用。比如绕开我们的认证机制，在不知道用户名和密码的情况下完成登录。

基于上一节的示例，我们看一下sql注入怎么搞事情的。

以下还是上述示例的代码

```
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='666',
    database='crm',
    charset='utf8'
)

cursor = conn.cursor(pymysql.cursors.DictCursor)
uname = input('请输入用户名：')
pword = input('请输入密码：')

sql = "select * from userinfo where username='%s' and password='%s';"%(uname,pword)

res = cursor.execute(sql) #res我们说是得到的行数，如果这个行数不为零，说明用户输入的用户名和密码存在，如果为0说名存在，你想想对不

print(res) #如果输入的用户名和密码错误，这个结果为0，如果正确，这个结果为1
if res:
    print('登陆成功')
else:
    print('用户名和密码错误！')
```

但是我们来看下面的操作，如果将在输入用户名的地方输入一个 chao'空格然后--空格然后加上任意的字符串，就能够登陆成功，也就是只知道用户名的情况下，他就能登陆成功的情况：

```
uname = input('请输入用户名：')
pword = input('请输入密码：')

sql = "select * from userinfo where username='%s' and password='%s';"%(uname,pword)
print(sql)
res = cursor.execute(sql) #res我们说是得到的行数，如果这个行数不为零，说明用户输入的用户名和密码存在，如果为0说名存在，你想想对不

print(res) #如果输入的用户名和密码错误，这个结果为0，如果正确，这个结果为1
if res:
    print('登陆成功')
else:
    print('用户名和密码错误！')
#运行看结果：居然登陆成功
请输入用户名：chao' -- xxx   
请输入密码：
select * from userinfo where username='chao' -- xxx' and password='';
1
登陆成功

```

我们来分析一下：

```
此时uname这个变量等于什么，等于chao' -- xxx,然后我们来看我们的sql语句被这个字符串替换之后是个什么样子：
	select * from userinfo where username='chao' -- xxx' and password=''; 其中chao后面的这个'，在进行字符串替换的时候，我们输入的是chao',这个引号和前面的引号组成了一对，然后后面--在sql语句里面是注释的意思，也就是说--后面的sql语句被注释掉了。也就是说，拿到的sql语句是select * from userinfo where username='chao';然后就去自己的数据库里面去执行了，发现能够找到对应的记录，因为有用户名为chao的记录，然后他就登陆成功了，但是其实他连密码都不知道，只知道个用户名。。。，他完美的跳过了你的认证环节。
```

然后我们再来看一个例子，直接连用户名和密码都不知道，但是依然能够登陆成功的情况：

```
请输入用户名：xxx' or 1=1 -- xxxxxx
请输入密码：
select * from userinfo where username='xxx' or 1=1 -- xxxxxx' and password='';
3
登陆成功

我们只输入了一个xxx' 加or 加 1=1 加 -- 加任意字符串
看上面被执行的sql语句你就发现了，or 后面跟了一个永远为真的条件，那么即便是username对不上，但是or后面的条件是成立的，也能够登陆成功。
```

出现这样的问题，我们怎么解决的？通过pymysql给我们提供的execute方法可以解决，看示例：

```
之前我们的sql语句是这样写的：
sql = "select * from userinfo where username='%s' and password='%s';"%(uname,pword)

以后再写的时候，sql语句里面的%s左右的引号去掉，并且语句后面的%(uname,pword)这些内容也不要自己写了，按照下面的方式写
sql = "select * from userinfo where username=%s and password=%s;"
难道我们不传值了吗，不是的，我们通过下面的形式，在excute里面写参数：
#cursor.execute(sql,[uname,pword]) ，其实它本质也是帮你进行了字符串的替换，只不过它会将uname和pword里面的特殊字符给过滤掉。

看下面的例子：
uname = input('请输入用户名：') #输入的内容是：chao' -- xxx或者xxx' or 1=1 -- xxxxx
pword = input('请输入密码：')

sql = "select * from userinfo where username=%s and password=%s;"
print(sql)
res = cursor.execute(sql,[uname,pword]) #res我们说是得到的行数，如果这个行数不为零，说明用户输入的用户名和密码存在，如果为0说名存在，你想想对不

print(res) #如果输入的用户名和密码错误，这个结果为0，如果正确，这个结果为1
if res:
    print('登陆成功')
else:
    print('用户名和密码错误！')
#看结果：
请输入用户名：xxx' or 1=1 -- xxxxx
请输入密码：
select * from userinfo where username=%s and password=%s;
0
用户名和密码错误！
```

## 2.4 commit方法

当我们通过pymysql来执行增删改动作的时候，需要commit以下才能生效。

```
sql='insert into userinfo(name,password) values(%s,%s);'
res=cursor.executemany(sql,[("root","123456"),("lhf","12356"),("eee","156")]) #执行sql语句，返回sql影响成功的行数，一次插多条记录
print(res)
#上面的几步，虽然都有返回结果，也就是那个受影响的函数res，但是你去数据库里面一看，并没有保存到数据库里面，
conn.commit() #必须执行conn.commit,注意是conn，不是cursor，执行这句提交后才发现表中插入记录成功，没有这句，上面的这几步操作其实都没有成功保存。
```





# 第三节 DBUtils

DBUtils是Python的一个用于实现数据库连接池的模块。

此连接池有两种连接模式：

模式一：为每个线程创建一个连接，线程即使调用了close方法，也不会关闭，只是把连接重新放到连接池，供自己线程再次使用。当线程终止时，连接自动关闭。

```
POOL = PersistentDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    closeable=False,
    # 如果为False时， conn.close() 实际上被忽略，供下次使用，再线程关闭时，才会自动关闭链接。如果为True时， conn.close()则关闭链接，那么再次调用pool.connection时就会报错，因为已经真的关闭了连接（pool.steady_connection()可以获取一个新的链接）
    threadlocal=None,  # 本线程独享值得对象，用于保存链接对象，如果链接对象被重置
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    database='pooldb',
    charset='utf8'
)

def func():
    conn = POOL.connection(shareable=False)
    cursor = conn.cursor()
    cursor.execute('select * from tb1')
    result = cursor.fetchall()
    cursor.close()
    conn.close()

func()
```



模式二：创建一批连接到连接池，供所有线程共享使用。

PS：由于pymysql、MySQLdb等threadsafety值为1，所以该模式连接池中的线程会被所有线程共享。

```
import time
import pymysql
import threading
from DBUtils.PooledDB import PooledDB, SharedDBConnection
POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=3,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    database='pooldb',
    charset='utf8'
)


def func():
    # 检测当前正在运行连接数的是否小于最大链接数，如果不小于则：等待或报raise TooManyConnections异常
    # 否则
    # 则优先去初始化时创建的链接中获取链接 SteadyDBConnection。
    # 然后将SteadyDBConnection对象封装到PooledDedicatedDBConnection中并返回。
    # 如果最开始创建的链接没有链接，则去创建一个SteadyDBConnection对象，再封装到PooledDedicatedDBConnection中并返回。
    # 一旦关闭链接后，连接就返回到连接池让后续线程继续使用。
    conn = POOL.connection()

    # print(th, '链接被拿走了', conn1._con)
    # print(th, '池子里目前有', pool._idle_cache, '\r\n')

    cursor = conn.cursor()
    cursor.execute('select * from tb1')
    result = cursor.fetchall()
    conn.close()


func()
```

如果没有连接池，使用pymysql来连接数据库时，单线程应用完全没有问题，但如果涉及到多线程应用那么就需要加锁，一旦加锁那么连接势必就会排队等待，当请求比较多时，性能就会降低了。

加锁的情况：

```
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
import threading
from threading import RLock

LOCK = RLock()
CONN = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='123',
                       database='pooldb',
                       charset='utf8')


def task(arg):
    with LOCK:
        cursor = CONN.cursor()
        cursor.execute('select * from tb1')
        result = cursor.fetchall()
        cursor.close()

        print(result)


for i in range(10):
    t = threading.Thread(target=task, args=(i,))
    t.start()
```

不加锁的情况，会报错：

```
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
import threading
CONN = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='123',
                       database='pooldb',
                       charset='utf8')


def task(arg):
    cursor = CONN.cursor()
    cursor.execute('select * from tb1')
    result = cursor.fetchall()
    cursor.close()

    print(result)


for i in range(10):
    t = threading.Thread(target=task, args=(i,))
    t.start()
```



# 本节作业

1. 通过pymysql完成下面表的数据的增长改查

   看表结构。

```
create table t1(
	id int primary key auto_increment,
	name char(10) not null unique,
	age int default 18,
)
```

