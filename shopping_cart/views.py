from django.db.models import F, Sum
from rest_framework import viewsets, permissions

from shopping_cart.models import ShoppingCart
from shopping_cart.serializers import (ShoppingCartReadSerializer,
                                       ShoppingCartWriteSerializer)


class ShoppingCartViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return (
            ShoppingCart.objects.filter(user=self.request.user)
            .prefetch_related('cart__product')
            .annotate(
                total_price=Sum(F('cart_products__price') * F('cart__quantity'))
            )
        )

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ShoppingCartReadSerializer
        return ShoppingCartWriteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
