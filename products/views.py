from rest_framework import viewsets

from products import serializers
from products.models import Category, Product


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с категориями."""

    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с продуктами."""
    queryset = Product.objects.all()
    serializer_class = serializers.ProductReadSerializer
