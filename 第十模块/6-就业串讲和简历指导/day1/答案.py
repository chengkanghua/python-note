# 第一题
编译型语言:一次性把代码都编译成二进制,然后运行
解释型语言:一行一行,编译一句,运行一句
1.python 解释型 简洁高效,容易上手
2.java   混合型(JVM,JIT编译器),开发周期慢,突出在web方向
3.c      编译型 属于计算机底层语言,只有面向过程,没有面向对象
4.c++	 编译型 属于计算机底层语言,既有面向过程,也有面向对象
5.go	 编译型 应用在区块链,高并发高可用,也可以突出在游戏领域

# 第二题
# python2.x
	1.print "123"
	2.range 返回列表
	3.默认编码 -- ascii
	4.两种类: 经典类 和 新式类
		class Car():pass  经典类(多继承当中的搜索原则采用深度优先)
		class Car(object):pass 新式类(多继承当中的搜索原则采用广度优先)
	5.除法/: 结果是整型
	6.int(4) long(长整型8)
	7.raw_input <=> python3.x input
	
	
# python3.x
	1.print("12")
	2.range 返回的是 可迭代对象
	3.默认编码 utf-8
	4.都是新式类(广度优先)  类.mro() => 继承关系列表
	5.除法/: 结果是小数
	6.int
	7.input
	
# 第三题
# 逻辑运算符优先级 () > not > and > or
逻辑短路
True or print(111)	
False and print(222)

and 逻辑与 全真则真 一假则假
or  逻辑或 全假则假 一真则真

布尔值为假的十种情况:
0 0.0 False 0j '' () [] set() {} None

复数: 实数 + 虚数
"""
复数: 3 + 4j
实数: 3  虚数: 4j
如果有一个数,他的平方等于-1,那么这个数就是j
科学家认为有,表达高精度类型;
"""

v1 = 1 or 2
print(v1)
	
v2 = 3 and 7 or 9 and 0
# v2 = 7 or 0
print(v2)
	
	
# 第四题
"""逗号是区分是否是元组的标识符"""
v1 = [1,2,3]
v2 = [(1),(2),(3)]
v3 = [(1,),(2,),(3,)]
# v1 列表  v2 列表 v3里面的元素是元组
	
# 第五题
# python特有
a,b = b,a
# 方法二
tmp = a
a = b
b = tmp
	
# 第六题
	单双引号没有任何区别,三引号可以支持跨行
	在引号互相嵌套时,里面不能使用相同的引号

# 第七题
	is 是判断内存地址是否相同
	== 判断两边的值是否相同

# 针对于整型 在-5 ~ 正无穷 [python3.6之前有效]
var1 = -100
var2 = -100
print(var1 is var2)


# 第八题
# int float complex bool str list tuple set dict
tuple(数据)  list(数据)

# 字典的键 和 集合的值 有数据类型上的要求
Number ( int float complex bool) str tuple (可哈希 不可变的数据类型)

# 强转成字典,对数据类型的要求是?
""" 里面容器的元素个数都相同 是等长  """
等长的二级容器,并且元素个数是2个
print(  dict([("a",1),["b",2]]) )

dict([ ("a",[1,2,3]) , ["b" , 456] ])
dic = {"a":1,"b":2}

# 第九题
name[::-1]

# 第十题
交集 & 
集合.intersection(集合2)

差集 -
difference

并集 | 
union

对称差集 ^
symmetric_difference

# 第十一题
"""非空集合且不为子父关系的两个集合"""

"""
x = {1,2,5}
y = {2,8}
y != x - (x-y)

{2,8} != {1,2,5} - {1,5}
{2,8} != {2}
"""

# 第十二题
# 浅拷贝
# 1
# import copy
# 2
# lst = [1,2,3].copy()
# 3 切片
# lst[:] 或者  lst[::]

lst = [1,2,3]
lst2 = lst[:]
lst.append(4)
print(lst,lst2)

# 深拷贝
import copy
copy.deepcopy()
[1,2,34,5,[3,4,5]]

# 第十三题
# 赋值 : 将变量和值在内存中形成映射指向关系
# 浅拷贝: 只拷贝第一层级里的所有元素,单独开辟空间成型独立的一份副本 copy.copy()
# 深拷贝: 所有层级的元素都单独拷贝一份,开辟全新的空间
"""
(地址:原不可变数据只是暂时的指向原数据,可变的数据独立开辟新空间)
"""
"""
import copy
lst1 = [1,2,3,[4,5,6]]
lst2 = copy.deepcopy(lst1)

lst2[0] = 100
print(lst1,lst2)
print( id(lst1[-1]) , id(lst2[-1]) )
"""
	
# 第十四题
# 占位

# 第十五题
import copy
a = [1,2,4,5,['b','c']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)
a[4].append('d')
# a,b 百分百一样
print(b) #[1,2,4,5,['b','c',"d"],5]
print(c) #[1,2,4,5,['b','c',"d"]]
print(a) #[1,2,4,5,['b','c',"d"],5]

# 第十六题
# 9成9乘法表
# while 写法
i = 1
while i<=9:
	# 打印表达式
	j = 1
	while j<=i:
		print("%d*%d=%2d " % (i,j,i*j) ,end="" )
		j+=1
	# 打印换行	
	print()
	i+=1

# for 写法
for i in range(1,10):
	# 打印表达式
	for j in range(1,i+1):
		print("%d*%d=%2d " % (j,i,i*j) ,end="" )
		
	# 打印换行
	print()

# 第十七题
# 1 1 2 3 5 8 13 21 34 .。。。
# 方法一
lst = [1,1]
for i in range(10):
	lst.append(lst[-1] + lst[-2])
print(lst)

# 方法二
a,b = 0,1
for i in range(10):
	print(b)
	a,b = b,a+b

# 方法三
def fib(n):
	if n <= 2:
		return 1
	# n n-1 n-2
	# 结果 = 上一个值 + 上上个值
	return fib(n-1) + fib(n-2)
print(fib(5))


"""

def fib(n):
	if n <= 2:
		return 1
	# 结果 = 上一个值 + 上上个值
	return fib(n-1) + fib(n-2)
print(fib(5))

1 1 2 3 5

# return 后面的值算完了才能通过return 进行返回
return  3 + 2 => 5
return  fib(4) => 3              +        fib(3)    => 2
	fib(3) + fib(2) => 1            fib(2) + fib(1) => 1 + 1
fib(2) + fib(1) => 1 + 1 => 2

调用函数时候,每调用一次,都需要在内存当中开辟一个栈帧空间
递归就是不停的开辟空间和释放空间的过程
递: 去
归: 回 
一去一回是递归

触发递归回的过程有两个条件:
	(1) 最后一层栈帧空间代码全部执行完毕,触发回的过程,回到上一层空间的调用处;
	(2) 最后一层栈帧空间代码遇到了return,触发回的过程,回到上一层空间的调用处;

"""




# 第十八题
list(set(lst))

# 第十九题
from collections import Iterator,Iterable
fp = open("文件",mode="r",encoding="utf-8")
# 方法一 fp 是迭代器
for i in fp:
	print(i) # 按照文本中的行进行遍历.

# 方法二
with open("文件",mode="r",encoding="utf-8") as fp:
	res = fp.read(100)
	while res:
		print(res)
		res = fp.read(100)


# 第二十题
# zip 拉链  返回迭代器
it = zip( ("a","b") , [1,2] )
print(it)

dic = dict(zip( ("a","b") , [1,2] ))
print(dic)

a = dict(zip(  ("a","b","c","d","e"),(1,2,3,4,5)  )  ) 
print(a)

# enumerate 枚举 返回迭代器
it = enumerate( ["a","b"] )
it = enumerate( ["a","b"] , start=1) # start 指定枚举值
dic = dict(it)
print(dic)

# 第二十一题
lambda 匿名函数 : 用一句话来表达只有返回值的无名函数
lambda 参数 : 返回值

# 第二十二题
# *arg     普通收集参数 : 收集多余没人要的普通实参
# **kwargs 关键字收集参数: 收集多余没人要的关键字实参

# 第二十三题
def func():
	global a
	a = 90
func()
print(a)

# 第二十四题
filter => 过滤数据
filter(函数,iterable)
# 保留偶数 , 过滤掉所有的奇数
lst = [1,2,3,4,5]
it = filter(lambda x : True if x % 2 == 0 else False , lst)
print(list(it))


# map -> 处理(映射)数据
map(func,iterable) => 迭代器
lst = [1,2,3]
it = map(lambda x : x * 3, lst)
print(list(it))


# reduce -> 计算数据(一次性计算两个参数)
reduce(func,iterable) => 计算的结果
from functools import reduce
res = reduce(lambda x,y : x*10 + y , lst)
print(res)
"""
[5,4,8,8] => 5488

5 * 10 + 4 = 54
54 * 10 + 8 = 548 
548 * 10 + 8 = 5488
"""

# 第二十六题

官方说法1000  实际是994 ~ 1000 层
设置递归最大层数
import sys
sys.setrecursionlimit(99999999999999999)

# 第二十七题
迭代器:    迭代数据的工具
可迭代对象:可以迭代的数据
可迭代对象 => 迭代器
把不能够直接通过next获取的数据 => 可以直接被next获取数据

dir(数据) => 查看该数据的内部成员
具有 __iter__() 和 __next__() 两个方法的是迭代器
具有 __iter__() 可迭代对象

# 第二十八题
生成器的本质就是迭代器,可以自定义迭代的逻辑
创建方式两种
	(1) 生成器表达式(推导式)  (i for i in range(10))
	(2) 生成器函数  (含有yield 关键字)

# 陷阱 tuple([i for i in range(10)]) => 强制转换成元组

# 第二十九题
# 装饰器: 再不改变原有代码的情况下,为原函数扩展新功能
# 闭包:
	# (1)互相嵌套的两个函数,内函数使用了外函数的局部变量
	# (2)外函数把内函数返回出来的过程,是闭包,内函数是闭包函数;
# 装饰器的本质就是闭包
# 应用:登录认证,框架(django,flask,@app.route("/",method=["GET","POST"]))



# 第三十题
# 通过字符串去操作类对象 或者 模块当中的属性方法
# hasattr  getattr() setattr() delattr()
# 可以配合用户的输入,进行动态操作,调用其中的成员 | 通过api接口调用


def func(x):
	pass
func(x)
0 4 5 7 8 5 2


lst = [7,-8,5,4,0,-2 ,-5]
def func(x):	
	if x >= 0:
		return x
	else:
		return abs(x)+x
res = sorted(lst,key=func)
print(res)







