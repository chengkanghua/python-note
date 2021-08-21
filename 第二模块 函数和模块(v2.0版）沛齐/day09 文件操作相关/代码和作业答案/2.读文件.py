# 判断路径是否存在？
import os

file_path = "/Users/kanghua/PycharmProjects/python-note/第二模块 函数和模块(v2.0版）沛齐/day09 文件操作相关/代码和作业答案/info.txt"
exists = os.path.exists(file_path)
if exists:
    # 1.打开文件
    file_object = open('info.txt', mode='rt', encoding='utf-8')
    # 2.读取文件内容，并赋值给data
    data = file_object.read()
    # 3.关闭文件
    file_object.close()
    print(data)
else:
    print("文件不存在")
