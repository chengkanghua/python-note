# coding=utf-8

from firefly.server.globalobject import GlobalObject


class RemoteServiceHandle:
    """
    重新定义原remoteservicehandler,使其可以对同一个函数/类进行多重绑定
    eg.
        @RemoteServiceHandle("gate_1")
        @RemoteServiceHandle("gate_2")
        def forwarding_gate():
            pass
    """

    def __init__(self):
        pass

    def __call__(self, target):
        for remote_node in GlobalObject().json_config["remoteport"]:
            GlobalObject().remote[remote_node["rootname"]]\
                ._reference._service.mapTarget(target)

        return target
