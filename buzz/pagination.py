# from rest_framework.pagination import PageNumberPagination
#
# class CustomPageNumberPagination(PageNumberPagination):
#     page_size = 5
#     page_size_query_param = 'page_size'
#     # page_query_param = "p"
#     max_page_size = 10
#     # last_page_strings = "end"


from rest_framework.pagination import LimitOffsetPagination

class BuzzLimitOffsetPagination(LimitOffsetPagination):
    pass
#
#
# from rest_framework.pagination import CursorPagination
#
# class BuzzCursorPagination(CursorPagination):
#     pass
