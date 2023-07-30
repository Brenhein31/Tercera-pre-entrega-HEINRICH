from django import forms

class LibrosFormulario(forms.Form):
    titulo = forms.CharField(max_length=256)
    nombre_autor = forms.CharField(max_length=256)
    apellido_autor = forms.CharField(max_length=256)
    ISBN = forms.IntegerField(required=True)

class MusicaFormulario(forms.Form):
    titulo = forms.CharField(max_length=256)
    nombre_autor = forms.CharField(max_length=256)
    genero = forms.CharField(max_length=256)