#Arreglos
usuario = {}

#Matrices
factura = []
paquete = []
guias = []

#variable para menú
opcion = 0

#Variables para usuario
correo = ""
nombreComercio = ""
telComercio = 0
nombreDueño = ""
ubiLocal = ""

#Variables para factura
tipoCedula = ""
numCedula = 0
nombreRegistrado = ""
telFactura = 0
correoFactura = ""
provincia = ""
canton = ""
distrito = ""

#Variables para la creación de paquetes
numGuia = 0
nombreDest = ""
telDest = 0
numCedulaDest = 0
pesoPaquete = 0
pago = ""
montoPagar = 0
estado = "Creado"

#Variables para la creación de guías
nombreComercioG = ""
numTelComercioG = 0
nombreDestG = ""
telDestG = 0
requiereCobro = ""
montoCobrarG = 0

#Función para crear usuario
def registrarUsuario(arreglo):

    print("\nPor favor cree su usuario ingresando la siguiente información:")

    for x in range(0,5):

        if x == 0:

            correo = input("\nCorreo electrónico del comercio:")
            arreglo [x] = correo
        
        elif x == 1:

            nombreComercio = input("\nNombre del comercio:")
            arreglo [x] = nombreComercio

        elif x == 2:

            esNumTelValido = False

            while esNumTelValido == False:

                try:

                    telComercio = int(input("\nTeléfono del comercio:"))
                    arreglo [x] = telComercio
                    esNumTelValido = True

                except:

                    print("\n------Error!------")
                    print("\npor favor ingrese un número telefónico válido")
                    esNumTelValido = False

        elif x == 3:

            nombreDueño = input("\nNombre del dueño del comercio:")
            arreglo [x] = nombreDueño

        elif x == 4:

            ubiLocal = input("\nUbicación del local:")
            arreglo [x] = ubiLocal
    
    print("\n------Usuario Creado con éxito------")

#Función para crear datos de factura
def registrarFactura(matriz):

    cedulaValida = False
    telValido = False

    print("\nCreación de datos para una factura electrónica:")

    tipoCedula = input("\nTipo de cédula:")

    while cedulaValida == False:

        try:

            numCedula = int(input("\nNúmero de cédula:"))
            cedulaValida = True

        except:

            print("\n------Error------")
            print("\n Por favor ingrese un número de Cédula válido")

            cedulaValida = False

    nombreRegistrado = input("\nNombre registrado:")

    while telValido == False:

        try:

            telFactura = int(input("\nTeléfono:"))
            telValido = True

        except:

            print("\n------Error------")
            print("\n Por favor ingrese un número de teléfono válido")

            telValido = False

    correoFactura = input("\nCorreo:")
    provincia = input("\nProvincia:")
    canton = input("\nCantón:")
    distrito = input("\nDistrito:")

    datosFactura = [tipoCedula, numCedula, nombreRegistrado, telFactura, correoFactura, provincia, canton, distrito]
    matriz.append(datosFactura)

    print("\n------Datos agregados y creados con éxito------")

def mostrarFactura(matriz):

    for fila in range(len(matriz)):

        for columna in range(len(matriz[fila])):
            
            print(matriz[fila][columna], end = " ")

        print()

def mostrarPaquete(matriz):

    for fila in range(len(matriz)):

        for columna in range(len(matriz[fila])):
            
            print(matriz[fila][columna], end = " ")

        print()


#Función para crear paquetes
def crearPaquete(matrizF, matrizP, guia, matrizG,arreglo):

    print()
    contraEntrega = 0
    opcionFactura = 0
    num = 0
    opcionFValida = False
    paqueteValido = False
    entregaValida = False
    montoValido = False

    for fila in range(len(matrizF)):

        for columna in range(len(matrizF[fila])):

            if columna == 1:

                num +=1
                print(num,".",matrizF[fila][columna],",", end = " ")

            if columna == 2:

                print(matrizF[fila][columna], end = " ")

        print()

    while opcionFValida == False:

        try:

            opcionFactura = int(input("\nIngrese el número del cleinte del que quiere crear el paquete:"))

            if opcionFactura != num or opcionFactura > num or opcionFactura < 1:

                print("\n------Error------")
                print("\npor favor ingrese una opcion válida")
                opcionFValida = False

            else:
                opcionFValida = True

        except:

            print("\n------Error------")
            print("\npor favor ingrese una opcion válida")
            opcionFValida = False

    for fila in range(len(matrizF)):

        for columna in range(len(matrizF[fila])):

            if fila == opcionFactura-1:

                if columna == 1:

                    numCedulaDest = matrizF[fila][columna]

                elif columna == 2:

                    nombreDest = matrizF[fila][columna]

                elif columna == 3:

                    telDest = matrizF[fila][columna]
        print()

    while paqueteValido == False:

        try:

            pesoPaquete = float(input("\nIngrese el peso del paquete (Kilogramos):"))
            paqueteValido = True

        except:

            print("\n------Error------")
            print("\npor favor ingrese un peso válido")
            paqueteValido = False

    print ("\n1.Pago contra entrega")
    print ("\n2.No requiere pago")

    while entregaValida == False:

        try:

            contraEntrega = int(input("\nIngrese la opción:"))

            if contraEntrega > 2:

                print("\n------Error------")
                print("\npor favor ingrese una opción válida")
                entregaValida = False

            else:

                entregaValida = True

        except:

            print("\n------Error------")
            print("\npor favor ingrese una opción válida")
            entregaValida = False

    if contraEntrega == 1:

        pago = "Contra entrega"

        while montoValido == False:
            try:

                montoPagar = int(input("\nIngrese el monto a pagar contra entrega (Colones):"))
                montoValido = True

            except:

                print("\n------Error------")
                print("\npor favor ingrese un monto válido")
                montoValido = False

    elif contraEntrega == 2:

        pago = "No requiere pago"
        montoPagar = 0


    datosPaquete = [guia, nombreDest, telDest, numCedulaDest, pesoPaquete, pago, montoPagar, estado]

    matrizP.append(datosPaquete)

    print ("\n------Paquete creado con éxito------")
    
    #Creación de guías
    print ("\nPor favor pegue la siguiente guía en el paquete antes de que sea recolectado:")
    print ("\nNúmero de guía:", guia)
    print ("\n-----información de comercio------")

    for x in range(0,5):

        if x == 1:
            nombreComercioG = arreglo[x]
            print ("\nNombre:",nombreComercioG)

        if x == 2:
            numTelComercioG = arreglo[x]
            print ("Número de teléfono :",numTelComercioG)

    print ("\n-----información de destinatario------")

    nombreDestG = nombreDest

    print("\nNombre:", nombreDestG)

    telDestG = telDest

    print("Teléfono:", telDestG)

    if pago == "Contra entrega":

        requiereCobro = True
        print ("\nRequiere cobro: si")
        montoCobrarG = montoPagar
        print("monto a cobrar:",montoCobrarG)

    else:

        requiereCobro = False

        print ("\nRequiere cobro: no")
        montoCobrarG = montoPagar

    datosGuia = [guia,nombreComercioG,numTelComercioG,nombreDestG,telDestG,requiereCobro,montoCobrarG]
    matrizG.append(datosGuia)

#Función para el cambio de estado de paquete
def cambiarEstado(matriz):

    esOpValida = False
    esOpValida2 = False
    numC = 0
    opcionCambiarP = 0
    opcionCambiarP2= 0

    for fila in range(len(matriz)):

        for columna in range(len(matriz[fila])):

            if columna == 1:

                numC +=1
                print(numC,".",matriz[fila][columna],",", end = " ")

            if columna == 2:

                print(matriz[fila][columna], end = " ")

        print()

    while esOpValida == False:

        try:

            opcionCambiarP = int(input("\nIngrese el número del paquete al que desea cambiar su estado:"))

            if opcionCambiarP != numC or opcionCambiarP > numC or opcionCambiarP < 1:

                print("\n------Error!------")
                print("\npor favor ingrese una opcion válida")
                esOpValida = False

            else:

                esOpValida = True

        except:

            print("\n------Error!------")
            print("\npor favor ingrese una opcion válida")
            esOpValida = False

        
    for fila in range(len(matriz)):

        for columna in range(len(matriz[fila])):

            if fila == opcionCambiarP-1:

                if columna == 7:

                    print("\nEstado actual del paquete:",matriz[fila][7], end = " ")

                    print("\nlos paquetes pueden cambiar a los siguientes estados:")

                    print("\n1.Creado")
                    print("2.Recolectado")
                    print("3.Entrega Fallida")
                    print("4.Entregado")

                    while esOpValida2 == False:

                        try:

                            opcionCambiarP2 = int(input("\nIngrese el número de estado para modificar:"))

                            if opcionCambiarP2 == 1:

                                matriz[fila][7] = "Creado"

                                print("\nEstado cambiado correctamente a:", matriz[fila][7])
                                esOpValida2 = True

                            elif opcionCambiarP2 == 2:

                                matriz[fila][7] = "Recolectado"

                                print("\nEstado cambiado correctamente a:", matriz[fila][7])
                                esOpValida2 = True

                            elif opcionCambiarP2 == 3:

                                matriz[fila][7] = "Entrega Fallida"

                                print("\nEstado cambiado correctamente a:", matriz[fila][7])
                                esOpValida2 = True

                            elif opcionCambiarP2 == 4:

                                matriz[fila][7] = "Entregado"

                                print("\nEstado cambiado correctamente a:", matriz[fila][7])
                                esOpValida2 = True

                            elif opcionCambiarP2 > 4:

                                print("\n------Error------")
                                print("\npor favor ingrese una opcion válida")
                                esOpValida2 = False

                        except:

                            print("\n------Error!------")
                            print("\npor favor ingrese una opcion válida")
                            esOpValida2 = False

#Función para rastrear paquete
def restrearPaquete(matriz):

    numguiaR = 0
    numguiaR  = int(input("\nIngrese el número de guía del paquete que desea rastrear:"))

    for fila in range(len(matriz)):

        for columna in range(len(matriz[fila])):

            if numguiaR == matriz[fila][columna]:

                print("\nEstado actual del paquete:",matriz[fila][7], end = " ")

#Principal
print("\n------Bienvenido al sistema especializado de control de mensajerías------")

registrarUsuario(usuario)

while opcion != 5 :

    opcionValida = False

    print("\n------Menú------")

    print("\n1.Registrar datos de factura")
    print("\n2.Crear paquete")
    print("\n3.Cambiar estado de paquete")
    print("\n4.Rastrear un paquete")
    print("\n5.Salir del sistema")

    while opcionValida == False:

        try:

            opcion = int(input("\nIngrese la opción que desea realizar:"))

            if opcion > 5:

                print("\n------Error------")
                print("\n Por favor ingrese una opción válida")
                opcionValida = False 

            else:
                opcionValida = True

        except:

            print("\n------Error------")
            print("\n Por favor ingrese una opción válida")
            opcionValida = False

    if opcion == 1:

        registrarFactura (factura)
    
    elif opcion == 2:

        if not factura:

            print("\n------ERROR------")
            print("\nAntes de crear un paquete, debe primero registar los datos para una factura electrónica")

        else:

            numGuia +=1

            crearPaquete(factura,paquete,numGuia,guias,usuario)
            mostrarPaquete(paquete)

    elif opcion ==3:

        if not paquete:

            print("\n------ERROR------")
            print("\nNo ha creado ningún paquete")

        else:

            cambiarEstado(paquete)
    
    elif opcion == 4:

        if not paquete:

            print("\n------ERROR------")
            print("\nNo ha creado ningún paquete")

        else:

            restrearPaquete(paquete)
    else:

        print("\nGracias por utilizar el sistema")