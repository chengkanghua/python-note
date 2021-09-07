import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    text = input("请输入要发送的内容：")
    if text.upper() == 'Q':
        break
    client.sendto(text.encode('utf-8'), ('127.0.0.1', 8002))
    data, (host, port) = client.recvfrom(1024)
    print(data.decode('utf-8'))

client.close()