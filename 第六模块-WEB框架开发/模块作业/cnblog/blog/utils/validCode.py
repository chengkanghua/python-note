import random
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


def get_random_color():
    return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))


def get_valid_code_img(request):
    img = Image.new('RGB', (270, 40), color=get_random_color())  # 新建一个270*40的画布
    draw = ImageDraw.Draw(img)
    kumo_font = ImageFont.truetype('static/font/kumo.ttf', size=32)

    valid_code_str = ""
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_low_alpha = chr(random.randint(95, 122))
        random_upper_alpha = chr(random.randint(65, 90))
        random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
        draw.text((i * 50 + 20, 5), random_char, get_random_color(), font=kumo_font)  # x y值

        valid_code_str += random_char

    # print('valid_code_str',valid_code_str)
    request.session['valid_code_str'] = valid_code_str

    f = BytesIO()
    img.save(f, 'png')
    data = f.getvalue()
    return data
