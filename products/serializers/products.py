from rest_framework import serializers

from products.models import Product
from products.serializers import CategorySerializer
from products.serializers.images import ImageSerializer


class ProductReadSerializer(serializers.ModelSerializer):
    """Сериализатор для получения и отображения данных о товаре."""

    images = ImageSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('name', 'slug', 'category', 'price', 'images',)


class ProductReadMiniFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'slug', 'category', 'images')
