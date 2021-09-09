import socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(("127.0.0.1", 8001))
server.listen(5)

inputs = [server]
while True:
    r, w, e = select.select(inputs, [], [], 0.1)
    for sock in r:
        if sock == server:
            conn, addr = sock.accept()
            print('一个新的链接')
            inputs.append(conn)
        else:
            data = sock.recv(1024)
            if data:
                print('收到消息: ', data.decode())
                sock.sendall('张开'.encode())
            else:
                print('关闭链接')
                inputs.remove(sock)