from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Image(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('Product'),
    )
    image = models.ImageField(
        upload_to='products/',
        null=True,
        verbose_name=_('Product image'),
    )

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __str__(self):
        return f'{self.product}'


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Category name'),
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories',
        verbose_name=_('Category parent'),
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        null=True,
        verbose_name=_('Category slug'),
    )

    image = models.ImageField(
        upload_to='categories/',
        null=True,
        blank=True,
        verbose_name=_('Category image'),
    )

    class Meta:
        ordering = ('name',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Product name'),
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=False,
        null=True,
        related_name='categories',
        verbose_name=_('Product category'),
    )
    price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        verbose_name=_('Product price'),
        validators=[MinValueValidator(0.01)],
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        null=True,
        verbose_name=_('Product slug'),
    )

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return f'{self.name}'
