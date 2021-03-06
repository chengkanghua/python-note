# by gaoxin

from django.middleware.security import SecurityMiddleware
from django.utils.deprecation import MiddlewareMixin


class MyCors(MiddlewareMixin):

    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        if request.method == "OPTIONS":
            response["Access-Control-Allow-Methods"] = "PUT, DELETE"
            response["Access-Control-Allow-Headers"] = "content-type"
        return response