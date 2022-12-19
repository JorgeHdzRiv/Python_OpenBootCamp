from django.contrib import admin

# Register your models here.
from .models import Pelicula, Director, Genero

admin.site.register(Pelicula)
admin.site.register(Director)
admin.site.register(Genero)
