#Instrucciones
#En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener 
# una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.font import Font

ventana = tk.Tk()

ventana.title("Ejercicio2")

label = tk.Label(ventana,text="Lenguaje favorito")
label.pack()
listbox = tk.Listbox(selectmode=tk.EXTENDED,font=Font(family="Sans Serif",size=12))
items = (
    "Python","C","Java","C++"
)
listbox.insert(0,*items)
listbox.pack()

#Funcion del boton
def obtener_seleccion():
    indices = listbox.curselection()
    messagebox.showinfo(
        title="Items seleccionados",
        message=" ,".join(listbox.get(i) for i in indices)
    )

btn_seleccion = ttk.Button(
    text="Obtener seleccion",command=obtener_seleccion
)
btn_seleccion.pack()

ventana.mainloop()