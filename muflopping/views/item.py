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

from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from muflopping.models.list import List
from muflopping.models.item import Item
from muflopping.permissions import IsListOwner
from muflopping.serializers.item import ItemSerializer


class ItemListCreateView(generics.ListCreateAPIView):
    """
    GET /api/lists/<list_pk>/items/
    POST /api/lists/<list_pk>/items/
    """
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def _get_list(self):
        shopping_list = get_object_or_404(klass=List,
                                          pk=self.kwargs['list_pk'])
        if shopping_list.owner != self.request.user:
            raise PermissionDenied()
        return shopping_list

    def get_queryset(self):
        return Item.objects.filter(list=self._get_list())

    def perform_create(self, serializer):
        serializer.save(list=self._get_list())


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET/PUT/PATCH/DELETE /api/lists/<list_pk>/items/<pk>/
    """
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsListOwner]

    def get_queryset(self):
        shopping_list = get_object_or_404(klass=List,
                                          pk=self.kwargs['list_pk'],
                                          owner=self.request.user)
        return Item.objects.filter(list=shopping_list)
