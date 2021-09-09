import socket
import select

client_list = []  # socket对象列表
for i in range(5):   # 5个对socket对象 非阻塞
    client = socket.socket()
    client.setblocking(False)
    try:
        client.connect(('127.0.0.1', 8001))
    except BlockingIOError as e:
        pass
    client_list.append(client)

recv_list = []  # 放已连接成功的socket对象
while True:

    r, w, e = select.select(recv_list, client_list, [], 0.1)

    for sock in w:
        # 连接成功，请求获取用户名
        sock.sendall("username".encode())
        recv_list.append(sock)
        client_list.remove(sock)

    for sock in r:
        # 将获取用户名的请求发送成功后，这里打印出server端的响应结果
        data = sock.recv(8196)
        print("接收到来自server端返回的用户名: ", data.decode())

    if not recv_list and not client_list:
        break