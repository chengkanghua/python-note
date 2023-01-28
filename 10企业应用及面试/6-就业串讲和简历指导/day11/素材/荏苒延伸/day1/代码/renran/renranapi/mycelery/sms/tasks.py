from mycelery.main import app
from .yuntongxun.sms import CCP
from renranapi.settings import constants
import logging
from django.conf import settings
log = logging.getLogger("django")

@app.task(name="send_sms")
def send_sms(mobile, sms_code):
    """异步发送短信"""
    ccp = CCP()
    try:
        result = ccp.send_template_sms(mobile, [sms_code, constants.SMS_CODE_EXPIRE//60 ], settings.SMS.get("_templateID"))
        return result
    except:
        log.error("发送短信验证码失败！手机号：%s" % mobile)