import os
'''
遍历打印目录文件
'''
def dirlist(path):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path,filename)
        if os.path.isdir(filepath):
            dirlist(filepath)
        else:
            print(filepath)


# dirlist('/Users/kanghua/PycharmProjects/python-note/Clang')
dirlist('/Library/Frameworks/Python.framework/Versions')
