import uuid
from queue import Queue, Empty
from flask import Flask, request, jsonify

app = Flask(__name__)

# 签名 任务队列
TASK_QUEUE = Queue()

# 结果队列
SIGN_DICT = {}


@app.route("/sign/task/", methods=["POST", "GET"])
def sign_task():
    if request.method == "POST":
        # ################ 第一步：客户端发送签名任务 ##############
        # 获取待签名字符串
        # 例如："abi=x86&appid=tv.danmaku.bili&appkey=1d8b6e7d45233436&brand=HUAWEI.."
        param_string = request.form.get('param_string')
        # sign_type=1，算法1加密 Libbili.g
        # sign_type=2，算法2加密 Libbili.h
        sign_type = request.form.get('sign_type')

        uid = str(uuid.uuid4())
        info = {"uid": uid, 'param_string': param_string, 'sign_type': sign_type}
        TASK_QUEUE.put(info)
        SIGN_DICT[uid] = Queue()
        return uid
    try:
        # ################ 第二步：app获取签名任务 ##############
        print("app取任务")
        task = TASK_QUEUE.get(block=True, timeout=8)
        res = jsonify(task)
    except Empty as e:
        res = "error"
    return res


@app.route("/sign/", methods=["POST", "GET"])
def sign():
    if request.method == "POST":
        # ################ 第三步：app签名后，签名的结果发送回来。 ##############
        print("app计算好并发送结果")
        info = request.json
        print('json--->', info)
        SIGN_DICT[info['uid']].put(info['total_string'])
        return "success"

    # ################ 第四步：客户端获取签名的结果 ##############
    print("等待获取 total string")
    uid = request.args.get('uid')
    total_string = SIGN_DICT[uid].get(block=True)
    del SIGN_DICT[uid]
    return total_string


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
