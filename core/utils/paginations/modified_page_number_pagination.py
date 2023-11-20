from collections                import OrderedDict
from rest_framework.pagination  import PageNumberPagination
from rest_framework.response    import Response

class ModifiedPageNumberPagination(PageNumberPagination):
    page_size = 10
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('total',       self.page.paginator.count),
            ('next',        self.get_next_link()),
            ('previous',    self.get_previous_link()),
            ('results',     data)
        ]))