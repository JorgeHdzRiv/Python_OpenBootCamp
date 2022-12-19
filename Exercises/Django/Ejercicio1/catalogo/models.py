from django.db import models
from django.urls import reverse


# Create your models here.
class Genero(models.Model):
    name = models.CharField(max_length=64, help_text='Genero de la pelicula')

    def __str__(self):
        return self.name


class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    resumen = models.TextField(max_length=200, help_text='Sinopsis de la pelicula')
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])


class Director(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_muerte = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("director-detail", args=[str(self.id)])

    def __str__(self):
        return '%s (%s)' % (self.apellido, self.nombre)
