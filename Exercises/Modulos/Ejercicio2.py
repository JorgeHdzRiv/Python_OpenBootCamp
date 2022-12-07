#Instrucciones
#En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. 
# Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

#En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario,
# haréis una operación para calcular el tiempo que queda de trabajo.

import time as t

hora_act = t.localtime()
print(hora_act.tm_hour,":",hora_act.tm_min)

if (hora_act.tm_hour) > 19:
    print("Hora de ir a casa son mas de las 7")
else:
    min_res = 60-hora_act.tm_min
    h_res = 19-hora_act.tm_hour-1
    print("Faltan",h_res,"horas y ",min_res,"minutos para la salida")


