#Instrucciones

#Crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
#Deberéis de definir los métodos para inicializar sus atributos, imprimirlos
#y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    
    def aprobado(self):
        if self.nota > 7:
            print("El alumno:",self.nombre,"aprobo")
        else:
            print("El alumno:",self.nombre,"reprobo")

a1 = Alumno('Juan',8.5)
a1.aprobado()
print("")
a2 = Alumno('Jorge',6.7)
a2.aprobado()