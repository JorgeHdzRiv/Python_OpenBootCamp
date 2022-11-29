#Instrucciones
#Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

nums = [n for n in range(1,100+1)]


for num in reversed(nums):
    print(num)