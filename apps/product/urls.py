from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_mongoengine.routers import DefaultRouter as monogo_router
from apps.product import views

router = monogo_router()
router.register(r'categories', views.CategoryViewSet, basename="category")
router.register(r'', views.ProductViewSet, basename="product")


urlpatterns = [
    path('', include(router.urls)),
]