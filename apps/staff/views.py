from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from apps.staff.models import Staff
from apps.staff.serializers import StaffSerializer
from base.models import CrudCommonMethods


# Create your views here.
class StaffViewSet(CrudCommonMethods):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (IsAuthenticated,)
