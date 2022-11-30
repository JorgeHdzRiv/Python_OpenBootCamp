#Instrucciones
"""
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

Color
Ruedas
Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

Velocidad
Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
"""

class Vehiculo:
    
    def __init__(self,color,ruedas,puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
    def info(self):
        print("El color es: ",self.color)
        print("Tiene",self.ruedas,"ruedas")
        print("Tiene",self.puertas,"puertas")

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas,velocidad,cilindros):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindros = cilindros
        
    def info_coche(self):
        print("El coche va a: ",self.velocidad,"km\h")
        print("El coche tiene: ",self.cilindros,"cilindros")

sedan = Coche('rojo',4,4,196.7,8)
print("Informacion general \n")
sedan.info()
print("\nInformacion del coche \n")
sedan.info_coche()
        
        
    
        