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

            if opcionFactura > num or opcionFactura < 1:

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

            if opcionCambiarP > numC or opcionCambiarP < 1:

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

#Función para mostrar la cantidad de envíos totales
def cantEnvios(mPaquete):

    cantEnvios = len(mPaquete)

    print("\nCantidad de envíos registrados:",cantEnvios)

#Función para mostrar la lista de paquetes enviados
def listaPaquetesEnviados(mPaquete):

    print("\nLista de paquetes enviados:")
    print()
    numPaquete = 0

    for fila in range(len(mPaquete)):

            for columna in range(len(mPaquete[fila])):

                if mPaquete [fila][columna] == "Entregado":

                    numPaquete += 1
                    print("#",numPaquete)

                    print(mPaquete[fila][3], end = " ")
                    print(mPaquete[fila][1], end = " ")

            print()

#Función para mostrar el monto de cobro total
def montoCobro(mPaquete):  

    cobroTotal = 0

    for fila in range(len(mPaquete)):

        cobroTotal += mPaquete[fila][6]

    print("Monto total a cobrar:₡",cobroTotal)

#Función para mostrar la cantidad de paquetes por número de teléfono
def cantPaquetesTel(mPaquete):

    telSValido = False
    numTelS = 0
    coincide = 0

    while telSValido == False:

        try:
            numTelS = int(input("\nIngrese el número de teléfono que desea buscar:"))

            for fila in range(len(mPaquete)):

                if numTelS == mPaquete[fila][2]:

                    coincide+=1
            
            if coincide >=1:

                print("\nEl número",numTelS,"Tiene un total de",coincide,"Paquetes registrados")
                telSValido = True

            else:

                print("\nNo se encontró ningún número de teléfono registrado, por favor intente nuevamente")
                telSValido == False
            
        except:

            print("\n!!Error\n Por favor ingrese un número de teléfono válido")
            telSValido =False

#Función para mostrar la cantidad de paquetes por número de cédula
def cantPaquetesCed(mPaquete):

    cedSValido = False
    cedS = 0
    coincideCed = 0

    while cedSValido == False:

        try:

            cedS = int(input("\nIngrese el número de cédula que desea buscar:"))

            for fila in range(len(mPaquete)):

                if cedS == mPaquete[fila][3]:

                    coincideCed+=1
            
            if coincideCed >=1:

                print("\nEl número de cédula",cedS,"Tiene un total de",coincideCed,"Paquetes registrados")
                cedSValido = True

            else:

                print("\nNo se encontró ningún número de cédula registrado, por favor intente nuevamente")
                cedSValido== False
            
        except:

            print("\n!!Error\n Por favor ingrese un número de cédula válido")
            cedSValido =False

#Función con menú del módulo de estadística
def moduloEstadistica(matrizP):

    print("\n------Módulo de estadísitica------")
    opcionMod = 0

    while opcionMod !=6:

        opcionMod = 0
        opcionModValida = False

        print("\n1.Cantidad de envíos")
        print("\n2.Lista de paquetes enviados")
        print("\n3.Monto total de cobro")
        print("\n4.Buscar cantidad de paquetes por número de teléfono")
        print("\n5.Buscar cantidad de paquetes por número de cédula")
        print("\n6.Salir del módulo de estadística")

        while opcionModValida == False:

            try:
                opcionMod = int(input("\nIngrese el número de estadística que desea observar:"))

                if opcionMod >6:

                    opcionModValida = False
                    print("\nError!!\nIngrese un número de estadística válido")

                else:

                    opcionModValida = True 

            except:

                opcionModValida = False
                print("\nError!!\nIngrese un número de estadística válido")
        
        if opcionMod == 1:

            cantEnvios(matrizP)

        elif opcionMod == 2:

            listaPaquetesEnviados(matrizP)
        
        elif opcionMod == 3:

            montoCobro(matrizP)

        elif opcionMod == 4:

            cantPaquetesTel(matrizP)

        elif opcionMod == 5:

            cantPaquetesCed(matrizP)
        
        else:

            print("\nSaliendo.....\nHa salido satisfactoriamente del módulo de estadística")

#Guardar datos de usuario en archivo
def archivoUsuario(arregloU):

    file = open("Usuario.txt", "a")

    for pos in range(len(arregloU)):

        if pos == 0:

            file.write("\nCorreo electrónico:")
            file.write(arregloU[pos])

        elif pos == 1:

            file.write("\nNombre del comercio:")
            file.write(arregloU[pos])

        elif pos == 2:

            file.write("\nTeléfono de comercio:")
            file.write(str(arregloU[pos]))

        elif pos == 3:

            file.write("\nNombre de dueño:")
            file.write(arregloU[pos])

        elif pos == 4:

            file.write("\nUbicación de local:")
            file.write(arregloU[pos])

    file.write("\n\n")
    file.close()

#Guardar datos de factura en archivo
def archivoFactura(matrizFactura,filas):

    file = open("Factura.txt", "a")

    for fila in range(len(matrizFactura)):

        for columna in range(len(matrizFactura[fila])):
            
            if fila == filas:
                
                if columna == 0:

                    file.write("\nTipo de cédula:")
                    file.write(matrizFactura[fila][columna])

                elif columna == 1:

                    file.write("\nNúmero de cédula:")
                    file.write(str(matrizFactura[fila][columna]))

                elif columna == 2:

                    file.write("\nNombre registrado:")
                    file.write(matrizFactura[fila][columna])

                elif columna == 3:

                    file.write("\nTeléfono:")
                    file.write(str(matrizFactura[fila][columna]))

                elif columna == 4:

                    file.write("\nCorreo:")
                    file.write(matrizFactura[fila][columna])

                elif columna == 5:

                    file.write("\nProvincia:")
                    file.write(matrizFactura[fila][columna])

                elif columna == 6:

                    file.write("\nCantón:")
                    file.write(matrizFactura[fila][columna])

                elif columna == 7:

                    file.write("\nDistrito:")
                    file.write(matrizFactura[fila][columna])

    file.write("\n\n")
    file.close()

#Guardar datos de paquete en archivo
def archivoPaquete(matrizPaquete,filas):

    file = open("Paquete.txt", "a")

    for fila in range(len(matrizPaquete)):

        for columna in range(len(matrizPaquete[fila])):
            
            if fila == filas:
                
                if columna == 0:

                    file.write("\nNúmero de guía:")
                    file.write(str(matrizPaquete[fila][columna]))

                elif columna == 1:

                    file.write("\nNombre de destinatario:")
                    file.write(matrizPaquete[fila][columna])

                elif columna == 2:

                    file.write("\nTeléfono de destinatario:")
                    file.write(str(matrizPaquete[fila][columna]))

                elif columna == 3:

                    file.write("\nNúmero de cédula de destinatario:")
                    file.write(str(matrizPaquete[fila][columna]))

                elif columna == 4:

                    file.write("\nPeso del paquete:")
                    file.write(str(matrizPaquete[fila][columna]))

                elif columna == 5:

                    file.write("\nPago:")
                    file.write(matrizPaquete[fila][columna])

                elif columna == 6:

                    file.write("\nMonto a pagar:")
                    file.write(str(matrizPaquete[fila][columna]))

                elif columna == 7:

                    file.write("\nEstado de paquete:")
                    file.write(matrizPaquete[fila][columna])

    file.write("\n\n")
    file.close()


#Principal
print("\n------Bienvenido al sistema especializado de control de mensajerías------")

filaFactura = 0
filaPaquete = 0


registrarUsuario(usuario)
archivoUsuario(usuario)

while opcion != 6 :

    opcionValida = False

    print("\n------Menú------")

    print("\n1.Registrar datos de factura")
    print("\n2.Crear paquete")
    print("\n3.Cambiar estado de paquete")
    print("\n4.Rastrear un paquete")
    print("\n5.Módulo de estadística")
    print("\n6.Salir del sistema")

    while opcionValida == False:

        try:

            opcion = int(input("\nIngrese la opción que desea realizar:"))

            if opcion > 6:

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

        if not factura:

            filaFactura = 0
            registrarFactura(factura)
            archivoFactura(factura,filaFactura)

        else:

            filaFactura += 1
            registrarFactura(factura)
            archivoFactura(factura,filaFactura)

    elif opcion == 2:

        if not factura:

            print("\n------ERROR------")
            print("\nAntes de crear un paquete, debe primero registar los datos para una factura electrónica")

        else:
            
            if not paquete:

                numGuia +=1
                filaPaquete = 0
                crearPaquete(factura,paquete,numGuia,guias,usuario)
                archivoPaquete(paquete,filaPaquete)

            else:

                numGuia +=1
                filaPaquete += 1
                crearPaquete(factura,paquete,numGuia,guias,usuario)
                archivoPaquete(paquete,filaPaquete)

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

    elif opcion == 5:

        if not paquete:

            print("\n------ERROR------")
            print("\nNo ha creado ningún paquete")

        else:

            moduloEstadistica(paquete)

    else:

        print("\nGracias por utilizar el sistema")