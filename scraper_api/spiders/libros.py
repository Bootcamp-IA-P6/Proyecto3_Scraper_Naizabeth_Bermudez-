

import scrapy

class LibrosSpider(scrapy.Spider):
    name = "libros"
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        for libro in response.css('article.product_pod'):
            # Capturamos los datos
            datos = {
                'titulo': libro.css('h3 a::attr(title)').get(),
                'precio': libro.css('p.price_color::text').get(),
                'rating': libro.css('p.star-rating::attr(class)').get().replace('star-rating ', ''),
                'disponibilidad': 'In stock' in libro.css('p.instock.availability::text').get(),
                'enlace': response.urljoin(libro.css('h3 a::attr(href)').get()),
            }
            # Enviamos los datos a la Pipeline (pipelines.py)
            yield datos