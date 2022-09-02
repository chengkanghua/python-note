# coding=utf-8
"""

"""

import random

from firefly.server.globalobject import GlobalObject
from twisted.internet import defer, reactor

from share.commontool import convert_to_json
from share.espoirlog import logger
from proxy.protocol import CustomWebProxyFactory, ProxyServiceHandle, server_name, session_gate_map


websocket_factory = CustomWebProxyFactory()
port = GlobalObject().json_config.get("port")
reactor.listenTCP(port, websocket_factory)


def get_gate_name(sessionno):
    """
    获取一个可用的消息转发gate节点
    :param sessionno: int
    :return:
    """
    gate_configs = GlobalObject().json_config["remoteport"]
    available_gates = [x["rootname"] for x in gate_configs if x.get("is_available")]
    if sessionno in session_gate_map.keys():
        gate = session_gate_map.get(sessionno)
        if gate in available_gates:
            return gate

    logger.debug(u"get_gate_name:%s", str([sessionno, available_gates]))
    gate = random.choice(available_gates)
    session_gate_map[sessionno] = gate
    return gate


def forward_to_gate(gate_name, keyname, session_id, data):
    logger.debug(u"forward_to_gate:%s", str([gate_name, keyname, session_id, data]))
    defered = GlobalObject().remote[gate_name].callRemote("forwarding_game", keyname, session_id, data)
    return defered


@ProxyServiceHandle
def forwarding_0(keyname, _conn, data):
    """
    选择一个
    :param keyname:
    :param _conn:
    :param data:
    :return:
    """
    session_id = "%s,%d" % (server_name, _conn.transport.sessionno)
    gate_name = get_gate_name(_conn.transport.sessionno)
    print "aaaaaaaaaaaaaaaaaaaaaAA:", data
    data = convert_to_json(data)
    logger.debug(u"forwarding_0: %s, %s", str(keyname), str(data))
    defered = forward_to_gate(gate_name, keyname, session_id, data)

    def on_time_out(a, b):
        logger.warn("%s is time out!" % gate_name)
        for node in GlobalObject().json_config["remoteport"]:
            if node["rootname"] == gate_name:
                node["is_available"] = False
            return forward_to_gate(get_gate_name(_conn.transport.sessionno), keyname, session_id, data)

    defered.addTimeout(200, reactor, on_time_out)
    return defered

