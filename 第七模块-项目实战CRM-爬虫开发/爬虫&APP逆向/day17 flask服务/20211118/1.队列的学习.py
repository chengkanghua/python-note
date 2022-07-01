import queue
import threading
import uuid

q = queue.Queue()
queue_dict = {
    # "ac2d368c-9b4b-486b-842e-5fda5a9c5e2f":queue.Queue()
}


def pc():
    while True:
        # 阻塞，永远等待。
        un_encrypt_dict = q.get(block=True)
        print("PC在队列中获取到任务：", un_encrypt_dict)

        # PC应该获取数据，进行加密。
        task_id = un_encrypt_dict['uid']
        task_string = un_encrypt_dict['text']

        queue_dict[task_id].put("kdkasdfasdfa")


# PC永远在等待
pc = threading.Thread(target=pc)
pc.start()

# 脚本
while True:
    text = input("【脚本】>>>")  # n1=123&n2=99&ts=1991212
    uid = str(uuid.uuid4())

    # 将任务发送到队列
    info = {'uid': uid, 'text': text}
    queue_dict[uid] = queue.Queue()

    q.put(info)

    # 等待结果的到来(等待）
    print("【脚本】开始等待：")
    res = queue_dict[uid].get(block=True)
    print("【脚本】结果", res)
