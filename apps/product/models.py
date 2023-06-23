from django.db import models

from base.models import BaseModel


# Create your models here.
class Category(BaseModel):
    name = models.CharField(verbose_name="product_category", max_length=255, unique=True)

    class Meta:
        db_table = "category"


class Product(BaseModel):
    name = models.CharField(max_length=255, verbose_name="product_name")
    price = models.IntegerField(verbose_name="product_price")

    class Meta:
        db_table = "product"


class ProductDetails(BaseModel):
    description = models.TextField(max_length=500, verbose_name="product_description")
    quantity = models.IntegerField(verbose_name="product_quantity")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_detail_category")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_detail_product")

    class Meta:
        db_table = "Product_details"

    @property
    def total_price(self):
        product_price = self.product.__dict__
        return self.quantity * product_price.get('price')

# from django_mongoengine import Document, EmbeddedDocument, fields
#
#
# class Product(Document):
#     name = fields.StringField(max_length=255, unique=True, verbose_name="product_name")
#     price = fields.IntField(verbose_name="product_price")
#     product_details = fields.DictField(fields.EmbeddedDocumentField('ProductDetails'), blank=True)
#
#     # meta = {
#     #     'collection': "product_collection"
#     # }
#
#
# class ProductDetails(EmbeddedDocument):
#     description = fields.StringField(max_length=500, null=False)
#     quantity = fields.IntField(verbose_name="product_quantity")
