from django.shortcuts import render, redirect
from django.urls import reverse
from productos.models import *
from productos.forms import *

def listar_libros(request):
    contexto = {
        "libros" : Libros.objects.all()
    }
    http_response = render(
    request=request,
    template_name="productos/libros.html",
    context=contexto,
    )
    return http_response

def listar_musica(request):
    contexto = {
        "musica" : Musica.objects.all()
    }
    http_response = render(
    request=request,
    template_name="productos/musica.html",
    context=contexto,
    )
    return http_response

def add_libro(request):
   if request.method == "POST":
       formulario1 = LibrosFormulario(request.POST)

       if formulario1.is_valid():
           data = formulario1.cleaned_data
           titulo = data["titulo"]
           nombre_autor = data["nombre_autor"]
           apellido_autor = data["apellido_autor"]
           ISBN = data["ISBN"]
           libro = Libros(titulo=titulo, nombre_autor=nombre_autor, apellido_autor=apellido_autor, ISBN=ISBN)
           libro.save()

           url_exitosa = reverse("listar_libros")
           return redirect(url_exitosa)
   else:
       formulario1 = LibrosFormulario()
   
   http_response = render(
    request=request,
    template_name="productos/formulario_libros.html",
    context={"formulario1": formulario1}
   )
   return http_response

def add_musica(request):
   if request.method == "POST":
       formulario2 = MusicaFormulario(request.POST)

       if formulario2.is_valid():
           data = formulario2.cleaned_data
           titulo = data["titulo"]
           nombre_autor = data["nombre_autor"]
           genero = data["genero"]
           musica = Musica(titulo=titulo, nombre_autor=nombre_autor, genero=genero)
           musica.save()

           url_exitosa = reverse("listar_musica")
           return redirect(url_exitosa)
   else:
       formulario2 = MusicaFormulario()
   
   http_response = render(
    request=request,
    template_name="productos/formulario_musica.html",
    context={"formulario2": formulario2}
   )
   return http_response

def buscar_libro(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        libros = Libros.objects.filter(titulo__contains=busqueda)
        contexto = {
            "libros": libros,
        }
        http_response = render(
            request=request,
            template_name="productos/libros.html",
            context=contexto,
        )
        return http_response

def buscar_musica(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        musica = Musica.objects.filter(titulo__contains=busqueda)
        contexto = {
            "musica": musica,
        }
        http_response = render(
            request=request,
            template_name='productos/musica.html',
            context=contexto,
        )
        return http_response