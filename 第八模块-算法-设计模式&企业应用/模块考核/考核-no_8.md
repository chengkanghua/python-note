



## 编程题

请用python实现一个单例模式

遍历给定目录，如输出D盘下所有的文件

## 问答题

1. Django 重定向是如何实现的？用的什么状态码？
2. django里 QuerySet 的 get 和 filter 方法的区别？
3. Django 对数据查询结果排序怎么做，降序怎么做，查询大于某个值怎么做?
4. django的orm中如何查询 id 不等于5的记录？
5. linux如何查看文件夹占用磁盘大小？
6. 列举熟悉的设计模式
7. 举例说明下Redis五种数据类型及应用场景
8. redis中数据库默认是多少个db 及作用？
9. redis是单进程还是单线程？
10. MySQL，什么是覆盖索引(索引覆盖)？
11. MySQL，普通索引和唯一索引的区别
12. 在对name做了唯一索引前提下，简述以下区别
```sql
select * from tb where name = "zhangkai";
select * from tb where name = "zhangkai" limit 1;
```
## 编程题答案

请用python实现一个单例模式

```plain
class Singleton(object):
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			cls._instance = super(Singleton, cls).__new__(cls)
		return cls._instance 
	
	def __init__(self, num):
		self.num = num
num1 = Singleton(10)
num2 = Singleton(20)
print(num1.num, num2.num)  # 20 20
print(id(num1), id(num2))  # 2467135043848 2467135043848
```
递归遍历给定目录，如输出D盘下所有的文件
```plain
import os
def recursion(root_path):
    """ 递归遍历给定目录 """
    path_list = os.listdir(root_path)
    for item in path_list:
        abs_path = os.path.join(root_path, item)
        if os.path.isdir(abs_path):
            print(f'\n[{root_path}] 下的 [{item}] 目录\n')
            recursion(abs_path)
        else:
            print(f'[{root_path}] 下的 [{item}] 文件')
recursion(r"D:\tmp\web\root")
"""
[D:\tmp\web\root] 下的 [dir_a] 目录

[D:\tmp\web\root\dir_a] 下的 [dir_a_dir_a] 目录
[D:\tmp\web\root\dir_a\dir_a_dir_a] 下的 [dir_a_dir_a_file_a.txt] 文件
[D:\tmp\web\root\dir_a\dir_a_dir_a] 下的 [dir_a_dir_a_file_b.txt] 文件
[D:\tmp\web\root\dir_a] 下的 [dir_a_file_a.txt] 文件
[D:\tmp\web\root\dir_a] 下的 [dir_a_file_b.txt] 文件
[D:\tmp\web\root] 下的 [dir_b] 目录

[D:\tmp\web\root\dir_b] 下的 [dir_b_dir_a] 目录
[D:\tmp\web\root\dir_b\dir_b_dir_a] 下的 [dir_b_dir_a_file_a.txt] 文件
[D:\tmp\web\root\dir_b\dir_b_dir_a] 下的 [dir_b_dir_a_file_b.txt] 文件
[D:\tmp\web\root] 下的 [dir_c] 目录
[D:\tmp\web\root\dir_c] 下的 [dir_c_file_a.txt] 文件
[D:\tmp\web\root\dir_c] 下的 [dir_c_file_b.txt] 文件
[D:\tmp\web\root] 下的 [file_a.txt] 文件
[D:\tmp\web\root] 下的 [file_b.txt] 文件
[D:\tmp\web\root] 下的 [file_c.txt] 文件
"""
```
## 问答题答案

Django 重定向是如何实现的？用的什么状态码？

```plain
使用HttpResponseRedirect
redirect和reverse
状态码：302,301
```
django里 QuerySet 的 get 和 filter 方法的区别？
```plain
get 的参数只能是model中定义的那些字段，只支持严格匹配
filter 的参数可以是字段，也可以是扩展的where查询关键字，如in，like等【返回值】
get 返回值是一个定义的model对象
filter 返回值是一个新的QuerySet对象，然后可以对QuerySet在进行查询返回新的QuerySet对象，支持链式操作QuerySet一个集合对象，可使用迭代或者遍历，切片等，但是不等于list类型(使用一定要注意)
get 只有一条记录返回的时候才正常,也就说明get的查询字段必须是主键或者唯一约束的字段。
当返回多条记录或者是没有找到记录的时候都会抛出异常
filter 有没有匹配的记录都不报错
```
Django 对数据查询结果排序怎么做，降序怎么做，查询大于某个字段怎么做?
```plain
排序使用order_by()
  如：按照 id 从小到大查询数据,Doc.objects.order_by('id')
降序需要在排序字段名前加-
  如：按照 id 从大到小查询数据，只需要在字段前加 - 即可 
  Doc.objects.order_by('-id')
查询字段大于某个值：使用filter(字段名_gt=值)
随机排序，性能较差，不推荐，Doc.objects.order_by('?')
```
django的orm中如何查询 id 不等于5的记录？
```plain
models.Project.objects.exclude(pk=5)
```
linux如何查看文件夹占用磁盘大小？
```plain
du -s	# 使用此选项时，du只显示目录所占用磁盘空间的大小，而不显示其下子目录和文件占用磁盘空间的信息
du -a 	# 使用此选项时，显示目录和目录下子目录和文件占用磁盘空间的大小
```
列举熟悉的设计模式
```plain
设计模式有：
工厂模式、抽象工厂模式、单例模式、建造者模式、原型模式、
适配器模式、桥接模式、过滤器模式、组合模式、装饰器模式、
外观模式、享元模式、代理模式、责任链模式、命令模式、解释器模式、
迭代器模式、中介者模式、备忘录模式、观察者模式等等。
```
举例说明下Redis五种数据类型及应用场景
```plain
string:
  session 共享
  常规计数：评论数、粉丝数、礼物数、订阅数
hash:
  数据缓存
list:
  消息队列系统
  最新的微博消息，比如我们将最新发布的热点消息都存储到Redis中，
    只有翻看"历史久远"的个人信息，这类冷数据时，才去MySQL中查询
set:
  适用于各种需要求交集、并集、差集的场景，比如共同好友，共同关注的场景。
zset:
  各种排行榜，音乐排行榜、热点新闻榜
```
redis中数据库默认是多少个db 及作用？
```plain
Redis 一个实例下有 16 个：0 - 15
相当于不同的库
```
redis是单进程还是单线程？
```plain
Redis是单线程的模式，它是利用队列技术将并发访问改为串行访问，
消除传统的传统数据库的串行操作开销
```
MySQL，什么是覆盖索引？
```sql
覆盖索引又可以称为索引覆盖:查询辅助索引的时候不需要进行回表操作,
即你查询的内容刚好是你的索引.
就是select的数据列只用从索引中就能够取得，
不必从数据表中读取，换句话说查询列要被所使用的索引覆盖
```
MySQL，普通索引和唯一索引的区别
```sql
普通索引只有加速功能；而唯一索引还对索引列有唯一约束功能。
```
在对name做了唯一索引前提下，简述以下区别
```plain
select * from tb where name = "zhangkai"
select * from tb where name = "zhangkai" limit 1
如果是唯一索引的话两者本质上没有什么区别，都是查询到一条数据后就不往下查询了，
但是如果不是唯一索引的前提下，第二种加limit的当查询到一条数据后就不往下执行了，
而第一种还是需要继续查询
```