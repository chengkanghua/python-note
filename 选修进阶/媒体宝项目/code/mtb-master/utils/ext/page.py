from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class MtbLimitOffsetPagination(LimitOffsetPagination):
    # xxxxxx?limit=10
    default_limit = 10
    max_limit = 100
    offset_query_param = None


class MtbPageNumberPagination(PageNumberPagination):
    page_size = 10  # 每页显示10条数据
