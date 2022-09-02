# coding=utf-8

from firefly.server.globalobject import GlobalObject, rootserviceHandle

from db.message_route import route_ins
from share.espoirlog import logger
from share.messageids import *
from share.errorcode import *


# 节点缓存, 只有在用户登录验证成功后才缓存 {session_id: {"user_id": user_id, "room":room_name}}
ROUTE_CACHE = {}
GATE_NAME = GlobalObject().json_config.get("name")


@rootserviceHandle
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
    passwd = data.get("passwd", -1)
    if -1 == user_id and key not in [USER_OFFLINE]:
        print "forwarding_game user_id =", user_id
        return

    if USER_LOGIN == key:
        logger.debug(u"forwarding_game2:%s", str([key, session_id, data]))
        return process_login(user_id, passwd, session_id, data)

    if session_id in ROUTE_CACHE.keys():
        room_name = ROUTE_CACHE[session_id]["room"]
        data.update({"gate_name": GATE_NAME})
        return GlobalObject().root.callChildByName(room_name, "forwarding_game", key, session_id, data)

    route_info = route_ins.get_route(user_id, session_id=session_id)
    print "route_info:", route_info
    if 200 == route_info.get('code'):
        data.update({"gate_name": GATE_NAME})
        room_name = route_info['info'].get("room")
        return GlobalObject().root.callChildByName(room_name, "forwarding_game", key, session_id, data)
    else:
        return


def process_login(user_id, passwd, session_id, data):
    """
    登录消息特殊处理, 包括踢之前用户下线
    :param user_id:
    :param session_id:
    :param data:
    :return:
    """
    login_result = route_ins.login(user_id=user_id, passwd=passwd, new_sessionid=session_id, data=data)
    print "login_result:", login_result
    if 200 == login_result.get('code'):
        info = login_result.get("info")
        old_session = info.get("old_session")
        if old_session and session_id != old_session:
            # 踢掉之前用户
            node_name, id = info.get("old_session").split(',')
            data = error_response(USER_LOGIN_OTHER_DEVICE)
            GlobalObject().root.callChildByName(node_name, "push_object", PUSH_USER_OTHER_LOGIN, data, [id])
        return login_result
    else:
        logger.error("process_login: unknown error:%s", str(login_result))
        return login_result


# @rootserviceHandle
# def lose_connect(session_id):
#     """
#     socket连接断开
#     :param session_id:
#     :return:
#     """
#     room_name = ROUTE_CACHE[session_id]["room"]
#     data = {"gate_name": GATE_NAME}
#     return GlobalObject().root.callChildByName(room_name, "forwarding_game", USER_OFFLINE, session_id, data)


@rootserviceHandle
def push_object(message_id, data, session_list):
    """
    主动向客户端推送消息
    :param message_id:
    :param data: json串
    :param session_list:
    :return:
    """
    for session in session_list:
        node_name, id = session.split(',')
        GlobalObject().root.callChildByName(node_name, "push_object", message_id, data, [int(id)])