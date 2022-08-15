"""
@FileName：start.py
@Author：chengkanghua
@Time：2022/8/14 9:02 下午
"""
'''启动入口文件'''
import os,sys
# sys.path.insert(0,os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__))
print(sys.path)

from core import src

if __name__ == '__main__':
    src.run()
