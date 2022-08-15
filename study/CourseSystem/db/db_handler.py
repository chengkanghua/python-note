"""
@FileName：db_handler.py
@Author：chengkanghua
@Time：2022/8/14 8:52 下午
"""

'''用于保存对象与获取对象'''
import os,pickle
from conf import settings

def save_data(obj):
    '''
    1.获取对象的保存文件夹路径
    以类名 当做 文件夹的名字
    obj.__class__: 获取当前对象的类
    obj.__class__.__name__: 获取类的名字
    '''
    class_name = obj.__class__.__name__
    user_dir_path = os.path.join(settings.DB_PATH,class_name)

    # 2 判断文件是否存在， 不存在就创建文件夹
    if not os.path.exists(user_dir_path):
        os.makedirs(user_dir_path)

    # 3 拼接当前用户的pickle文件路径， 以用户名做路径
    user_file_path = os.path.join(user_dir_path,obj.user)

    # 4 打开文件 保存对象 通过pickle
    with open(user_file_path, 'wb') as f:
        pickle.dump(obj, f)

    return obj


def select_data(cls,username):
    # 1 由 cls 获取类名
    class_name = cls.__name__
    user_dir_path = os.path.join(settings.DB_PATH,class_name)

    # 2 判断文件夹是否存在 不存在则创建
    if not os.path.exists(user_dir_path):
        os.makedirs(user_dir_path)

    # 3 拼接当前用户的 pickle 文件路径， 以用户名作为文件名
    user_file_path = os.path.join(user_dir_path,username)

    # 4 判断文件如果存在 再打开 并返回，不存在代表用户不存在
    if os.path.exists(user_file_path):
        with open(user_file_path, 'rb') as f:
            data = pickle.load(f)
            return data
