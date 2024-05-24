import socket


def handle_request(client):
    buf = client.recv(1024)  # 接收发来的请求（不做任何处理，登录、注册、....）
    # ....

    client.send(b"HTTP/1.1 200 OK\r\n\r\n")
    client.send(b"Hello,DSB  DDB  Alex")


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.bind(('192.168.11.11', 80))  # 本机的80端口
    # sock.bind(('127.0.0.1', 80))  # 本机的80端口
    sock.bind(('0.0.0.0', 80))      # 如果想要让外网访问（别的网络访问我们的程序）
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)  # 一旦有人来连接
        connection.close()


if __name__ == '__main__':
    main()
