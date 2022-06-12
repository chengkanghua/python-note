import json
import requests


def send_text_msg(access_token, user_open_id, content):
    requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
        params={"access_token": access_token},
        data=json.dumps({
            "touser": user_open_id,
            "msgtype": "text",
            "text": {
                "content": content
            }
        }, ensure_ascii=False).encode('utf-8')
    )
