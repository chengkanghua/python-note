# 编程题
# 请用python实现一个单例模式

# 遍历给定目录，如输出D盘下所有的文件



# 问答题

# Django 重定向是如何实现的？用的什么状态码？
'''
return  redirect()
状态码 301
'''
# django里 QuerySet 的 get 和 filter 方法的区别？
'''
get参数只能是model中定义的字段   返回值是一个定义的model对象   ，不存在的值会报错
filter可以是字段，还可以扩展 where in  like    返回一个queryset   # 不存在返回空
QuerySet 是一个 集合对象   还可以做二次查询 遍历 切片


'''

# Django 对数据查询结果排序怎么做，降序怎么做，查询字段大于某个值的怎么做?
'''
排序使用 结果集.order_by('字段').all()
降序     字段前面加-
models.objects.filter(条件).order_by('-字段').all()

filter(id_gt=5)
'''


# django的orm中如何查询 id 不等于5的记录？
'''
models.objects.filter.exclude(id="5").all()
'''

# linux如何查看文件夹占用磁盘大小？
'''
du -sh /root
'''

# 列举熟悉的设计模式
'''
设计模式有：
工厂模式、抽象工厂模式、单例模式、建造者模式、原型模式、
适配器模式、桥接模式、过滤器模式、组合模式、装饰器模式、
外观模式、享元模式、代理模式、责任链模式、命令模式、解释器模式、
迭代器模式、中介者模式、备忘录模式、观察者模式等等。

'''
# 举例说明下Redis五种数据类型及应用场景
'''
字符串（strings）    # 常用，字符串可以存json格式  用做网站内容的缓存服务器  计数
散列（hashes）       # 类似 python的dict  
列表（lists）        # 消息队列  先进先出  微博热榜20个
集合 （sets）        # 出重 ， 交集 并集 差集 ， 共同推荐  
有序集合（sort sets） # 可以用做数据的排名  点击量  播放量

'''
# redis中数据库默认是多少个db 及作用？
'''
默认有16个db 
'''
# redis是单进程还是单线程？
'''
单线程

'''
# MySQL，什么是覆盖索引(索引覆盖)？
'''
指一条查询语句的执行只用从索引中就能够取得，无需回表查询

'''
# MySQL，普通索引和唯一索引的区别
'''
普通索引被索引的数据列可以包含重复的值。
唯一索引不允许出现重复的值

使用的数据结构都是 b-tree  ，时间复杂度 o（log n）
'''
# 在对name做了唯一索引前提下，简述以下区别
# select * from tb where name = "zhangkai";
# select * from tb where name = "zhangkai" limit 1;
'''
没区别， 唯一索引表示name 不会重复 ，查询到即返回， 不会向后继续检索
'''
