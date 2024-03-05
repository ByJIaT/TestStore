from django.db import transaction
from rest_framework import serializers

from products.models import Product
from products.serializers.products import ProductReadMiniFieldSerializer
from shopping_cart.models import ShoppingCart, CartProduct


class CartProductReadSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения промежуточной модели."""
    product = ProductReadMiniFieldSerializer()

    class Meta:
        model = CartProduct
        fields = ('product', 'quantity')


class CartProductWriteSerializer(serializers.ModelSerializer):
    """Сериализатор для записи промежуточной модели."""

    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())

    class Meta:
        model = CartProduct
        fields = ('product', 'quantity')


class ShoppingCartReadSerializer(serializers.ModelSerializer):
    """Чтение корзины."""
    cart_products = CartProductReadSerializer(
        read_only=True, many=True, source='cart')
    total_price = serializers.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        model = ShoppingCart
        fields = ('id', 'cart_products', 'total_price')


class ShoppingCartWriteSerializer(serializers.ModelSerializer):
    """Запись корзины."""

    cart_products = CartProductWriteSerializer(many=True)

    class Meta:
        model = ShoppingCart
        fields = ('cart_products',)

    def create_or_update(self, validated_data, instance=None):
        cart_products = validated_data.pop('cart_products', None)
        shopping_cart = instance if instance else ShoppingCart()

        for key, value in validated_data.items():
            setattr(shopping_cart, key, value)
        shopping_cart.save()

        for cart_product in cart_products:
            product = cart_product.pop('product')
            shopping_cart.cart_products.remove(product)
            shopping_cart.cart_products.add(
                product, through_defaults=cart_product)

        return shopping_cart

    @transaction.atomic
    def create(self, validated_data):
        return self.create_or_update(validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        return self.create_or_update(validated_data, instance=instance)

    def to_representation(self, instance):
        serializer = ShoppingCartReadSerializer(
            instance, context=self.context)
        return serializer.data
