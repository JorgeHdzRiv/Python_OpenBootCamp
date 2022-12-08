#Instrucciones
# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. 
# Para ello, tendréis que acceder dos veces al archivo creado.

f = open('archivo.txt', 'w+')
f.write("Linea nueva")
f.write("Linea de prueba")
f.close()

f = open('archivo.txt','r')
for linea in f:
    print(linea)
f.close()