# coding=utf-8
"""

"""
import random

from websocket import ABNF

from __init__ import BaseTestClient

import logging as logger
# from utils import AesEncoder
from twisted.internet import reactor
import Queue
import threading
import inspect
import ujson
import sys
import time

s_time = None
e_time = None
q = Queue.Queue()


def random_weighted_choice(weights):
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i

"""
用于输入的线程
"""
class MyThread(threading.Thread):
    def __init__(self, q):
        super(MyThread, self).__init__()
        self.q = q

    def run(self):
        while True:
            try:
                input_str = input("Enter your bet num!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:")
                if isinstance(input_str, list) and len(input_str) == 5:
                    self.q.put(input_str)
                else:
                    print "input error!!"
            except Exception, e:
                print e
                print "input error"


input_thread = MyThread(q)


class RobotClient(BaseTestClient):
    def __init__(self, config_file):
        BaseTestClient.__init__(self, config_file=config_file)

        # super(RobotClient, self).__init__()
        self.response_seq = self.all_config.get("response_seq")
        self.sendhandler = {
            100002: self.send_100002,
            100010: self.send_100010,
            100100: self.send_100100,
            100101: self.send_100101,
            100102: self.send_100102,
            100104: self.send_100104,
            100110: self.send_100110,
            100111: self.send_100111,
            100103: self.send_100103,
            100120: self.send_100120,
            9999: self.send_9999
        }

    def on_open(self):
        print "on_open!!!"
        # self.send_data(100002, {"userid": self.user_id, "pass": self.all_config.get("USER_PASSWORD")}, ws)
        global s_time
        s_time = time.time()
        self.send_100002(self.client)

    def on_message(self, message):
        length = self.head_len
        unpackdata = self.unpack(message)  # 这一行的作用
        print "接收数据：", unpackdata
        if unpackdata is None:
            print '!'*20, 'unpack_data is None!'
            return
        command = unpackdata.get('command')
        rlength = unpackdata.get('length')
        data = unpackdata.get("data")
        n = random.randint(1, 3)

        # print "#"*88
        # print u"接收数据:", n, data, command
        # reactor.callLater(n, self.receivehandler, command, data)
        self.receivehandler(self.client, command, data)

    def receivehandler(self, ws, key, params):
        if params and isinstance(params, str):
            params = ujson.loads(params)
        global responseConfig
        print u"接收处理:", key, [params]
        # print "@"*88,'str(key)=', str(key)
        rconfig = self.response_seq.get(str(key), None)
        if not rconfig:
            logger.error("index(%s):Error: response config error! key=%s", 1, str(key))
            # print "@"*88, "rconfig is none"
            return

        if not rconfig.get("msg", None):
            # logger.warning("response has not receiver msg handler")F
            return
        # if key == 100002 and params.get("info"):
        #     return self.send_100801(ws, params)
        random_index = random_weighted_choice(rconfig.get("weight"))
        # print "@"*20, random_index, key, params, rconfig.get("msg")
        return self.sendhandler.get(rconfig.get("msg")[random_index])(ws, params)

    def send_data(self, commandID, data, ws):
        print u"*******发送数据*********：", commandID, data, ws, "||"
        s = self.pack(data, commandID)
        print [s]
        ws.send(s, opcode=ABNF.OPCODE_BINARY)

    def send_100002(self, ws, params={}):
        '''  登录
        '''
        print "@" * 33, 'this is %s' % inspect.stack()[1][3]
        passwd = self.all_config.get("password")
        data = {"user_id": 1, "passwd": passwd}
        self.send_data(100002, data, ws)

    def send_100010(self, ws, params={}):
        """断线重连"""
        data = {"user_id": self.user_id}
        self.send_data(100010, data, ws)

    def send_100100(self, ws, params={}):
        """
        玩家准备
        """
        data = {"user_id": self.user_id, "ready": 1}
        self.send_data(100100, data, ws)

    def send_100101(self, ws, params={}):
        """创建好友桌"""
        data = {"user_id": self.user_id}
        self.send_data(100101, data, ws)

    def send_100102(self, ws, params={}):
        """加入好友桌"""
        data = {"user_id": self.user_id, "desk_id": 100000}
        self.send_data(100102, data, ws)

    def send_100103(self, ws, params={}):
        """玩家退出桌子"""
        data = {"user_id": self.user_id}
        self.send_data(100103, data, ws)

    def send_100104(self, ws, params={}):
        """玩家加入匹配场"""
        data = {"user_id": self.user_id}
        self.send_data(100104, data, ws)

    def send_100110(self, ws, params={}):
        """解散桌子"""
        data = {"user_id": self.user_id}
        self.send_data(100110, data, ws)

    def send_100111(self, ws, params={}):
        """解散房间应答"""
        data = {"user_id": self.user_id, "agree": 1}
        self.send_data(100111, data, ws)

    def send_100120(self, ws, params={}):
        """玩家自定义配置"""
        data = {"user_id": self.user_id, "custom_config": {}}
        self.send_data(100120, data, ws)

    def send_9999(self, ws, params={}):
        pass
        # print "stop..."


# if __name__ == '__main__':
#     # input_thread.start()
#     # reactor.suggestThreadPoolSize(100)
#     for i in range(0, 1):
#         user_id = 1
#         robot = RobotClient("robot.json")
#         # reactor.callInThread(robot.run)
#         reactor.callInThread(robot.run)
#     reactor.run()
    # config_dict= {
    #     "1": "config1.ini",
    #     "2": "config2.ini",
    #     "3": "config3.ini",
    #     "4": "config4.ini"
    # }
    # config_index = None
    # try:
    #     config_index = sys.argv[1]
    #     print config_index in config_dict.keys()
    # except IndexError,e:
    #     print u"请输入config_index (1,2,3,4)"
    # if config_index is not None and config_index in config_dict.keys():
    #     robot = RobotClient(config_dict[config_index])
    #     print "robot config%s start!!!!!"%config_index
    #     reactor.callInThread(robot.run)
    #     reactor.run()
