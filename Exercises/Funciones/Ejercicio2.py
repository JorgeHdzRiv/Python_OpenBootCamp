#Instrucciones
#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de 
# una lista pasada por parámetro con filter y 
# realizará una suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce

limite = int(input("Limite de la lista: "))
lista = list(i for i in range(limite))

def impares(x):
    if x % 2 != 0:
        return True
    
    return False

def suma(a,b):
    return a+b

l_impares = list(filter(impares,lista))
print("La lista de impares es: ",l_impares)
res = reduce(suma,l_impares)
print("La suma de los numeros impares es: ",res)

