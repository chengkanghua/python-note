import os
import json
import socket
import struct

# 从网卡的read buffer获取数据
def recv_data(conn, chunk_size=1024):         #参数 连接对象，数据块大小
    # 获取头部信息：数据长度
    has_read_size = 0                          #已经读取的数据大小
    bytes_list = []
    while has_read_size < 4:                   #保证获取头部4个字节数据
        chunk = conn.recv(4 - has_read_size)   #固定取4个字节，少多少取多少
        has_read_size += len(chunk)            #得到已经取得的数据大小
        bytes_list.append(chunk)
    header = b"".join(bytes_list)              #获取的数据拼接起来
    data_length = struct.unpack('i', header)[0] #数据解包 取得数据长度

    # 获取数据
    data_list = []
    has_read_data_size = 0
    while has_read_data_size < data_length:   #刚好取得数据大小
        size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
        chunk = conn.recv(size)  #取数据
        data_list.append(chunk)  #放入数据列表里
        has_read_data_size += len(chunk)  #已经取得数据大小

    data = b"".join(data_list)     #拼接起来
    return data
#从网卡的read buffer 获取文件
def recv_file(conn, save_file_name, chunk_size=1024):    #参数 连接对象，数据块大小
    save_file_path = os.path.join('files', save_file_name)  #文件路径
    # 获取头部信息：数据长度
    has_read_size = 0                         #已读取大小
    bytes_list = []
    while has_read_size < 4:
        chunk = conn.recv(4 - has_read_size)
        bytes_list.append(chunk)
        has_read_size += len(chunk)
    header = b"".join(bytes_list)
    data_length = struct.unpack('i', header)[0]  #解包获取数据长度

    # 获取数据
    file_object = open(save_file_path, mode='wb')  #文件写对象
    has_read_data_size = 0
    while has_read_data_size < data_length:
        size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
        chunk = conn.recv(size)   #取数据
        file_object.write(chunk)  #写入
        file_object.flush()       #刷进硬盘
        has_read_data_size += len(chunk)  #已经读取大小。
    file_object.close()

def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # IP可复用  #ip 端口重复用
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(('127.0.0.1', 8001))  # 开通服务 端口
    sock.listen(5)                  #可监听5个客户端
    while True:
        conn, addr = sock.accept()     #接收对象 conn
        while True:
            # 获取消息类型
            message_type = recv_data(conn).decode('utf-8')   #调用接收数据方法
            if message_type == 'close':  # 四次挥手，空内容。
                print("关闭连接")
                break
            # 文件：{'msg_type':'file', 'file_name':"xxxx.xx" }
            # 消息：{'msg_type':'msg'}
            message_type_info = json.loads(message_type)  #反序列化
            if message_type_info['msg_type'] == 'msg':
                data = recv_data(conn)        #调用接收数据方法
                print("接收到消息：", data.decode('utf-8'))
            else:
                file_name = message_type_info['file_name']
                print("接收到文件，要保存到：", file_name)
                recv_file(conn, file_name)    #调用接收文件方法

        conn.close()
    sock.close()

if __name__ == '__main__':
    run()