from django.contrib import admin
from django.urls import path
from productos.views import *

urlpatterns = [
    path("libros/", listar_libros, name="listar_libros"),
    path("musica/", listar_musica, name="listar_musica"),
    path("agregarlibros/", add_libro, name="agregar_libros"),
    path("agregarmusica/", add_musica, name="agregar_musica"),
    path("buscarlibros/", buscar_libro, name="buscar_libro"),
    path("buscaralbum/", buscar_musica, name="buscar_musica"),
    ]