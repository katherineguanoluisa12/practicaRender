from django.contrib import admin
# importamos la clase genero y director
from.models import Genero,Director,Pais,Pelicula

# le voy a pasar parametros 
admin.site.register(Genero)
admin.site.register(Director)
admin.site.register(Pais)
admin.site.register(Pelicula)