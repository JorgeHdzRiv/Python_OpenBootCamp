#Instrucciones

# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: 
# la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido 
# que también será de tipo texto.

#Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

#Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3
def main():
    crear_tabla()
    insertar_datos()
    buscar_alumno()

#Creamos la base de datos con cmd sqlite3 base.db

def crear_tabla():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS alumnos(
        id INT PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL)''')
    
    cursor.close()
    conn.close()

def insertar_datos():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    id = 1
    
    iteraciones = int(input("Numero de datos a insertar: "))
    
    for i in range(iteraciones):
        nombre = input("Nombre del alumno: ").capitalize()
        apellido = input("Apellido del alumno: ").capitalize()
        cursor.execute(f"INSERT INTO alumnos(id,nombre,apellido) VALUES ({id},'{nombre}','{apellido}')")
        id += 1
        conn.commit()
        
    cursor.close()
    conn.close()

def buscar_alumno():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    nombre = input("Nombre del alumno a buscar: ").capitalize()
    rows = cursor.execute(f"SELECT * FROM alumnos WHERE nombre='{nombre}'")
    data = rows.fetchone()
    
    cursor.close()
    conn.close()
    
    if data == None:
        print("No hay datos del alumno")
    else:
        print("Los datos del alumno son:")
        print("ID: ",data[0])
        print("Nombre: ",data[1])
        print("Apellido: ",data[2])

main()