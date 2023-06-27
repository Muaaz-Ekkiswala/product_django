# from django.db import models


# Create your models here.
# class Category(BaseModel):
#     name = models.CharField(verbose_name="product_category", max_length=255, unique=True)
#
#     class Meta:
#         db_table = "category"
#
#
# class Product(BaseModel):
#     name = models.CharField(max_length=255, verbose_name="product_name")
#     price = models.IntegerField(verbose_name="product_price")
#
#     class Meta:
#         db_table = "product"
#
#
# class ProductDetails(BaseModel):
#     description = models.TextField(max_length=500, verbose_name="product_description")
#     quantity = models.IntegerField(verbose_name="product_quantity")
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_detail_category")
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_detail_product")
#
#     class Meta:
#         db_table = "Product_details"
#
#     @property
#     def total_price(self):
#         product_price = self.product.__dict__
#         return self.quantity * product_price.get('price')

from django_mongoengine import Document, fields

from base.models import generate_obj_id


class Category(Document):
    id = fields.StringField(primary_key=True, db_column='id', default=generate_obj_id)
    name = fields.StringField(max_length=255, unique=True, verbose_name="product_category")

    meta = {"db_alias": "default", 'collection': 'category_collection'}


class Product(Document):
    id = fields.StringField(primary_key=True, db_column='id', default=generate_obj_id)
    name = fields.StringField(max_length=255, unique=True, verbose_name="product_name")
    price = fields.IntField(verbose_name="product_price")

    meta = {"db_alias": "default", 'collection': 'product_collection'}


class ProductDetails(Document):
    id = fields.StringField(primary_key=True, db_column='id', default=generate_obj_id)
    description = fields.StringField(max_length=500, null=False)
    quantity = fields.IntField(verbose_name="product_quantity")
    product = fields.ReferenceField('Product')
    category = fields.ReferenceField('Category')

    meta = {"db_alias": "default", 'collection': 'product_details_collection'}
