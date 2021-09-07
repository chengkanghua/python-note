import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 8002))

while True:
    data, (host, port) = server.recvfrom(1024) # 阻塞
    print(data, host, port)
    server.sendto("好的".encode('utf-8'), (host, port))