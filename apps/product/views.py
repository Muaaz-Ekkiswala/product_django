
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.product.models import Product, ProductDetails, Category
from apps.product.serializers import ProductSerializer, CategorySerializer
# from apps.product.models import Product, ProductDetails
# from apps.product.serializers import ProductSerializer
from base.models import CrudCommonMethods


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(
    CrudCommonMethods
):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter]
    # search_fields = ("name", "price")

    # def create(self, request, *args, **kwargs):
    #     serializer = ProductSerializer(data=request.data)
    #     try:
    #         if serializer.is_valid():
    #             serializer.save()
    #             success = True
    #             data = serializer.data
    #             error = {}
    #         else:
    #             success = False
    #             data = {}
    #             error = serializer.errors
    #         return Response({
    #             "success": success,
    #             "data": data,
    #             "errors": error
    #         }, status=status.HTTP_201_CREATED if success == "True" else status.HTTP_400_BAD_REQUEST)
    #     except Exception as e:
    #         error = custom_error_response(errors=e)
    #         return Response({
    #             "success": False,
    #             "data": {},
    #             "errors": error
    #         }, status=status.HTTP_400_BAD_REQUEST)
    #
    # def list(self, request, *args, **kwargs):
    #     serializer = ProductSerializer(self.queryset, many=True)
    #     return Response({
    #         "success": True,
    #         "data": serializer.data,
    #         "errors": {}
    #     })
    #
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response({
    #         "success": True,
    #         "data": serializer.data,
    #         "errors": serializer.errors if serializer.errors else {}
    #     })
    #
    # def update(self, request, pk=None, *args, **kwargs):
    #     try:
    #         instance = Product.objects.filter(pk=pk).first()
    #         if instance:
    #             serializer = ProductSerializer(data=request.data, instance=instance, partial=True)
    #             if serializer.is_valid():
    #                 serializer.save()
    #                 return JsonResponse({
    #                     "success": True,
    #                     "data": serializer.data,
    #                     "errors": {}
    #                 }, status=status.HTTP_200_OK)
    #             return JsonResponse(success=False, data={}, error=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except Exception as e:
    #         error = custom_error_response(errors=e)
    #         return JsonResponse(error=error, data={}, success=False, status=status.HTTP_400_BAD_REQUEST)
    #
    # def retrieve(self, request, pk=None, *args, **kwargs):
    #     product = get_object_or_404(self.queryset, pk=pk)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    #
    # def destroy(self, request, pk=None, *args, **kwargs):
    #     instance = self.queryset.filter(pk=pk).first()
    #     if instance:
    #         self.perform_destroy(instance)
    #         return Response({
    #             "success": "True",
    #             "data": {},
    #             "errors": {}
    #         }, status=status.HTTP_204_NO_CONTENT)
    #     else:
    #         return Response({
    #             "success": False,
    #             "data": {},
    #             "errors": f"Product with {pk} not found"
    #         }, status=status.HTTP_404_NOT_FOUND)

    def get_serialized_list_response(self, query_set):
        products = query_set
        product_details = ProductDetails.objects.all()
        product_details_dict = {ele.product_id: ele for ele in product_details}
        list_data = []
        for obj in products:
            product = dict()
            product['id'] = obj.id
            product['name'] = obj.name
            product['price'] = obj.price
            product['updated_at'] = obj.updated_at
            product['product_details'] = dict()
            product_detail_obj = product_details_dict.get(obj.id)
            if product_detail_obj:
                product['product_details']['id'] = product_detail_obj.id
                product['product_details']['description'] = product_detail_obj.description
                product['product_details']['quantity'] = product_detail_obj.quantity
                product['total_price'] = int(obj.price * product_detail_obj.quantity)
            list_data.append(product)
        return list_data

    # def list(self, request, *args, **kwargs):
    #     list_data = self.get_serialized_list_response(query_set=self.queryset)
    #     if request.query_params.get('apply_pagination') == '1':
    #         list_data = self.get_paginated_response(request)
    #     return self.get_success_response(status_code=status.HTTP_200_OK, data=list_data)
