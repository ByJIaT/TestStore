from rest_framework import serializers

from products.models import Image


class ImageSerializer(serializers.ModelSerializer):
    """Сериализатор для получения данных об изображении."""

    class Meta:
        model = Image
        fields = ('image',)
