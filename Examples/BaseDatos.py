import getpass
import sqlite3

#Funcion verificar credenciales

def main():
    crear_usuario(4,'Jesus','15')
    
def main2():
    username = input("Nombre del usuario: ")
    password = getpass.getpass("Pass: ")
    
    if verifica(username,password):
        print("Login correcto")
    else:
        print("Login incorrecto")
    
def verifica(username,password):
    conn = sqlite3.connect('./Examples/base.db')
    cursor = conn.cursor()
    
    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}' "
    
    rows = cursor.execute(query)
    #Fetchone devuelve un elemento
    data = rows.fetchone()
    print("Data es: ",type(data))
    
    #Cerrar conexiones
    cursor.close()
    conn.close()
    
    if data == None:
        return False
    
    return True

def crear_usuario(id,username,password):
    conn = sqlite3.connect('./Examples/base.db')
    cursor = conn.cursor()
    
    query = f"INSERT INTO users(id,username,password) VALUES({id},'{username}','{password}')"
    
    rows = cursor.execute(query)
    print(type(rows))
    
    #Mandar la actualizacion con commit para insertar,actualizar o borrar
    conn.commit()
    
    #Cerrar conexiones
    cursor.close()
    conn.close()
    
    
main()
"""
Ejemplo basico sin funciones

#Abrir base de datos
conn = sqlite3.connect('./Examples/base.db')

#Cursores enviar datos a la base
cursor = conn.cursor()

#Consultas
rows = cursor.execute('SELECT * FROM users WHERE id=1')
for row in rows:
    print(row)

#Cerrar cursor
cursor.close()

#Cerrar conexion
conn.close()

"""  

