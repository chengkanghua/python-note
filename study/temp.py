'''
基于csv格式实现 用户的注册 & 登录认证。详细需求如下：

- 用户注册时，新注册用户要写入文件csv文件中，输入Q或q则退出。
- 用户登录时，逐行读取csv文件中的用户信息并进行校验。
- 提示：文件路径须使用os模块构造的绝对路径的方式。
'''

'''
import os

# 定位文件
base_dir = os.path.dirname(os.path.abspath(__file__))
db_file_path = os.path.join(base_dir,'files/db1.csv')

# 用户注册
while True:
    choice = input('enter registry Y/y， quit N/n: ')
    if not choice.upper() in {'Y','N'}:
        print('error: repeat')
        continue
    if choice.upper() == 'N':
        break
    with open(db_file_path,mode='a',encoding='utf-8') as f:
        while True:
            username = input('please username: Q/q quit:')
            if username.upper() == 'Q':
                break
            password = input('please passwrod:')
            f.write(f'{username},{password}\n')
            f.flush()
    break

# 用户登录
username = input('wecome login  please username: ')
password = input('please password: ')

if not os.path.exists(db_file_path):
    print('error: db-file not find ')
else:
    with open(db_file_path,mode='r',encoding='utf-8') as f_read:
        for line in f_read:
            uname,pwd = line.strip().split(',')
            if uname == username and pwd == password:
                print('login success：')
                break
        else:
            print('error：username or password wroing')
'''

