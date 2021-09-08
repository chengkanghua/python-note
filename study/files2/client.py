import os
import json
import socket
import struct
#发送数据方法
def send_data(conn, content):   #参数 连接对象，内容
    data = content.encode('utf-8')   #编码
    header = struct.pack('i', len(data))  #结构化数据大小 得到4字节
    conn.sendall(header)                  #发送文件头 标记文件大小
    conn.sendall(data)                    #发送内容
#发送文件方法
def send_file(conn, file_path):  #参数 连接对象，文件路径
    file_size = os.stat(file_path).st_size    #获取文件大小
    header = struct.pack('i', file_size)      #结构化数据文件大小
    conn.sendall(header)                      #发送文件头 标记文件大小

    has_send_size = 0                         #已经发送文件大小
    file_object = open(file_path, mode='rb')
    while has_send_size < file_size:
        chunk = file_object.read(2048)
        conn.sendall(chunk)
        has_send_size += len(chunk)
    file_object.close()

def run():
    client = socket.socket()
    client.connect(('127.0.0.1', 8001))
    while True:
        """
        请发送消息，格式为：
            - 消息：msg|你好呀
            - 文件：file|xxxx.png
        """
        content = input(">>>")  # msg or file
        if content.upper() == 'Q':
            send_data(client, "close")  #调用发送数据方法
            break
        input_text_list = content.split('|')  #切分内容
        if len(input_text_list) != 2:
            print("格式错误，请重新输入")
            continue
        message_type, info = input_text_list  # 文件类型，文件或消息
        # 发消息
        if message_type == 'msg':
            # 发消息类型
            send_data(client, json.dumps({"msg_type": "msg"}))  #调用发送数据方法，发送消息内容
            # 发内容
            send_data(client, info)
        # 发文件
        else:
            file_name = info.rsplit(os.sep, maxsplit=1)[-1]     #os.sep 获得路径分隔符/  从右边切割1次， 取最后的文件名
            # 发消息类型
            send_data(client, json.dumps({"msg_type": "file", 'file_name': file_name})) #发送文件夹类型 文件名
            # 发内容
            send_file(client, info)

    client.close()

if __name__ == '__main__':
    run()

