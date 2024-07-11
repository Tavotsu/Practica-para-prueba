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
          return True
     else:
     #Si no devuelve False
          return False
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
               for fila in escritor_csv:
                    fcod=int(fila['Codigo'])
                    fnom=fila['Nombre']
                    fpre=int(fila['Precio'])
                    fcan=int(fila['Cantidad'])
                    print
     except:
          print("\nNo se ha podido leer el archivo de inventario.");
#Funcion para mostrar el menu al usuario
def menu():
     print("==========================\nMenu\n==========================\n1.- Agregar producto\n2.- Modificar producto\n3.- Quitar producto\n4.- Guardar inventario en excel\n5.- Salir del programa\n");
#Funcion para agregar productos al inventario
def agregar_productos():
     print('============\nAgregar productos\n============');
     while True:
          try:
               codigoprod=int(input("Ingrese el codigo del producto: "));
          except:
               print("\nIngrese una opcion valida.");
          if codigoprod==int:
               listaproducto.append(codigoprod)
               break
          else:
               True
     nombreprod=input('Ingrese el nombre del producto: ');
     listaproducto.append(nombreprod)
     while True:
          try:
               precioprod=int(input("Ingrese el precio del producto: "));
          except:
               print("\nIngrese una opcion valida.");
          if precioprod==int:
               listaproducto.append(precioprod)
               break
          else:
               True
     while True:
          try:
               cantidadprod=int(input("Ingrese las unidades disponibles del producto: "));
          except:
               print("\nIngrese una opcion valida.");
          if cantidadprod==int:
               listaproducto.append(cantidadprod)
               break
          else:
               True
     print("Datos agregados correctamente.\n")
     return listaproducto
#
def modificar_producto():
     for x in listaproducto:
          print(listaproducto[x])
     print("Elija una opcion para editar")
#Funcion para animacion de ...
def animacion_salida():
     print("Saliendo del programa",end='');
     for x in range(3):
          print('.',end='')
          time.sleep(0.2)