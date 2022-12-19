from django.shortcuts import render
from . models import BookInstance,Autor,Genero,Libro

# Create your views here.
def index(request):
    num_libros = Libro.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_autors = Autor.objects.all().count()
    
    disponibles = BookInstance.objects.filter(status__exact='a').count()
    
    return render(
        request,'index.html',
        context={'num_libros':num_libros,'num_instances':num_instances,'num_autors':num_autors,'disponibles':disponibles}
    )
    