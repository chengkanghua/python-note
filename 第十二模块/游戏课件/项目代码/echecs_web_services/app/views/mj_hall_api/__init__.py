#!/usr/bin/env python
# coding=utf-8
from app.extensions.blueprint import Blueprint
mj_hall = Blueprint('mj_hall', url_prefix="/majapi")

import login_hall
import email
import good
import personal
import income_support
import user_info

