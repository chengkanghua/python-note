# coding=utf-8

from game.room.handlers.basehandler import BaseHandler, RegisterEvent
from game.room.validators.user_act import UserActValidator
from share.messageids import *
from game.room.notifybridge import user_act


@RegisterEvent(USER_ACT)
class UserActHandler(BaseHandler):

    def execute(self, *args, **kwargs):
        """
        测试接口
        :param args:
        :param kwargs:
        :return:
        """
        ret = {"need_push":1}
        validator = UserActValidator(handler=self)
        r = user_act(validator.desk.desk_id, validator.user.seat_id, validator.act.data, validator.act_params.data)
        ret["need_push"] = 0
        return ret
