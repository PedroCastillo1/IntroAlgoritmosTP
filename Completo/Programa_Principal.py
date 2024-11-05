Fin = -1

Lista_Usuarios = ["Martin","luca","Pedro","Lucia","Lautaro"]
Lista_Contraseñas = ["123","1234","2210","123456","1234567"]

#Listas 
Productos = ["Remeras","Pantalon","Buzos","Gorras","Zapatillas"]
Stocks = [10,20,30,40,50]
Precios = [10,22,32,14,99]
Stock_total = 150

########################## mostrar productos #########################################################################
def read_product (Productos):
    for i in range(len(Productos)):
        print(Productos[i], end=" ")
    return    

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
def CREAR_PRODUCTO(Stock_total):
    print("=================================================================================================")
    print("|                                    AGREGAR PRODUCTO                                           |")
    print("=================================================================================================")
    print("=================================================================================================")
    New_producto = input("Ingrese el producto: ")
    print("=================================================================================================")
    while chequear_si_exsiste_producto(New_producto, Productos):
        print("=================================================================================================")
        print("|                       EL PRODUCTO YA EXISTE, INGRESE UNO NUEVO                                |")
        print("=================================================================================================")
        New_producto = input("Ingrese el producto: ")
        print("=================================================================================================")

    print("=================================================================================================")    
    New_cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
    print("=================================================================================================")
    while New_cantidad <= 0:
        print("=================================================================================================")
        print("|                      CANTIDAD NO VALIDA, INGRESE UNA CANTIDAD MAYOR A 0                       |")
        print("=================================================================================================")
        New_cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
        print("=================================================================================================")

    print("=================================================================================================")
    New_precio = int(input("Ingrese el precio del producto: "))
    print("=================================================================================================")
    while New_precio < 0:
        print("=================================================================================================")
        print("|                    PRECIO NO VALIDO, INGRESE UN PRECIO MAYOR O IGUAL A 0                      |")
        print("=================================================================================================")
        New_precio = int(input("Ingrese el precio del producto: "))
        print("=================================================================================================")

    Stock_total = agregar_producto(New_producto, New_cantidad, New_precio, Productos, Stocks, Precios, Stock_total)
     
    Ordenamiento_ListasParaleas_Burbuja(Productos, Precios,Stocks)
    print("=================================================================================================")
    print("|                         EL PRODUCTO HA SIDO AGREGADO AL SISTEMA                               |")
    print("=================================================================================================")
    return Stock_total
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
        Borrar_Producto(Productos, Precios, Stocks, Producto_Eliminar)
        print("=================================================================================================")
        Verificar_Eliminar = int (input("Quiere eliminar un Producto 1= Si , -1 = No: "))
        print("=================================================================================================")
    IMPRIMIR_STOCK()
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
                        
        actualizar_stock(producto, cantidad, Productos, Stocks, Stock_total)
        print("=================================================================================================")
        print("|                             STOCK ACTUALIZADO CON EXITO                                       |")
        print("=================================================================================================")
        Ordenamiento_ListasParaleas_Burbuja(Productos, Precios,Stocks)
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
def retirar_stock():
    continuar = 1
    while continuar == 1:
        IMPRIMIR_STOCK()
        indice_producto = solicitar_producto()
        cantidad_extraer = solicitar_cantidad(Stocks[indice_producto])

        # Ajuste del stock
        Stocks[indice_producto] -= cantidad_extraer
        global Stock_total
        Stock_total -= cantidad_extraer
        print("=================================================================================================")
        print(f"| Extracción exitosa de {cantidad_extraer} unidades de '{Productos[indice_producto]}'.            |")
        print("=================================================================================================")
        print(f"| Stock actual de '{Productos[indice_producto]}': {Stocks[indice_producto]} unidades.             |")
        print(f"| Stock total actualizado: {Stock_total} unidades.                                                |")
        print("=================================================================================================")

        # Pregunta si el usuario desea continuar o finalizar
        print("=================================================================================================")
        continuar = int(input("| ¿Desea retirar otro producto? Ingrese 1 para continuar o 2 para finalizar: "))
        print("=================================================================================================")
    print("=================================================================================================")
    print("| Ha finalizado el programa. ¡Hasta luego!                                                      |")
    print("=================================================================================================")

#================================================ OPCION 5 STOCK A IMPRIMIR =============================================
def Ordenamiento_ListasParaleas_Burbuja(Productos, Precios,Stocks):
    n = len(Stocks)
    for i in range(n):
        for j in range(0, n - i - 1):
            if Stocks[j] > Stocks[j + 1]:
                # Intercambiar Stocks
                AUX = Stocks[j]
                Stocks[j] = Stocks[j + 1]
                Stocks[j + 1] = AUX
                # Intercambiar precios para mantener la correspondencia
                AUX = Precios[j]
                Precios[j] = Precios[j + 1]
                Precios[j + 1] = AUX
                # Intercambiar productos para mantener la correspondencia
                AUX = Productos[j]
                Productos[j] = Productos[j + 1]
                Productos[j + 1] = AUX
    return Productos, Precios, Stocks

def IMPRIMIR_STOCK():
    print("=================================================================================================")
    print("|                                   PRODUCTOS DISPONIBLES                                       |")
    print("=================================================================================================")
    print("| Producto     | Stock disponible | Precio por unidad                                           |")
    print("=================================================================================================")
    for i in range(len(Productos)):
        print(f"| {Productos[i]:<12} | {Stocks[i]:<15}  | ${Precios[i]:<20}                                       |")
    print("=================================================================================================")
    print(f"Stock total: {Stock_total} unidades ")
    
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
            Stock_total += cantidad
            print("El stock del producto: "+ productos[i] + " ha sido actualizado")

def actualizar_precio(producto, precio, productos, precios):
    for i in range(len(productos)):
        if producto == productos[i]:
            precios[i] = precio
            print("El precio del producto: "+ productos[i] + " ha sido actualizado")
                
def agregar_producto(New_producto, New_cantidad, New_precio, Productos, Stocks, Precios, Stock_total):
    # Se agrega el producto a la lista de productos
    Productos.append(New_producto)
    # Se agrega el stock a la lista de stocks
    Stocks.append(New_cantidad)
    # Se agrega el precio a la lista de precios
    Precios.append(New_precio)

    Stock_total += New_cantidad

    print(f"El producto {New_producto} ha sido agregado al sistema")
    return Stock_total
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
def Buscar_Producto(Productos, Producto_Buscar):
    for i in range(len(Productos)):
        if Productos[i] == Producto_Buscar:
            return i
    return -1

def solicitar_producto():
    producto_valido = -1
    while producto_valido == -1:
        print("=================================================================================================")
        producto_buscado = input("| ¿Qué producto desea extraer?: ")
        print("=================================================================================================")
        producto_valido = Buscar_Producto(Productos, producto_buscado)
        if producto_valido == -1:
            print("=================================================================================================")
            print("| El producto ingresado es incorrecto. Intente nuevamente.                                      |")
            print("=================================================================================================")
        else:
            print("=================================================================================================")
            print(f"| Producto '{Productos[producto_valido]}' encontrado.                                           |")
            print("=================================================================================================")
            confirmacion = int(input("| ¿Está seguro? Ingrese 1 para confirmar o 2 para elegir otro producto: "))
            print("=================================================================================================")
            if confirmacion != 1:
                producto_valido = -1  
    return producto_valido

def solicitar_cantidad(stock_disponible):
    cantidad = -1  # Inicialización con un valor inválido
    while cantidad <= 0 or cantidad > stock_disponible:
        print("=================================================================================================")
        cantidad = int(input(f"| Ingrese la cantidad de unidades que desea extraer (disponible: {stock_disponible}): "))
        print("=================================================================================================")
        
        if cantidad <= 0:
            print("=================================================================================================")
            print("| Cantidad inexistente. Ingrese un valor mayor a 0.                                             |")
            print("=================================================================================================")
        elif cantidad > stock_disponible:
            print("=================================================================================================")
            print(f"| Stock insuficiente. Solo hay {stock_disponible} unidades disponibles.                          |")
            print("=================================================================================================")
    
    return cantidad


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
                    Stock_total = CREAR_PRODUCTO(Stock_total)

                if(Menu == 2):
                    ELIMINAR_PRODUCTO()
                
                if(Menu == 3):
                    ACTUALIZAR_PRODUCTO()

                if(Menu == 4):
                    retirar_stock()

                if(Menu == 5):
                    IMPRIMIR_STOCK()

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
