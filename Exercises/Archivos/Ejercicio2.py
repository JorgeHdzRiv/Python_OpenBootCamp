#Instrucciones
#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
import pickle

class Vehiculo:
    
    def __init__(self,tipo,color):
        self.tipo = tipo
        self.color = color
    
    def datos(self):
        print("El vehiculo es tipo:",self.tipo)
        print("El color es:",self.color)

c1 = Vehiculo('sedan','rojo')

#Creamos el objeto dentro del archivo
f=open('datos.bin','wb')
pickle.dump(c1,f)
f.close()

#Acceder al archivo
f=open('datos.bin','rb')
carro = pickle.load(f)
f.close()

#Instancia y metodo de la clase
print(type(carro))
carro.datos()