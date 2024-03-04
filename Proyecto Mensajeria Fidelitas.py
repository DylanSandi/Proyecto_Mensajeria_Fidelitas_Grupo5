#Menú Principal

opcion = 0

print("Bienvenido al sistema de mensajería fidélitas.")
print("\ningrese los credenciales de su usuario")

#Aquí va el código de usuario

while True:

    print("\n------Menú------")

    print("\n1.Registrar un usuario")
    print("\n2.Registrar factura electrónica")
    print("\n3.Salir del sistema")
   
    opcion = int(input("\nIngrese la opción deseada:"))

    if opcion == 1:

         
         
         print("Por favor registre su cuenta de usuario")
         print("")
         correo=str(input("Ingrese su correo electrónico:"))
         comercio=str(input("Ingrese el nombre del comercio:"))
         telefono=int(input("Ingrese el número de teléfono del comercio:"))
         nombre=str(input("Ingrese el nombre del usuario:"))
         ubicacion=str(input("Ingrese la dirección de comercio:"))
         print("")
         print("Su correo es:",correo)
         print("El nombre del comercio es:",comercio)
         print("El teléfono del comercio es:",telefono)
         print("El nombre de usuario es:",nombre)
         print("La dirección del comercio es:",ubicacion)


        #Codigo de registro de factura electrónica

    elif opcion == 2:

        print("\nIngrese los siguientes datos:")
        
        print("Por favor complete los siguientes datos")
        tipoced= str(input("Especifíque si Física o Jurídica: "))
        cedula=int(input("Ingrese el número de cédula: " ))
        empresa=str(input("Ingrese el nombre registrado: "))
        telefo=int(input("Ingrese el número de teléfono: "))
        correoemp=str(input("Ingrese el correo electrónico: "))
        provincia=str(input("Ingrese la Provincia: "))
        canton=str(input("Ingrese el Cantón: "))
        distrito=str(input("Ingrese el Distrito: "))
        print("")
        print("Su tipo de cédula es: ",tipoced)
        print("Su número de cédula es:",cedula)
        print("El nombre registrado de comercio es: ",empresa)
        print("El teléfono registrado es: ",telefo)
        print("El correo empresarial es: ",empresa)
        print("La Provincia es: ",provincia)
        print("El Cantón  es: ",canton)
        print("El Distrito es: ",distrito)

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
# Función para la creación de paquetes
def crear_paquete():
    print("\nIngrese los siguientes datos para crear el paquete:")
    destinatario = input("Nombre del destinatario: ")
    telefono_destinatario = input("Teléfono del destinatario: ")
    cedula_destinatario = input("Número de cédula del destinatario: ")
    peso_paquete = float(input("Peso del paquete (Kilogramos): "))
    cobro_contra_entrega = input("Monto en colones a cobrar contra entrega: ")
    print("\nPaquete creado con éxito:")
    print("Nombre del destinatario:", destinatario)
    print("Teléfono del destinatario:", telefono_destinatario)
    print("Número de cédula del destinatario:", cedula_destinatario)
    print("Peso del paquete (Kilogramos):", peso_paquete)
    print("Monto a cobrar contra entrega:", cobro_contra_entrega)

opcion = 0

print("Bienvenido al sistema de mensajería fidélitas.")
print("\ningrese los credenciales de su usuario")

# Aquí va el código de usuario

while True:
    print("\n------Menú------")
    print("\n1.Registrar un usuario")
    print("\n2.Registrar factura electrónica")
    print("\n3.Salir del sistema")

    opcion = int(input("\nIngrese la opción deseada:"))

    if opcion == 1:
        # Código para registrar un usuario
        print("Por favor registre su cuenta de usuario")
        # Aquí iría el código para registrar un usuario

    elif opcion == 2:
        # Código para registrar una factura electrónica
        print("\nIngrese los siguientes datos:")
        # Aquí iría el código para registrar una factura electrónica

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

    # Llamar a la función para crear paquete si la opción es válida (opción 4)
    if opcion == 4:
        crear_paquete()