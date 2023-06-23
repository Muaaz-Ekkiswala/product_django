from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.staff import views

router = DefaultRouter()
router.register(r'', views.StaffViewSet, basename='staff')

urlpatterns = [
    path('', include(router.urls))
]