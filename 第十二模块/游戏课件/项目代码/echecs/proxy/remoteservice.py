# coding=utf-8

"""

"""

from twisted.internet import reactor
from share.customhandler import RemoteServiceHandle
from controller import websocket_factory
import ujson


DISCONNECT_CLIENT_INTERVAL = 0.5
CLOSE_NORMAL = 1000
CLOSE_SOCKET_CODE = 10000


@RemoteServiceHandle()
def push_object(msgid, msg, send_list):
    print "push_object:", msgid, msg, send_list
    if isinstance(msg, dict):
        msg = ujson.dumps(msg)
    data = websocket_factory._datapack._pack(msg, msgid)
    websocket_factory.push_object(send_list, data, True)


# @RemoteServiceHandle()
# def disconnect_client(sessionid):
#     reactor.callLater(DISCONNECT_CLIENT_INTERVAL, websocket_factory._clients[sessionid].sendClose, CLOSE_NORMAL, "task over".decode())
