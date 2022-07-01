import requests

while True:
    # 1.PC端去Flask获取任务
    res = requests.get(
        url="http://127.0.0.1:5000/fetch/task",
    )

    result_dict = res.json()
    # 没获取到任务，即：30s超时
    if not result_dict['status']:
        print("没获取到任务，重新请求")
        continue

    # 获取到任务，接下来就应该生成签名并写入到结果队列中。
    # {'tid': 'b1e17266-bda8-4724-bb83-049c98bd5b71', 'un_sign_str': 'n1&n2&n3&n4'}
    tid = result_dict['data']['tid']
    un_sign_str = result_dict['data']['un_sign_str']
    print("获取任务：", tid)

    # 调用frida-rpc和un_sign_str去进行加密，加密后得到结果。
    sign_string = "hhhhhhhhhhhhhhhhhh"

    # 将结果返回到任务队列 tid=队列名称    sign_string就是签名结果
    requests.post(
        url="http://127.0.0.1:5000/sign/result",
        json={
            "tid": tid,
            "sign": sign_string,
        }
    )
    print("生成签名：", sign_string)
