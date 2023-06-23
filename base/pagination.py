# from collections import OrderedDict
#
# from django.core.paginator import Paginator
# from rest_framework import status
# from rest_framework.pagination import LimitOffsetPagination, BasePagination
# from rest_framework.response import Response
#
# from base.custom_response import JsonResponse
# from demo import settings
#
#
# class CustomPagination:
#
#     def get_paginated_response(self, queryset, request):
#         page = request.query_params.get('page') if request.query_params.get('page') else 1
#         page = int(page) if not page.isdigit() else page
#         limit = request.query_params.get('limit') if request.query_params.get('limit') else settings.PAGE_SIZE
#         limit = int(limit) if not limit.isdigit() else limit
#         total_records = len(queryset)
#         offset = (page - 1) * limit
#
#         if total_records == 0 or offset > total_records:
#             return []
#         query_set = queryset[offset: offset + limit]
#         return JsonResponse(success=True, data=query_set, error={}, status=status.HTTP_200_OK)