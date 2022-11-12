# coding=utf-8

from game.room.handlers.basehandler import BaseHandler, RegisterEvent
from game.room.validators.friend_desk.join_desk import JoinDeskValidator
from game.room.common_define import DeskType
from game.room.models.user_manager import UserManager
from game.room.models.user import User
from game.room.models.room_desk import RoomDesk
from game.room.models.roomdesk_manager import desk_mgr
from game.session_gate_rel import session_gate_ins
from db.desk import Desk as DBDesk
from share.messageids import *


@RegisterEvent(JOIN_FRIEND_DESK)
class JoinDeskHandler(BaseHandler):

    def execute(self, *args, **kwargs):
        """
        加入桌子请求处理
        :param args:
        :param kwargs:
        :return:
        """
        validator = JoinDeskValidator(handler=self)
        user = UserManager().add_user(validator.user_id.data, validator.desk_id.data, validator.session_id.data)
        session_gate_ins.update_rel(validator.session_id.data, self.gate_name)
        desk = desk_mgr.get_room_desk(validator.desk_id.data)
        desk.user_sit(user)

        data = user.to_dict()
        desk.notify_desk_some_user(PUSH_USER_JOIN_DESK, data, [user.user_id])

        return {"desk_id": validator.desk_id.data, "seat_info": desk.get_users_info()}
