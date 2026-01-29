from buscador.models import Libro # Importamos tu modelo de Django

class ScraperApiPipeline:
    def process_item(self, item, spider):
        # Aquí es donde ocurre la magia: guardamos en MySQL
        # Usamos update_or_create por si el libro ya existe, que no se repita
        Libro.objects.update_or_create(
            enlace=item.get('enlace'), # Usamos el enlace como identificador único
            defaults={
                'titulo': item.get('titulo'),
                'precio': item.get('precio'),
                'rating': item.get('rating'),
                'disponibilidad': item.get('disponibilidad'),
            }
        )
        return item