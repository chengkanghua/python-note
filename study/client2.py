# ################### socket客户端 ###################
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',8001))

while True:
    text = input('>>>>')
    if text.upper() == 'Q':
        break
    client.sendall(text.encode('utf-8'))
    reply = client.recv(1024)
    print('收到消息{}'.format(reply.decode('utf-8')))

client.close()

