import time, datetime, csv
#Credenciales de login
logincredentials={"Gustavo": "G234",
                  "Javier":"12345",
                  "admin":"admin",
                  "a":"a"}
#Funcion para Login  
def login(inputusuario, inputcontraseña):
     #Si estan correctas las credenciales devuelve True
     if inputusuario in logincredentials and logincredentials[inputusuario]==inputcontraseña:
          return True
     else:
     #Si no devuelve False
          return False
#Funcion para mostrar el menu al usuario
def menu():
     print("==========================\nMenu\n==========================\n1.- Agregar producto\n2.- Modificar producto\n3.- Quitar producto\n4.- Guardar inventario en excel\n5.- Salir del programa\n")
#Funcion para animacion de salida
def animacionsalida():
    print("Saliendo del programa",end='')
    for i in range(3)
        print('.',end='')
        time.sleep(0.2)
   