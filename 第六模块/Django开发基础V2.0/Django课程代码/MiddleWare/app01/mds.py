from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class IpValid(MiddlewareMixin):

    def process_request(self, request):
        '''

        :param request: 请求信息对象
        :return: 默认返回None，当返回一个响应体的时候，实现了拦截，原路返回
        '''
        print("MD1 process_request")

        # 非法IP识别
        visit_ip = request.META.get("REMOTE_ADDR")
        if visit_ip in []:
            return HttpResponse("<h1>非法IP！</h1>")

        return None



    # def process_response(self, request, response):
    #     '''
    #
    #     :param request: 请求信息对象
    #     :param response: 视图函数返回的响应体
    #     :return:
    #     '''
    #     print("MD1 process_response")
    #     print("MD1 response:", response)
    #
    #     return response


class HI(MiddlewareMixin):

    # def process_request(self, request):
    #     '''
    #
    #     :param request: 请求信息对象
    #     :return:
    #     '''
    #     print("MD2 process_request")

    def process_response(self, request, response):
        '''

        :param request: 请求信息对象
        :param response: 视图函数返回的响应体
        :return:必须返回一个响应体对象
        '''
        print("MD2 process_response")
        print("MD2 response:", response.content)

        response.content = b"<h1>welcome to luffyCity!</h1>" + response.content

        return response
