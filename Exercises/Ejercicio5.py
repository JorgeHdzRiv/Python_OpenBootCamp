#Instrucciones

#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

#Pasos de determinacion

#1.Si el año es uniformemente divisible por 4, vaya al paso 2. De lo contrario, vaya al paso 5.
#2.Si el año es uniformemente divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 4.
#3.Si el año es uniformemente divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 5.
#4.El año es un año bisiesto (tiene 366 días).
#5.El año no es un año bisiesto (tiene 365 días).
def bisiesto(year):
    if year % 4 == 0 and (year %100 !=0 or year %400 == 0):
        print("Bisiesto")
    else:
        print("No bisiesto")

bisiesto(2022) #Actual

