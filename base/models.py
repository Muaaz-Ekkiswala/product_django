import uuid


from django.db import models
from rest_framework import status, viewsets

from base.custom_error_response import custom_error_response
from base.custom_response import JsonResponse
from demo import settings


# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
#
#
# class CrudCommonMethods(viewsets.GenericViewSet):
#
#     def __int__(self, serializer_class, queryset, permission_class=None):
#         self.serializer_class = serializer_class
#         self.queryset = queryset
#         self.permission_class = permission_class
#
#     def get_instance(self, pk):
#         return self.queryset.filter(pk=pk).first()
#
#     def get_serialized_list_response(self, query_set):
#         """
#             Common method to get serialized response
#         """
#         list_data = []
#         for obj in query_set:
#             list_data.append(self.serializer_class(obj).data)
#         return list_data
#
#     def get_paginated_response(self, request):
#         """
#             Common method for pagination
#         """
#         page = request.query_params.get('page', "1")
#         page = int(page) if page.isdigit() else page
#         limit = request.query_params.get('limit', str(settings.PAGE_SIZE))
#         limit = int(limit) if limit.isdigit() else limit
#         total_records = len(self.queryset)
#         offset = (page - 1) * limit
#
#         if total_records == 0 or offset > total_records:
#             return []
#
#         pagination = dict()
#         pagination['total_records'] = total_records
#         pagination['limit'] = limit
#         pagination['page'] = page
#         data = dict()
#         data['pagination'] = pagination
#         data['list'] = self.get_serialized_list_response(query_set=self.queryset[offset: offset + limit])
#         return data
#
#     def get_success_response(self, status_code, data, ):
#         """
#             Common success Response
#         """
#         return JsonResponse(status=status_code, data=data, success=True, error={})
#
#     def get_error_response(self, status_code, errors):
#         """
#             Common error Response
#         """
#         return JsonResponse(status=status_code, data={}, success=True, error=errors)
#
#     def create(self, request, *args, **kwargs):
#         """
#             Common create() method
#         """
#         serializer = self.serializer_class(data=request.data)
#         valid_serializer = serializer.is_valid()
#         if valid_serializer:
#             serializer.save()
#             return self.get_success_response(
#                 status_code=status.HTTP_201_CREATED,
#                 data=serializer.data,
#             )
#         else:
#             return self.get_error_response(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 errors=custom_error_response(serializer.errors)
#             )
#
#     def list(self, request, *args, **kwargs):
#         """
#             Common list() method
#         """
#         if request.query_params.get('apply_pagination') == '1':
#             list_data = self.get_paginated_response(request)
#         else:
#             list_data = self.get_serialized_list_response(query_set=self.queryset)
#         return self.get_success_response(status_code=status.HTTP_200_OK, data=list_data)
#
#     def retrieve(self, request, pk=None, *args, **kwargs):
#         """
#             Common retrieve() method
#         """
#         instance = self.get_instance(pk=pk)
#         if instance:
#             serializer = self.serializer_class(instance)
#             return self.get_success_response(status_code=status.HTTP_200_OK, data=serializer.data)
#         else:
#             return self.get_error_response(status_code=status.HTTP_404_NOT_FOUND, errors=f"Data with {pk} not found")
#
#     def update(self, request, pk=None, *args, **kwargs):
#         """
#             Common update method
#         """
#         partial = request.query_params.get('partial', False)
#         instance = self.get_instance(pk=pk)
#         if not instance:
#             return self.get_error_response(status_code=status.HTTP_404_NOT_FOUND, errors=f"Data with {pk} not found")
#         serializer = self.serializer_class(instance, data=request.data, partial=partial)
#         valid_serializer = serializer.is_valid()
#         if valid_serializer:
#             serializer.save()
#             return self.get_success_response(status_code=status.HTTP_200_OK, data=serializer.data)
#         else:
#             return self.get_error_response(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 errors=custom_error_response(serializer.errors)
#             )
#
#     def destroy(self, request, pk=None, *args, **kwargs):
#         """
#             Common delete method
#         """
#         instance = self.get_instance(pk=pk)
#         if instance:
#             instance.delete()
#             return self.get_success_response(status_code=status.HTTP_204_NO_CONTENT, data=None)
#         else:
#             return self.get_error_response(status_code=status.HTTP_404_NOT_FOUND, errors=f"Data with {pk} not found")


class CrudCommonMethods(viewsets.GenericViewSet):

    def __int__(self, serializer_class, queryset, permission_class=None):
        self.serializer_class = serializer_class
        self.queryset = queryset
        self.permission_class = permission_class

    def get_instance(self, pk):
        return self.queryset.filter(pk=pk).first()

    def get_serialized_list_response(self, query_set):
        """
            Common method to get serialized response
        """
        list_data = []
        for obj in query_set:
            list_data.append(self.serializer_class(obj).data)
        return list_data

    def get_paginated_response(self, request):
        """
            Common method for pagination
        """
        page = request.query_params.get('page', "1")
        page = int(page) if page.isdigit() else page
        limit = request.query_params.get('limit', str(settings.PAGE_SIZE))
        limit = int(limit) if limit.isdigit() else limit
        total_records = len(self.queryset)
        offset = (page - 1) * limit

        if total_records == 0 or offset > total_records:
            return []

        pagination = dict()
        pagination['total_records'] = total_records
        pagination['limit'] = limit
        pagination['page'] = page
        data = dict()
        data['pagination'] = pagination
        data['list'] = self.get_serialized_list_response(query_set=self.queryset[offset: offset + limit])
        return data

    def get_success_response(self, status_code, data, ):
        """
            Common success Response
        """
        return JsonResponse(status=status_code, data=data, success=True, error={})

    def get_error_response(self, status_code, errors):
        """
            Common error Response
        """
        return JsonResponse(status=status_code, data={}, success=True, error=errors)

    def create(self, request, *args, **kwargs):
        """
            Common create() method
        """
        serializer = self.serializer_class(data=request.data)
        valid_serializer = serializer.is_valid()
        if valid_serializer:
            serializer.save()
            return self.get_success_response(
                status_code=status.HTTP_201_CREATED,
                data=serializer.data,
            )
        else:
            return self.get_error_response(
                status_code=status.HTTP_400_BAD_REQUEST,
                errors=custom_error_response(serializer.errors)
            )

    def list(self, request, *args, **kwargs):
        """
            Common list() method
        """
        if request.query_params.get('apply_pagination') == '1':
            list_data = self.get_paginated_response(request)
        else:
            list_data = self.get_serialized_list_response(query_set=self.queryset)
        return self.get_success_response(status_code=status.HTTP_200_OK, data=list_data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        """
            Common retrieve() method
        """
        instance = self.get_instance(pk=pk)
        if instance:
            serializer = self.serializer_class(instance)
            return self.get_success_response(status_code=status.HTTP_200_OK, data=serializer.data)
        else:
            return self.get_error_response(status_code=status.HTTP_404_NOT_FOUND, errors=f"Data with {pk} not found")

    def update(self, request, pk=None, *args, **kwargs):
        """
            Common update method
        """
        partial = request.query_params.get('partial', False)
        instance = self.get_instance(pk=pk)
        if not instance:
            return self.get_error_response(status_code=status.HTTP_404_NOT_FOUND, errors=f"Data with {pk} not found")
        serializer = self.serializer_class(instance, data=request.data, partial=partial)
        valid_serializer = serializer.is_valid()
        if valid_serializer:
            serializer.save()
            return self.get_success_response(status_code=status.HTTP_200_OK, data=serializer.data)
        else:
            return self.get_error_response(
                status_code=status.HTTP_400_BAD_REQUEST,
                errors=custom_error_response(serializer.errors)
            )

    def destroy(self, request, pk=None, *args, **kwargs):
        """
            Common delete method
        """
        instance = self.get_instance(pk=pk)
        if instance:
            instance.delete()
            return self.get_success_response(status_code=status.HTTP_204_NO_CONTENT, data=None)
        else:
            return self.get_error_response(status_code=status.HTTP_404_NOT_FOUND, errors=f"Data with {pk} not found")