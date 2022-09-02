# coding=utf-8

from ...extensions.blueprint import Blueprint
admin = Blueprint("admin", url_prefix="/admin")
import login_handler
import status_handler
