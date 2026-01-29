from django.db import models

# Create your models here.
# Este modelo es la base o sea mi tabla para que pueda entender que quiero extraer datos de una web 
from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    precio = models.CharField(max_length=50)
    rating = models.CharField(max_length=50) # Ejemplo: "Three stars"
    disponibilidad = models.BooleanField(default=True)
    enlace = models.URLField(unique=True)

    def __str__(self):
       return f"{self.titulo} - {self.precio} ({self.rating})"
    #Ejemplo de visualización The Alchemist - £15.99 (Four stars)
