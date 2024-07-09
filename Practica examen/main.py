#Funciones
import funcionesmain as func
#Opciones para los menus
opcion_main_menu=0
opcion_add=0
opcion_modify=0
opcion_remove=0
#Proceso de login
while func.login==False:
    print("Bienvenid@!")
    inputusuario=input("Ingrese su usuario: ")
    inputcontraseña=input("Ingrese su contraseña: ")
    func.login(inputusuario,inputcontraseña)
#Empieza el programa
while opcion_main_menu!=5:
    func.menu()
    try:
        opcion_main_menu=int(input(""))
    except:
        print("\nIngrese una opcion valida.")
    else:
        if opcion_main_menu==1:
            print()
        elif opcion_main_menu==2:
            print()
        elif opcion_main_menu==3:
            print()
        elif opcion_main_menu==4:
            print()
        elif opcion_main_menu==5:
            print()
        else:
            print("\nIngrese una opcion valida.")