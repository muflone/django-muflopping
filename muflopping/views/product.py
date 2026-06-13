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

from django.db.models import Q

from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from muflopping.models.product import Product
from muflopping.serializers.product import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    """
    GET/POST /api/products/
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(
            Q(is_global=True) |
            Q(created_by=user)
        )


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET/PUT/PATCH/DELETE /api/products/<pk>/
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(
            Q(is_global=True) |
            Q(created_by=user)
        )

    def perform_update(self, serializer):
        if self.get_object().is_global:
            raise PermissionDenied('Global products cannot be modified.')
        serializer.save()

    def perform_destroy(self, instance):
        if instance.is_global:
            raise PermissionDenied('Global products cannot be deleted.')
        instance.delete()
