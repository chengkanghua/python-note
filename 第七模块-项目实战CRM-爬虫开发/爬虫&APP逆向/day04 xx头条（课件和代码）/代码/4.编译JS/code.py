"""
1. 安装node.js         （Python + pip install xxxx)
2. npm install 模块名 -g

"""
import os
import subprocess

os.environ["NODE_PATH"] = "/usr/local/lib/node_modules/"
signature = subprocess.getoutput('node local1.js')
print("结果是--->", signature)
