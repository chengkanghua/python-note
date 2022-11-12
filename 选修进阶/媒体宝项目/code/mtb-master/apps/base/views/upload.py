from rest_framework.views import APIView
from rest_framework.response import Response

import os
from datetime import datetime
from django.conf import settings
from django.core.files.storage import default_storage
from utils import return_code


def get_upload_filename(file_name):
    date_path = datetime.now().strftime('%Y/%m/%d')
    upload_path = os.path.join(settings.UPLOAD_PATH, date_path)
    return default_storage.get_available_name(
        os.path.join(upload_path, file_name)
    )


class UploadImageView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            # 获取用上传的图片对象
            uploaded_file = request.FILES.get('file')

            file_name = get_upload_filename(uploaded_file.name)
            saved_path = default_storage.save(file_name, uploaded_file)
            local_url = default_storage.url(saved_path)
            context = {
                'code': return_code.SUCCESS,
                'data': {
                    'url': local_url,
                    'abs_url': "{}{}".format("http://mtb.pythonav.com", local_url)
                }
            }
        except Exception as e:
            context = {
                'code': return_code.ERROR,
                'error': str(e),
            }
        return Response(context)
