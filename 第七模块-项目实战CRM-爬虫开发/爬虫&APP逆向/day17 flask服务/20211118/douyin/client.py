import requests

# 1.向Flask服务发送请求（希望Flask帮我生成签名），获取任务ID
res = requests.post(
    url="http://127.0.0.1:5000/create/task",
    json={
        "un_sign_str": "n1&n2&n3&n4"
    }
)
task_id = res.text.strip()

# 2.获取签名结果
# http://127.0.0.1:5000/get/result?tid=c2806776-13dd-461b-b9ac-c80d2627481c
res = requests.get(
    url="http://127.0.0.1:5000/get/result",
    params={
        "tid": task_id
    }
)

print("获取签名结果：", res.text)
