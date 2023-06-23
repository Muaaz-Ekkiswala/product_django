from apps.product.models import ProductDetails


def get_serialized_list_response(query_set):
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
        product['product_detail'] = dict()
        product_detail_obj = product_details_dict.get(obj.id)
        if product_detail_obj:
            product['product_detail']['id'] = product_detail_obj.id
            product['product_detail']['description'] = product_detail_obj.description
            product['product_detail']['quantity'] = product_detail_obj.quantity
            product['total_price'] = product_detail_obj.total_price
        list_data.append(product)
    return list_data