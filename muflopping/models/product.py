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

from django.conf import settings
from django.contrib import admin
from django.db import models

from .category import Category
from .unit import Unit


class Product(models.Model):
    """
    A product that can appear on a shopping list item.

    - is_global=True: preset product, visible to everyone (created_by is NULL)
    - is_global=False: user-created product, visible only to its owner
    """
    name = models.CharField(
        max_length=200,
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name='products',
    )
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
    )
    is_global = models.BooleanField(
        default=False,
    )
    unit = models.ForeignKey(
        to=Unit,
        blank=False,
        null=True,
        default=None,
        on_delete=models.PROTECT,
        related_name='products',
    )
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='custom_products',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_global', 'unit',
                    'created_by', 'created_at')
    list_filter = ('is_global', 'category')
    search_fields = ('name', )
