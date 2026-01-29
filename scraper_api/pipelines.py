from asgiref.sync import sync_to_async
from buscador.models import Libro

class ScraperApiPipeline:
    async def process_item(self, item, spider):
        # Usamos sync_to_async para que Django permita el guardado
        await sync_to_async(self.save_item)(item)
        return item

    def save_item(self, item):
        # Esta es la parte que guarda en MySQL
        Libro.objects.update_or_create(
            enlace=item.get('enlace'),
            defaults={
                'titulo': item.get('titulo'),
                'precio': item.get('precio'),
                'rating': item.get('rating'),
                'disponibilidad': item.get('disponibilidad', False),
            }
        )