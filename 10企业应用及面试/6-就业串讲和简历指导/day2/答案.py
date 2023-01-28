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

# 第三十一题
"""
装饰器的本质是闭包
闭包特点:可以延长局部变量的生命周期
"""
def wrapper(func):
	def inner(*args,**kwargs):
		res = func(*args,**kwargs)
		print("新添加一句话")
		return res
	return inner
	
@wrapper
def func():
	print("心中存有一丝希望,终将带你走向光明 --正道的光")

func()
"""
@符功能
1.先把装饰器修饰的函数当成参数传递给装饰器
2.将新函数返回,去替换旧函数  func = inner
"""


# 第三十二题
# 定义一个装饰器
def outer(n):
	def wrapper(func):
		def inner1(*args,**kwargs):
			res = func(*args,**kwargs)
			print("我是金角大王")
			return res			
			
		def inner2(*args,**kwargs):
			res = func(*args,**kwargs)
			print("我是银角大王")
			return res
			
		if n == "alex":
			return inner1
		else:
			return inner2
	return wrapper
	
# 先去执行outer("alex") => @wrapper => @发动技能
# 1.把func当成参数传递给wrapper
# 2.func = inner1
@outer("alex")
def func():
	print("how are you ?")

func()


# 第三十三题
def num():
	return [lambda x:i*x for i in range(4)]
# print([m(2) for m in num()])

# (1) 辨别 我到底是什么?
# 推导式    (正确)
[lambda x:i*x        for i in range(4)]

# lambda表达式
func = lambda x    :    [i*x for i in range(4)]
func(3)


# (2) 对原表达式进行拆解 
def num():
	lst = []
	for i in range(4): # 0 1 2 3 
		def func(x):
			return i*x 
		lst.append(func)
	return lst



lst = num()
print(lst)

print([m(2) for m in num()])

lst_new = []
for m in [func1,func2,func3,func4]:
	lst_new.append(m(2))
print(lst_new) # [6 , 6 , 6 , 6]

# ### 理解概念1
# 函数的定义处 和 函数的调用处
def func():
	print(123)

# 只有在调用的时候,才会去执行函数内的代码,不调用的话,不执行;
func()


# ### 理解概念2
for i in range(4):
	print(i)

# 此刻的i到底是多少?
print(i)


# ### 理解概念3 : 为什么可以拿到i=3的这个值(因为是闭包)
"""
在for循环里 i这个变量在内函数func里面被使用了
内函数使用了外函数的局部变量,该变量会延长生命周期,
暂时不释放,把 i = 3的这个值给与保留,以备下次使用
"""


# 第三十四题
b参数(默认参数)身上的值是列表,提前在内存中开辟好空间,进行存储
	如果用户传递实参,那么使用用户自己的值,
	如果用户没有传递实参,那么使用内存存好的列表值

# 第三十五题
def func(a,b=[]):
	b.append(a)
	return b
v1 = func(1) # [1]
v2 = func(2,[10,20]) # [10,20,2]
v3 = func(3) # [1,3]
print(v1,v2,v3)


def func(a,b=[]):
	b.append(a)
	return b
v1 = func(1)
print(v1)
v2 = func(2,[10,20])
print(v2)
v3 = func(3)
print(v3)


# 第三十七题
"""
ljust 原字符串居左,填充符号
rjust 原字符串居右,填充符号
"""
ip = "10.3.9.12"
strvar = ""
for i in ip.split("."):
	bin_str = str(bin(int(i)))[2:]
	print(bin_str)
	# 补8位,不够8位的拿0来补位
	strvar +=  bin_str.rjust(8,"0")
print(strvar)
# 把二进制字符串转换成十进制(默认)
print(int(strvar,2))

# 方法二
ip = "10.3.9.12"
strvar = ""
for i in ip.split("."):
	# 8 总长度8位 0 拿0来补齐8位 b代表二进制
	strvar += format(int(i) , "08b")
print(strvar)
print(int(strvar,2))

# rjust
res = "alex".rjust(10,"z")
print(res) # zzzzzzalex 总长度加一起是10个;

# 第三十八题
import os
def getallsize(pathvar):
	size = 0
	lst = os.listdir(pathvar)
	# print(lst)
	for i in lst:
		pathvar2 = os.path.join(pathvar,i)
		# 判断是否是文件
		if os.path.isfile(pathvar2):
			size += os.path.getsize(pathvar2)
		# 判断是否是文件夹
		elif os.path.isdir(pathvar2):
			size += getallsize(pathvar2)
			
	return size

pathvar = r"E:\python26_27\two\ceshi"
res = getallsize(pathvar)
print(res)

# 方法二
import os
pathvar = r"E:\python26_27\two\ceshi"
gen = os.walk(pathvar)
size = 0
for root , dirs , files in gen:
	for name in files:
		pathvar = os.path.join(root,name)
		# print(pathvar)
		size += os.path.getsize(pathvar)

print(size)


# 第三十九题
# floor 地板   向下取整
# ceil  天花板 向上取整
import math
print(math.floor(5.5))
print(math.floor(5.1))


# 第四十题
from functools import reduce
# 在装饰器中使用,保留原函数的属性,加上wraps
from functools import wraps

def wrapper(func):
	@wraps(func)
	def inner(*args,**kwargs):
		res = func(*args,**kwargs)
		print("我是alex")
		return res
		
	return inner

@wrapper
def func():
	print("我是最棒的")
	return 123
res = func()
print(res) 
# print(func) # <function func at 0x000001D9F7F13378>


# 第四十一题
"""
match : 必须从字符串的开头进行匹配
search: 从任意位置开始,匹配到就返回
"""

# 第四十二题
. 除了\n的任意字符
* ? + {3,10} 都是量词
在量词的后面 + ? => 非贪婪
.*  贪婪匹配   按照最多值进行匹配
.*? 非贪婪匹配 按照最少值进行匹配



<.> 匹配除了\n之外的一个字符
<.?>匹配除了\n之外的一个字符或者0个字符
<.*?>

# 第四十三题
import random
random.random  随机获取 0 <= x < 1
random.randrange 随机获取指定范围内的整数 用法同range
random.uniform   随机获取指定范围内的小数

# 第四十四题
# super 可以调用父类的属性或方法,用来解决多继承之间复杂的调用关系
"""
类.mro() => 返回继承关系的调用顺序列表
super在调用父类属性或者方法的时候,
会按照mro列表中的继承顺序依次的调用
"""

# 第四十五题
封装:  公有public  私有 private  受保护的 protected
python : 公有成员  私有成员:2个下划线来表达私有成员
受保护的: 在python中有一个约定俗称的写法,在成员的前面加一个下划线_
(可以在继承的子类当中使用,但是无法在类外调用)

双下划线 __init__ __call__ __new__ ....

# 第四十六题
@staticmethod  静态方法
	无论是类还是对象,都可以调用,不会默认传递任何参数
@classmethod   类方法
	无论是类还是对象,都可以调用,默认传递类这个参数

# 第四十七题
# 单例(态)模式 : 这个类无论实例化多少次,都有且只有一个对象
"""
目的:节省内存空间,提高运行效率,应用在多人操作场景中.
没生成一个对象,都会在内存中占用空间,单例模式可以减少对象的创建;
多人操作时,公用同一个类:比如操作mysql的增删改查
"""

from threading import Lock
class Ceshi():
	__obj = None
	lock = Lock()
	
	def __new__(cls,*args,**kwargs):
		with cls.lock:
			if not cls.__obj: # None 空的
				cls.__obj = object.__new__(cls)
			return cls.__obj
	
obj1 = Ceshi()
obj2 = Ceshi()
obj3 = Ceshi()
print( id(obj1) , id(obj2) , id(obj3))

# 第四十八题
栈: 先进后出  或 后进先出
队列: 先进先出

# 第四十九题
class Parent(object):
	x = 1
class Child1(Parent):
	pass
class Child2(Parent):
	pass
	
# 1 1 1
print(Parent.x, Child1.x, Child2.x)
# 1 2 1
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
# 3 2 3
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)

# 第五十题
'''面向对象的上下文管理 with语法的具体实现'''
class Context:
	# 在使用with语法的时候,自动触发,功能可以返回对象
	def __enter__(self):
		return self
	
	# 执行完with语法之后,执行的收尾操作
	def __exit__(self,exc_type, exc_val, exc_tb):
		print("close")
		
	def do_something(self):
		print("我是do_thing'")
	
# 为Content()实例化的对象赋值一个别名 名字叫做ctx
with Context() as ctx:
	ctx.do_something()

# 附加题
# 1
lst = [1,2,3,100,200,200,100]
setvar = set(lst)
lst_new = sorted(setvar)
print(lst_new)
print(lst_new[-2])

# 2,3
计数器,垃圾回收,缓存池
# 1.计数器
特点: 
a = 100 (100计数为1,被引用过1次)
b = a   (100计数位2,被引用过2次)
del b   (100计数为1,被引用过1次)
100什么时候会被彻底的删除?就是在引用计数为0的时候,彻底删除
(没有任何变量引用100这个值,100会在内存中被删掉)


# 2.分代回收 和 标记清除 (用来辅助计数引用)
标记清除 : 用来解决循环引用出现的问题,避免删不掉;
第0代 新生代
第1代 老年代
第2代 永久代

分代回收 : 
	import gc
	print(gc.get_threshold())
	(700, 10, 10)
	# 参数1, 700 新增的对象-消亡对象个数 == 700 会触发垃圾检测时机
	# 参数2, 10 代表: 当第0代对象检测次数达到10次,会触发第0代和第1代对象的检测
	# 参数3, 10 代表: 当第1代对象检测次数达到10次,会触发第0代和第1代和第2代对象的检测

# 3.缓存池
	"""为了避免频繁创建销毁标量,影响效率,提前缓存一下数据"""
	1.-5 ~256 公用对象,常驻内存
	2.单个字符,公用对象,常驻内存
	3.不可变类型,默认开启inern驻留机制;
	


# 附加题 第四题


















