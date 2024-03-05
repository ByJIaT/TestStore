from _decimal import Decimal, ROUND_HALF_UP

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import F
from django.utils.translation import gettext_lazy as _

from products.models import Product

User = get_user_model()


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user',
        verbose_name=_('User'),
    )
    cart_products = models.ManyToManyField(
        Product,
        through='CartProduct',
        related_name='cart_products',
    )

    class Meta:
        verbose_name = _('ShoppingCart')
        verbose_name_plural = _('ShoppingCarts')


class CartProduct(models.Model):
    cart = models.ForeignKey(
        ShoppingCart,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name=_('ShoppingCart'),
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product',
        verbose_name=_('Product')
    )
    quantity = models.PositiveIntegerField(verbose_name=_('Product quantity'))

    class Meta:
        verbose_name = _('Product in the shopping cart')
        verbose_name_plural = _('Products in the shopping cart')

    def __str__(self):
        return (
            f'{self.quantity} x {self.product} in Basket for '
            f'User: {self.cart.user}'
        )
