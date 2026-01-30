from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio', 'rating', 'disponibilidad') # Columnas que verás en el panel
