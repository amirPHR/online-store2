from rest_framework.pagination import PageNumberPagination 

# Pagination Class for API response
class DefaultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 200