from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name='country_name', unique=True)
    country_code = models.CharField(max_length=3, verbose_name='country_code', unique=True)

    class Meta:
        db_table = "country"
