import tkinter 
from tkinter import ttk #Estilo para las apps

#Ventana para poner los componentes widgets o controles

ventana = tkinter.Tk()

#Geometrias para ventanas

#Crear componentes
label_saludo = tkinter.Label(ventana,text="Hola!",bg="yellow",fg='blue')
label_adios = tkinter.Label(ventana,text='Adios',bg='red',fg='white')


#Geometria pack
#label_saludo.pack(ipadx=50,ipady=50,expand=True,side='left')
#label_adios.pack(ipadx=50,ipady=100,fill='both',expand=True)

#Geometria grid
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=3)

# Usuario
usuario_label = ttk.Label(ventana,text='Usuario:')
usuario_label.grid(column=0,row=0,sticky=tkinter.W,padx=5,pady=5) #La W es una coordenada de las 4 coordenadas

usuario_entrada = ttk.Entry(ventana)
usuario_entrada.grid(column=1,row=0,sticky=tkinter.E,padx=5,pady=5)

# Password
password_label = ttk.Label(ventana,text='Password:')
password_label.grid(column=0,row=1,sticky=tkinter.W,padx=5,pady=5) #La W es una coordenada de las 4 coordenadas

password_entrada = ttk.Entry(ventana,show='*')
password_entrada.grid(column=1,row=1,sticky=tkinter.E,padx=5,pady=5)

#Boton para mandar datos
login_boton = ttk.Button(ventana,text='Ingresar')
login_boton.grid(column=1,row=3,sticky=tkinter.E,padx=5,pady=5)

 #Ciclo infinito para que no se cierre la ventana
ventana.mainloop()

