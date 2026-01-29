from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Libro

def lista_libros(request):
    # Traemos todos los libros de la base de datos
    libros = Libro.objects.all()
    # Los enviamos al archivo HTML (que crearemos luego)
    return render(request, 'lista.html', {'libros': libros})
