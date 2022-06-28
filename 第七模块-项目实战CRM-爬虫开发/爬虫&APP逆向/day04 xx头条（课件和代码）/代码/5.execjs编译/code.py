import execjs
import os

os.environ["NODE_PATH"] = "/usr/local/lib/node_modules/"
with open('local.js', mode='r', encoding='utf-8') as f:
    js = f.read()

JS = execjs.compile(js)

sign = JS.call("func", "微信")
print(sign)
