# coding=utf-8

from wtforms import fields, validators

from game.room.validators.basevalidator import BaseValidator
from game.room.models.user_manager import UserManager
from game.room.models.roomdesk_manager import desk_mgr
from share import errorcode


class JoinMatchDeskValidator(BaseValidator):
    user_id = fields.IntegerField("user_id")
    session_id = fields.StringField("session_id")

    def validate_user_id(self, field):
        if UserManager().get_user_by_id(self.user_id.data):
            raise validators.ValidationError(errorcode.USER_IN_OTHER_DESK)

    def validate_session_id(self, field):
        if not self.session_id.data:
            raise validators.ValidationError(errorcode.SESSION_NOT_EXIST)
