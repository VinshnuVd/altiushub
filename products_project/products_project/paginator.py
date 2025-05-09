from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPaginator(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    def get_paginated_response(self, data):
        response = {
            'status': '200',
            'data':{
                'count': self.page.paginator.count,
                'results': data
            }
        }
        return Response(response, status=200)
