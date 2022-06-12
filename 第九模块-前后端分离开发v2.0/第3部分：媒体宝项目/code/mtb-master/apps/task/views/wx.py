import os
import requests
from django.shortcuts import HttpResponse, redirect, render
from utils.token import get_component_access_token, get_authorizer_access_token
from django.conf import settings
from .. import models
from urllib.parse import urlencode
from apps.base import models as base_models


def oauth(request):
    # code/state/appid
    code = request.GET.get("code")
    state = request.GET.get("state")  # tp_id
    appid = request.GET.get("appid")  # 公众号

    # 获取参加活动的对象
    tp_object = models.TakePartIn.objects.filter(id=state).first()
    if not tp_object:
        return HttpResponse("授权失败")

    # 获取公众号对象
    pub_object = base_models.PublicNumbers.objects.filter(authorizer_app_id=appid).first()

    # 1. 用参数信息和component_access_token换 access_token
    component_access_token = get_component_access_token()
    url = "https://api.weixin.qq.com/sns/oauth2/component/access_token?appid={}&code={}&grant_type=authorization_code&component_appid={}&component_access_token={}"
    url = url.format(appid, code, settings.WX_APP_ID, component_access_token)
    ret_dict = requests.get(url).json()
    access_token = ret_dict.get('access_token')
    if not access_token:
        return HttpResponse("授权失败")

    # 2.使用access_token获取用户信息
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    url = 'https://api.weixin.qq.com/sns/userinfo?access_token={}&openid={}&lang=zh_CN'
    url = url.format(access_token, tp_object.open_id)
    info_dict = requests.get(url, headers=header).json()
    if not info_dict:
        return HttpResponse("授权失败")

    # 3.获取用户名和头像
    username = info_dict.get("nickname").encode('iso-8859-1').decode('utf-8')
    head_img_url = info_dict.get("headimgurl")

    # 4.头像写入media目录，方便后续使用
    # .../media/images/tp.id/
    local_img_folder = os.path.join(settings.MEDIA_ROOT, "images", str(tp_object.id))
    if not os.path.exists(local_img_folder):
        os.makedirs(local_img_folder)
    local_img_path = os.path.join(local_img_folder, "avatar.png")
    img_content = requests.get(head_img_url).content
    with open(local_img_path, mode='wb') as f:
        f.write(img_content)

    # 5.生成二维码
    # https://developers.weixin.qq.com/doc/offiaccount/Account_Management/Generating_a_Parametric_QR_Code.html
    # 获取公众号的token
    access_token = get_authorizer_access_token(pub_object)
    qr_res = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/qrcode/create",
        params={
            "access_token": access_token
        },
        json={
            "expire_seconds": 2592000,
            "action_name": "QR_STR_SCENE",
            "action_info": {
                "scene": {
                    "scene_str": "1_{}".format(tp_object.id)  # 自定义字段，客户扫码后，自动携带（助力用）
                }
            }
        }
    )
    """
    {
        'ticket': 'gQEC8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAydWl0QUFrN3NhRFQxVXhIejF3Y2sAAgQhHrxgAwQAjScA', 
        'expire_seconds': 2592000, 
        'url': 'http://weixin.qq.com/q/02uitAAk7saDT1UxHz1wck'
    }
    """
    qr_data_dict = qr_res.json()
    # print(qr_data_dict)
    qr_content = requests.get(
        "https://mp.weixin.qq.com/cgi-bin/showqrcode",
        params={"ticket": qr_data_dict["ticket"]}
    ).content

    # 6.生成海报 pip install pillow
    from PIL import Image, ImageFont, ImageDraw
    import io

    background_image_path = tp_object.activity.poster.img[1:]
    base_img = Image.open(background_image_path)  # 背景图

    # 写二维码
    qr_size = 350
    qr_img = Image.open(io.BytesIO(qr_content))  # 二维码
    qr_position = [
        base_img.width - qr_size - 130,
        base_img.height - qr_size - 70
    ]
    region = qr_img.resize([qr_size, qr_size])
    base_img.paste(region, qr_position)

    # 写头像
    avatar_img = Image.open(io.BytesIO(img_content))  # 头像
    avatar_size = 200
    avatar_position = [120, 120]
    region = avatar_img.resize([avatar_size, avatar_size])
    base_img.paste(region, avatar_position)

    # 写昵称
    setFont = ImageFont.truetype("simkai.ttf", 80)
    text = username
    size = [350, 150]
    draw = ImageDraw.Draw(base_img)
    draw.text(size, text, font=setFont, fill='blue', direction=None)

    # 写入media目录文件 C:/xx/xxx/x/media/images/1/poster.png
    local_poster_path = os.path.join(local_img_folder, "poster.png")
    base_img.save(local_poster_path, 'png')

    # 生成media访问连接 /media/images/1/poster.png
    poster_image_url = "{}images/{}/poster.png".format(settings.MEDIA_URL, tp_object.id)
    avatar_image_url = "{}images/{}/avatar.png".format(settings.MEDIA_URL, tp_object.id)

    tp_object.nick_name = username
    tp_object.avatar = avatar_image_url
    tp_object.poster = poster_image_url
    tp_object.save()

    return render(request, "poster.html", {"image_url": poster_image_url})
