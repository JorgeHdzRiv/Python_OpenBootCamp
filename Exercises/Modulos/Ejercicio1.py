#Instrucciones
#En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: 
# sumar, restar, multiplicar y dividir.
#Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. 
# Los resultados tenéis que mostrarlos por consola.

import operaciones

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))

print("La suma es: ",operaciones.sumar(a,b))
print("La resta es: ",operaciones.restar(a,b))
print("La multiplicacion es: ",operaciones.multiplicar(a,b))
print("La division es: ",operaciones.dividir(a,b))