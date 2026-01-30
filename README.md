
# Bienvenido al mundo de Scrapy

<img src="https://github.com/Bootcamp-IA-P6/Proyecto3_Scraper_Naizabeth_Bermudez-/blob/develop/buscador/templates/img/scrapy.png?raw=true" alt="Logo Scrapy" width="850">

 ![Scrapy](https://img.shields.io/badge/SCRAPY-2.11+-60A839?style=for-the-badge&logo=scrapy&logoColor=white)
![MySQL](https://img.shields.io/badge/MYSQL_WORKBENCH-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Django](https://img.shields.io/badge/DJANGO-5.0+-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/PYTHON-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)

## Objetivo del proyecto 🚀

Extraer datos de sitios webs con la finalidad de presentar un flujo de trabajo que nos permita interpretar a traves de Dasbhoard como sera el comportamiento y analisis del mercado.

### Recomendación:
* Antes de acceder a cualquier página tus líneas de código tienen que ir relacionadas con lo que deseas extraer y donde sera la ruta en la que se guardaran esos datos, recuerda que eres tu el que hace mas inteligente a tu robot 

#### ¿Al principio pensabas que no podias ejecutar tu scrapy con Django?
He decidido intentarlo con estos Framework y me funciono todo en mi local.
si quieres hacer un git clone, hazlo y vas estudiando las lineas de codigo o puedes leer todo el Readme y empezar a ejecutar comandos divertido con posibles ¡ERRORES!, lo bueno es que aprendemos de ellos

#### Lo primero que nos planteamos, es como iran las estructuras de nuestras carpetas por eso te las muestro aquí debajo 


```
PROYECTO SCRAPY/
├── Buscador/
│   ├── Templates/          
│   |      ├── Lista.html
│   ├── admin.py --------Observación de datos         
│   ├── apps.py  ----- usualmente no se toca       
│   |--models.py ---------- aquí se guarda los precios titulos etc  
│   ├── Test.py ----------- Realización de pruebas automaticas           
│   ├── view.py -------Interfaz (Lógica donde el usuario hace búsqueda)        
│           
├── Proyecto Django              
|         |-- __init__.py  
|         |-- asqi.py             
|         |-- settings.py
|         |-- urls.py
|         |-- wsgi.py
|
|--- Scraper_apy
|    |   |-- Spiders/
|    |         |-- __init__py
|    |         |-- Libros.py
|    |--__init__.py
|    |--items.py
|    |--middelwares.py
|    |--pipelines.py
|    |-- settings.py
|   
|--requirements.txt  
```

#### No te apresures. no vayas a crear aun todas estas carpetas, recuerda que a traves de los comandos y pasos que debes de realizar se van a ir creando 

Cada uno de estos archivos tienen un por que ? y como participan en la ejecución del scarpy 

OK AVANZAMOS 🚀 Este proyecto será desde cero y olvidate de la estructura de carpetas por el momento. LETS GOOOO

* Abre tu terminal y empieza a crear tu carpeta principal, como la quieras llamar, no se te olviden los comandos magicos (mkdir), si estas leyendo esto ya sabes hacerlo
* Ve a tu Github y crea tu repositorio 
* Haz un git init desde tu visual studio, recuerda del proyecto que estas creando 
* con el comando git remote, deberia de figurar en la terminal que estas conectado 
* RECOMENDACIÓN : Si deseas trabajar en grupo bloquea tu rama Main y empiecen a trabajar cada uno en su rama 
  
### AHORA AGREGAMOS MÁS MAGIA YUJUUU
* Activa tu entorno virtual, si tu sistema operativo es Window el comando por defecto en la terminal de git bash es (python -m venv venv)
* Activa tus Scripts (source venv/Scripts/activate) 
* Crea tu ignore puedes hacerlo con el comando (touch .gitignore)
* Crea tu archivo .env(Aquí van las variables de entorno todo lo que se encuentra en tu base de datos) ubicate en el proyecto principal

  #### Puedes usar varias librerias para extraer datos, como por ejemplo Request, Selenium,Beatiful Soup o Scrapy 
  * En este caso he decidido usar Scrapy porque es complejo y potente para proyectos profesionales y grandes 

-  Como este proyecto que es relativamente pequeño he decidido trabajar con ![MySQL](https://img.shields.io/badge/MYSQL_WORKBENCH-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
-  Te voy a dejar un enlace para que puedas descargar este Software en tu sistema operativo [Mysl Workbench](https://www.youtube.com/watch?v=unjlhan8wsk)
-  Una vez configuarada tu base datos, damos el siguiente paso 
-  
### Instalando Django
* Django es un framework monolítico, pero con un matiz muy importante: es un "monolito modular"
- Esto significa que en un solo paquete ya tienes casi todo lo que necesitas para que una web funcione:

- Manejo de Base de Datos (ORM).

- Sistema de autenticación de usuarios.

- Panel de administración.

- Enrutamiento de URLs.

- Motor de plantillas (Templates).
Ok AVANZAMOS
* Ubicate en tu terminal y ejecuta (pip install django)
* django - admin startproject Nombre_de_tu_proyecto . 
  - está línea de comando ejecuta instrucciones que serviran para el scrapy no se te olvide el . porque le estas diciendo que cree el proyecto dentro de carpeta principal
  -  
  ### Crea tu archivo .env y coloca tus datos que tiene tu base de datos
  ```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_de_tu_bd',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

# Setting.py 
```from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'buscador',  # <--- Si no pones esto, Django ignorará tu nueva carpeta
]
  
  WSGI_APPLICATION = 'El_nombre_que le_hayas_dado.wsgi.application'

####  os aqui estamos llamando la funcion os 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}`
  ```
### una vez colocado esto en tu archivo setting.py, instala la libreria os 
* pip install dotenv --- con este comando le estamos diciendo a Djago que ya tiene acceso a las variables 
  
* pip install PyMySQL==1.1.2 Django trabaja bien por defecto con esta base de datos ya que estariamos trabajando con MyMySQl Workbench, por defecto se deberia de ejecutar MySqlclient para Django pero si llegas hacerlo te daria error ya que tendria que descargarte el Visual Studio too +CC ya que viene en compilación, para este pryecto ejecute pip install PyMySQL

### Base da datos 
* Ejecutamos python manage.py migrate 
* ¿Que hace este comando?
* Con este coamando Django construye las tablas en tu base de datos Workbench
  ---- Correee, ve en tu base de datos que ya las tablas estan construidas 
 
  * Ejecutamos: python manage.py startapp buscador (Con este comando creamos una carpeta llamada buscador y automaticamente se abren archivos, es donde la app tiene que empezar a funcionar)
   * Vamos a crear un archivo que se llame model.py y que este dentro de buscador 

## Scrapy, tu recolector 
* Scrapy se ira a tu models, ya que alli se encuentran las tablas 
  Para que scrapy haga las cosas de manera correcta tienes que indicarle que va a extraer, por eso es importante saber que pagina vas a extraer, por recomendación y para empezar a ver como funciona 
  puedes visitar está página web, no tiene cache books.toscrape.com

  * Cda vez que se cambie un modelo hay que avisarlo a la base de datos 
  * comandos: python manage.makemigrationbuscador
  * comando: python manage.py migrate
```
  Admin.py  
  from django.contrib import admin
from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio', 'rating', 'disponibilidad') # Columnas que verás en el panel`
  ```

## LLEGÓ LA HORA, A EJECUTAR SCRAPY 

  - pip install scrapy 
  - scrapy startproject scraper_api
## Puente Mágico, para que scrapy guarde tus datos hay que decirle por donde los va a pasar.
## Tiene que gguardarlos en la tabla buscador_libros de MysQl y por ende tenemos que conectar ambos puentes 
```

import os
import sys
import django

# Añadimos la carpeta raíz del proyecto al camino de Python
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))

# Le decimos a Scrapy cuál es el archivo de configuración de Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'NombreDeTuProyecto.settings'

# Arrancamos Django
django.setup()
```
### Explicación del proceso 
1. Scrapy captura el libro
2. Lo pasa por la tuberia pipelines 
3. la tuberia lo entrega Django 
4. Django lo entrega a MsQli Workbench

```
scraper_api/pipelines.py
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
```

### llegó el momento de ejcutar nuestro Robot Scrapy 
- ejecuta scrapy crawl libros 
- python manage.py runserver Para ver tu frontend y tus libros guardados
  

  No te olvides de hacer un git clone y a la misma ves guiarte de el paso a paso de este repo 
