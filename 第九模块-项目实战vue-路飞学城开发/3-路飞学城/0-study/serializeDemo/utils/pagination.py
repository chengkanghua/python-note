from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination


# class MyPagination(PageNumberPagination):
#     # xxx?page=1&size=2
#     page_size = 1
#     page_query_param = "page"
#     page_size_query_param = "size"
#     max_page_size = 3

# http://127.0.0.1:8000/page/book?limit=1&offset=1
# class MyPagination(LimitOffsetPagination):
#     default_limit = 1
#     limit_query_param = "limit"   # 向后找几条数据
#     offset_query_param = "offset"  # 初始位置
#     max_limit = 3


# 游标的地址是加密的 http://127.0.0.1:8000/page/book?cursor=cj0xJnA9Mg%3D%3D
class MyPagination(CursorPagination):
    cursor_query_param = "cursor"
    page_size = 2
    ordering = "-id"  # 以id倒叙