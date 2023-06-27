

from rest_framework import viewsets, status

from rest_framework.permissions import IsAuthenticated
from rest_framework_mongoengine import viewsets as mongo_viewsets
from apps.product.models import Product, ProductDetails, Category
from apps.product.serializers import ProductSerializer, CategorySerializer

from base.models import CrudCommonMethods


# Create your views here.
class CategoryViewSet(mongo_viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(
    CrudCommonMethods
):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serialized_list_response(self, query_set):
        products = query_set
        product_details = ProductDetails.objects.all()
        product_details_dict = {ele.product.pk: ele for ele in product_details}

        list_data = []
        for obj in products:
            product = dict()
            product['id'] = obj.pk
            product['name'] = obj.name
            product['price'] = obj.price
            # product['updated_at'] = obj.updated_at
            product['product_details'] = dict()
            product_detail_obj = product_details_dict.get(obj.pk)
            if product_detail_obj:
                product['product_details']['id'] = product_detail_obj.pk
                product['product_details']['description'] = product_detail_obj.description
                product['product_details']['quantity'] = product_detail_obj.quantity
                product['total_price'] = int(obj.price * product_detail_obj.quantity)
            list_data.append(product)
        return list_data
