from django.shortcuts import render
from django.http import JsonResponse

def demo1(request):
    """
    示例1：直接通过秘钥对cos进行上传文件【不推荐】
    """
    return render(request,'demo1.html')

def demo2(request):
    """
    示例2：通过临时凭证上传
    """
    return render(request,'demo2.html')

def cos_credential(request):
    from sts.sts import Sts
    config = {
        # 临时密钥有效时长，单位是秒（30分钟=1800秒）
        'duration_seconds': 1800,
        # 固定密钥 id
        'secret_id': "AKIDFPJSXQEk8PXVL3Tx5zf6MSL0Sf7Qoikg",
        # 固定密钥 key
        'secret_key': "yiCWfZCXcQxJZlqncKvRu5DKHySg8sMp",
        # 换成你的 bucket
        'bucket': "wangyang-1251317460",
        # 换成 bucket 所在地区
        'region': "ap-chengdu",
        # 这里改成允许的路径前缀，可以根据自己网站的用户登录态判断允许上传的具体路径
        # 例子： a.jpg 或者 a/* 或者 * (使用通配符*存在重大安全风险, 请谨慎评估使用)
        'allow_prefix': '*',
        # 密钥的权限列表。简单上传和分片需要以下的权限，其他权限列表请看 https://cloud.tencent.com/document/product/436/31923
        'allow_actions': [
            'name/cos:PostObject',
            # 'name/cos:DeleteObject',
            # "name/cos:UploadPart",
            # "name/cos:UploadPartCopy",
            # "name/cos:CompleteMultipartUpload",
            # "name/cos:AbortMultipartUpload",
            "*",
        ],

    }

    sts = Sts(config)
    result_dict = sts.get_credential()
    return JsonResponse(result_dict)
    