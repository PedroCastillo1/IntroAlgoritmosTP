Fin = -1

Lista_Usuarios = ["Martin","luca","Pedro","Lucia","Lautaro"]
Lista_Contraseñas = ["123","1234","2210","123456","1234567"]

"""
IDEA PARA LOS NOMBRES DE LAS LISTAS!!!

Esto a modo ejemplo para que usen en sus partes los mismos nombres en las listas
para que luego en este programa principal se pueda unificar en este mismo archivo

Productos = [] -------> (Ej: Productos = [Remeras,Pantalones,Buzos,Camperas,zapatillas])
Precio = []  -------> (Ej: Precio = [100, 9.99 , 23.50 , 200 , 450])
Entrada = Involucran estas listas = Productos - Cant_Stock.
Salida = Involucran estas listas = Productos - Cant_Stock.
Cant_Stock = [] -------> (Ej: Cant_Stock = [20,10,30,15,5]) 

"""
"""
!!!!    Para poder aplicar esa comunicacion entre las listas creen funciones donde por medio de la 
posicion de cada elemento es compartida por las posiciones de las demas listas    !!!

Productos = [] -------> (Ej: Productos = [Remeras,Pantalones,Buzos,Camperas,zapatillas])
Precio = []  -------> (Ej: Precio = [100, 9.99 , 23.50 , 200 , 450])
Entrada = Involucran estas listas = Productos - Cant_Stock.
Salida = Involucran estas listas = Productos - Cant_Stock.
Cant_Stock = [] -------> (Ej: Cant_Stock = [20,10,30,15,5]) 

"""

#Listas 
productos = ["Remeras","Pantalon","Buzos","Gorras","Zapatillas"]
stocks = [10,20,15,23,25]
precios = [10,22,32,14,99]
stock_total = 150

############################################ INTERFACES DEL PROGRAMA ##################################################
def Menu_Interactivo_GestionUsuario():
    print("=================================================================================================")
    print("|                          BIENVENIDO AL PROGRAMA DE CONTROL DE STOCKS                          |")
    print("=================================================================================================")
    print("=================================================================================================")
    print("|                     SI USTED QUIERE INGRESAR A SU CUENTA, INGRESE EL VALOR 1                  |")
    print("=================================================================================================")
    print("=================================================================================================")
    print("|                     SI USTED QUIERE CREAR A SU CUENTA, INGRESE EL VALOR 2                     |")
    print("=================================================================================================")
    print("=================================================================================================")
    print("|                     SI USTED QUIERE VER LA LISTA DE CUENTAS, INGRESE EL VALOR 3               |")
    print("=================================================================================================")
    print("=================================================================================================")
    print("|                     SI USTED QUIERE TERMINAR EL PROGRAMA, INGRESE EL VALOR -1                 |")
    print("=================================================================================================")
    return

def Menu_Interactivo_ControlStock():
    print("#################################################################################################")
    print("|                                      CONTROL DE STOCKS                                        |")
    print("#################################################################################################")
    print("#################################################################################################")
    print("|                             CREAR PRODUCTO, INGRESE EL VALOR 1                                |")
    print("#################################################################################################")
    print("#################################################################################################")
    print("|                             ELIMINAR PRODUCTO, INGRESE EL VALOR 2                             |")
    print("#################################################################################################")
    print("#################################################################################################")
    print("|                             ACTUALIZAR PRODUCTOS, INGRESE EL VALOR 3                          |")
    print("#################################################################################################")
    print("#################################################################################################")
    print("|                             SALIDA DE STOCK, INGRESE EL VALOR 4                               |")
    print("#################################################################################################")
    print("#################################################################################################")
    print("|                             STOCK A IMPRIMIR, INGRESE EL VALOR 5                              |")
    print("#################################################################################################")
    print("#################################################################################################")
    print("|                     SI USTED QUIERE TERMINAR EL PROGRAMA, INGRESE EL VALOR -1                 |")
    print("#################################################################################################")
    return
############################################ INTERFACES DEL PROGRAMA ##################################################

################################### FUNCIONES DE LAS OPCIONES DEL MENU DE USUARIOS ####################################
#================================================ OPCION 1 INICIAR SESESION =============================================
def INICIAR_SESION(Lista_Usuarios,Lista_Contraseñas):
    Intentos = 0
    Max_Intentos = 3
    print("=================================================================================================")
    print("|                                         INICIAR SESION                                        |")
    print("=================================================================================================")

    Inicio = int (input("Si quiere iniciar sesion ponga 1, si quiere salir ponga -1:  "))
    while(Inicio != Fin):
        while((Inicio != 1) and (Inicio != Fin)):
            print("Ingresaste mal las opciones a elegir")
            Inicio = int (input("Si quiere iniciar sesion ponga 1, si quiere salir ponga -1"))
        
        if Inicio == Fin:
            print("Has decidido salir del programa.")
            return False

        while(Intentos < Max_Intentos):
            print("=================================================================================================")
            Nombre_Usuario = input("INGRESAR SU NOMBRE DE USUARIO: ")
            print("=================================================================================================")
            Contraseña_Usuario = input("INGRESAR SU CONTRASEÑA: ")

            if(Buscar_Usuario(Lista_Usuarios, Lista_Contraseñas, Nombre_Usuario, Contraseña_Usuario)):
                print("Inicio de sesión exitoso.")
                return True
            else:
                Intentos += 1
                print(f"Intento fallido. Te quedan {Max_Intentos - Intentos} intentos.")

        if(Intentos >= Max_Intentos):
            print("Demasiados intentos fallidos. Sesión bloqueada.")
            return False
#================================================ OPCION 2 CREAR =============================================
def CREAR_SESSION():
    print("=================================================================================================")
    print("|                                         CREAR SESION                                          |")
    print("=================================================================================================")
    print("=================================================================================================")
    Nombre_Usuario = input("INGRESAR SU NOMBRE DE USUARIO = ")
    print("=================================================================================================")
    while not(Verificar_Existencia_Usuario(Lista_Usuarios,Nombre_Usuario)):
        print("=================================================================================================")
        print("|                                 INGRESAR NUEVAMENTE SU NOMBRE                                 |")
        print("=================================================================================================")
        print("=================================================================================================")
        Nombre_Usuario = input("INGRESAR SU NOMBRE DE USUARIO = ")
        print("=================================================================================================")
    print("=================================================================================================")
    Contraseña_Usuario = input("INGRESAR SU CONTRASEÑA DE USUARIO = ")
    print("=================================================================================================")
    Agregar_Usuario(Lista_Usuarios,Lista_Contraseñas,Nombre_Usuario,Contraseña_Usuario)
    return
#=================================== OPCION 3 IMPRIMIR LISTAS DE USUARIOS =========================================
def Imprimir_Listas_Usuarios(Lista_Usuarios, Lista_Contraseñas):
    print("=================================================================================================")
    print("|                                         IMPRIMIR LISTAS                                        |")
    print("=================================================================================================")
    print("Lista de Usuarios Registrados:", end=" ")
    for i in range(len(Lista_Usuarios)):
        print(Lista_Usuarios[i], end=" ")
    print() 
    print("---------------------------------------")
    print("Lista de Contraseñas Registradas:", end=" ")
    for i in range(len(Lista_Contraseñas)):
        print('*' * len(Lista_Contraseñas[i]), end=" ")
    print()
    print("=================================================================================================")
    return

################################### FUNCIONES DE LAS OPCIONES DEL MENU DE USUARIOS ####################################




########################################## FUNCIONES DE USUARIOS #####################################################
def Verificar_Existencia_Usuario(Lista_Usuarios,Nombre_Usuario):
    i = 0
    while((i < len(Lista_Usuarios)) and (Lista_Usuarios[i] != Nombre_Usuario)):
        i = i + 1
    if(i < len(Lista_Usuarios)):
        print("EL NOMBRE YA SE ENCUENTRA UTILIZANDOSE, POR FAVOR INTENTE CON OTRO NUEVO")
        return False
    print("EL NOMBRE SE ENCUENTA DISPONIBLE :) ")
    return True

def Agregar_Usuario(Lista_Usuarios,Lista_Contraseñas,Nombre_Usuario,Contraseña_Usuario):
    Lista_Usuarios.append(Nombre_Usuario)
    Lista_Contraseñas.append(Contraseña_Usuario) 
    return Lista_Usuarios,Lista_Contraseñas

def Verificacion_Menu(Valor_Mini_Interfaz):
    while((Valor_Mini_Interfaz != 1) and (Valor_Mini_Interfaz != 2) and (Valor_Mini_Interfaz != 3) and (Valor_Mini_Interfaz != Fin)):
        print("=================================================================================================")
        print("|                        INGRESASTE MAL EL VALOR DE LAS OPCIONES                                |")
        print("|                             INTENTAR NUEVAMENTE POR FAVOR                                     |")
        print("=================================================================================================")
        print("=================================================================================================")
        Valor_Mini_Interfaz = int (input("INGRESAR SU VALOR POR FAVOR = "))
        print("=================================================================================================")
    return

def Verificacion_Menu_Stocks(Menu):
    while((Menu != 1) and (Menu != 2) and (Menu != 3) and (Menu != 4) and (Menu != 5) and (Menu != Fin)):
        print("=================================================================================================")
        print("|                        INGRESASTE MAL EL VALOR DE LAS OPCIONES                                |")
        print("|                             INTENTAR NUEVAMENTE POR FAVOR                                     |")
        print("=================================================================================================")
        Menu = int (input("Ingrese la Opcion elegida: "))
    return

def Buscar_Usuario(Lista_Usuarios, Lista_Contraseñas, Nombre_Usuario, Contraseña_Usuario):
    i = 0
    while ((i < len(Lista_Usuarios)) and (Lista_Usuarios[i] != Nombre_Usuario)):
        i = i + 1
    if(i < len(Lista_Usuarios)):
        Pos = i
        if Lista_Contraseñas[Pos] == Contraseña_Usuario:
            return True
    return False

########################################## FUNCIONES DE USUARIOS #####################################################

################################## AGREGAR O ACTUALIZAR PRODUCTO  ##############################################


def chequear_si_exsiste_producto(producto, productos):
    for i in range(len(productos)):
        if producto == productos[i]:
            return True
    return False

def actualizar_stock(producto, cantidad, productos, stocks, stocksTotales):
    for i in range(len(productos)):
        if producto == productos[i]:
            stocks[i] += cantidad
            stocksTotales += cantidad
            print("El stock del producto: "+ productos[i] + " ha sido actualizado")

def actualizar_precio(producto, precio, productos, precios):
    for i in range(len(productos)):
        if producto == productos[i]:
            precios[i] = precio
            print("El precio del producto: "+ productos[i] + " ha sido actualizado")
                
def agregar_producto(producto, productos, stocks, precios, precio, cantidad):
    # Se agrega el producto a la lista de productos
    productos.append(producto)
    # Se agrega el stock a la lista de stocks
    stocks.append(cantidad)
    # Se agrega el precio a la lista de precios
    precios.append(precio)

    print(f"El producto {producto} ha sido agregado al sistema")

# Hace todo lo que se pide en la opción 1
def opcion_1(producto, productos, stocks, precios, precio, cantidad):
    if chequear_si_exsiste_producto(producto, productos):
        actualizar_stock(producto, cantidad, productos, stocks)
        actualizar_precio(producto, precio, productos, precios)
    else:   
        agregar_producto(producto, productos, stocks, precios, precio, cantidad)   
    print(productos)
    print(stocks)
    print(precios)
################################## AGREGAR O ACTUALIZAR PRODUCTO  ##############################################


################################## salida de productos  ##############################################
def seleccionar_producto():
    extraer = int(input("¿Qué producto desea extraer? 0-r , 1-z, 2-b , 3-g , 4-p (o -1 para salir): "))
    if extraer == -1:
        print("Saliendo del programa.")
        return -1  
    while extraer < 0 or extraer > 4:
        print("Producto inexistente. Inténtelo de nuevo.")
        extraer = int(input("¿Qué producto desea extraer? 0-r , 1-z, 2-b , 3-g , 4-p (o -1 para salir): "))
    return extraer


def seleccionar_cantidad(producto):
    cantidad_a_extraer = int(input(f"Cantidad de {productos[producto]} a extraer (o -1 para cancelar): "))
    if cantidad_a_extraer == -1:
        print("Operación cancelada.")
        return -1 
    while cantidad_a_extraer > stocks[producto] or cantidad_a_extraer < 0:
        if cantidad_a_extraer > stocks[producto]:
            print(f"Stock insuficiente. Solo hay {stocks[producto]} unidades de {productos[producto]}.")
        elif cantidad_a_extraer < 0:
            print("Cantidad negativa no permitida.")
        cantidad_a_extraer = int(input(f"Cantidad de {productos[producto]} a extraer (o -1 para cancelar): "))
    return cantidad_a_extraer

def mostrar_stock():
    print(f"El stock final quedó en {stock_total}.")
    for i, producto in enumerate(productos):
        print(f"La cantidad de {producto} es de {stocks[i]}.")
    return


################################## salida de productos  ##############################################


######################################################             PROGRAMA PRINCIPAL             #####################################################################################
Menu_Interactivo_GestionUsuario()
print("=================================================================================================")
Valor_Mini_Interfaz = int (input("INGRESAR SU VALOR POR FAVOR = "))
print("=================================================================================================")

while(Valor_Mini_Interfaz != Fin):
    Verificacion_Menu(Valor_Mini_Interfaz)


    if(Valor_Mini_Interfaz == 1):   
        while(INICIAR_SESION(Lista_Usuarios,Lista_Contraseñas)):
            Menu_Interactivo_ControlStock()
            Menu = int (input("Ingrese la Opcion elegida: "))
            while(Menu != Fin):
                Verificacion_Menu_Stocks(Menu)
                """
                #######################################################################################
                ACA  VAN A ESTAR LAS OPCIONES DEL PROGRAMA (AGREGAR,ELIMINAR,ENTRADA,SALIDA,TOTAL_STOCK)
                #######################################################################################
                """
                if(Menu == 1):
                    print("=================================================================================================")
                    print("|                                         AGREGAR PRODUCTO                                      |")
                    print("=================================================================================================")
                    # Se pide al usuario que ingrese el producto, su precio y la cantidad de unidades ingresadas
                    print("=================================================================================================")
                    producto = input("Ingrese el producto: ")
                    print("=================================================================================================")
                    while chequear_si_exsiste_producto(producto, productos):
                        print("=================================================================================================")
                        print("|                             EL PRODUCTO YA EXISTE, INGRESE UNO NUEVO                          |")
                        print("=================================================================================================")
                        producto = input("Ingrese el producto: ")
                        print("=================================================================================================")

                    print("=================================================================================================")    
                    cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
                    print("=================================================================================================")
                    while cantidad <= 0:
                        print("=================================================================================================")
                        print("|                             CANTIDAD NO VALIDA, INGRESE UNA CANTIDAD MAYOR A 0                |")
                        print("=================================================================================================")
                        cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
                        print("=================================================================================================")

                    print("=================================================================================================")
                    precio = int(input("Ingrese el precio del producto: "))
                    print("=================================================================================================")
                    while precio < 0:
                        print("=================================================================================================")
                        print("|                             PRECIO NO VALIDO, INGRESE UN PRECIO MAYOR O IGUAL A 0             |")
                        print("=================================================================================================")
                        precio = int(input("Ingrese el precio del producto: "))
                        print("=================================================================================================")
                    
                    agregar_producto(producto, productos, stocks, precios, precio, cantidad)
                    
                    print("=================================================================================================")
                    print("|                            EL PRODUCTO HA SIDO AGREGADO AL SISTEMA                            |")
                    print("=================================================================================================")
                    print("Productos:", productos)
                    print("Stocks:", stocks)
                    print("Precios:", precios)
                    
                
                if(Menu == 2):
                    print("ESTA ES LA PARTE 2")
                
                if(Menu == 3):
                    #Le pregunto si quiere actualizar stock o Precios
                    print("=================================================================================================")
                    print("|                                         ACTUALIZAR PRODUCTOS                                  |")
                    print("=================================================================================================")

                    print("=================================================================================================")
                    print("|                             1- ACTUALIZAR STOCK                                               |")
                    print("=================================================================================================")
                    print("=================================================================================================")
                    print("|                             2- ACTUALIZAR PRECIO                                              |")
                    print("=================================================================================================")
                    opcion = int(input("Ingrese la opción deseada: "))
                    print("=================================================================================================")

                    while opcion != 1 and opcion != 2:
                        print("=================================================================================================")
                        print("|                             OPCION NO VALIDA, INGRESE UNA OPCION VALIDA                       |")
                        print("=================================================================================================")
                        opcion = int(input("Ingrese la opción deseada: "))
                        print("=================================================================================================")
                    if opcion == 1:
                        #Le pido el producto a actualizar stock
                        print("=================================================================================================")
                        print("|                             ACTUALIZAR STOCK                                                  |")
                        print("=================================================================================================")
                        producto = input("Ingrese el producto a actualizar stock: ")
                        print("=================================================================================================")
                        while not chequear_si_exsiste_producto(producto, productos):
                            print("=================================================================================================")
                            print("|                             EL PRODUCTO NO EXISTE, INGRESE UN PRODUCTO VALIDO                 |")
                            print("=================================================================================================")
                            producto = input("Ingrese el producto a actualizar stock: ")
                            print("=================================================================================================")
                            
                        print("=================================================================================================")    
                        cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
                        print("=================================================================================================")
                        while cantidad <= 0:
                            print("=================================================================================================")
                            print("|                             CANTIDAD NO VALIDA, INGRESE UNA CANTIDAD MAYOR A 0                |")
                            print("=================================================================================================")
                            cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
                            print("=================================================================================================")
                        
                        actualizar_stock(producto, cantidad, productos, stocks, stock_total)
                        print("=================================================================================================")
                        print("|                             STOCK ACTUALIZADO CON EXITO                                       |")
                        print("=================================================================================================")
                        print("Productos:", productos)
                        print("Stocks:", stocks)
                        print("Precios:", precios)

                    if opcion == 2:
                        #Le pido el producto a actualizar precio
                        print("=================================================================================================")
                        print("|                             ACTUALIZAR PRECIO                                                 |")
                        print("=================================================================================================")
                        producto = input("Ingrese el producto a actualizar precio: ")
                        print("=================================================================================================")
                        while not chequear_si_exsiste_producto(producto, productos):
                            print("=================================================================================================")
                            print("|                             EL PRODUCTO NO EXISTE, INGRESE UN PRODUCTO VALIDO                 |")
                            print("=================================================================================================")
                            producto = input("Ingrese el producto a actualizar precio: ")
                            print("=================================================================================================")


                        print("=================================================================================================")
                        precio = int(input("Ingrese el precio del producto: "))
                        print("=================================================================================================")
                        while precio < 0:
                            print("=================================================================================================")
                            print("|                             PRECIO NO VALIDO, INGRESE UN PRECIO MAYOR O IGUAL A 0             |")
                            print("=================================================================================================")
                            precio = int(input("Ingrese el precio del producto: "))
                            print("=================================================================================================")
                        
                        actualizar_precio(producto, precio, productos, precios)
                        print("=================================================================================================")
                        print("|                             PRECIO ACTUALIZADO CON EXITO                                      |")
                        print("=================================================================================================")
                        print("Productos:", productos)
                        print("Stocks:", stocks)
                        print("Precios:", precios)

                if(Menu == 4):
                    print("ESTA ES LA PARTE 4")
                    pregunta = int(input("¿Quiere retirar un producto? Pulse 1 para iniciar y -1 para finalizar: "))

                    while pregunta != -1:
                        if pregunta != 1:
                            print("Opción no válida.")
                            pregunta = int(input("¿Quiere retirar un producto? Pulse 1 para iniciar y -1 para finalizar: "))
                        else:
                            
                            producto_seleccionado = seleccionar_producto()
                            if producto_seleccionado == -1:
                                pregunta = -1  
                            else:
                            
                                cantidad_a_extraer = seleccionar_cantidad(producto_seleccionado)
                                if cantidad_a_extraer == -1:
                                    pregunta = int(input("¿Quiere retirar otro producto? Pulse 1 para continuar y -1 para finalizar: "))
                                else:
                                    
                                    seguro = int(input(f"¿Está seguro de retirar {cantidad_a_extraer} {productos[producto_seleccionado]}? 1-Sí, 2-No: "))
                                    if seguro == 2:
                                        print("Operación cancelada.")
                                        pregunta = int(input("¿Quiere retirar otro producto? Pulse 1 para continuar y -1 para finalizar: "))
                                    else:
                                        stocks[producto_seleccionado] -= cantidad_a_extraer
                                        stock_total -= cantidad_a_extraer
                                        print(f"Operación confirmada. Quedan {stocks[producto_seleccionado]} {productos[producto_seleccionado]}.")
                                        pregunta = int(input("¿Quiere retirar otro producto? Pulse 1 para continuar y -1 para finalizar: "))

                    mostrar_stock()

                if(Menu == 5):
                    print("ESTA ES LA PARTE 5")



                Menu_Interactivo_ControlStock()
                Menu = int (input("Ingrese la Opcion elegida: "))
            print("USTED A CERRADO SESSION.")



    if(Valor_Mini_Interfaz == 2):
        CREAR_SESSION()
    if(Valor_Mini_Interfaz == 3):
        Imprimir_Listas_Usuarios(Lista_Usuarios, Lista_Contraseñas)  
    Menu_Interactivo_GestionUsuario()
    print("=================================================================================================")
    Valor_Mini_Interfaz = int (input("INGRESAR SU VALOR POR FAVOR = "))
    print("=================================================================================================")
print("USTED A FINALIZADO EL PROGRAMA, HASTA LUEGOO")
######################################################             PROGRAMA PRINCIPAL             #####################################################################################
