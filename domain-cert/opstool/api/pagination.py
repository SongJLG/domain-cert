from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class OpsPageNumberPagination(PageNumberPagination):
    page_size = 5  # 每页显示3条数据
    page_query_param = 'page'  # 查询参数
    page_size_query_param = "size"
    page_size_query_description = 'size'
    max_page_size = 10  # 最大每页显示五条数据
# class MyPageNumberPagination(LimitOffsetPagination):
#     default_limit = 3
#     limit_query_param = 'limit'
#     offset_query_param = 'offset'
#     max_limit = 5
# class MyPageNumberPagination(CursorPagination):
#     cursor_query_param = 'cursor'               # 查询方式
#     page_size = 2                               # 每页显示多少条
#     ordering = '-id'                            # 排序方式,按什么排序
#     page_size_query_description = None          # 查询的时候指定每页显示多少条
#     max_page_size = None                        # 每页最多显示多少