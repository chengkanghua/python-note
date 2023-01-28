# python 面试重点 (基础)

第一部分 必答题

1.   简述列举了解的编程及语言间的区别?

2.   列举python2 和python3的区别?

3.   看代码写结果

     ```
     v1 = 1 or 2
     v2 = 3 and 7 or 9 and 0
     ```

4.   比较一下值有什么不同?

     ```
     v1 = [1,2,3]
     v2 = [(1),(2),(3)]
     v3 = [(1,),(2,),(3,)]
     ```

5.   用一行代码实现数值交换.

     ```
     a = 1
     b = 2
     ```

6.   Python中单引号、双引号、三引号的区别

7.   is 和 ==的区别?

8.   python里如何实现tuple和list的转化?

9.   如何实现字符串 `name='老男孩'` 的反转?

10.   两个set如何获取交集、并集、差集?

11.   哪些情况下y!=x-(x-y) 会成立?

12.   Python中如何拷贝一个对象?

13.   简述 赋值、浅拷贝、深拷贝的区别?

14.   pass的作用?

15.   阅读代码写结果.

      ```
      import copy
      a = [1,2,4,5,['b','c']]
      b = a
      c = copy.copy(a)
      d = copy.deepcopy(a)
      
      a.append(5)
      a[4].append('d')
      
      print(b)
      print(c)
      print(a)
      ```

16.   用Python 实现9*9乘法表.

17.   用Python显示一个斐波那契数列.

18.   如何删除列表中重复的值?

19.   一个大小为100G的文件etl_log.txt,要读取文件中的内容,写出具体过程代码?

20.   a = dict(zip(("a","b","c","d","e"),(1,2,3,4,5))) 请问a是什么?

21.   lambda关键字的作用?

22.   *arg和**kwargs作用?

23.   如何在函数中设置一个全局变量?

24.   filter 、map、reduce的作用?

25.   什么是匿名函数?匿名函数有什么作用?

26.   Python递归的最大层数?

27.   什么是迭代器?什么是可迭代对象?

28.   什么是生成器?

29.   什么是装饰器及应用场景?

30.   什么是反射及应用场景?

31.   写一个普通的装饰器.

32.   写一个带参数的装饰器.

33.   求结果

      ```python
      def mum():
        return[lambda x:i*x for i in range(4) ]
      print([m(2) for m in num()])
      ```

34.   def(a,b=[]) 这种写法有什么陷阱?

35.   看代码写结果

      ```
      def func(a,b=[]):
      		b.append(a)
      		return b
      
      v1 = func(1)
      v2 = func(2,[10,20])
      v3 = func(3)
      print(v1,v2,v3)
      
      ```

36.   看代码写结果

      ```python
      def func(a,b=[]):
      		b.append(a)
          return b
       
      v1 = func(1)
      print(v1)
      v2 = func(2,[10,20])
      print(v2)
      v3 = func(3)
      print(v3)
      
      ```

37.   请编写一个函数实现将IP地址转换成一个整数.

      ```tex
      如 10.3.9.12 转换规则为:
      		10       00001010
      		 3		 00000010
      		 9		 00001001
      		12 		 00001100
      
      再将以上二进制拼接起来计算十进制结果: 00001010 00000011 00001001 00001100
      ```
      
38.   请查找一个目录下的所有文件(可能存在文件嵌套)。

39.   求结果

      ```python
      import math
      print(math.floor(5.5))
      ```

40.   是否使用过functools中的函数？其作用是什么？

41.   re的match和search区别？

42.   用Python匹配HTML tag的时候，<.> 和<.?>有什么区别？

43.   如何生成一个随机数？

44.   super的作用？

45.   双下划线和单下划线的区别？

46.   @staticmethod 和 @classmethod的区别？

47.   实现一个单例模式（加锁）。

48.   栈和队列的区别？

49.   以下代码输出是什么？请给出答案并解释。

      ```python
      class parent(object):
          x = 1
          
      class Child1(parent):
          pass
      class Child2(parent):
          pass
      ```
      
50. 参考下面的代码片段
    
    ```python
    class Context:
        pass
    
    with Content() as ctx:
        ctx.do_something()
    请在Context类下添加代码完成该类的实现
    ```
    
    
    
    # 第二部分 可选题
    
    1.   如何获取列表中第二大的值？
    2.   简述Python内存管理机制。
    3.   简述Python的垃圾回收机制。
    4.   请用两个队列实现一个栈。
    5.   请用Python实现一个链表。
    6.   请用Python实现链表的逆转。 
    
    
    
      
    
      
    

















































