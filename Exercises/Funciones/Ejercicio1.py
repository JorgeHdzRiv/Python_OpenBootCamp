#Instrucciones
# Crea un script que le pida al usuario una lista de países (separados por comas). 
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

cantidad = int(input("Cantidad de paises a ingresar: "))
paises = []

for i in range(cantidad):
    pais = input("Pais a ingresar: ").capitalize()
    paises.append(pais)
 

print("Los paises ingresados y unicos son:",sorted(set(paises)))
    