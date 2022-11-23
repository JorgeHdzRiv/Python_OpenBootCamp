#Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase 
# Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("Introducir peso en kg: "))
estatura = float(input("Introducir estatura en metros: "))

imc = peso / estatura ** 2

print("Tu indice de masa corporal es:",round(imc,2))

