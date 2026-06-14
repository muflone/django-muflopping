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

from rest_framework import generics, permissions

from muflopping.models.list import List
from muflopping.permissions import IsListOwner
from muflopping.serializers.list import ListSerializer


class ListListCreateView(generics.ListCreateAPIView):
    """
    GET/POST /api/lists/
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListSerializer

    def get_queryset(self):
        return List.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET/PUT/PATCH/DELETE /api/lists/<pk>/
    """
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated, IsListOwner]

    def get_queryset(self):
        return List.objects.filter(owner=self.request.user)
