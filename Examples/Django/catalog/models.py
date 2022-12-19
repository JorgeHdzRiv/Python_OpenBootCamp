import uuid
from django.urls import reverse
from django.db import models

# Create your models here.
class Genero(models.Model):
    name = models.CharField(max_length=64,help_text='Nombre del genero')
    
    #Devuelve la variable en formato string
    def __str__(self):
        return self.name

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey('Autor',on_delete=models.SET_NULL,null=True)
    resumen = models.TextField(max_length=200,help_text='Sinopsis del libro')
    isbn = models.CharField('ISBN',max_length=13,help_text='El ISBN es de 13 caracteres')
    genero = models.ManyToManyField(Genero)
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('book-detail',args=[str(self.id)])

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='ID unico para este libro')
    libro = models.ForeignKey('Libro',on_delete=models.SET_NULL,null=True)
    imprenta = models.CharField(max_length=200)
    due_back = models.DateField(null=True,blank=True)
    
    LOAN_STATUS = (
        ('m','Mantenimiento'),
        ('o','On loan'),
        ('a','Available'),
        ('r','Reserved')
    )
    
    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m',help_text='Disponibilidad')
    
    class Meta:
        ordering = ['due_back']
    
    def __str__(self):
        return '%s (%s)' % (self.id,self.libro.titulo)

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True,blank=True)
    fecha_muerte = models.DateField('Died',null=True,blank=True)
    
    def get_absolute_url(self):
        return reverse("autor-detail", args=[str(self.id)])
    
    def __str__(self):
        return '%s (%s)' % (self.apellido,self.nombre)
    
    
    
    