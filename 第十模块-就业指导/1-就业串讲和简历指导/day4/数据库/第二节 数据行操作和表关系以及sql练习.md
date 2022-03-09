





# 引入

本节内容我们准备讲一下数据的操作，也就是增删改查，重点在于语法。

在MySQL管理软件中，可以通过SQL语句中的DML语言来实现数据的操作，包括

1. *使用INSERT实现数据的插入*
2. *UPDATE实现数据的更新*
3. *使用DELETE实现数据的删除*
4. *使用SELECT查询数据以及。*

# 第一节 增删改操作



## 1.1 增加

看语法

```
1. 插入完整数据（顺序插入）
    语法一：
    INSERT INTO 表名(字段1,字段2,字段3…字段n) VALUES(值1,值2,值3…值n); #指定字段来插入数据，插入的值要和你前面的字段相匹配

    语法二：
    INSERT INTO 表名 VALUES (值1,值2,值3…值n); #不指定字段的话，就按照默认的几个字段来插入数据

2. 指定字段插入数据
    语法：
    INSERT INTO 表名(字段1,字段2,字段3…) VALUES (值1,值2,值3…);

3. 插入多条记录
    语法：#插入多条记录用逗号来分隔
    INSERT INTO 表名 VALUES
        (值1,值2,值3…值n),
        (值1,值2,值3…值n),
        (值1,值2,值3…值n);
        
4. 插入查询结果
    语法：
    INSERT INTO 表名(字段1,字段2,字段3…字段n) 
                    SELECT (字段1,字段2,字段3…字段n) FROM 表2
                    WHERE …; #将从表2里面查询出来的结果来插入到我们的表中，但是注意查询出来的数据要和我们前面指定的字段要对应好
```



## 1.2 更新

看语法

```
语法：
    UPDATE 表名 SET 
        字段1=值1,  #注意语法，可以同时来修改多个值，用逗号分隔
        字段2=值2,
        WHERE CONDITION; #更改哪些数据，通过where条件来定位到符合条件的数据

示例：
    UPDATE mysql.user SET password=password(‘123’) 
        where user=’root’ and host=’localhost’; #这句话是对myslq这个库中的user表中的user字段为'root'并且host字段为'localhost'的这条记录的password字段的数据进行修改，将passord字段的那个数据改为password('123')这个方法对123加工后的密码数据，password()这个方法是mysql提供的密码进行加密用的方法。
    定位到某个记录，并把这个记录中的某项内容更改掉
```



## 1.3 删除

看语法

```
语法：
    DELETE FROM 表名 
        WHERE CONITION; #删除符合条件的一些记录
    DELETE FROM 表名；如果不加where条件，意思是将表里面所有的内容都删掉，但是清空所有的内容，一般我们用truncate ，能够将id置为零，delete不能将id置零，再插入数据的时候，会按照之前的数据记录的id数继续递增
示例：
    DELETE FROM mysql.user 
        WHERE password=’123’;

练习：
    更新MySQL root用户密码为mysql123
    删除除从本地登录的root用户以外的所有用户
```



# 第二节 单查询操作

　　我们在工作中，多数的场景都是对数据的增删改操作少，读数据的操作多，所以我们的重点就在读取数据这里了。我们先来把单表查询学习一下。

## 2.1 单表查询语法

看语法

```
#查询数据的本质：mysql会到你本地的硬盘上找到对应的文件，然后打开文件，按照你的查询条件来找出你需要的数据。下面是完整的一个单表查询的语法

select * from，这个select * 指的是要查询所有字段的数据。

SELECT distinct 字段1,字段2... FROM 库名.表名 #from后面是说从库的某个表中去找数据，mysql会去找到这个库对应的文件夹下去找到你表名对应的那个数据文件，找不到就直接报错了，找到了就继续后面的操作
                  WHERE 条件       #从表中找符合条件的数据记录，where后面跟的是你的查询条件
                  GROUP BY field（字段）   #分组
                  HAVING 筛选      #过滤，过滤之后执行select后面的字段筛选，就是说我要确定一下需要哪个字段的数据，你查询的字段数据进行去重，然后在进行下面的操作
                  ORDER BY field（字段）   #将结果按照后面的字段进行排序
                  LIMIT 限制条数    #将最后的结果加一个限制条数，就是说我要过滤或者说限制查询出来的数据记录的条数

```

以上语句中关键字的执行顺序

```
1.找到表:from

2.拿着where指定的约束条件，去文件/表中取出一条条记录

3.将取出的一条条记录进行分组group by，如果没有group by，则整体作为一组

4.将分组的结果进行having过滤

5.执行select

6.去重

7.将结果按条件排序：order by

8.限制结果的显示条数
```



**简单查询练习**

先来创建表和插入一些数据

```
#我们来创建一个员工表，然后对员工表进行一个简单的查询，来看一下效果，下面是员工表的字段
company.employee
    员工id      id                  int             
    姓名        emp_name            varchar
    性别        sex                 enum
    年龄        age                 int
    入职日期     hire_date           date
    岗位        post                varchar
    职位描述     post_comment        varchar
    薪水        salary              double
    办公室       office              int
    部门编号     depart_id           int



#创建表
create table employee(
    id int not null unique auto_increment,
    name varchar(20) not null,
    sex enum('male','female') not null default 'male', #大部分是男的
    age int(3) unsigned not null default 28,
    hire_date date not null,
    post varchar(50),
    post_comment varchar(100),
    salary double(15,2),
    office int, #一个部门一个屋子
    depart_id int
);


#查看表结构
mysql> desc employee;
+--------------+-----------------------+------+-----+---------+----------------+
| Field        | Type                  | Null | Key | Default | Extra          |
+--------------+-----------------------+------+-----+---------+----------------+
| id           | int(11)               | NO   | PRI | NULL    | auto_increment |
| name         | varchar(20)           | NO   |     | NULL    |                |
| sex          | enum('male','female') | NO   |     | male    |                |
| age          | int(3) unsigned       | NO   |     | 28      |                |
| hire_date    | date                  | NO   |     | NULL    |                |
| post         | varchar(50)           | YES  |     | NULL    |                |
| post_comment | varchar(100)          | YES  |     | NULL    |                |
| salary       | double(15,2)          | YES  |     | NULL    |                |
| office       | int(11)               | YES  |     | NULL    |                |
| depart_id    | int(11)               | YES  |     | NULL    |                |
+--------------+-----------------------+------+-----+---------+----------------+

#插入记录
#三个部门：教学，销售，运营
insert into employee(name,sex,age,hire_date,post,salary,office,depart_id) values
('egon','male',18,'20170301','老男孩驻沙河办事处外交大使',7300.33,401,1), #以下是教学部，全都是老师
('alex','male',78,'20150302','teacher',1000000.31,401,1),
('wupeiqi','male',81,'20130305','teacher',8300,401,1),
('yuanhao','male',73,'20140701','teacher',3500,401,1),
('liwenzhou','male',28,'20121101','teacher',2100,401,1),
('jingliyang','female',18,'20110211','teacher',9000,401,1),
('jinxin','male',18,'19000301','teacher',30000,401,1),
('成龙','male',48,'20101111','teacher',10000,401,1),

('歪歪','female',48,'20150311','sale',3000.13,402,2),#以下是销售部门
('丫丫','female',38,'20101101','sale',2000.35,402,2),
('丁丁','female',18,'20110312','sale',1000.37,402,2),
('星星','female',18,'20160513','sale',3000.29,402,2),
('格格','female',28,'20170127','sale',4000.33,402,2),

('张野','male',28,'20160311','operation',10000.13,403,3), #以下是运营部门
('程咬金','male',18,'19970312','operation',20000,403,3),
('程咬银','female',18,'20130311','operation',19000,403,3),
('程咬铜','male',18,'20150411','operation',18000,403,3),
('程咬铁','female',18,'20140512','operation',17000,403,3)
;

#ps：如果在windows系统中，插入中文字符，select的结果为空白，可以将所有字符编码统一设置成gbk
```



简单查询练习

```
		查询所有员工的id，姓名年龄
    SELECT id,name,sex,age FROM employee;
    
	  查询所有字段数据
    SELECT * FROM employee; 
    
    查询员工的姓名和工资
    SELECT name,salary FROM employee;
```



### 2.1.1 where条件

​	where语句中可以使用：

​	之前我们用where 后面跟的语句是不是id=1这种类型的啊，用=号连接的，除了=号外，还能使用其他的，看下面：

　　1. 比较运算符：> < >= <= <> !=
　　2. between 80 and 100 值在80到100之间
　　3. in(80,90,100)  值是80或90或100
　　4. like 'egon%'
    　　pattern可以是%或_，

    　　%表示任意多字符
    　　_表示一个字符
　　5. 逻辑运算符：在多个条件直接可以使用逻辑运算符 and or not



**简单操作**

```
#1:单条件查询
    SELECT name FROM employee
        WHERE post='sale';  #注意优先级，我们说where的优先级是不是比select要高啊，所以我们的顺序是先找到这个employee表，然后按照post='sale'的条件，然后去表里面select数据
        
#2:多条件查询
    SELECT name,salary FROM employee 
        WHERE post='teacher' AND salary>10000;

#3:关键字BETWEEN AND 写的是一个区间
    SELECT name,salary FROM employee 
        WHERE salary BETWEEN 10000 AND 20000; #就是salary>=10000 and salary<=20000的数据

    SELECT name,salary FROM employee 
        WHERE salary NOT BETWEEN 10000 AND 20000; #加个not，就是不在这个区间内，薪资小于10000的或者薪资大于20000的，注意没有等于，
    
#4:关键字IS NULL(判断某个字段是否为NULL不能用等号，需要用IS) 判断null只能用is
    SELECT name,post_comment FROM employee 
        WHERE post_comment IS NULL;

    SELECT name,post_comment FROM employee 
        WHERE post_comment IS NOT NULL;
        
    SELECT name,post_comment FROM employee 
        WHERE post_comment=''; 注意''是空字符串，不是null，两个是不同的东西，null是啥也没有，''是空的字符串的意思，是一种数据类型，null是另外一种数据类型
    ps：
        执行
        update employee set post_comment='' where id=2;
        再用上条查看，就会有结果了

#5:关键字IN集合查询
    SELECT name,salary FROM employee 
        WHERE salary=3000 OR salary=3500 OR salary=4000 OR salary=9000 ; #这样写是不是太麻烦了，写一大堆的or，下面我们用in这个简单的写法来搞
    
    SELECT name,salary FROM employee 
        WHERE salary IN (3000,3500,4000,9000) ;

    SELECT name,salary FROM employee 
        WHERE salary NOT IN (3000,3500,4000,9000) ;

#6:关键字LIKE模糊查询，模糊匹配，可以结合通配符来使用
    通配符’%’  #匹配任意所有字符
    SELECT * FROM employee 
            WHERE name LIKE 'eg%';

    通配符’_’  #匹配任意一个字符   
    SELECT * FROM employee 
            WHERE name LIKE 'al__'; #注意我这里写的两个_，用1个的话，匹配不到alex，因为al后面还有两个字符ex。
```

​	where条件咱们就说完了，这个where条件到底怎么运作的，我们来说一下：我们以select id,name,age from employee where id>7;这个语句来说一下

​	首先先找到employee表，找到这个表之后，mysql会拿着where后面的约束条件去表里面找符合条件的数据，然后遍历你表中所有的数据，查看一下id是否大于7，逐条的对比，然后只要发现id比7大的，它就会把这一整条记录给select，但是select说我只拿id、name、age这个三个字段里面的数据，然后就打印了这三个字段的数据，然后where继续往下过滤，看看id是不是还有大于7的，然后发现一个符合条件的就给select一个，然后重复这样的事情，直到把数据全部过滤一遍才会结束。这就是where条件的一个工作方式。

**小练习**

```
1. 查看岗位是teacher的员工姓名、年龄
2. 查看岗位是teacher且年龄大于30岁的员工姓名、年龄
3. 查看岗位是teacher且薪资在9000-1000范围内的员工姓名、年龄、薪资
4. 查看岗位描述不为NULL的员工信息
5. 查看岗位是teacher且薪资是10000或9000或30000的员工姓名、年龄、薪资
6. 查看岗位是teacher且薪资不是10000或9000或30000的员工姓名、年龄、薪资
7. 查看岗位是teacher且名字是jin开头的员工姓名、年薪
```

**答案**

```
select name,age from employee where post = 'teacher';
select name,age from employee where post='teacher' and age > 30; 
select name,age,salary from employee where post='teacher' and salary between 9000 and 10000;
select * from employee where post_comment is not null;
select name,age,salary from employee where post='teacher' and salary in (10000,9000,30000);
select name,age,salary from employee where post='teacher' and salary not in (10000,9000,30000);
select name,salary*12 from employee where post='teacher' and name like 'jin%';
```



### 2.1.2 分组查询GROUP BY



```
1、首先明确一点：分组发生在where之后，即分组是基于where之后得到的记录而进行的

2、分组指的是：将所有记录按照某个相同字段进行归类，比如针对员工信息表的职位分组，或者按照性别进行分组等

3、为何要分组呢？是因为我们有时候会需要以组为单位来统计一些数据或者进行一些计算的，对不对，比方说下面的几个例子
    取每个部门的最高工资  
    取每个部门的员工数
    取男人数和女人数  

    小窍门：‘每’这个字后面的字段，就是我们分组的依据，只是个小窍门，但是不能表示所有的情况，看上面第三个分组，没有'每'字，这个就需要我们通过语句来自行判断分组依据了
    我们能用id进行分组吗，能，但是id是不是重复度很低啊，基本没有重复啊，对不对，这样的字段适合做分组的依据吗？不适合，对不对，依据性别分组行不行，当然行，因为性别我们知道，是不是就两种啊，也可能有三种是吧，这个重复度很高，对不对，分组来查的时候才有更好的意义
　　
4、大前提：
    可以按照任意字段分组，但是分组完毕后，比如group by post，只能查看post字段，如果想查看组内信息，需要借助于聚合函数

注意一点，在查询语句里面select 字段 from 表，这几项是必须要有的，其他的什么where、group by等等都是可有可无的

GROUP BY一般都会与聚合函数一起使用，聚合是什么意思：聚合就是将分组的数据聚集到一起，合并起来搞事情，拿到一个最后的结果。
    
```

**小练习**

```
查询每个岗位的人数
```

**答案**

```
select post,count(id) as count from employee group by post;
#按照岗位分组，并查看每个组有多少人，每个人都有唯一的id号，我count是计算一下分组之后每组有多少的id记录，通过这个id记录我就知道每个组有多少人了
```



### 2.1.3 聚合函数

聚合函数一般配合着分组来用，进行一些统计。

```
    SELECT COUNT(*) FROM employee;  #count是统计个数用的
    SELECT COUNT(*) FROM employee WHERE depart_id=1;  #后面跟where条件的意思是统计一下满足depart_id=1这个的所有记录的个数
    SELECT MAX(salary) FROM employee;  #max（）统计分组后每组的最大值，这里没有写group by，那么就是统计整个表中所有记录中薪资最大的，薪资的值
    SELECT MIN(salary) FROM employee;
    SELECT AVG(salary) FROM employee; #平均值
    SELECT SUM(salary) FROM employee; #总和
    SELECT SUM(salary) FROM employee WHERE depart_id=3;
```

另外在学一个concat()函数：自定义显示格式

```
CONCAT() 函数用于连接字符串
```

示例：

```
SELECT CONCAT('姓名: ',name,'  年薪: ', salary*12)  AS Annual_salary  #我想让name这个字段显示的字段名称是中文的姓名，让salary*12显示的是中文的年薪，
   FROM employee;#看结果：通过结果你可以看出，这个concat就是帮我们做字符串拼接的，并且拼接之后的结果，都在一个叫做Annual_salary的字段中了
　　　　+---------------------------------------+
　　　　| Annual_salary |
　　　　+---------------------------------------+
　　　　| 姓名: egon 年薪: 87603.96 |
　　　　| 姓名: alex 年薪: 12000003.72 |
　　　　| 姓名: wupeiqi 年薪: 99600.00 |
　　　　| 姓名: yuanhao 年薪: 42000.00 |

　　　　.....

       +---------------------------------------+
```



**小练习**

```4
1. 查询岗位名以及各岗位内包含的员工个数
2. 查询公司内男员工和女员工的个数
3. 查询岗位名以及各岗位的平均薪资
4. 查询岗位名以及各岗位的最高薪资
5. 查询岗位名以及各岗位的最低薪资
6. 查询男员工与男员工的平均薪资，女员工与女员工的平均薪资。 #这道题我们自己提炼一下分组依据，是不是就是性别啊
```

**答案**

```
#题目1：
mysql> select post,count(id) from employee group by post;
+-----------------------------------------+-----------+
| post                                    | count(id) |
+-----------------------------------------+-----------+
| operation                               |         5 |
| sale                                    |         5 |
| teacher                                 |         7 |
| 老男孩驻沙河办事处外交大使              |         1 |
+-----------------------------------------+-----------+


#题目2：
mysql> select sex,count(id) from employee group by sex;
+--------+-----------+
| sex    | count(id) |
+--------+-----------+
| male   |        10 |
| female |         8 |
+--------+-----------+

#题目3：
mysql> select post,avg(salary) from employee group by post;
+-----------------------------------------+---------------+
| post                                    | avg(salary)   |
+-----------------------------------------+---------------+
| operation                               |  16800.026000 |
| sale                                    |   2600.294000 |
| teacher                                 | 151842.901429 |
| 老男孩驻沙河办事处外交大使              |   7300.330000 |
+-----------------------------------------+---------------+

#题目4：
mysql> select post,max(salary) from employee group by post;
+-----------------------------------------+-------------+
| post                                    | max(salary) |
+-----------------------------------------+-------------+
| operation                               |    20000.00 |
| sale                                    |     4000.33 |
| teacher                                 |  1000000.31 |
| 老男孩驻沙河办事处外交大使              |     7300.33 |
+-----------------------------------------+-------------+

#题目5：
mysql> select post,min(salary) from employee group by post;
+-----------------------------------------+-------------+
| post                                    | min(salary) |
+-----------------------------------------+-------------+
| operation                               |    10000.13 |
| sale                                    |     1000.37 |
| teacher                                 |     2100.00 |
| 老男孩驻沙河办事处外交大使              |     7300.33 |
+-----------------------------------------+-------------+

#题目6：
mysql> select sex,avg(salary) from employee group by sex;
+--------+---------------+
| sex    | avg(salary)   |
+--------+---------------+
| male   | 110920.077000 |
| female |   7250.183750 |
+--------+---------------+
```



### 2.1.4 HAVING过滤

​	讲having之前，我们补充一个点：之前我们写的查询语句是这样的：select id,name from employee;实际上我们在select每个字段的时候，省略了一个表名，有的人可能会这样写，select employee.id,employee.name from employee;你会发现查询出来的结果是一样的，但是如果你要将查询出来的结果表，起一个新表名的话，带着表名这样写就错了

```
　select employee.id,employee.name from employee as tb1;这样执行会下面的报错：

　mysql> select employee.id,employee.name from employee as tb1;
　ERROR 1054 (42S22): Unknown column 'employee.id' in 'field list'
```

 

​	因为这个语句先执行的是谁啊，是不是我们的from啊，那么后面的as也是比select要先执行的，所以你先将表employee起了个新名字叫做tb1，然后在tb1里面取查询数据，那么tb1里面找不到employee.id这个字段，就会报错，如果我们查询的时候不带表名，你as来起一个新的表名也是没问题的，简单提一下这个内容，知道就好了

　　

**HAVING与WHERE不一样的地方在于!!!!!!**

```
having的语法格式和where是一模一样的，只不过having是在分组之后进行的进一步的过滤，where不能使用聚合函数，having是可以使用聚合函数的

执行优先级从高到低：where > group by > having 

1. Where 发生在分组group by之前，因而Where中可以有任意字段，但是绝对不能使用聚合函数。
2. Having发生在分组group by之后，因而Having中可以使用分组的字段，无法直接取到其他字段,having是可以使用聚合函数
```

**简单测试**

```
统计各部门年龄在30岁及以上的员工的平均薪资，并且保留平均工资大于10000的部门
答案：select post,avg(salary) as new_sa from employee where age>=30 group by post having avg(salary) > 10000;
看结果：
　　+---------+---------------+
　　| post | new_sa |
　　+---------+---------------+
　　| teacher | 255450.077500 |
　　+---------+---------------+
　　1 row in set (0.00 sec)

然后我们看这样一句话：select * from employee having avg(salary) > 10000;
只要一运行就会报错：
	mysql> select * from employee having avg(salary) > 10000;
	ERROR 1140 (42000): Mixing of GROUP columns (MIN(),MAX(),COUNT(),...) with no GROUP columns is illegal if there is no GROUP BY clause

是因为having只能在group by后面运行
```

**小练习**

```
1. 查询各岗位内包含的员工个数小于2的岗位名、岗位内包含员工名字、个数
3. 查询各岗位平均薪资大于10000的岗位名、平均工资
4. 查询各岗位平均薪资大于10000且小于20000的岗位名、平均工资
```

**答案**

```
#题1：
mysql> select post,group_concat(name),count(id) from employee group by post having count(id) < 2;
+-----------------------------------------+--------------------+-----------+
| post                                    | group_concat(name) | count(id) |
+-----------------------------------------+--------------------+-----------+
| 老男孩驻沙河办事处外交大使              | egon               |         1 |
+-----------------------------------------+--------------------+-----------+

#题目2：
mysql> select post,avg(salary) from employee group by post having avg(salary) > 10000;
+-----------+---------------+
| post      | avg(salary)   |
+-----------+---------------+
| operation |  16800.026000 |
| teacher   | 151842.901429 |
+-----------+---------------+

#题目3：
mysql> select post,avg(salary) from employee group by post having avg(salary) > 10000 and avg(salary) <20000;
+-----------+--------------+
| post      | avg(salary)  |
+-----------+--------------+
| operation | 16800.026000 |
+-----------+--------------+
```

### 2.1.5 **去重distinct** 

​	将查询的结果进行去重：select distinct post from employee; 注意distinct去重要写在查询字段的前面，不然会报错，关于distinct使用时的其他问题看下面的总结

```
有时需要查询出某个字段不重复的记录，这时可以使用mysql提供的distinct这个关键字来过滤重复的记录，但是实际中我们往往用distinct来返回不重复字段的条数（count(distinct id)）,其原因是distinct只能返回他的目标字段，而无法返回其他字段，distinct 想写在其他字段后面需要配合聚合函数来写。

mysql> select id,count(distinct post) from employee;
ERROR 1140 (42000): Mixing of GROUP columns (MIN(),MAX(),COUNT(),...) with no GROUP columns is illegal if there is no GROUP BY clause
报错了：是因为distinct不能返回其他的字段，只能返回目标字段
mysql> select count(distinct post) from employee;
+----------------------+
| count(distinct post) |
+----------------------+
|                    4 |
+----------------------+
1 row in set (0.00 sec)
```



### 2.1.6 排序ORDER BY

直接看示例吧

```
按单列排序
    SELECT * FROM employee ORDER BY salary; #默认是升序排列
    SELECT * FROM employee ORDER BY salary ASC; #升序
    SELECT * FROM employee ORDER BY salary DESC; #降序
    
按多列排序
但是你看，如果我们按照age来排序，你看看是什么效果：
mysql> SELECT * FROM employee ORDER BY age;
+----+------------+--------+-----+------------+-----------------------------------------+--------------+------------+--------+-----------+
| id | name | sex | age | hire_date | post | post_comment | salary | office | depart_id |
+----+------------+--------+-----+------------+-----------------------------------------+--------------+------------+--------+-----------+
| 1 | egon | male | 18 | 2017-03-01 | 老男孩驻沙河办事处外交大使 | NULL | 7300.33 | 401 | 1 |
| 17 | 程咬铜 | male | 18 | 2015-04-11 | operation | NULL | 18000.00 | 403 | 3 |
| 16 | 程咬银 | female | 18 | 2013-03-11 | operation | NULL | 19000.00 | 403 | 3 |
| 15 | 程咬金 | male | 18 | 1997-03-12 | operation | NULL | 20000.00 | 403 | 3 |
| 12 | 星星 | female | 18 | 2016-05-13 | sale | NULL | 3000.29 | 402 | 2 |
| 11 | 丁丁 | female | 18 | 2011-03-12 | sale | NULL | 1000.37 | 402 | 2 |
| 18 | 程咬铁 | female | 18 | 2014-05-12 | operation | NULL | 17000.00 | 403 | 3 |
| 7 | jinxin | male | 18 | 1900-03-01 | teacher | NULL | 30000.00 | 401 | 1 |
| 6 | jingliyang | female | 18 | 2011-02-11 | teacher | NULL | 9000.00 | 401 | 1 |
| 13 | 格格 | female | 28 | 2017-01-27 | sale | NULL | 4000.33 | 402 | 2 |
| 14 | 张野 | male | 28 | 2016-03-11 | operation | NULL | 10000.13 | 403 | 3 |
| 5 | liwenzhou | male | 28 | 2012-11-01 | teacher | NULL | 2100.00 | 401 | 1 |
| 10 | 丫丫 | female | 38 | 2010-11-01 | sale | NULL | 2000.35 | 402 | 2 |
| 9 | 歪歪 | female | 48 | 2015-03-11 | sale | NULL | 3000.13 | 402 | 2 |
| 8 | 成龙 | male | 48 | 2010-11-11 | teacher | NULL | 10000.00 | 401 | 1 |
| 4 | yuanhao | male | 73 | 2014-07-01 | teacher | NULL | 3500.00 | 401 | 1 |
| 2 | alex | male | 78 | 2015-03-02 | teacher | NULL | 1000000.31 | 401 | 1 |
| 3 | wupeiqi | male | 81 | 2013-03-05 | teacher | NULL | 8300.00 | 401 | 1 |
+----+------------+--------+-----+------------+-----------------------------------------+--------------+------------+--------+-----------+

  发现什么，按照年龄来升序排的，没问题，但是你看年龄相同的那些按什么排的，是不是看着是乱的啊，但是不管它对这种相同数据的内容怎么排序，我们是不是想如果出现相同的数据，那么这些相同的数据也按照一个依据来排列啊：

  所以我们可以给相同的这些数据指定一个排序的依据，看下面：
按多列排序:先按照age升序，如果年纪相同，则按照薪资降序
    SELECT * from employee
        ORDER BY age, #注意排序的条件用逗号分隔
        salary DESC;
```

**小练习**

```
1. 查询所有员工信息，先按照age升序排序，如果age相同则按照hire_date降序排序
2. 查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资升序排列
3. 查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资降序排列
```

**答案**

```
题目1
mysql> select * from employee ORDER BY age asc,hire_date desc;

题目2 
mysql> select post,avg(salary) from employee group by post having avg(salary) > 10000 order by avg(salary) asc;
#注意：查询语句的语法是固定上面这样写的，但是运行顺序是这样的：1、from  2、where  3、group by  4、having  5、select  6、distinct 7、order by  8、limit，我们下面要学的
+-----------+---------------+
| post      | avg(salary)   |
+-----------+---------------+
| operation |  16800.026000 |
| teacher   | 151842.901429 |
+-----------+---------------+

题目3
mysql> select post,avg(salary) from employee group by post having avg(salary) > 10000 order by avg(salary) desc;
+-----------+---------------+
| post      | avg(salary)   |
+-----------+---------------+
| teacher   | 151842.901429 |
| operation |  16800.026000 |
+-----------+---------------+
```

### 2.1.7 限制查询的记录数LIMIT

直接看示例吧

```

　　#取出工资最高的前三位
    SELECT * FROM employee ORDER BY salary DESC LIMIT 3;   #默认初始位置为0,从第一条开始顺序取出三条 
    
    SELECT * FROM employee ORDER BY salary DESC LIMIT 0,5; #从第0开始，即先查询出第一条，然后包含这一条在内往后查5条 

    SELECT * FROM employee ORDER BY salary DESC LIMIT 5,5; #从第5开始，即先查询出第6条，然后包含这一条在内往后查5条
```



### 2.1.8 正则表达式查询

看示例

```
#之前我们用like做模糊匹配，只有%和_，局限性比较强，所以我们说一个正则，之前我们是不是学过正则匹配，你之前学的正则表达式都可以用，正则是通用的
SELECT * FROM employee WHERE name REGEXP '^ale';

SELECT * FROM employee WHERE name REGEXP 'on$';

SELECT * FROM employee WHERE name REGEXP 'm{2}';


小结：对字符串匹配的方式
WHERE name = 'egon';
WHERE name LIKE 'yua%';
WHERE name REGEXP 'on$';
```



**练习**

```
查看所有员工中名字是jin开头，n或者g结果的员工信息
```

**答案**

```
select * from employee where name regexp '^jin.*[g|n]$';
```





# 第三节 表关系

我们知道，将来我们存的数据表肯定不止一个，并且很多表之间是有关系的，那么到底有什么关系呢，我们来看看。

简单举个例子：(重点理解一下什么是foreign key)

员工信息表有三个字段：工号  姓名  部门

公司有3个部门，但是有1个亿的员工，那意味着部门这个字段需要重复存储，部门名字越长，越浪费

那这就体现出来了三个缺点：

​	1.表的组织结构不清晰：员工的信息、部门的信息等等都掺在一张表里面。

​	2.浪费空间，每一条信息都包含员工和部门，多个员工从属一个部门，也需要每个员工的信息里都包含着部门的信息，浪费硬盘空间。

​	3.扩展性极差：如果想修改一个部门的信息，比如修改部门名称，那么这个包含员工和部门信息的表中的所有的包含这个部门信息的数据都需要进行修改，那么修改起来就非常麻烦，这是非常致命的缺点。

​	解决方法：（画一个excel表格来表示一下效果~~）

​	我们完全可以定义一个部门表，解耦和

​	我们虽然将部门表提出来了，但是员工表本身是和部门有联系的，你光把部门信息提出来还是不够的，还需要建立关联

​	然后让员工信息表关联该表，如何关联，即foreign key　

​	　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120134926941-1019804865.png)

 

​	在解释一下：数据要拆到不同表里面存着，你要站在两个表的角度来看两者之间的关系，你站在部门表的角度看，一个部门包含多个员工，站在员工表看，多个员工属于一个部门，以我们上课来举个例子看：现在的多个老师可以讲一个课程python，那么老师对于课程表来说就是多对一个关系，那这是不是就是最终关系呢，我们还需要站在课程表的角度来看，多个课程能不能被一个老师教啊，这个看业务场景，你看咱们学校就不行，讲python的只能讲python，但是我们上的小学，初中，高中是不是多个课程可以被一个老师教啊，所以从老男孩的业务来看，课程表对老师表是一对一的，即便是你多个老师可以讲这一门课程，但是这一门可能对应的那几个老师只能讲这一门，不能讲其他的课程，所以他们只是单纯的多对一的关系，多个老师对应一门课程，但是小学、初中、高中的业务，多个老师可以教一门课程，同样这多个老师每个老师又可以教多门课程，那么从课程表角度来看，多个课程也能从属一个老师，所以是多对多的关系：看下图

　　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120140818625-1670827769.png)





### 一对多的关系　

​	我们在看看员工和部门这个多对一的关系表：

　　　　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120144851634-1641860170.png)

​	如果我们没有做强制的约束关系，那么在员工表里面那个部门id可以随便写，即便是部门表里面没有这个id号，它也是可以写的，但是这样写就错了，因为业务不允许，并且这个数据完全没用，根本就不存在这个部门，哪里来的这个部门的员工呢，对不对，所以要做一个硬性的关系，你员工里面的部门id一定要来自于部门表的id字段。怎么来做这个硬性关系呢，通过外键foreign key，怎么叫外键，就是跟外部的一个表进行关联，建立这种硬性的关系，就叫做外键，就像我们上面这两个表似的，左边的员工表有一个字段(部门id字段)来自于右边的部门表，那么我们就可以通过数据库在员工表的部门id字段加上一个foreign key，外键关联到右边部门表的id字段，这样就建立了这种硬性的关系了，之前我们是看着两张表之间有关系，但是没有做强制约束，还是两张普通的表，操作其中任何一个，另外一个也没问题，但是加上了这种强制关系之后，他们两个的操作也就都关联起来了，具体操作看下面的代码：

　　　　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120151602446-643961969.png)

 

​	部门表是被关联的表，员工表是关联表，也就是员工表要关联部门表，对吧，如果我们先创建员工表，在创建员工表的时候加外键关系，就会报错，看效果：

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120152533625-1565302510.png)

​	所以我们应该先建立部门表，也就是被关联的表，因为关联表中的字段的数据是来根据被关联表的被关联字段的数据而来的。

 　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120152712430-25536712.png)

​	然后看一下表结构：

　　　　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120152905752-1329526259.png)

​	表创建好了，如果我们直接给员工表插入几条数据，那么会报错，因为，你的部门还没有呢，你的员工表里面的那个dep_id外键字段的数据从何而来啊？看效果：

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120153111250-1169885498.png)

​	然后我们先插入部门的数据，然后再插入员工的数据：

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120153240961-1689722900.png)

​	然后查看一下数据：

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120153315045-1186082443.png)

​	数据没问题了，但是你有没有发现一个问题，就是员工表的id从6开始的，因为我们前面插入了5条数据，失败了，虽然失败了，但是id自动增长了。

​	所以有引出一个问题，如果想让id从头开始，我们可以把这些数据删掉，用delete的删除是没用的，需要用truncate来删除，这是清空表的意思。

​	看一下delete：

 　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120153554703-1406210070.png)

​	delete不是用来清空表的，是用来删除一些你想删除的符合某些条件的数据，一般用在delete from tb1 where id>20；这样的，如果要清空表，让id置零，使用truncate

​	再看一下truncate：

​	![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120154024721-179214293.png)

​	然后查看一下数据看看：

​	![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120154051601-284934776.png)



​	我们来看一下，如果对关联的表进行修改的话会有什么效果，首先我们先修改一下部门表的id字段中的某个数据，将id的值改一下

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120154500902-1514552894.png)

​	报错了，那我们改一改员工表里面的外键字段dep_id，改它的值来试试：

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120154652114-761405114.png)

​	还是报错了！我靠，那我试试删除一下试试，解散一个部门，删除他的数据：

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120154736474-1820083889.png)

​	报错了！不让你删除，因为你删除之后，员工表里面的之前属于这个部门的记录找不到对应的部门id了，就报错了

​	那我删除一下员工表里面关于这个要被解散的部门的员工数据，按理说是不是应该没问题啊，来看看效果：

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120155057295-1099231759.png)

​	删除成功了，完全没问题啊，那么关于这个部门的所有员工数据都被删除了，也就是说，你这个部门下面没有任何员工了，没有了限制了相当于，所以我们尝试一下看看现在能不能删除部门表里面的这个部门了

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120155259498-1676374078.png)

​	ok~可以删除了

​	虽然我们修改部门表或者员工表里面的部门id，但是我们可以删除，但是删除这个被关联表部门表的数据的时候由于有关联关系的存在，所以删除的时候也很麻烦，要先将关联数据删除，才能删除被关联的表的数据。

​	刚才我们删除了教学部这个部门，当我们想解散这个部门的时候，首先想到的是什么，是不是我们的部门表，想直接操作部门表进行删除，对吧，想修改部门的id号，是不是首先想到的也是操作部门表进行修改，把部门的id修改了，但是我们由于关联关系的存在，不得不考虑关联表中的数据，对不对，所以操作就变得很麻烦了，有没有简单的方法呢？我们想做的是不是说，我想删除一个部门，直接删除部门表里面的数据就行了，是不是达到这个效果，删除一个部门的时候，与这个部门关联的所有的员工表的那些数据都跟着删除，或者我更新部门表中一个部门的id号，那么关联的员工表中的关联字段的部门id号跟着自动更新了，

 　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120160841065-272740197.png)

　　

​	看一下解决办法：

​	首先我们把之前的两个表删除了，能先删除部门表吗？如果删了部门表，你的员工表是不是找不到对应关系了，你说会不会报错啊，所以先删除员工表：

​	1.先删除关联表，再删除被关联表，然后我们重新建立两个表，然后建表的时候说一下咱们的解决方案。

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120161230284-1451777591.png)

 

​	2.重建表，我们现在要解决的问题是：我们要达到一个在做某个表(被关联表)更新或者删除操作的时候，关联表的数据同步的进行更新和删除的效果，所以我们在建表的时候，可以加上两个功能：同步更新和同步删除：看看如何实现：在建立关联关系的时候，加上这两句： on delete cascade和 on update cascade

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120162027140-391143965.png)

​	然后把我们之间的表和数据都插入进去：然后再进行更新删除操作：

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120162127654-2145260854.png)

 

​	然后我们再直接删除部门表里面的数据的时候，你看看结果：

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120162232053-2012516333.png)

​	成功了，并且员工表里面关联部门表id的数据也都删除了，是不是达到了我们刚才想要实现的效果呀

​	下面我们来看一下更新操作，我们之前说更新一个部门的id号，注意一个问题昂，我更新部门的名称，你说有影响吗？肯定没有啊，因为我员工表并不是关联的部门的名称字段，而是关联的部门的id字段，你改部门名称没关系，我通过你的id照样找到你，但是你如果改了id号，那么我员工表里面的id号和你不匹配了，我就没法找到你，所有当你直接更新部门的id的时候，我就给你报错了，大哥，你想改的是关联字段啊，考虑一下关联表的数据们的感受行不行。我们来看一下加上 on update cascade之后的效果：

 　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120162743120-1025924790.png)

​	将部门id为2的部门的id改成了200，完全ok，员工表里面之前关联id为2的部门的数据都改成了关联id为200的数据了。说明同步更新也是没问题的。

 

 　**我们总结一下foreign key的下面几个约束作用：**

```
1、先要建立被关联的表才能建立关联表

2、在插入数据记录的时候，要先想被关联表中插入数据，才能往关联表里面插入数据

3、更新或者删除数据的时候，都需要考虑关联表和被关联表的关系

解决方案：

  a.删除表的时候，先删除关联表，再删除被关联表
  b.重建表的时候，在加外键关联的时候加上这两句：on delete cascade 和 on update cascade
```

　　　　

**简单测试**

```
表类型必须是innodb存储引擎，且被关联的字段，即references指定的另外一个表的字段，必须保证唯一
create table department(
id int primary key,
name varchar(20) not null
)engine=innodb;

#dpt_id外键，关联父表（department主键id），同步更新，同步删除
create table employee(
id int primary key,
name varchar(20) not null,
dpt_id int,
constraint fk_name foreign key(dpt_id) #这句话的意思是constraint 是声明我们要建立一个约束啦，fk_name是约束的名称，foreign key是约束的类型，整体的意思是，我要创建一个名为fk_name的外键关联啦，这个constraint就是一个声明的作用，在创建外键的时候不加constraint fk_name也是没问题的。先理解一下就行了，后面我们会细讲的。
references department(id)
on delete cascade
on update cascade 
)engine=innodb;


#先往父表department中插入记录
insert into department values
(1,'欧德博爱技术有限事业部'),
(2,'艾利克斯人力资源部'),
(3,'销售部');


#再往子表employee中插入记录
insert into employee values
(1,'chao',1),
(2,'alex1',2),
(3,'alex2',2),
(4,'alex3',2),
(5,'李坦克',3),
(6,'刘飞机',3),
(7,'张火箭',3),
(8,'林子弹',3),
(9,'加特林',3)
;


#删父表department，子表employee中对应的记录跟着删
mysql> delete from department where id=3;
mysql> select * from employee;
+----+-------+--------+
| id | name  | dpt_id |
+----+-------+--------+
|  1 | chao  |      1 |
|  2 | alex1 |      2 |
|  3 | alex2 |      2 |
|  4 | alex3 |      2 |
+----+-------+--------+


#更新父表department，子表employee中对应的记录跟着改
mysql> update department set id=22222 where id=2;
mysql> select * from employee;
+----+-------+--------+
| id | name  | dpt_id |
+----+-------+--------+
|  1 | chao  |      1 |
|  3 | alex2 |  22222 |
|  4 | alex3 |  22222 |
|  5 | alex1 |  22222 |
+----+-------+--------+
```



### **多对多的关系**

我们上面大致提了一下多对多的关系，下面我们通过一个例子来细讲一下，这个例子就用-->书和出版社的关系来看吧：

　　　　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120171740684-1420625094.png)

​	上面是一对多没问题，我们再来看看书和作者的关系：

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120171943958-248866141.png)

​	一本书可以有多个作者，一个作者可不可以写多本书，两者之间是不是站在谁的角度去看都是一个一对多的关系啊，那这就是多对多的关系，那我们创建表的时候，需要将两个表都加一个foreign key的字段，但是你添加字段的时候，你想想，能直接给两个表都这一个foreign key字段吗，两个谁先创建，谁后创建，是不是都不行啊，两个表的创建是不是都依赖着另外一张表啊，所以我们之前的加外键字段的方式对于这种多对多的关系是不是就不好用啦，怎么办，我们需要通过第三张表来缓和一下两者的关系，通过第三张表来创建双方的关系

​	我们先创建书表和作者表，然后创建第三张表，第三张表就需要有一个字段外键关联书表，还有一个字段外键关联作者表

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120172905486-41616144.png)

​	然后我们如果想查一下alex出了哪些书，你可以怎么查，想一下，首先在author作者表里面找一个alex的id是多少，alex的id为2，然后找一个第三张表里面author_id为2的数据中book的id，然后拿着这些book的id去book表里面找对应的book名称，你就能够知道alex这个作者出了哪几本书了，对不对，这就是一个多表查询的一个思路

​	来我们创建一下试试看（学了foreign key，这个东西是不是很简单啊，两个foreign key嘛~~）

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120173957460-1521536555.png)

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120174227313-2029106582.png)

​	建立前两张表，插入数据，建立第三张表

​	然后给第三张表插入一些数据：

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120174348982-440298530.png)

​	查看一下数据：

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120174408928-1564991357.png)

数据就创建好了，多对多就讲完了



### **一对一关系**

​	我们来以咱们学校的学生来举例：

​	最开始你只是一个客户，可能还处于咨询考虑的阶段，还没有转化为学生，也有的客户已经转换为学生了，说白了就是你交钱了，哈哈

​	那我们来建两个表：客户表和学生表

　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120190209104-630390523.png)

​	客户表里面存着客户的信息，学生表里面存着客户转换为学生之后的学生信息，那么这两个表是什么关系呢？你想一下，学生是不是从客户转换过来的，那么一个学生能对应多个用户的信息吗？当然是不能的，那么一个客户能对应多个学生的信息吗，当然也是不能的，那么他们两个就是一对一的关系，那这个关系该怎么建立呢？我们知道通过外键可以建立关系，如果在客户表里面加外键关联学生表的话，那说明你的学生表必须先被创建出来，这样肯定是不对的，因为你的客户表先有的，才能转换为学生，那如果在学生表加外键关联客户表的话，貌似是可以的，不过一个学生只对应一个客户，那么这个关系怎么加呢，外键我们知道是一对多的，那怎么搞？我们可以把这个关联字段设置成唯一的，不就可以了吗，我既和你有关联，我还不能重复，那就做到了我和你一对一的关联关系。

　　　　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181120191244240-594088333.png)



**表关系总结**

```
分析步骤：
#1、先站在左表的角度去找
是否左表的多条记录可以对应右表的一条记录，如果是，则证明左表的一个字段foreign key 右表一个字段（通常是id）

#2、再站在右表的角度去找
是否右表的多条记录可以对应左表的一条记录，如果是，则证明右表的一个字段foreign key 左表一个字段（通常是id）

#3、总结：
#多对一：
如果只有步骤1成立，则是左表多对一右表
如果只有步骤2成立，则是右表多对一左表

#多对多
如果步骤1和2同时成立，则证明这两张表时一个双向的多对一，即多对多,需要定义一个这两张表的关系表来专门存放二者的关系

#一对一:
如果1和2都不成立，而是左表的一条记录唯一对应右表的一条记录，反之亦然。这种情况很简单，就是在左表foreign key右表的基础上，将左表的外键字段设置成unique即可
```



### 外键约束的模式

```
外键约束有三种约束模式（都是针对父表的约束）：

模式一： district 严格约束（默认的 ），父表不能删除或者更新已经被子表数据引用的记录

模式二：cascade 级联模式：父表的操作，对应的子表关联的数据也跟着操作 。

模式三：set null：置空模式，父表操作之后，子表对应的数据（外键字段）也跟着被置空。

通常的一个合理的约束模式是：删除的时候子表置空；更新的时候子表级联。

指定模式的语法：foreign key(外键字段)references 父表(主键字段)on delete 模式 on update 模式;

注意：删除置空的前提条件是 外键字段允许为空，不然外键会创建失败。

外键虽然很强大，能够进行各种约束，但是外键的约束降低了数据的可控性和可拓展性。通常在实际开发时，很少使用外键来约束。
```



# 第四节 多表操作

在企业中其实很多时候都不会加上foreign key外键约束的，因为操作起来有很多限制的地方，我们在上面的操作中已经看到了，所以企业中有两种方式，一种加外键，一种不加外键，但是不管加不加外键，我们下面要进行的多表操作，都是可以的。下面的多表操作讲解，我们以无外键，也就是不加foreign key的方式来进行多表之间的数据操作。

首先说一下，我们写项目一般都会建一个数据库，那数据库里面是不是存了好多张表啊，不可能把所有的数据都放到一张表里面，肯定要分表来存数据，这样节省空间，数据的组织结构更清晰，解耦和程度更高，但是这些表本质上是不是还是一个整体啊，是一个项目所有的数据，那既然分表存了，就要涉及到多个表连接查询了，比如说员工信息一张表，部门信息一张表，那如果我想让你帮我查一下技术部门有哪些员工的姓名，你怎么办，单独找员工表能实现吗，不能，单独找部门表也无法实现，因为部门表里面没有员工的信息，对不对，所以就涉及到部门表和员工表来关联到一起进行查询了，好，那我们来建立这么两张表：

**表和数据准备**

```
#建表
#部门表
create table department(
id int,
name varchar(20) 
);

#员工表，之前我们学过foreign key，强行加上约束关联，但是我下面这个表并没有直接加foreign key，这两个表我只是让它们在逻辑意义上有关系，并没有加foreign key来强制两表建立关系，为什么要这样搞，是有些效果要给大家演示一下
#所以，这两个表是不是先建立哪个表都行啊，如果有foreign key的话，是不是就需要注意表建立的顺序了。那我们来建表。
create table employee(
id int primary key auto_increment,
name varchar(20),
sex enum('male','female') not null default 'male',
age int,
dep_id int
);

#给两个表插入一些数据
insert into department values
(200,'技术'),
(201,'人力资源'),
(202,'销售'),
(203,'运营'); #注意这一条数据，在下面的员工表里面没有对应这个部门的数据

insert into employee(name,sex,age,dep_id) values
('egon','male',18,200),
('alex','female',48,201),
('wupeiqi','male',38,201),
('yuanhao','female',28,202),
('liwenzhou','male',18,200),
('jingliyang','female',18,204) #注意这条数据的dep_id字段的值，这个204，在上面的部门表里面也没有对应的部门id。所以两者都含有一条双方没有涉及到的数据，这都是为了演示一下效果设计的昂
;


#查看表结构和数据
mysql> desc department;
+-------+-------------+------+-----+---------+-------+
| Field | Type | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id | int(11) | YES | | NULL | |
| name | varchar(20) | YES | | NULL | |
+-------+-------------+------+-----+---------+-------+

mysql> desc employee;
+--------+-----------------------+------+-----+---------+----------------+
| Field | Type | Null | Key | Default | Extra |
+--------+-----------------------+------+-----+---------+----------------+
| id | int(11) | NO | PRI | NULL | auto_increment |
| name | varchar(20) | YES | | NULL | |
| sex | enum('male','female') | NO | | male | |
| age | int(11) | YES | | NULL | |
| dep_id | int(11) | YES | | NULL | |
+--------+-----------------------+------+-----+---------+----------------+

mysql> select * from department;
+------+--------------+
| id | name |
+------+--------------+
| 200 | 技术 |
| 201 | 人力资源 |
| 202 | 销售 |
| 203 | 运营 |
+------+--------------+

mysql> select * from employee;
+----+------------+--------+------+--------+
| id | name | sex | age | dep_id |
+----+------------+--------+------+--------+
| 1 | egon | male | 18 | 200 |
| 2 | alex | female | 48 | 201 |
| 3 | wupeiqi | male | 38 | 201 |
| 4 | yuanhao | female | 28 | 202 |
| 5 | liwenzhou | male | 18 | 200 |
| 6 | jingliyang | female | 18 | 204 |
+----+------------+--------+------+--------+
```



## 4.1 笛卡尔积

当我们直接select多张表的时候，就会出现一个笛卡尔积现象，看示例

```
mysql> select * from department,employee; #表用逗号分隔，看我查询时表的顺序，先department后employee，所以你看结果表的这些字段，是不是就是我们两个表字段并且哪个表在前面，哪个表的字段就在前面
+------+--------------+----+------------+--------+------+--------+
| id   | name         | id | name       | sex    | age  | dep_id |
+------+--------------+----+------------+--------+------+--------+
|  200 | 技术         |  1 | egon       | male   |   18 |    200 |
|  201 | 人力资源     |  1 | egon       | male   |   18 |    200 |
|  202 | 销售         |  1 | egon       | male   |   18 |    200 |
|  203 | 运营         |  1 | egon       | male   |   18 |    200 |
|  200 | 技术         |  2 | alex       | female |   48 |    201 |
|  201 | 人力资源     |  2 | alex       | female |   48 |    201 |
|  202 | 销售         |  2 | alex       | female |   48 |    201 |
|  203 | 运营         |  2 | alex       | female |   48 |    201 |
|  200 | 技术         |  3 | wupeiqi    | male   |   38 |    201 |
|  201 | 人力资源     |  3 | wupeiqi    | male   |   38 |    201 |
|  202 | 销售         |  3 | wupeiqi    | male   |   38 |    201 |
|  203 | 运营         |  3 | wupeiqi    | male   |   38 |    201 |
|  200 | 技术         |  4 | yuanhao    | female |   28 |    202 |
|  201 | 人力资源     |  4 | yuanhao    | female |   28 |    202 |
|  202 | 销售         |  4 | yuanhao    | female |   28 |    202 |
|  203 | 运营         |  4 | yuanhao    | female |   28 |    202 |
|  200 | 技术         |  5 | liwenzhou  | male   |   18 |    200 |
|  201 | 人力资源     |  5 | liwenzhou  | male   |   18 |    200 |
|  202 | 销售         |  5 | liwenzhou  | male   |   18 |    200 |
|  203 | 运营         |  5 | liwenzhou  | male   |   18 |    200 |
|  200 | 技术         |  6 | jingliyang | female |   18 |    204 |
|  201 | 人力资源     |  6 | jingliyang | female |   18 |    204 |
|  202 | 销售         |  6 | jingliyang | female |   18 |    204 |
|  203 | 运营         |  6 | jingliyang | female |   18 |    204 |
+------+--------------+----+------------+--------+------+--------+
24 rows in set (0.12 sec)

我们让employee表在前面看看结果，注意看结果表的字段
mysql> select * from employee,department;
+----+------------+--------+------+--------+------+--------------+
| id | name | sex | age | dep_id | id | name |
+----+------------+--------+------+--------+------+--------------+
| 1 | egon | male | 18 | 200 | 200 | 技术 |
| 1 | egon | male | 18 | 200 | 201 | 人力资源 |
| 1 | egon | male | 18 | 200 | 202 | 销售 |
| 1 | egon | male | 18 | 200 | 203 | 运营 |
| 2 | alex | female | 48 | 201 | 200 | 技术 |
| 2 | alex | female | 48 | 201 | 201 | 人力资源 |
| 2 | alex | female | 48 | 201 | 202 | 销售 |
| 2 | alex | female | 48 | 201 | 203 | 运营 |
| 3 | wupeiqi | male | 38 | 201 | 200 | 技术 |
| 3 | wupeiqi | male | 38 | 201 | 201 | 人力资源 |
| 3 | wupeiqi | male | 38 | 201 | 202 | 销售 |
| 3 | wupeiqi | male | 38 | 201 | 203 | 运营 |
| 4 | yuanhao | female | 28 | 202 | 200 | 技术 |
| 4 | yuanhao | female | 28 | 202 | 201 | 人力资源 |
| 4 | yuanhao | female | 28 | 202 | 202 | 销售 |
| 4 | yuanhao | female | 28 | 202 | 203 | 运营 |
| 5 | liwenzhou | male | 18 | 200 | 200 | 技术 |
| 5 | liwenzhou | male | 18 | 200 | 201 | 人力资源 |
| 5 | liwenzhou | male | 18 | 200 | 202 | 销售 |
| 5 | liwenzhou | male | 18 | 200 | 203 | 运营 |
| 6 | jingliyang | female | 18 | 204 | 200 | 技术 |
| 6 | jingliyang | female | 18 | 204 | 201 | 人力资源 |
| 6 | jingliyang | female | 18 | 204 | 202 | 销售 |
| 6 | jingliyang | female | 18 | 204 | 203 | 运营 |
+----+------------+--------+------+--------+------+--------------+
24 rows in set (0.00 sec)

```

​	关于笛卡儿积：我们看一下上面的这些数据，有什么发现，首先看到这些字段都显示出来了，并且数据变得很多，我们来看一下，这么多条数据都是怎么来的，为什么会出现这么条数据，笛卡儿积这是一个数据名词，你可以去研究研究~~

​	因为我们要进行连表查询，那么mysql并不知道你想要如何连接两个表的关系进行查询，那么mysql会将你两个表数据的所有组合关系都给你拼接成一条数据来显示，这样你就可以想查哪个关联关系的数据就查哪个了，如果还是不太理解看一下下面的图：

![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181123165130845-264296897.png)

　　

​	咱们为了更好的管理数据，为了节省空间，为了数据组织结构更清晰，将数据拆分到了不同表里面，但是本质上是不是还是一份数据，一份重复内容很多的很大的数据，所以我们即便是分表了，但是咱们是不是还需要找到一个方案把两个本来分开的表能够合并到一起来进行查询，那你是不是就可以根据部门找员工，根据员工找部门了，对不对，但是我们合并两个表的时候，如何合并，根据什么来合并，通过笛卡儿积这种合并有没有浪费，我们其实想做的是不是说我们的员工表中dep_id这个字段中的数据和部门表里面的id能够对应上就可以了，因为我们知道我们设计表的时候，是通过这两个字段来给两个表建立关系的，对不对，看下图：

　　　　**![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181123170733686-1528734466.png)**

​	我们的目标就是将两个分散出去的表，按照两者之间有关系的字段，能对应上的字段，把两者合并成一张表，这就是多表查询的一个本质。那么笛卡儿积干了什么事儿，就是简单粗暴的将两个表的数据全部对应了一遍，用处就是什么呢，它肯定就能保证有一条是对应准的，你需要做的事情就是在笛卡儿积的基础上只过滤出我们需要的那些数据就行了，笛卡儿积不是咱们最终要得到的结果，只是给你提供了一个基础，它不管对应的对不对，全部给你对应一遍，然后你自己去筛选就可以了，然后基于笛卡儿积我们来找一下对应的数据，看看能不能找到：

```
#我们要找的数据就是员工表里面dep_id字段的值和部门表里面id字段的值能对应上的那些数据啊，所以你看下面的写法：
mysql> select * from employee,department where employee.dep_id=department.id;
+----+-----------+--------+------+--------+------+--------------+
| id | name      | sex    | age  | dep_id | id   | name         |
+----+-----------+--------+------+--------+------+--------------+
|  1 | egon      | male   |   18 |    200 |  200 | 技术         |
|  2 | alex      | female |   48 |    201 |  201 | 人力资源     |
|  3 | wupeiqi   | male   |   38 |    201 |  201 | 人力资源     |
|  4 | yuanhao   | female |   28 |    202 |  202 | 销售         |
|  5 | liwenzhou | male   |   18 |    200 |  200 | 技术         |
+----+-----------+--------+------+--------+------+--------------+
5 rows in set (0.14 sec)
拿到了我们想要的结果。

但是你看，我们左表employee表中的dep_id为204的那个数据没有了，右表department表的id为203的数据没有了，因为我们现在要的就是两表能对应上的数据一起查出来，那个204和203双方对应不上。

#再看一个需求，我要查出技术部的员工的名字
mysql> select name from employee,department where employee.dep_id=department.id and department.name='技术';
ERROR 1052 (23000): Column 'name' in field list is ambiguous
#上面直接就报错了，因为select后面直接写的name，在两个表合并起来的表中，是有两个name字段的，直接写name是不行的，要加上表名，再看：
mysql> select employee.name from employee,department where employee.dep_id=department.id and department.name='技术';
+-----------+
| name      |
+-----------+
| egon      |
| liwenzhou |
+-----------+
2 rows in set (0.09 sec)
结果就没问题了
```



​	但是你看上面的代码有没有什么不太好的地方，虽然我们能够完成我们的事情，但是代码可读性不好，所以以后不要这么写，但是看图：

　　　　![img](https://img2018.cnblogs.com/blog/988061/201811/988061-20181123180131254-1636098034.png)

​	所以mysql为我们提供了一些专门做连表操作的方法，这些方法语义更加的明确，你一看就知道那些代码是连表的，那些代码是查询的，其实上面的连表也是个查询操作，但是我们为了区分明确，连表专门用连表的方法，查询就专门用查询的方法。那这些专门的方法都是什么呢，看后面的内容。



## 4.2 连表查询

### 4.2.1 内连接 inner join

看题：请查出技术部的员工的名字

```
mysql> select employee.id,employee.name,department.name as depart_name from employee inner join department on employee.dep_id=department.id where department.name='技术';
+----+------------+--------------+
| id | name       | depart_name  |
+----+------------+--------------+
|  1 | egon       | 技术         |
|  5 | liwenzhou  | 技术         |
+----+------------+--------------+
```



### 4.2.2 外连接之左连接

**优先显示左表全部记录**

看示例：

```
#以左表为准，即找出所有员工信息，当然包括没有部门的员工
#本质就是：在内连接的基础上增加左边有右边没有的结果  #注意语法：
mysql> select employee.id,employee.name,department.name as depart_name from employee left join department on employee.dep_id=department.id;
+----+------------+--------------+
| id | name       | depart_name  |
+----+------------+--------------+
|  1 | egon       | 技术         |
|  5 | liwenzhou  | 技术         |
|  2 | alex       | 人力资源     |
|  3 | wupeiqi    | 人力资源     |
|  4 | yuanhao    | 销售         |
|  6 | jingliyang | NULL         |  #通过null来补充
+----+------------+--------------+
```



### 4.2.4 外链接之右连接

**优先显示右表全部记录**

看示例

```
#以右表为准，即找出所有部门信息，包括没有员工的部门
#本质就是：在内连接的基础上增加右边有左边没有的结果
mysql> select employee.id,employee.name,department.name as depart_name from employee right join department on employee.dep_id=department.id;
+------+-----------+--------------+
| id   | name      | depart_name  |
+------+-----------+--------------+
|    1 | egon      | 技术         |
|    2 | alex      | 人力资源     |
|    3 | wupeiqi   | 人力资源     |
|    4 | yuanhao   | 销售         |
|    5 | liwenzhou | 技术         |
| NULL | NULL      | 运营         |
+------+-----------+--------------+
```



### 4.2.4  全外连接：

**显示左右两个表全部记录**

```
全外连接：在内连接的基础上增加左边有右边没有的和右边有左边没有的结果
#注意：mysql不支持全外连接 full JOIN
#强调：mysql可以使用此种方式间接实现全外连接
select * from employee left join department on employee.dep_id = department.id
union
select * from employee right join department on employee.dep_id = department.id
;
#查看结果
+------+------------+--------+------+--------+------+--------------+
| id   | name       | sex    | age  | dep_id | id   | name         |
+------+------------+--------+------+--------+------+--------------+
|    1 | egon       | male   |   18 |    200 |  200 | 技术         |
|    5 | liwenzhou  | male   |   18 |    200 |  200 | 技术         |
|    2 | alex       | female |   48 |    201 |  201 | 人力资源     |
|    3 | wupeiqi    | male   |   38 |    201 |  201 | 人力资源     |
|    4 | yuanhao    | female |   28 |    202 |  202 | 销售         |
|    6 | jingliyang | female |   18 |    204 | NULL | NULL         |
| NULL | NULL       | NULL   | NULL |   NULL |  203 | 运营         |
+------+------------+--------+------+--------+------+--------------+

```



## 4.3 子查询



​	子查询其实就是将你的一个查询结果用括号括起来，这个结果也是一张表，就可以将它交给另外一个sql语句，作为它的一个查询依据来进行操作。

​	来，我们简单来个需求：技术部都有哪些员工的姓名，都显示出来：　1、看一下和哪个表有关，然后from找到两个表  2、进行一个连表操作　3、基于连表的结果来一个过滤就可以了

```
#我们之前的做法是：先连表
mysql> select * from employee inner join department on employee.dep_id = department.id; 
+----+-----------+--------+------+--------+------+--------------+
| id | name      | sex    | age  | dep_id | id   | name         |
+----+-----------+--------+------+--------+------+--------------+
|  1 | egon      | male   |   18 |    200 |  200 | 技术         |
|  2 | alex      | female |   48 |    201 |  201 | 人力资源     |
|  3 | wupeiqi   | male   |   38 |    201 |  201 | 人力资源     |
|  4 | yuanhao   | female |   28 |    202 |  202 | 销售         |
|  5 | liwenzhou | male   |   18 |    200 |  200 | 技术         |
+----+-----------+--------+------+--------+------+--------------+
5 rows in set (0.10 sec)

#然后根据连表的结果进行where过滤，将select*改为select employee.name

mysql> select employee.name from employee inner join department on employee.dep_id = department.id where department.name='技术';
  +-----------+
  | name |
  +-----------+
  | egon |
  | liwenzhou |
  +-----------+
  2 rows in set (0.09 sec)
```



​	然后看一下子查询这种方式的写法：它的做法就是解决完一个问题，再解决下一个问题，针对我们上面的需求，你想，我们的需求是不是说找技术部门下面有哪些员工对不对，如果你直接找员工表，你能确定哪个dep_id的数值表示的是技术部门吗，不能，所以咱们是不是应该先确定一个技术部门对应的id号是多少，然后根据部门的id号，再去员工表里面查询一下dep_id为技术部门对应的部门表的那个id号的所有的员工表里面的记录：好，那我们看一下下面的操作：

```
#首先从部门表里面找到技术部门对应的id
mysql> select id from department where name='技术';
+------+
| id   |
+------+
|  200 |
+------+
1 row in set (0.00 sec)

#那我们把上面的查询结果用括号括起来，它就表示一条id=200的数据，然后我们通过员工表来查询dep_id=这条数据作为条件来查询员工的name
mysql> select name from employee where dep_id = (select id from department where name='技术');
+-----------+
| name      |
+-----------+
| egon      |
| liwenzhou |
+-----------+
2 rows in set (0.00 sec)
上面这些就是子查询的一个思路，解决一个问题，再解决另外一个问题，你子查询里面可不可以是多个表的查询结果，当然可以，然后再通过这个结果作为依据来进行过滤，然后我们学一下子查询里面其他的内容，往下学。
```



**子查询的一些其他用法**

```
#1：子查询是将一个查询语句嵌套在另一个查询语句中。
#2：内层查询语句的查询结果，可以为外层查询语句提供查询条件。
#3：子查询中可以包含：IN、NOT IN、ANY、ALL、EXISTS 和 NOT EXISTS等关键字
#4：还可以包含比较运算符：= 、 !=、> 、<等
```

**小练习**

**1、带IN关键字的子查询**

```
#查询员工平均年龄在25岁以上的部门名，可以用连表，也可以用子查询，我们用子查询来搞一下
select id,name from department
    where id in 
        (select dep_id from employee group by dep_id having avg(age) > 25);
#连表来搞一下上面这个需求
select department.name from department inner join employee on department.id=employee.dep_id 
    group by department.name 
    having avg(age)>25;
总结：子查询的思路和解决问题一样，先解决一个然后拿着这个的结果再去解决另外一个问题，连表的思路是先将两个表关联在一起，然后在进行group by啊过滤啊等等操作，两者的思路是不一样的

#查看技术部员工姓名
select name from employee
    where dep_id in 
        (select id from department where name='技术');

#查看不足1人的部门名(子查询得到的是有人的部门id)
select name from department where id not in (select distinct dep_id from employee);
```



**2、带比较运算符的子查询**

```
#比较运算符：=、!=、>、>=、<、<=、<>
#查询大于所有人平均年龄的员工名与年龄
mysql> select name,age from emp where age > (select avg(age) from emp);
+---------+------+
| name | age |
+---------+------+
| alex | 48 |
| wupeiqi | 38 |
+---------+------+
2 rows in set (0.00 sec)


#查询大于部门内平均年龄的员工名、年龄
select t1.name,t1.age from emp t1
inner join 
(select dep_id,avg(age) avg_age from emp group by dep_id) t2
on t1.dep_id = t2.dep_id
where t1.age > t2.avg_age; 
```

**3、带EXISTS关键字的子查询**

​	EXISTS关字键字表示存在。在使用EXISTS关键字时，内层查询语句不返回查询的记录。而是返回一个真假值。True或False
​	当返回True时，外层查询语句将进行查询；当返回值为False时，外层查询语句不进行查询。还可以写not exists，和exists的效果就是反的

```
#department表中存在dept_id=203，Ture
mysql> select * from employee
    ->     where exists  
    ->         (select id from department where id=200); 
+----+------------+--------+------+--------+
| id | name       | sex    | age  | dep_id |
+----+------------+--------+------+--------+
|  1 | egon       | male   |   18 |    200 |
|  2 | alex       | female |   48 |    201 |
|  3 | wupeiqi    | male   |   38 |    201 |
|  4 | yuanhao    | female |   28 |    202 |
|  5 | liwenzhou  | male   |   18 |    200 |
|  6 | jingliyang | female |   18 |    204 |
+----+------------+--------+------+--------+

#department表中存在dept_id=205，False
mysql> select * from employee
    ->     where exists
    ->         (select id from department where id=204);
Empty set (0.00 sec)
```



# 第五节 mysqldump

我们在工作中可能需要将数据库进行备份，那么就可以用到我们的mysqldump指令。

语法

```
mysqldump -uroot -p -B crm2> xx\xx\xx.sql
```



看示例

**数据库和数据准备**

```
1.首先我们先创建一个名为crm2的库

　　　　mysql> create database crm2;
　　　　mysql> show create database crm2;
　　2.切换到crm2库下
　　　　mysql> use crm2;
　　3.创建两张表，student表和class表
　　　　mysql> create table tb1(id int primary key,name char(8) not null,age int,class_id int not null);
　　　　Query OK, 0 rows affected (0.63 sec)

　　　　mysql> create table class(id int primary key,cname char(20) not null);
　　　　Query OK, 0 rows affected (0.34 sec)

　　4.给两张表插入一些数据

　　　　mysql> insert into class values(1,'一班'),(2,'二班');
　　　　mysql> insert into student values(1,'Jaden',18,1),(2,'太白',45,1),(3,'彦涛',30,2);

　　5.查看一下两个表的数据
　　　　mysql> select * from student;
　　　　+----+--------+------+----------+
　　　　| id | name | age | class_id |
　　　　+----+--------+------+----------+
　　　　| 1 | Jaden | 18 | 1 |
　　　　| 2 | 太白 | 45 | 1 |
　　　　| 3 | 彦涛 | 30 | 2 |
　　　　+----+--------+------+----------+
　　　　3 rows in set (0.00 sec)

　　　　mysql> select * from class;
　　　　+----+--------+
　　　　| id | cname |
　　　　+----+--------+
　　　　| 1 | 一班 |
　　　　| 2 | 二班 |
　　　　+----+--------+
　　　　2 rows in set (0.00 sec)
```



```

1.mysqldump -uroot -p -B crm2> 备份的sql文件存放路径
	例如：mysqldump -uroot -p -B crm2> f:\数据库备份练习\crm2.sql
	备份完成之后，我们删除一下数据库crm2，然后再执行下面的数据库恢复指令。
2.在cmd窗口下执行：mysql -uroot -p < f:\数据库备份练习\crm2.sql
3.查看一下是否恢复了：
mysql> show databases;
+--------------------+
| Database |
+--------------------+
| information_schema |
| crm2 |
| d1 |
| mysql |
| performance_schema |
| test |
+--------------------+
mysql> use crm2;
Database changed
mysql> show tables;
+----------------+
| Tables_in_crm2 |
+----------------+
| class |
| student |
+----------------+
2 rows in set (0.00 sec)
mysql> select * from class;
+----+--------+
| id | cname |
+----+--------+
| 1 | 一班 |
| 2 | 二班 |
+----+--------+
2 rows in set (0.00 sec)

mysql> desc student;
+----------+---------+------+-----+---------+-------+
| Field | Type | Null | Key | Default | Extra |
+----------+---------+------+-----+---------+-------+
| id | int(11) | NO | PRI | NULL | |
| name | char(8) | NO | | NULL | |
| age | int(11) | YES | | NULL | |
| class_id | int(11) | NO | | NULL | |
+----------+---------+------+-----+---------+-------+
4 rows in set (0.02 sec)
```

数据恢复了，上面我们就完成了一个简单数据库备份和恢复的过程。



# 本节作业

通过下面的表，完成后面的习题。

表结构为

![img](https://images2017.cnblogs.com/blog/1036857/201802/1036857-20180211190041138-168655281.png)

建表语句和数据准备

```
#创建表及插入记录
CREATE TABLE class (
  cid int(11) NOT NULL AUTO_INCREMENT,
  caption varchar(32) NOT NULL,
  PRIMARY KEY (cid)
) ENGINE=InnoDB CHARSET=utf8;

INSERT INTO class VALUES
(1, '三年二班'), 
(2, '三年三班'), 
(3, '一年二班'), 
(4, '二年九班');

CREATE TABLE course(
  cid int(11) NOT NULL AUTO_INCREMENT,
  cname varchar(32) NOT NULL,
  teacher_id int(11) NOT NULL,
  PRIMARY KEY (cid),
  KEY fk_course_teacher (teacher_id),
  CONSTRAINT fk_course_teacher FOREIGN KEY (teacher_id) REFERENCES teacher (tid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO course VALUES
(1, '生物', 1), 
(2, '物理', 2), 
(3, '体育', 3), 
(4, '美术', 2);

CREATE TABLE score (
  sid int(11) NOT NULL AUTO_INCREMENT,
  student_id int(11) NOT NULL,
  course_id int(11) NOT NULL,
  num int(11) NOT NULL,
  PRIMARY KEY (sid),
  KEY fk_score_student (student_id),
  KEY fk_score_course (course_id),
  CONSTRAINT fk_score_course FOREIGN KEY (course_id) REFERENCES course (cid),
  CONSTRAINT fk_score_student FOREIGN KEY (student_id) REFERENCES student(sid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO score VALUES
(1, 1, 1, 10),
(2, 1, 2, 9),
(5, 1, 4, 66),
(6, 2, 1, 8),
(8, 2, 3, 68),
(9, 2, 4, 99),
(10, 3, 1, 77),
(11, 3, 2, 66),
(12, 3, 3, 87),
(13, 3, 4, 99),
(14, 4, 1, 79),
(15, 4, 2, 11),
(16, 4, 3, 67),
(17, 4, 4, 100),
(18, 5, 1, 79),
(19, 5, 2, 11),
(20, 5, 3, 67),
(21, 5, 4, 100),
(22, 6, 1, 9),
(23, 6, 2, 100),
(24, 6, 3, 67),
(25, 6, 4, 100),
(26, 7, 1, 9),
(27, 7, 2, 100),
(28, 7, 3, 67),
(29, 7, 4, 88),
(30, 8, 1, 9),
(31, 8, 2, 100),
(32, 8, 3, 67),
(33, 8, 4, 88),
(34, 9, 1, 91),
(35, 9, 2, 88),
(36, 9, 3, 67),
(37, 9, 4, 22),
(38, 10, 1, 90),
(39, 10, 2, 77),
(40, 10, 3, 43),
(41, 10, 4, 87),
(42, 11, 1, 90),
(43, 11, 2, 77),
(44, 11, 3, 43),
(45, 11, 4, 87),
(46, 12, 1, 90),
(47, 12, 2, 77),
(48, 12, 3, 43),
(49, 12, 4, 87),
(52, 13, 3, 87);


CREATE TABLE student(
  sid int(11) NOT NULL AUTO_INCREMENT,
  gender char(1) NOT NULL,
  class_id int(11) NOT NULL,
  sname varchar(32) NOT NULL,
  PRIMARY KEY (sid),
  KEY fk_class (class_id),
  CONSTRAINT fk_class FOREIGN KEY (class_id) REFERENCES class (cid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO student VALUES
(1, '男', 1, '理解'), 
(2, '女', 1, '钢蛋'), 
(3, '男', 1, '张三'), 
(4, '男', 1, '张一'), 
(5, '女', 1, '张二'), 
(6, '男', 1, '张四'), 
(7, '女', 2, '铁锤'), 
(8, '男', 2, '李三'), 
(9, '男', 2, '李一'), 
(10, '女', 2, '李二'), 
(11, '男', 2, '李四'), 
(12, '女', 3, '如花'), 
(13, '男', 3, '刘三'), 
(14, '男', 3, '刘一'), 
(15, '女', 3, '刘二'), 
(16, '男', 3, '刘四');

CREATE TABLE teacher(
  tid int(11) NOT NULL AUTO_INCREMENT,
  tname varchar(32) NOT NULL,
  PRIMARY KEY (tid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO teacher VALUES
(1, '张磊老师'), 
(2, '李平老师'), 
(3, '刘海燕老师'), 
(4, '朱云海老师'), 
(5, '李杰老师');
```



**习题**

```
1、查询所有的课程的名称以及对应的任课老师姓名

2、查询学生表中男女生各有多少人

3、查询物理成绩等于100的学生的姓名

4、查询平均成绩大于八十分的同学的姓名和平均成绩

5、查询所有学生的学号，姓名，选课数，总成绩

6、 查询姓李老师的个数

7、 查询没有报李平老师课的学生姓名

8、 查询物理课程比生物课程高的学生的学号

9、 查询没有同时选修物理课程和体育课程的学生姓名

10、查询挂科超过两门(包括两门)的学生姓名和班级

11 、查询选修了所有课程的学生姓名

12、查询李平老师教的课程的所有成绩记录
 
13、查询全部学生都选修了的课程号和课程名

14、查询每门课程被选修的次数

15、查询之选修了一门课程的学生姓名和学号

16、查询所有学生考出的成绩并按从高到低排序（成绩去重）

17、查询平均成绩大于85的学生姓名和平均成绩

18、查询生物成绩不及格的学生姓名和对应生物分数

19、查询在所有选修了李平老师课程的学生中，这些课程(李平老师的课程，不是所有课程)平均成绩最高的学生姓名

20、查询每门课程成绩最好的前两名学生姓名

```

**答案**

```
#1、查询所有的课程的名称以及对应的任课老师姓名
SELECT
    course.cname,
    teacher.tname
FROM
    course
INNER JOIN teacher ON course.teacher_id = teacher.tid;




#2、查询学生表中男女生各有多少人
SELECT
    gender 性别,
    count(1) 人数
FROM
    student
GROUP BY
    gender;




#3、查询物理成绩等于100的学生的姓名
SELECT
    student.sname
FROM
    student
WHERE
    sid IN (
        SELECT
            student_id
        FROM
            score
        INNER JOIN course ON score.course_id = course.cid
        WHERE
            course.cname = '物理'
        AND score.num = 100
    );




#4、查询平均成绩大于八十分的同学的姓名和平均成绩
SELECT
    student.sname,
    t1.avg_num
FROM
    student
INNER JOIN (
    SELECT
        student_id,
        avg(num) AS avg_num
    FROM
        score
    GROUP BY
        student_id
    HAVING
        avg(num) > 80
) AS t1 ON student.sid = t1.student_id;




#5、查询所有学生的学号，姓名，选课数，总成绩(注意：对于那些没有选修任何课程的学生也算在内)
SELECT
    student.sid,
    student.sname,
    t1.course_num,
    t1.total_num
FROM
    student
LEFT JOIN (
    SELECT
        student_id,
        COUNT(course_id) course_num,
        sum(num) total_num
    FROM
        score
    GROUP BY
        student_id
) AS t1 ON student.sid = t1.student_id;




#6、 查询姓李老师的个数
SELECT
    count(tid)
FROM
    teacher
WHERE
    tname LIKE '李%';




#7、 查询没有报李平老师课的学生姓名(找出报名李平老师课程的学生，然后取反就可以)
SELECT
    student.sname
FROM
    student
WHERE
    sid NOT IN (
        SELECT DISTINCT
            student_id
        FROM
            score
        WHERE
            course_id IN (
                SELECT
                    course.cid
                FROM
                    course
                INNER JOIN teacher ON course.teacher_id = teacher.tid
                WHERE
                    teacher.tname = '李平老师'
            )
    );




#8、 查询物理课程比生物课程高的学生的学号(分别得到物理成绩表与生物成绩表，然后连表即可)
SELECT
    t1.student_id
FROM
    (
        SELECT
            student_id,
            num
        FROM
            score
        WHERE
            course_id = (
                SELECT
                    cid
                FROM
                    course
                WHERE
                    cname = '物理'
            )
    ) AS t1
INNER JOIN (
    SELECT
        student_id,
        num
    FROM
        score
    WHERE
        course_id = (
            SELECT
                cid
            FROM
                course
            WHERE
                cname = '生物'
        )
) AS t2 ON t1.student_id = t2.student_id
WHERE
    t1.num > t2.num;




#9、 查询没有同时选修物理课程和体育课程的学生姓名(没有同时选修指的是选修了一门的，思路是得到物理+体育课程的学生信息表，然后基于学生分组，统计count(课程)=1)
SELECT
    student.sname
FROM
    student
WHERE
    sid IN (
        SELECT
            student_id
        FROM
            score
        WHERE
            course_id IN (
                SELECT
                    cid
                FROM
                    course
                WHERE
                    cname = '物理'
                OR cname = '体育'
            )
        GROUP BY
            student_id
        HAVING
            COUNT(course_id) = 1
    );




#10、查询挂科超过两门(包括两门)的学生姓名和班级(求出<60的表，然后对学生进行分组，统计课程数目>=2)
SELECT
    student.sname,
    class.caption
FROM
    student
INNER JOIN (
    SELECT
        student_id
    FROM
        score
    WHERE
        num < 60
    GROUP BY
        student_id
    HAVING
        count(course_id) >= 2
) AS t1
INNER JOIN class ON student.sid = t1.student_id
AND student.class_id = class.cid;




#11、查询选修了所有课程的学生姓名(先从course表统计课程的总数，然后基于score表按照student_id分组，统计课程数据等于课程总数即可)
SELECT
    student.sname
FROM
    student
WHERE
    sid IN (
        SELECT
            student_id
        FROM
            score
        GROUP BY
            student_id
        HAVING
            COUNT(course_id) = (SELECT count(cid) FROM course)
    );




#12、查询李平老师教的课程的所有成绩记录
SELECT
    *
FROM
    score
WHERE
    course_id IN (
        SELECT
            cid
        FROM
            course
        INNER JOIN teacher ON course.teacher_id = teacher.tid
        WHERE
            teacher.tname = '李平老师'
    );




#13、查询全部学生都选修了的课程号和课程名(取所有学生数，然后基于score表的课程分组，找出count(student_id)等于学生数即可)
SELECT
    cid,
    cname
FROM
    course
WHERE
    cid IN (
        SELECT
            course_id
        FROM
            score
        GROUP BY
            course_id
        HAVING
            COUNT(student_id) = (
                SELECT
                    COUNT(sid)
                FROM
                    student
            )
    );




#14、查询每门课程被选修的次数
SELECT
    course_id,
    COUNT(student_id)
FROM
    score
GROUP BY
    course_id;




#15、查询之选修了一门课程的学生姓名和学号
SELECT
    sid,
    sname
FROM
    student
WHERE
    sid IN (
        SELECT
            student_id
        FROM
            score
        GROUP BY
            student_id
        HAVING
            COUNT(course_id) = 1
    );




#16、查询所有学生考出的成绩并按从高到低排序（成绩去重）
SELECT DISTINCT
    num
FROM
    score
ORDER BY
    num DESC;




#17、查询平均成绩大于85的学生姓名和平均成绩
SELECT
    sname,
    t1.avg_num
FROM
    student
INNER JOIN (
    SELECT
        student_id,
        avg(num) avg_num
    FROM
        score
    GROUP BY
        student_id
    HAVING
        AVG(num) > 85
) t1 ON student.sid = t1.student_id;




#18、查询生物成绩不及格的学生姓名和对应生物分数
SELECT
    sname 姓名,
    num 生物成绩
FROM
    score
LEFT JOIN course ON score.course_id = course.cid
LEFT JOIN student ON score.student_id = student.sid
WHERE
    course.cname = '生物'
AND score.num < 60;




#19、查询在所有选修了李平老师课程的学生中，这些课程(李平老师的课程，不是所有课程)平均成绩最高的学生姓名
SELECT
    sname
FROM
    student
WHERE
    sid = (
        SELECT
            student_id
        FROM
            score
        WHERE
            course_id IN (
                SELECT
                    course.cid
                FROM
                    course
                INNER JOIN teacher ON course.teacher_id = teacher.tid
                WHERE
                    teacher.tname = '李平老师'
            )
        GROUP BY
            student_id
        ORDER BY
            AVG(num) DESC
        LIMIT 1
    );




#20、查询每门课程成绩最好的前两名学生姓名
#查看每门课程按照分数排序的信息，为下列查找正确与否提供依据
SELECT
    *
FROM
    score
ORDER BY
    course_id,
    num DESC;
```