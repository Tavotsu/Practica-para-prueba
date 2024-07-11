import time, datetime, csv
#Credenciales de login
logincredentials={"Gustavo": "G234",
                  "Javier":"12345",
                  "admin":"admin",
                  "a":"a"}
#Titulo csv
titulo=['Codigo','Nombre','Precio','Cantidad'];
#Lista para despues agregarla al inventario
listaproducto=[]
#Funcion para Login  
def login(inputusuario, inputcontraseña):
     #Si estan correctas las credenciales devuelve True
     if inputusuario in logincredentials and logincredentials[inputusuario]==inputcontraseña:
          animacion_login()
          return True
     else:
     #Si no devuelve False
          print("\nUsuario o contraseña incorrectos, intente nuevamente\n")
          return False
#Funcion para animacion ... de entrada
def animacion_login():
     print("Iniciando sesion",end='');
     for x in range(3):
          print('.',end='',flush=True)
          time.sleep(0.2)
#Funcion para precargar el archivo csv
def crear_inventario():
     try:
          with open('inventario.csv',"w",newline='',encoding='UTF-8') as archivo_csv:
               escritor_csv=csv.writer(archivo_csv)
               escritor_csv.writerow(titulo)
     except:
          print("\nNo se ha podido crear el archivo de inventario, por favor reinicie el programa.");
#Cargar inventario creado previamente
def leer_inventario():
     try:
          with open('inventario.csv',"r",) as archivo_csv:
               escritor_csv=csv.DictReader(archivo_csv)
               print('   Codigo   |   Nombre   |   Precio   |   Cantidad   ')
               for fila in escritor_csv:
                    fcod=int(fila['Codigo'])
                    fnom=fila['Nombre']
                    fpre=int(fila['Precio'])
                    fcan=int(fila['Cantidad'])
                    print(f"{fcod}  |  {fnom}  |  {fpre}  |  {fcan}")
     except:
          print("\nNo se ha podido leer el archivo de inventario.");
#Funcion para mostrar el menu al usuario
def menu():
     print("\n==========================\nMenu\n==========================\n1.- Agregar producto\n2.- Modificar producto\n3.- Quitar producto\n4.- Guardar inventario en excel\n5.- Salir del programa\n");
#Funcion para agregar productos al inventario
def agregar_productos():
     print('============\nAgregar productos\n============');
     while True:
        try:
               codigoprod = int(input("Ingrese el codigo del producto: "))
               listaproducto.append(codigoprod)
               break 
        except ValueError:  
               print("\nIngrese una opcion valida.")
     nombreprod=input('Ingrese el nombre del producto: ');
     listaproducto.append(nombreprod)
     while True:
        try:
               precioprod = int(input("Ingrese el codigo del producto: "))
               listaproducto.append(precioprod)
               break 
        except ValueError:  
               print("\nIngrese una opcion valida.")
     while True:
        try:
               cantprod = int(input("Ingrese el codigo del producto: "))
               listaproducto.append(cantprod)
               break 
        except ValueError:  
               print("\nIngrese una opcion valida.")
     print("Datos agregados correctamente.\n")
     return listaproducto
#Funcion para modificar productos
def modificar_producto():
     for x in listaproducto:
          print(listaproducto[x])
     print("Elija una opcion para editar")
#Funcion para animacion de ...
def animacion_salida():
     print("Saliendo del programa",end='');
     for x in range(3):
          print('.',end='',flush=True)
          time.sleep(0.2)