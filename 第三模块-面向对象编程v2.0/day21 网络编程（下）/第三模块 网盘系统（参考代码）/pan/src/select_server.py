import socket
import select
from config import settings


class SelectServer(object):
    def __init__(self):
        self.host = settings.HOST
        self.port = settings.PORT
        self.socket_object_list = []   #server和client 的所有 socket 连接对象 [server_object,client_object,.......]
        self.conn_handler_map = {}     # {conn:handler_object,...} conn客户端连接对象的内存地址：handler对象的内存地址

    def run(self, handler):
        server_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_object.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 非阻塞（ blocking error )
        # server_object.setblocking(False)
        server_object.setblocking(True)

        server_object.bind((self.host, self.port))
        server_object.listen(5)
        self.socket_object_list.append(server_object)

        while True:
            r, w, e = select.select(self.socket_object_list, [], [], 0.05)
            for sock in r:
                # 新连接到来，执行 handler的 __init__ 方法
                if sock == server_object:  #socket_objetct_list[server_object] 第一个，有新连接才执行这条御酒
                    print("新客户端来连接")
                    conn, addr = server_object.accept()
                    self.socket_object_list.append(conn)
                    # 实例化handler类，即：类(conn)
                    self.conn_handler_map[conn] = handler(conn)  #是传参过来的PanHandler 类
                    continue

                # 新数据到来，执行 handler的 __call__ 方法
                handler_object = self.conn_handler_map[sock]  #这里的sock是遍历socket_object_list中已有clien_objet,给它复制一个变量名
                # 执行handler类对象的 execute 方法，如果返回False，则意味关闭服务端与客户端的连接
                result = handler_object.execute()
                if not result:
                    self.socket_object_list.remove(sock)
                    del self.conn_handler_map[sock]
        sock.close()
