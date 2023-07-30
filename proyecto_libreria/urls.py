from django.contrib import admin
from django.urls import path, include
from proyecto_libreria.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio, name="inicio"),
    path("productos/", include("productos.urls")),
    path("clientes/", include("clientes.urls")),
]
