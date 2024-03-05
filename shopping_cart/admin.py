from django.contrib import admin

from shopping_cart.models import ShoppingCart, CartProduct


class CartProductInline(admin.TabularInline):
    model = CartProduct
    extra = 1


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    list_filter = ('user',)
    search_fields = ('user',)
    empty_value_display = '-empty-'
    inlines = (CartProductInline,)
