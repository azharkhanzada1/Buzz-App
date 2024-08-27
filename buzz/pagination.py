from rest_framework.pagination import LimitOffsetPagination

class BuzzLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
