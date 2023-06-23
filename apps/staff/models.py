from django.db import models

from base.models import BaseModel


# Create your models here.
class Staff(BaseModel):
    first_name = models.CharField(max_length=255, verbose_name="employee_first_name")
    last_name = models.CharField(max_length=255, verbose_name="employee_last_name")
    address = models.TextField(verbose_name="employee_address")

    class Meta:
        db_table = "Staff"
