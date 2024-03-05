from django.urls import include, path
from rest_framework import routers

from shopping_cart import views

router = routers.DefaultRouter()
router.register('shopping-cart', views.ShoppingCartViewSet,
                basename='shopping-cart')

urlpatterns = [path('', include(router.urls))]
