import time, datetime, csv
#Credenciales de login
logincredentials={"Gustavo": "G234",
                  "Javier":"12345",
                  "admin":"admin",
                  "a":"a"}
#
titulo=['Codigo','Nombre','Precio','Cantidad']
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

def animacion_salida():
     print("Saliendo del programa",end='')
     for x in range(3):
          print('.',end='')
          time.sleep(0.2)

def cargar_archivo_csv():
     try:
          with open('inventario.csv',"w",newline='',encoding='UTF-8') as archivo_csv:
               escritor_csv=csv.writer(archivo_csv)
               escritor_csv.writerow(titulo)
     except:
          print("\nNo se ha podido crear el archivo de inventario, por favor reinicie el programa.")