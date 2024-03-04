
opcion = 0
opcionValida = False
usuarioValido = False
facturaValida = False
salirValido = False
paqueteValido = False


print("\nBienvenido al sistema de mensajería fidélitas.")

#Menú Principal

while True:

    opcionValida = False
    opcion = 0

    print("\n------Menú------")

    print("\n1.Registrar un usuario")
    print("\n2.Registrar factura electrónica")
    print("\n3.Crear paquete")
    print("\n4.Salir del sistema")

    #Validar opción
    while opcionValida == False:

        try:

            opcion = int(input("\nIngrese la opción deseada:"))

            if opcion > 4:

                print("\nDato incorrecto, por favor ingrese una opción válida")
                opcionValida = False 

            else:

                opcionValida = True

        except:

            print("\nDato incorrecto, por favor ingrese una opción válida")
            opcionValida = False

    #Formulario para usuario           
    if opcion == 1:

        usuarioValido = False

        #validar usuario
        while usuarioValido == False:

            try:

                print("\nPor favor registre su cuenta de usuario")

                print("")

                correo=str(input("\nIngrese su correo electrónico:"))
                comercio=str(input("\nIngrese el nombre del comercio:"))
                telefono=int(input("\nIngrese el número de teléfono del comercio:"))
                nombre=str(input("\nIngrese el nombre del usuario:"))
                ubicacion=str(input("\nIngrese la dirección de comercio:"))

                print("\n------Usuario registrado------")

                print("\nSu correo es:",correo)
                print("\nEl nombre del comercio es:",comercio)
                print("\nEl teléfono del comercio es:",telefono)
                print("\nEl nombre de usuario es:",nombre)
                print("\nLa dirección del comercio es:",ubicacion)

                usuarioValido = True

            except:

                print("\nDato incorrecto, por favor ingrese un dato válido")
                usuarioValido = False
         
    #Formulario para factura electrónica
    elif opcion == 2:

        facturaValida = False

        #validar Factura
        while facturaValida == False:

            try:

                print("\nPor favor complete los siguientes datos")
                
                tipoced = input("\nEspecifíque si su cédula es Física o Jurídica: ")
                cedula = input("\nIngrese el número de cédula: " )
                empresa = input("\nIngrese el nombre registrado: ")
                telefo = int(input("\nIngrese el número de teléfono: "))
                correoemp = input("\nIngrese el correo electrónico: ")
                provincia = input("\nIngrese la Provincia: ")
                canton = input("\nIngrese el Cantón: ")
                distrito = input("\nIngrese el Distrito: ")

                print("\n------Factura creada con éxito------")

                print("\nTipo de cédula:",tipoced)
                print("\nNúmero de cédula:",cedula)
                print("\nNombre registrado de comercio es:",empresa)
                print("\nTeléfono registrado:",telefo)
                print("\nCorreo empresarial es:",empresa)
                print("\nProvincia:",provincia)
                print("\nCantón:",canton)
                print("\nDistrito: ",distrito)

                facturaValida = True

            except:

                print("\nDato incorrecto, por favor ingrese un dato válido")
                facturaValida = False

    #Formulario para paquete           
    elif opcion == 3:

        paqueteValido = False

        #validar paquete 
        while paqueteValido == False:

            try:

                print("\nIngrese los siguientes datos para crear el paquete:")
                destinatario = input("\nNombre del destinatario: ")
                telefono_destinatario = int(input("\nTeléfono del destinatario: "))
                cedula_destinatario = input("\nNúmero de cédula del destinatario: ")
                peso_paquete = float(input("\nPeso del paquete (Kilogramos): "))
                cobro_contra_entrega = input("\nMonto en colones a cobrar contra entrega: ")

                print("\n------Paquete creado con éxito------")
                print("\nNombre del destinatario:", destinatario)
                print("\nTeléfono del destinatario:", telefono_destinatario)
                print("\nNúmero de cédula del destinatario:", cedula_destinatario)
                print("\nPeso del paquete (Kilogramos):", peso_paquete)
                print("\nMonto a cobrar contra entrega:", cobro_contra_entrega)

                paqueteValido = True

            except:

                print("\nDato incorrecto, por favor ingrese un dato válido")

                paqueteValido = False

    elif opcion == 4:

        opcionSalir = 0

        while True:

            salirValido = False

            print("\n¿Está seguro(a) que desea salir del sistema?")

            print("\n1.Si")
            print("\n2.No")

            while salirValido == False:

                try:

                    opcionSalir = int(input("\nIngrese la opción deseada:"))
                    salirValido = True

                except:

                    print("\nDato incorrecto, por favor ingrese un dato válido")
                    salirValido = False

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