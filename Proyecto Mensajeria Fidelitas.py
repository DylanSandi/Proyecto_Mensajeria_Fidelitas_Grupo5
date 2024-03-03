#Menú Principal

opcion = 0

print("Bienvenido al sistema de mensajería fidélitas.")
print("\ningrese los credenciales de su usuario")

#Aquí va el código de usuario

while True:

    print("\n------Menú------")

    print("\n1.Registrar una factura electrónica")
    print("\n2.Crear un paquete")
    print("\n3.Salir del sistema")
   
    opcion = int(input("\nIngrese la opción deseada:"))

    if opcion == 1:

        print("\nIngrese los siguientes datos:") 

        #Codigo de registro de factura electrónica

    elif opcion == 2:

        print("\nIngrese los siguientes datos:")
        
        #Código de registro de paquete

    elif opcion == 3:

        opcionSalir = 0

        while True:

            print("\n¿Está seguro(a) que desea salir del sistema?")

            print("\n1.Si")
            print("\n2.No")

            opcionSalir = int(input("\nIngrese la opción deseada:"))
            
            if opcionSalir == 1:

                print("\nGracias por utilizar nuestro sistema")

                break

            elif opcionSalir == 2:

                break

            else:

                print("\nHa digitado una opción inválida, por favor intente de nuevo")
        
        if opcionSalir == 1:

            break
        else:
            print("\nRegresando al menú.....")

    else:

        print("\nHa digitado una opción inválida, por favor intente de nuevo")  