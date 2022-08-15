"""
@FileName：common_interface.py
@Author：chengkanghua
@Time：2022/8/14 8:58 下午
"""
'''公共接口'''
import os
from conf import settings

def get_all_school():
    school_dir = os.path.join(settings.DB_PATH, 'school')

    if not os.path.exists(school_dir):
        return False,'school not exists '
    # 获取文件夹所有文件名字
    school_list = os.listdir(school_dir)
    return True,school_list