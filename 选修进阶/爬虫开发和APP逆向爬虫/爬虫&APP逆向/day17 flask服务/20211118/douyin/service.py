import uuid
import queue
from flask import Flask, request, jsonify

app = Flask(__name__)

# 任务队列
TASK_QUEUE = queue.Queue()

# 结果队列
RESULT_TASK_DICT = {}


# 脚本
@app.route('/create/task', methods=["POST"])
def create_task():
    # 1.接收待签名的数据
    un_sign_str = request.json.get("un_sign_str")

    # 2.生成任务id
    task_id = str(uuid.uuid4())

    # 3.为当前任务创建队列
    RESULT_TASK_DICT[task_id] = queue.Queue()

    # 4.任务和代码签名的字符串扔到队列中
    info = {'tid': task_id, 'un_sign_str': un_sign_str}
    TASK_QUEUE.put(info)

    return task_id


# 脚本
@app.route('/get/result', methods=["GET"])
def get_result():
    task_id = request.args.get("tid")
    result_queue = RESULT_TASK_DICT.get(task_id)
    sign = result_queue.get(block=True)

    del RESULT_TASK_DICT[task_id]

    return jsonify({"status": True, "data": sign})


# PC
@app.route('/fetch/task', methods=["GET"])
def fetch_task():
    result = {"status": False}
    try:
        task_dict = TASK_QUEUE.get(block=True, timeout=10)
        result['status'] = True
        result['data'] = task_dict
    except queue.Empty as e:
        pass
    return jsonify(result)


# PC
@app.route('/sign/result', methods=["POST"])
def sign_result():
    # {tid:"xxx","sign":"xxx"}
    tid = request.json.get("tid")
    sign = request.json.get("sign")
    RESULT_TASK_DICT[tid].put(sign)
    return "success"


if __name__ == '__main__':
    app.run()
