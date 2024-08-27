# from rest_framework.pagination import PageNumberPagination
#
# class UserPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = "page_size"
#     max_page_size = 5
#
from rest_framework.pagination import LimitOffsetPagination

class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 6

# from rest_framework.pagination import CursorPagination
#
# class UserCursorPagination(CursorPagination):
#     page_size = 5
#     ordering = 'title'