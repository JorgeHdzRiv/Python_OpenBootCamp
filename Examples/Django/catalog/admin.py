from django.contrib import admin

# Register your models here.
from . models import Autor,Genero,BookInstance,Libro

admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(BookInstance)
admin.site.register(Libro)