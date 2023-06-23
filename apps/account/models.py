# Create your models here
from django.contrib.auth import get_user_model

from base.models import BaseModel
from django.db import models


class Profile(BaseModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)

    class Meta:
        db_table = "profile"

