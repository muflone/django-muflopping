##
#     Project: Django Muflopping
# Description: Backend for Muflopping
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2026 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

from django.contrib import admin
from django.db import models

from .product import Product
from .unit import Unit


class Item(models.Model):
    """
    Items for the shopping lists.
    """
    list = models.ForeignKey(
        to='List',
        on_delete=models.CASCADE,
        related_name='items',
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.PROTECT,
        related_name='items',
    )
    quantity = models.IntegerField(
        default=1,
    )
    unit = models.ForeignKey(
        to=Unit,
        on_delete=models.PROTECT,
        related_name='items',
    )
    is_checked = models.BooleanField(
        default=False,
    )
    note = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ['product__category__order', 'product__category__name',
                    'product__name']

    def __str__(self):
        return f'{self.product.name} × {self.quantity} {self.unit}'


class ItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'list', 'quantity', 'unit', 'is_checked')
    list_filter = ('list', )


class ItemInlineAdmin(admin.TabularInline):
    model = Item
    extra = 0
