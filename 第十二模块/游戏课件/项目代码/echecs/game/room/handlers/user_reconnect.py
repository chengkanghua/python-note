# coding=utf-8
import time

from game.room.handlers.basehandler import BaseHandler, RegisterEvent
from game.room.validators.user_reconnect import UserReconnectValidator
from game.room.models.user_manager import UserManager
from game.session_gate_rel import session_gate_ins
from share.messageids import *


@RegisterEvent(USER_RECONNECT)
class UserReconnectHandler(BaseHandler):

    def execute(self, *args, **kwargs):
        """
        玩家断线重连
        :param args:
        :param kwargs:
        :return:
        """

        validator = UserReconnectValidator(handler=self)
        UserManager().add_user(validator.user.user_id, validator.desk.desk_id, self.session_id)
        session_gate_ins.update_rel(self.session_id, self.gate_name)
        validator.user.is_online = 1

        data = {"user_id": validator.user.user_id, "nick": validator.user.nick_name}
        validator.desk.notify_desk(PUSH_USER_RECONNECT, data)

        game_data = validator.desk.get_reconnect_info(validator.user.seat_id)
        user_info = validator.desk.get_users_info()
        end_time = game_data["wait_task"].get("end_time", 0)
        if end_time:
            game_data["wait_task"]["end_time"] = end_time - time.time()
        else:
            game_data["wait_task"]["end_time"] = end_time
        validator.desk.notify_player(validator.user.seat_id,
                                     USER_RECONNECT,
                                     {"user_info": user_info, "game_data": game_data})
        if game_data.get('wait_task', None):
            pass
            # 每个玩家同时只可能有一个定时任务待执行
            # validator.desk.notify_player(validator.user.seat_id, game_data["wait_task"]["command_id"], act_info)

        return {"need_push": 0}
