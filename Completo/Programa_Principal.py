Fin = -1

Lista_Usuarios = ["Martin","luca","Pedro","Lucia","Lautaro"]
Lista_Contraseñas = ["123","1234","2210","123456","1234567"]

#Listas 
Productos = ["Remeras","Pantalon","Buzos","Gorras","Zapatillas"]
Stocks = [30,25,15,60,25]
Precios = [10,22,32,14,99]
Stock_total = 93

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
########################################## FUNCIONES DE USUARIOS ###############################################

################################### FUNCIONES DE LAS OPCIONES DEL CONTROL DE STOCK ####################################
#================================================ OPCION 1 CREAR_PRODUCTO =============================================
def CREAR_PRODUCTO():
    print("=================================================================================================")
    print("|                                    AGREGAR PRODUCTO                                           |")
    print("=================================================================================================")
    print("=================================================================================================")
    producto = input("Ingrese el producto: ")
    print("=================================================================================================")
    while chequear_si_exsiste_producto(producto, Productos):
        print("=================================================================================================")
        print("|                       EL PRODUCTO YA EXISTE, INGRESE UNO NUEVO                                |")
        print("=================================================================================================")
        producto = input("Ingrese el producto: ")
        print("=================================================================================================")

    print("=================================================================================================")    
    cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
    print("=================================================================================================")
    while cantidad <= 0:
        print("=================================================================================================")
        print("|                      CANTIDAD NO VALIDA, INGRESE UNA CANTIDAD MAYOR A 0                       |")
        print("=================================================================================================")
        cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
        print("=================================================================================================")

    print("=================================================================================================")
    precio = int(input("Ingrese el precio del producto: "))
    print("=================================================================================================")
    while precio < 0:
        print("=================================================================================================")
        print("|                    PRECIO NO VALIDO, INGRESE UN PRECIO MAYOR O IGUAL A 0                      |")
        print("=================================================================================================")
        precio = int(input("Ingrese el precio del producto: "))
        print("=================================================================================================")
                    
    agregar_producto(producto, Productos, Stocks, Precios, precio, cantidad, Stock_total)
                    
    print("=================================================================================================")
    print("|                         EL PRODUCTO HA SIDO AGREGADO AL SISTEMA                               |")
    print("=================================================================================================")
    return
#================================================ OPCION 2 ELIMINAR_PRODCUTO =============================================
def ELIMINAR_PRODUCTO():
    print("=================================================================================================")
    print("|                                     ELIMINAR PRODUCTOS                                        |")
    print("=================================================================================================")
    print("=================================================================================================")
    Verificar_Eliminar = int (input("Quiere eliminar un Producto 1= Si , -1 = No: "))
    print("=================================================================================================")
    while(Verificar_Eliminar != Fin):
        print("=================================================================================================")
        Producto_Eliminar = (input("Ingrese el nombre del producto que desea eliminar: "))
        print("=================================================================================================")
        ELIMINAR_PRODUCTO(Productos, Precios, Stocks, Producto_Eliminar)
        print("=================================================================================================")
        Verificar_Eliminar = int (input("Quiere eliminar un Producto 1= Si , -1 = No: "))
        print("=================================================================================================")
    IMPRIMIR_STOCK(Productos, Precios, Stocks)
    return
#================================================ OPCION 3 ACTUALIZAR_PRODCUTO =============================================
def ACTUALIZAR_PRODUCTO():
    print("=================================================================================================")
    print("|                                     ACTUALIZAR PRODUCTOS                                      |")
    print("=================================================================================================")

    print("=================================================================================================")
    print("|                                     1- ACTUALIZAR STOCK                                       |")
    print("=================================================================================================")
    print("=================================================================================================")
    print("|                                     2- ACTUALIZAR PRECIO                                      |")
    print("=================================================================================================")
    opcion = int(input("Ingrese la opción deseada: "))
    print("=================================================================================================")

    while opcion != 1 and opcion != 2:
        print("=================================================================================================")
        print("|                      OPCION NO VALIDA, INGRESE UNA OPCION VALIDA                              |")
        print("=================================================================================================")
        opcion = int(input("Ingrese la opción deseada: "))
        print("=================================================================================================")
    if (opcion == 1):
        print("=================================================================================================")
        print("|                                   ACTUALIZAR STOCK                                            |")
        print("=================================================================================================")
        producto = input("Ingrese el producto a actualizar stock: ")
        print("=================================================================================================")
        while not chequear_si_exsiste_producto(producto, Productos):
            print("=================================================================================================")
            print("|                  EL PRODUCTO NO EXISTE, INGRESE UN PRODUCTO VALIDO                            |")
            print("=================================================================================================")
            producto = input("Ingrese el producto a actualizar stock: ")
            print("=================================================================================================")
                            
        print("=================================================================================================")    
        cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
        print("=================================================================================================")
        while cantidad <= 0:
            print("=================================================================================================")
            print("|                  CANTIDAD NO VALIDA, INGRESE UNA CANTIDAD MAYOR A 0                           |")
            print("=================================================================================================")
            cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
            print("=================================================================================================")
        print(Stock_total)                
        actualizar_stock(producto, cantidad, Productos, Stocks, Stock_total)
        print(Stock_total)
        print("=================================================================================================")
        print("|                             STOCK ACTUALIZADO CON EXITO                                       |")
        print("=================================================================================================")

    if (opcion == 2):
        print("=================================================================================================")
        print("|                                   ACTUALIZAR PRECIO                                           |")
        print("=================================================================================================")
        producto = input("Ingrese el producto a actualizar precio: ")
        print("=================================================================================================")
        while not chequear_si_exsiste_producto(producto, Productos):
            print("=================================================================================================")
            print("|                     EL PRODUCTO NO EXISTE, INGRESE UN PRODUCTO VALIDO                         |")
            print("=================================================================================================")
            producto = input("Ingrese el producto a actualizar precio: ")
            print("=================================================================================================")

        print("=================================================================================================")
        precio = int(input("Ingrese el precio del producto: "))
        print("=================================================================================================")
        while precio < 0:
            print("=================================================================================================")
            print("|                     PRECIO NO VALIDO, INGRESE UN PRECIO MAYOR O IGUAL A 0                     |")
            print("=================================================================================================")
            precio = int(input("Ingrese el precio del producto: "))
            print("=================================================================================================")
                        
        actualizar_precio(producto, precio, Productos, Precios)
        print("=================================================================================================")
        print("|                                  PRECIO ACTUALIZADO CON EXITO                                 |")
        print("=================================================================================================")
    return
#================================================ OPCION 4 SALIDA_STOCK =============================================
def SALIDA_STOCK():
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
                    seguro = int(input(f"¿Está seguro de retirar {cantidad_a_extraer} {Productos[producto_seleccionado]}? 1-Sí, 2-No: "))
                    if seguro == 2:
                        print("Operación cancelada.")
                        pregunta = int(input("¿Quiere retirar otro producto? Pulse 1 para continuar y -1 para finalizar: "))
                    else:
                        Stocks[producto_seleccionado] -= cantidad_a_extraer
                        global stock_total
                        stock_total -= cantidad_a_extraer
                        print(f"Operación confirmada. Quedan {Stocks[producto_seleccionado]} {Productos[producto_seleccionado]}.")
                        pregunta = int(input("¿Quiere retirar otro producto? Pulse 1 para continuar y -1 para finalizar: "))
    mostrar_stock()
    return
#================================================ OPCION 5 STOCK A IMPRIMIR =============================================
def Ordenamiento_ListasParaleas_Burbuja(Productos, Precios,Stocks):
    n = len(Stocks)
    for i in range(n):
        for j in range(0, n - i - 1):
            if Stocks[j] > Stocks[j + 1]:
                AUX = Stocks[j]
                Stocks[j] = Stocks[j + 1]
                Stocks[j + 1] = AUX
                AUX = Precios[j]
                Precios[j] = Precios[j + 1]
                Precios[j + 1] = AUX
                AUX = Productos[j]
                Productos[j] = Productos[j + 1]
                Productos[j + 1] = AUX
    return Productos, Precios, Stocks

def IMPRIMIR_STOCK(Productos, Precios, Stock):
    Ordenamiento_ListasParaleas_Burbuja(Productos, Precios,Stocks)
    print("=================================================================================================")
    print("|                                         IMPRIMIR LISTAS                                        |")
    print("=================================================================================================")
    print("Lista de Productos Registrados:", end=" ")
    for i in range(len(Productos)):
        print(Productos[i], end=" ")
    print() 
    print("---------------------------------------")
    print("Lista de Precios Registradas:", end=" ")
    for i in range(len(Precios)):
        print(Precios[i], end=" ")
    print()
    print("=================================================================================================")
    print("---------------------------------------")
    print("Lista de Cantidad Stock Registradas:", end=" ")
    for i in range(len(Stock)):
        print(Stock[i], end=" ")
    print()
    print("=================================================================================================")
    print(f"El Stock Total es de: {Stock_total}")
    print("=================================================================================================")
    return

################################### FUNCIONES DE LAS OPCIONES DEL CONTROL DE STOCK ####################################

########################################## FUNCIONES DE CONTROL DE STOCK #####################################################
################################## AGREGAR Y ACTUALIZAR PRODUCTO  ##############################################
def chequear_si_exsiste_producto(producto, productos):
    for i in range(len(productos)):
        if producto == productos[i]:
            return True
    return False

def actualizar_stock(producto, cantidad, productos, stocks, Stock_total):
    for i in range(len(productos)):
        if producto == productos[i]:
            stocks[i] += cantidad
            global Stock_total
            Stock_total += cantidad
            print("El stock del producto: "+ productos[i] + " ha sido actualizado")

def actualizar_precio(producto, precio, productos, precios):
    for i in range(len(productos)):
        if producto == productos[i]:
            precios[i] = precio
            print("El precio del producto: "+ productos[i] + " ha sido actualizado")
                
def agregar_producto(producto, productos, stocks, precios, precio, cantidad, stockTotal):
    # Se agrega el producto a la lista de productos
    productos.append(producto)
    # Se agrega el stock a la lista de stocks
    stocks.append(cantidad)
    # Se agrega el precio a la lista de precios
    precios.append(precio)

    global Stock_total
    Stock_total += cantidad

    print(f"El producto {producto} ha sido agregado al sistema")
################################## AGREGAR O ACTUALIZAR PRODUCTO  ##############################################

######################################## ELIMINAR PRODUCTOS ####################################################
def Borrar_Producto(productos, precios, stock, nombre_producto):
    for i in range(len(productos)):
        if (productos[i] == nombre_producto):
            print(f"El producto '{nombre_producto}' fue encontrado y se procederá a eliminarlo.")
            productos.pop(i)
            precios.pop(i)
            stock.pop(i)
            print(f"Lista de productos actualizada: {productos}")
            print(f"Lista de precios actualizada: {precios}")
            print(f"Lista de stock actualizada: {stock}")
            return
    print("=================================================================================================")
    print(f"                  El producto '{nombre_producto}' no fue encontrado en la lista.                ")
    print("=================================================================================================")    
    return
######################################## SALIDA DE PRODUCTOS  ##################################################
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
    cantidad_a_extraer = int(input(f"Cantidad de {Productos[producto]} a extraer (o -1 para cancelar): "))
    if cantidad_a_extraer == -1:
        print("Operación cancelada.")
        return -1 
    while cantidad_a_extraer > Stocks[producto] or cantidad_a_extraer < 0:
        if cantidad_a_extraer > Stocks[producto]:
            print(f"Stock insuficiente. Solo hay {Stocks[producto]} unidades de {Productos[producto]}.")
        elif cantidad_a_extraer < 0:
            print("Cantidad negativa no permitida.")
        cantidad_a_extraer = int(input(f"Cantidad de {Productos[producto]} a extraer (o -1 para cancelar): "))
    return cantidad_a_extraer

def mostrar_stock():
    print(f"El stock final quedó en {Stock_total}.")
    for i, producto in enumerate(Productos):
        print(f"La cantidad de {producto} es de {Stocks[i]}.")
    return
################################## SALIDA DE PRODUCTOS  ########################################################

###################################   PROGRAMA PRINCIPAL     ###################################################
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
                if(Menu == 1):
                    CREAR_PRODUCTO()

                if(Menu == 2):
                    ELIMINAR_PRODUCTO()
                
                if(Menu == 3):
                    ACTUALIZAR_PRODUCTO()

                if(Menu == 4):
                    SALIDA_STOCK()

                if(Menu == 5):
                    IMPRIMIR_STOCK(Productos, Precios, Stocks)

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
###################################   PROGRAMA PRINCIPAL     ###################################################
