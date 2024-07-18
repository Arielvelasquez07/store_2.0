from django.contrib import admin
from .models import Categoria,Pelicula

#registro de modelos en el panel de adminstracion
admin.site.register(Categoria)
admin.site.register(Pelicula)