# （选做题）用map来处理列表,把列表中所有人都变成xx_666，如张开_666,
'''
name = ["张开", "李开", "王开", "赵开"]
new_name= [i for i in map( lambda x: x+'_666',name)]
print(new_name)
'''

# （选做题）使用map来处理列表，将列表中每个人的名字都变成以xx_666，如张开_666
# tmp_list = [{'name': '张开'}, {'name': '李开'}, {'name': '王开'}, {'name': '赵开'}]
#
# new_list= map(lambda x: x["name"].replace(x["name"],x["name"]+"_666") ,tmp_list)
# print(new_list)
# for i in new_list
#     print(i)

# a = "张开"
# a=a.replace(a,a+'_666')
# print(a)
# （选做题）将下面的列表内的元素以age升序排序：
'''
tmp_list = [
    {'name': '张开', 'age': 18},
    {'name': '李开', 'age': 8},
    {'name': '王开', 'age': 32},
    {'name': '赵开', 'age': 25}
]
new_list = sorted(tmp_list,key=lambda x: x["age"])
print(new_list)
'''

# 请将时间'2018-11-11 11:11:11'转换成时间戳时间
# import datetime
# str1 = '2018-11-11 11:11:11'
# datetime.

# 使用函数完成三次登录，要求是用户名和密码都保存在一个info.txt中，info.txt自行创建
#     info文件内容格式如下：
#         zhangkai|123
#         likai|123
#         root|123
#     且info.txt文件中存储有多个用户名和和密码，每个用户名和密码占用一行。
#     三次登录失败即退出程序。
'''
# db_dict
db_dict = {}
with open("info.txt",mode='rt',encoding='utf-8') as f_r:
    for line in f_r:
        line_list = line.strip().split("|")
        db_dict[line_list[0]] = line_list[1]

#循环登陆
i = 0
while i< 3:
    username = input('please uname: ')
    password = input('please password: ')
    if not db_dict.get(username):
        print(f'第{i+1}次： 账号错误，请重试')
        i += 1
        continue
    pw = db_dict.get(username)
    if password != pw :
        print(f'第{i+1}次：密码错误，请重试')
        i += 1
        continue
    print('登陆成功')
    break
'''

# 文件操作，使用Python将图片新建一个副本，比如有图片a,使用Python得到新的图片b
'''
with open('a.png',mode='rb') as f_r,open('b.png',mode='wb') as f_w:
    data = f_r.read()
    f_w.write(data)
'''
# 使用相关模块生成6位的验证码，得到的验证码必须是字符串，而且必须包括随机数字、随机小写字符、随机大写字符
'''
import string
import itertools
import random
#生成基础数据列表
data = list([i for i in itertools.chain(string.digits,string.ascii_uppercase,string.ascii_lowercase)])
#随机生成验证，传值数字表示取几位的验证码
def sixcode(num: int):
    li = []
    for i in range(num):
        num=random.randint(0,len(data))
        li.append(data[num])
    str1 = ''.join(li)
    return str1
num = sixcode(6)
print(num)
'''

# 实现一个统计函数执行时间的装饰器
'''
import time
import functools
#装饰器
def other(func):
    # functools.wraps()
    def inner(*args,**kwargs):
        start_time = time.time()
        st = func(*args,**kwargs)
        stop_time = time.time()
        print('函数执行花费时间秒:{}'.format(stop_time-start_time))
        return st
    return inner

#普通函数
@other
def func():
    print('111')
    return 1
func()
'''
# 写函数,接收两个数字参数,将较小的数字返回.
'''
func = lambda x,y:y if x > y else x
print(func(5,55))
'''

# 如何获取当前脚本的绝对路径
'''
import os
file_path = os.path.abspath(__file__)
print(file_path)
'''

# 如何获取当前脚本的父级目录
'''
import os
file_path = os.path.dirname(__file__)
print(file_path)
'''

# 有派3.1415926  如何保留小数位？ 请用内置函数实现，注意不能使用切片，也不能使用字符串格式化
'''
pi = 3.1415926
new_pi = round(pi,2)
print(new_pi)
'''


# 什么是可迭代对象(问答题，可先略过)
#
# 什么是迭代器(问答题，可先略过)
#
# 可迭代对象和迭代器的区别是什么(问答题，可先略过)
#
# 什么是生成器，如何得到一个生成器

# def gen(num: int):
#     for i in range(num)
#         yield i
#
# gen(1000)
# 写函数，完成给一个列表去重的功能。（不能使用set集合）[1,2,2,1,3,4,5,6]
'''
data = [1,2,2,1,3,4,5,6]
def single(data: list):
    new_data = []
    while True:
        if len(data) > 0:
            a = data.pop()
            new_data.append(a)
            for i in data:
                if i == a:
                    data.remove(i)
        else:
            break
    return new_data

data =single(data)
print(data)
'''
# 有d = {'a': 1, 'b': 2, 'c': 3},请使用json将它序列化到文件
'''
import json
d = {'a': 1, 'b': 2, 'c': 3}
d2 = json.dumps(d)
with open('d.txt',mode='w') as f_w:
    f_w.write(d2)
'''

# file_object = open('d.txt',mode='wb')
# json.dump(d2,file_object)
# file_object.close()

# 使用列表解析式(生成式)和range得到这样一个列表[1,4,9,16,25,36,49]
# print([i ** 2 for i in range(1,8)])