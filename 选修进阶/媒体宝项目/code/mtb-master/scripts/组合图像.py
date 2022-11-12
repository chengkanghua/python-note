"""
# 二维码
with open('0_3_oXEWb6Shzn8srgCfbwY7WUTDKt24', mode='rb') as f:
    buffer = f.read()
qr_img = Image.open(io.BytesIO(buffer))
"""
from PIL import Image, ImageFont, ImageDraw
import io
from PIL import Image

base_img = Image.open("D8110630D048139753BEBA9240C74BC9.jpg")  # 背景图
# qr_img = Image.open("0_3_oXEWb6Shzn8srgCfbwY7WUTDKt24")  # 二维码
with open('0_3_oXEWb6Shzn8srgCfbwY7WUTDKt24', mode='rb') as f:
    buffer = f.read()

qr_img = Image.open(io.BytesIO(buffer))


qr_size = 350
qr_position = [
    base_img.width - qr_size - 130,
    base_img.height - qr_size - 70
]
region = qr_img.resize([qr_size, qr_size])
base_img.paste(region, qr_position)

# 头像
avatar_img = Image.open('wx71bf291c758aaabf_oXEWb6dTufDJ78KxragosOrEi384')
avatar_size = 200
avatar_position = [120, 120]
region = avatar_img.resize([avatar_size, avatar_size])
base_img.paste(region, avatar_position)

# 昵称
setFont = ImageFont.truetype("simkai.ttf", 80)
text = "武沛齐"
size = [350, 150]
draw = ImageDraw.Draw(base_img)
draw.text(size, text, font=setFont, fill='blue', direction=None)

base_img.save("x.png", 'png')  # 保存图片
