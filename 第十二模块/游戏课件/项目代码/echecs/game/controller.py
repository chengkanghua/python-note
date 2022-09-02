# coding=utf-8

from firefly.utils.services import CommandService
from firefly.server.globalobject import GlobalObject
from twisted.internet import defer, reactor

from game.room.handlers.basehandler import RegisterEvent, BaseHandler
from db.message_route import route_ins
from share.espoirlog import logger
from share.customhandler import RemoteServiceHandle
from share.messageids import *
from share.errorcode import COMMAND_NOT_FOUND


def init_node():
    """启动时初始化"""
    room_name = GlobalObject().json_config.get("name", '')
    route_ins.clear_room(room_name=room_name)
    # 删除桌子信息



@RemoteServiceHandle()
def forwarding_game(key, session_id, data):
    """
    消息转发给游戏节点
    :param key: 消息id
    :param session_id:
    :param data: json串, 里面必须包含userid
    :return:
    """
    logger.debug(u"forwarding_game:%s", str([key, session_id, data]))
    user_id = data.get("user_id", -1)
    if -1 == user_id and key not in [USER_OFFLINE]:
        return

    class_obj = RegisterEvent.events.get(key)
    if not class_obj:
        return BaseHandler.error_response(COMMAND_NOT_FOUND)
    data.update({"session_id": session_id})
    event_ins = class_obj(data, key, session_id)
    return event_ins.execute_event()


