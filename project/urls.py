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

import django.conf
from django.contrib import admin
from django.urls import path

from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularSwaggerView)


urlpatterns = [
    path(route=django.conf.settings.ADMIN_URL,
         view=admin.site.urls),
    path(route='api/schema/',
         view=SpectacularAPIView.as_view(),
         name='schema'),
    path(route='api/swagger/',
         view=SpectacularSwaggerView.as_view(),
         name='swagger-ui'),
]
