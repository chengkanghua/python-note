# 引入

本节内容，我们准备学一下MySQL数据库中的锁和事务，以及一些sql题的练习。

学习过并发编程之后，我们知道任务是可以并发执行的，那么如果我们并发操作共享数据的时候，会造成数据不安全的问题，怎么解决呢？加锁，而MySQL数据库已经给我们提供了锁，下面我们来学习一下。

数据库锁定机制简单来说，就是数据库为了保证数据的一致性，而使各种共享资源在被并发访问变得有序所设计的一种规则。对于任何一种数据库来说都需要有相应的锁定机制，所以MySQL自然也不能例外。MySQL数据库由于其自身架构的特点，存在多种数据存储引擎，每种存储引擎所针对的应用场景特点都不太一样，为了满足各自特定应用场景的需求，每种存储引擎的锁定机制都是为各自所面对的特定场景而优化设计，所以各存储引擎的锁定机制也有较大区别。MySQL各存储引擎使用了三种类型（级别）的锁定机制：表级锁定，行级锁定。

# 第一节 锁



我们知道mysql中支持很多个存储引擎，在不同的存储引擎下所能支持的锁是不同的，我们通过MyISAM和InnoDB来进行一下对比。

## 1.1 表级锁定（table-level）


​	表级别的锁定是MySQL各存储引擎中最大颗粒度的锁定机制。该锁定机制最大的特点是实现逻辑非常简单，带来的系统负面影响最小。所以获取锁和释放锁的速度很快。由于表级锁一次会将整个表锁定，所以可以很好的避免困扰我们的死锁问题。
​	当然，锁定颗粒度大所带来最大的负面影响就是出现锁定资源争用的概率也会最高，致使并大度大打折扣。
​	使用表级锁定的主要是MyISAM，MEMORY，CSV等一些非事务性存储引擎。

## 1.2 行级锁定　　　　

​	行级锁定最大的特点就是锁定对象的颗粒度很小，也是目前各大数据库管理软件所实现的锁定颗粒度最小的。由于锁定颗粒度很小，所以发生锁定资源争用的概率也最小，能够给予应用程序尽可能大的并发处理能力而提高一些需要高并发应用系统的整体性能。
​	虽然能够在并发处理能力上面有较大的优势，但是行级锁定也因此带来了不少弊端。由于锁定资源的颗粒度很小，所以每次获取锁和释放锁需要做的事情也更多，带来的消耗自然也就更大了。此外，行级锁定也最容易发生死锁。
​	使用行级锁定的主要是InnoDB存储引擎。

表级锁：开销小，加锁快；不会出现死锁；锁定粒度大，发生锁冲突的概率最高，并发度最低；
行级锁：开销大，加锁慢；会出现死锁；锁定粒度最小，发生锁冲突的概率最低，并发度也最高；



## 1.3 乐观锁和悲观锁

​	**乐观锁**，顾名思义，对加锁持有一种乐观的态度，即先进行业务操作，不到最后一步不进行加锁，"乐观"的认为加锁一定会成功的，在最后一步更新数据的时候在进行加锁，乐观锁的实现方式一般为每一条数据加一个版本号，具体流程是这样的：

​	1）、创建一张表时添加一个version字段，表示是版本号，如下：
　　　　![img](https://img-blog.csdn.net/20180527165210793)

​	2）、修改数据的时候首先把这条数据的版本号查出来，update时判断这个版本号是否和数据库里的一致，如果一致则表明这条数据没有被其他用户修改，若不一致则表明这条数据在操作期间被其他客户修改过，此时需要在代码中抛异常或者回滚等。伪代码如下：

```
update tb set name='yyy' and version=version+1 where id=1 and version=version;
```

​	

```
1. SELECT name AS old_name, version AS old_version FROM tb where ...;
2. 根据获取的数据进行业务操作，得到new_dname和new_version
3. UPDATE SET name = new_name, version = new_version WHERE version = old_version
if (updated row > 0) {
    // 乐观锁获取成功，操作完成
} else {
    // 乐观锁获取失败，回滚并重试

}
```

​		update其实在不在事物中都无所谓，在内部是这样的：update是单线程的，及如果一个线程对一条数据进行		update操作，会获得锁，其他线程如果要对同一条数据操作会阻塞，直到这个线程update成功后释放锁。



​	**悲观锁**，正如其名字一样，悲观锁对数据加锁持有一种悲观的态度。因此，在整个数据处理过程中，将数据处于锁定状态。悲观锁的实现，往往依靠数据库提供的锁机制（也只有数据库层提供的锁机制才能真正保证数据访问的排他性，否则，即使在本系统中实现了加锁机制，也无法保证外部系统不会修改数据）。

　　首先我们需要set autocommit=0，即不允许自动提交

　　用法：select * from tablename where id = 1 for update;

　　申请前提：没有线程对该结果集中的任何行数据使用排他锁或共享锁，否则申请会阻塞。

　　for update仅适用于InnoDB，且必须在事务块(BEGIN/COMMIT)中才能生效。在进行事务操作时，通过“for update”语句，MySQL会对查询结果集中每行数据都添加排他锁，其他线程对该记录的更新与删除操作都会阻塞。排他锁包含行锁、表锁。

　　假设有一张商品表 shop，它包含 id，商品名称，库存量三个字段，表结构如下：

　	![img](https://img-blog.csdn.net/20180527172945324)

　　插入如下数据：

　　![img](https://img-blog.csdn.net/2018052717305475)

　　

　　并发导致数据一致性的问题：

　　如果有A、B两个用户需要购买id=1的商品，AB都查询商品数量是1000，A购买后修改商品的数量为999，B购买后修改数量为999。

　　**用乐观锁的解决方案：**

​			每次获取商品时，不对该商品加锁。在更新数据的时候需要比较程序中的库存量与数据库中的库存量是否相等，如果相等则进行更新，反之程序重新获取库存量，再次进行比较，直到两个库存量的数值相等才进行数据更新。伪代码如下：

```
//不加锁
select id,name,stock where id=1;
 
//业务处理
 
begin;
 
update shop set stock=stock-1 where id=1 and stock=stock;
 
commit;
```

​		**悲观锁方案：**

​			每次获取商品时，对该商品加排他锁。也就是在用户A获取获取 id=1 的商品信息时对该行记录加锁，期间其他用户阻塞等待访问该记录。悲观锁适合写入频繁的场景。代码如下：

```
begin;
 
select id,name,stock as old_stock from shop  where id=1 for update;
 
update shop set stock=stock-1 where id=1 and stock=old_stock;
 
commit;
```

​	我们可以看到，首先通过begin开启一个事物，在获得shop信息和修改数据的整个过程中都对数据加锁，保证了数据的一致性。



# 第二节 事务



## 2.1 事务介绍

​	简单地说，事务就是指逻辑上的一组SQL语句操作，组成这组操作的各个SQL语句，执行时要么全成功要么全失败。
​	例如：你给我转账5块钱，流程如下
​		a.从你银行卡取出5块钱，剩余计算money-5
​		b.把上面5块钱打入我的账户上，我收到5块，剩余计算money+5.
​	上述转账的过程，对应的sql语句为：

```
update 你_account set money=money-5 where name='你'；
update 我_account set money=money+5 where name='我'；
```

​	上述的两条SQL操作，在事务中的操作就是要么都执行，要么都不执行，不然钱就对不上了。
​	这就是事务的原子性(Atomicity)。

## 2.2 事务的四大特性

​        1.原子性(Atomicity)
​            事务是一个不可分割的单位，事务中的所有SQL等操作要么都发生，要么都不发生。
​        2.一致性(Consistency)
​            事务发生前和发生后，数据的完整性必须保持一致。
​        3.隔离性(Isolation)
​            当并发访问数据库时，一个正在执行的事务在执行完毕前，对于其他的会话是不可见的，多个并发事务之间的数据是相互隔离的。也就是其他人的操作在这个事务的执行过程中是看不到这个事务的执行结果的，也就是他们拿到的是这个事务执行之前的内容，等这个事务执行完才能拿到新的数据。
​        4.持久性(Durability)
​            一个事务一旦被提交，它对数据库中的数据改变就是永久性的。如果出了错误，事务也不允撤销，只能通过'补偿性事务'。



## 2.3 MySQL中事务操作指令

看语法：

```
BEGIN或START TRANSACTION；显式地开启一个事务；
COMMIT；                  也可以使用COMMIT WORK，不过二者是等价的。COMMIT会提交事务，并使已对数据库进行的所有修改成为永久性的；
ROLLBACK；                有可以使用ROLLBACK WORK，不过二者是等价的。回滚会结束用户的事务，并撤销正在进行的所有未提交的修改；
```

事务简单实例

```
create table user(
id int primary key auto_increment,
name char(32),
balance int
);

insert into user(name,balance)
values
('wsb',1000),
('chao',1000),
('ysb',1000);

#原子操作
start transaction;
update user set balance=900 where name='wsb'; #买支付100元
update user set balance=1010 where name='chao'; #中介拿走10元
update user set balance=1090 where name='ysb'; #卖家拿到90元
commit;  #只要不进行commit操作，就没有保存下来，没有刷到硬盘上
 
#出现异常，回滚到初始状态
start transaction;
update user set balance=900 where name='wsb'; #买支付100元
update user set balance=1010 where name='chao'; #中介拿走10元
uppdate user set balance=1090 where name='ysb'; #卖家拿到90元,出现异常没有拿到
rollback;  #如果上面三个sql语句出现了异常，就直接rollback，数据就直接回到原来的状态了。但是执行了commit之后，rollback这个操作就没法回滚了
commit;
```



# 第三节 SQL题练习



练习题

将下面的内容放到某个sql文件中，比如叫做test.sql，这是我们练题的时候需要的表结构和数据。

```
/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50624
 Source Host           : localhost
 Source Database       : sqlexam

 Target Server Type    : MySQL
 Target Server Version : 50624
 File Encoding         : utf-8

 Date: 10/21/2016 06:46:46 AM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `class`
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(32) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `class`
-- ----------------------------
BEGIN;
INSERT INTO `class` VALUES ('1', '三年二班'), ('2', '三年三班'), ('3', '一年二班'), ('4', '二年九班');
COMMIT;

-- ----------------------------
--  Table structure for `course`
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(32) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`cid`),
  KEY `fk_course_teacher` (`teacher_id`),
  CONSTRAINT `fk_course_teacher` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `course`
-- ----------------------------
BEGIN;
INSERT INTO `course` VALUES ('1', '生物', '1'), ('2', '物理', '2'), ('3', '体育', '3'), ('4', '美术', '2');
COMMIT;

-- ----------------------------
--  Table structure for `score`
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `num` int(11) NOT NULL,
  PRIMARY KEY (`sid`),
  KEY `fk_score_student` (`student_id`),
  KEY `fk_score_course` (`course_id`),
  CONSTRAINT `fk_score_course` FOREIGN KEY (`course_id`) REFERENCES `course` (`cid`),
  CONSTRAINT `fk_score_student` FOREIGN KEY (`student_id`) REFERENCES `student` (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `score`
-- ----------------------------
BEGIN;
INSERT INTO `score` VALUES ('1', '1', '1', '10'), ('2', '1', '2', '9'), ('5', '1', '4', '66'), ('6', '2', '1', '8'), ('8', '2', '3', '68'), ('9', '2', '4', '99'), ('10', '3', '1', '77'), ('11', '3', '2', '66'), ('12', '3', '3', '87'), ('13', '3', '4', '99'), ('14', '4', '1', '79'), ('15', '4', '2', '11'), ('16', '4', '3', '67'), ('17', '4', '4', '100'), ('18', '5', '1', '79'), ('19', '5', '2', '11'), ('20', '5', '3', '67'), ('21', '5', '4', '100'), ('22', '6', '1', '9'), ('23', '6', '2', '100'), ('24', '6', '3', '67'), ('25', '6', '4', '100'), ('26', '7', '1', '9'), ('27', '7', '2', '100'), ('28', '7', '3', '67'), ('29', '7', '4', '88'), ('30', '8', '1', '9'), ('31', '8', '2', '100'), ('32', '8', '3', '67'), ('33', '8', '4', '88'), ('34', '9', '1', '91'), ('35', '9', '2', '88'), ('36', '9', '3', '67'), ('37', '9', '4', '22'), ('38', '10', '1', '90'), ('39', '10', '2', '77'), ('40', '10', '3', '43'), ('41', '10', '4', '87'), ('42', '11', '1', '90'), ('43', '11', '2', '77'), ('44', '11', '3', '43'), ('45', '11', '4', '87'), ('46', '12', '1', '90'), ('47', '12', '2', '77'), ('48', '12', '3', '43'), ('49', '12', '4', '87'), ('52', '13', '3', '87');
COMMIT;

-- ----------------------------
--  Table structure for `student`
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `gender` char(1) NOT NULL,
  `class_id` int(11) NOT NULL,
  `sname` varchar(32) NOT NULL,
  PRIMARY KEY (`sid`),
  KEY `fk_class` (`class_id`),
  CONSTRAINT `fk_class` FOREIGN KEY (`class_id`) REFERENCES `class` (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `student`
-- ----------------------------
BEGIN;
INSERT INTO `student` VALUES ('1', '男', '1', '理解'), ('2', '女', '1', '钢蛋'), ('3', '男', '1', '张三'), ('4', '男', '1', '张一'), ('5', '女', '1', '张二'), ('6', '男', '1', '张四'), ('7', '女', '2', '铁锤'), ('8', '男', '2', '李三'), ('9', '男', '2', '李一'), ('10', '女', '2', '李二'), ('11', '男', '2', '李四'), ('12', '女', '3', '如花'), ('13', '男', '3', '刘三'), ('14', '男', '3', '刘一'), ('15', '女', '3', '刘二'), ('16', '男', '3', '刘四');
COMMIT;

-- ----------------------------
--  Table structure for `teacher`
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `tname` varchar(32) NOT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `teacher`
-- ----------------------------
BEGIN;
INSERT INTO `teacher` VALUES ('1', '张磊老师'), ('2', '李平老师'), ('3', '刘海燕老师'), ('4', '朱云海老师'), ('5', '李杰老师');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;

```

然后执行下面的指令

```
mysqldump -uroot -p密码  数据库名称 < sql文件路径  
```



习题和答案

```
1、查询所有的课程的名称以及对应的任课老师姓名
SELECT
    course.cname,
    teacher.tname
FROM
    course
INNER JOIN teacher ON course.teacher_id = teacher.tid;

2、查询“生物”课程比“物理”课程成绩高的所有学生的学号；
思路：
    获取所有有生物课程的人（学号，成绩） - 临时表
    获取所有有物理课程的人（学号，成绩） - 临时表
    根据【学号】连接两个临时表：
        学号  物理成绩   生物成绩
 
    然后再进行筛选
 
        select A.student_id,sw,ty from
 
        (select student_id,num as sw from score left join course on score.course_id = course.cid where course.cname = '生物') as A
 
        left join
 
        (select student_id,num  as ty from score left join course on score.course_id = course.cid where course.cname = '体育') as B
 
        on A.student_id = B.student_id where sw > if(isnull(ty),0,ty);
 
3、查询平均成绩大于60分的同学的学号和平均成绩；
    思路：
        根据学生分组，使用avg获取平均值，通过having对avg进行筛选
 
        select student_id,avg(num) from score group by student_id having avg(num) > 60
 
4、查询所有同学的学号、姓名、选课数、总成绩；
 
    select score.student_id,sum(score.num),count(score.student_id),student.sname
    from
        score left join student on score.student_id = student.sid  
    group by score.student_id
 
5、查询姓“李”的老师的个数；
    select count(tid) from teacher where tname like '李%'
 
    select count(1) from (select tid from teacher where tname like '李%') as B
 
6、查询没学过“叶平”老师课的同学的学号、姓名；
    思路：
        先查到“李平老师”老师教的所有课ID
        获取选过课的所有学生ID
        学生表中筛选
    select * from student where sid not in (
        select DISTINCT student_id from score where score.course_id in (
            select cid from course left join teacher on course.teacher_id = teacher.tid where tname = '李平老师'
        )
    )
 
7、查询学过“001”并且也学过编号“002”课程的同学的学号、姓名；
    思路：
        先查到既选择001又选择002课程的所有同学
        根据学生进行分组，如果学生数量等于2表示，两门均已选择
 
    select student_id,sname from
 
    (select student_id,course_id from score where course_id = 1 or course_id = 2) as B
      
    left join student on B.student_id = student.sid group by student_id HAVING count(student_id) > 1
 
 
8、查询学过“叶平”老师所教的所有课的同学的学号、姓名；
 
    同上，只不过将001和002变成 in (叶平老师的所有课)
 
9、查询课程编号“002”的成绩比课程编号“001”课程低的所有同学的学号、姓名；
    同第1题
 
 
10、查询有课程成绩小于60分的同学的学号、姓名；
         
    select sid,sname from student where sid in (
        select distinct student_id from score where num < 60
    )
 
11、查询没有学全所有课的同学的学号、姓名；
    思路：
        在分数表中根据学生进行分组，获取每一个学生选课数量
        如果数量 == 总课程数量，表示已经选择了所有课程
 
        select student_id,sname
        from score left join student on score.student_id = student.sid
        group by student_id HAVING count(course_id) = (select count(1) from course)
 
 
12、查询至少有一门课与学号为“001”的同学所学相同的同学的学号和姓名；
    思路：
        获取 001 同学选择的所有课程
        获取课程在其中的所有人以及所有课程
        根据学生筛选，获取所有学生信息
        再与学生表连接，获取姓名
 
        select student_id,sname, count(course_id)
        from score left join student on score.student_id = student.sid
        where student_id != 1 and course_id in (select course_id from score where student_id = 1) group by student_id
 
13、查询至少学过学号为“001”同学所有课的其他同学学号和姓名；
        先找到和001的学过的所有人
        然后个数 ＝ 001所有学科     ＝＝》 其他人可能选择的更多
 
        select student_id,sname, count(course_id)
        from score left join student on score.student_id = student.sid
        where student_id != 1 and course_id in (select course_id from score where student_id = 1) group by student_id having count(course_id) ＝ (select count(course_id) from score where student_id = 1)
 
14、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；
         
        个数相同
        002学过的也学过
 
        select student_id,sname from score left join student on score.student_id = student.sid where student_id in (
            select student_id from score  where student_id != 1 group by student_id HAVING count(course_id) = (select count(1) from score where student_id = 1)
        ) and course_id in (select course_id from score where student_id = 1) group by student_id HAVING count(course_id) = (select count(1) from score where student_id = 1)
 
 
15、删除学习“叶平”老师课的score表记录；
 
    delete from score where course_id in (
        select cid from course left join teacher on course.teacher_id = teacher.tid where teacher.name = '叶平'
    )
 
16、向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩；
    思路：
        由于insert 支持 
                inset into tb1(xx,xx) select x1,x2 from tb2;
        所有，获取所有没上过002课的所有人，获取002的平均成绩
 
    insert into score(student_id, course_id, num) select sid,2,(select avg(num) from score where course_id = 2)
    from student where sid not in (
        select student_id from score where course_id = 2
    )
     
17、按平均成绩从低到高 显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；
    select sc.student_id,
        (select num from score left join course on score.course_id = course.cid where course.cname = "生物" and score.student_id=sc.student_id) as sy,
        (select num from score left join course on score.course_id = course.cid where course.cname = "物理" and score.student_id=sc.student_id) as wl,
        (select num from score left join course on score.course_id = course.cid where course.cname = "体育" and score.student_id=sc.student_id) as ty,
        count(sc.course_id),
        avg(sc.num)
    from score as sc
    group by student_id desc        
 
18、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
     
    select course_id, max(num) as max_num, min(num) as min_num from score group by course_id;
 
19、按各科平均成绩从低到高和及格率的百分数从高到低顺序；
    思路：case when .. then
    select course_id, avg(num) as avgnum,sum(case when score.num > 60 then 1 else 0 END)/count(1)*100 as percent from score group by course_id order by avgnum asc,percent desc;
 
20、课程平均分从高到低显示（现实任课老师）；
 
    select avg(if(isnull(score.num),0,score.num)),teacher.tname from course
    left join score on course.cid = score.course_id
    left join teacher on course.teacher_id = teacher.tid
 
    group by score.course_id
 
 
21、查询各科成绩前三名的记录:(不考虑成绩并列情况)
    select score.sid,score.course_id,score.num,T.first_num,T.second_num from score left join
    (
    select
        sid,
        (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 0,1) as first_num,
        (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 3,1) as second_num
    from
        score as s1
    ) as T
    on score.sid =T.sid
    where score.num <= T.first_num and score.num >= T.second_num
 
22、查询每门课程被选修的学生数；
     
    select course_id, count(1) from score group by course_id;
 
23、查询出只选修了一门课程的全部学生的学号和姓名；
    select student.sid, student.sname, count(1) from score
 
    left join student on score.student_id  = student.sid
 
     group by course_id having count(1) = 1
 
 
24、查询男生、女生的人数；
    select * from
    (select count(1) as man from student where gender='男') as A ,
    (select count(1) as feman from student where gender='女') as B
 
25、查询姓“张”的学生名单；
    select sname from student where sname like '张%';
 
26、查询同名同姓学生名单，并统计同名人数；
 
    select sname,count(1) as count from student group by sname;
 
27、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
    select course_id,avg(if(isnull(num), 0 ,num)) as avg from score group by course_id order by avg     asc,course_id desc;
 
28、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；
 
    select student_id,sname, avg(if(isnull(num), 0 ,num)) from score left join student on score.student_id = student.sid group by student_id;
 
29、查询课程名称为“数学”，且分数低于60的学生姓名和分数；
 
    select student.sname,score.num from score
    left join course on score.course_id = course.cid
    left join student on score.student_id = student.sid
    where score.num < 60 and course.cname = '生物'
 
30、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名；
    select * from score where score.student_id = 3 and score.num > 80
 
31、求选了课程的学生人数
 
    select count(distinct student_id) from score
 
    select count(c) from (
        select count(student_id) as c from score group by student_id) as A
 
32、查询选修“杨艳”老师所授课程的学生中，成绩最高的学生姓名及其成绩；
     
    select sname,num from score
    left join student on score.student_id = student.sid
    where score.course_id in (select course.cid from course left join teacher on course.teacher_id = teacher.tid where tname='张磊老师') order by num desc limit 1;
 
33、查询各个课程及相应的选修人数；
    select course.cname,count(1) from score
    left join course on score.course_id = course.cid
    group by course_id;
 
 
34、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；
    select DISTINCT s1.course_id,s2.course_id,s1.num,s2.num from score as s1, score as s2 where s1.num = s2.num and s1.course_id != s2.course_id;
 
35、查询每门课程成绩最好的前两名；
 
    select score.sid,score.course_id,score.num,T.first_num,T.second_num from score left join
    (
    select
        sid,
        (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 0,1) as first_num,
        (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 1,1) as second_num
    from
        score as s1
    ) as T
    on score.sid =T.sid
    where score.num <= T.first_num and score.num >= T.second_num
 
36、检索至少选修两门课程的学生学号；
    select student_id from score group by student_id having count(student_id) > 1
 
37、查询全部学生都选修的课程的课程号和课程名；
    select course_id,count(1) from score group by course_id having count(1) = (select count(1) from student);
 
38、查询没学过“叶平”老师讲授的任一门课程的学生姓名；
    select student_id,student.sname from score
    left join student on score.student_id = student.sid
    where score.course_id not in (
        select cid from course left join teacher on course.teacher_id = teacher.tid where tname = '张磊老师'
    )
    group by student_id
 
39、查询两门以上不及格课程的同学的学号及其平均成绩；
 
    select student_id,count(1) from score where num < 60 group by student_id having count(1) > 2
 
40、检索“004”课程分数小于60，按分数降序排列的同学学号；
    select student_id from score where num< 60 and course_id = 4 order by num desc;
 
41、删除“002”同学的“001”课程的成绩；
    delete from score where course_id = 1 and student_id = 2
```



























