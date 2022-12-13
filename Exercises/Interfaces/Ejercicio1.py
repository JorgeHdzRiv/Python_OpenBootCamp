#Instrucciones

#En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción 
# que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

#Al principio no tiene que haber una opción seleccionada

import tkinter
import os


ventana = tkinter.Tk()


valor = tkinter.StringVar(ventana,"0")



#Creacion componentes
label = tkinter.Label(ventana,text="Selecciona una opcion: ")
label.pack()
r_button = tkinter.Radiobutton(ventana,text="Opcion1",variable=valor,value="1")
r_button.pack()
r_button2 = tkinter.Radiobutton(ventana,text="Opcion2",variable=valor,value="2")
r_button2.pack()
r_button3 = tkinter.Radiobutton(ventana,text="Opcion3",variable=valor,value="3")
r_button3.pack()

def reinicio():
    ventana.destroy()
    os.startfile('Exercises\Interfaces\Ejercicio1.py')
    
btn_reinicio = tkinter.Button(ventana,text="Reiniciar",command=reinicio)
btn_reinicio.pack()

ventana.mainloop()

