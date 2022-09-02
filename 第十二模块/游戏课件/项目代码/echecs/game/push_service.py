# coding=utf-8

from firefly.server.globalobject import GlobalObject
from session_gate_rel import session_gate_ins
from share.espoirlog import logger
from game.room.handlers.basehandler import BaseHandler


def push_msg(message_id, data, session_list, code=200):
    """
    主动向客户端推送消息
    :param message_id:
    :param data: json串
    :param session_list:
    :return:
    """
    for session in session_list:
        # node_name, id = session.split(',')
        gate_name = session_gate_ins.get_gate(session)
        if not gate_name:
            logger.warn("push_msg cannot find gate_name:%s", session)
            continue
        if code == 200:
            pack_data = BaseHandler.success_response(data)
        else:
            pack_data = BaseHandler.error_response(code)
        # print "game push _objecttttttttttttttttt:", pack_data
        GlobalObject().remote[gate_name].callRemote("push_object", message_id, pack_data, [session])