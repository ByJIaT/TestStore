from rest_framework import serializers

from products.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для получения данных о категории."""

    parent_id = serializers.PrimaryKeyRelatedField(
        read_only=True, source='parent',
    )

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'parent_id', 'image', 'subcategories')

    def get_fields(self):
        fields = super().get_fields()
        fields['subcategories'] = CategorySerializer(many=True)
        return fields
