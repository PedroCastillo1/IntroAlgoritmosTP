# Una Constante para generar cortes en el programa
Fin = -1
#Listas de Usuarios del Programa
Lista_Usuarios = ["Martin","luca","Pedro","Lucia","Lautaro"]
Lista_Contraseñas = ["123","1234","2210","123456","1234567"]

#Listas 
Productos = ["Remeras","Pantalon","Buzos","Gorras","Zapatillas"]
Stocks = [10,20,30,40,50]
Precios = [10,22,32,14,99]
Stock_total = 150

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
    # 2 variables para verificar la cantidad de intentos de inicio de sesion
    Intentos = 0
    Max_Intentos = 3
    print("=================================================================================================")
    print("|                                         INICIAR SESION                                        |")
    print("=================================================================================================")
    # ingresamos por teclado 1 o Fin para iniciar sesion o querer volver a la interfaz de usuario
    Inicio = int (input("Si quiere iniciar sesion ponga 1, si quiere salir ponga -1:  "))
    # Verificamos que el valor sea el correspondiente para realizar las posibles opciones
    while(Inicio != Fin):
        # Verificamos que mientras no esten en esos 2 valores correctos tengra que ingresarlo nuevamente
        while((Inicio != 1) and (Inicio != Fin)):
            print("Ingresaste mal las opciones a elegir")
            Inicio = int (input("Si quiere iniciar sesion ponga 1, si quiere salir ponga -1"))
        # Si ingresa Fin significa que decidio salir del Programa
        if Inicio == Fin:
            print("Has decidido salir del programa.")
            return False
        # Aca vamos a estar verificando que no supere la cantidad de intentos permitidos para ingresar
        while(Intentos < Max_Intentos):
            # Pedimos sus datos a ingresar Nombre y Contraseña
            print("=================================================================================================")
            Nombre_Usuario = input("INGRESAR SU NOMBRE DE USUARIO: ")
            print("=================================================================================================")
            Contraseña_Usuario = input("INGRESAR SU CONTRASEÑA: ")
            # verificamos que dicho usuario ingresado exista dentro de nuestras listas
            if(Buscar_Usuario(Lista_Usuarios, Lista_Contraseñas, Nombre_Usuario, Contraseña_Usuario)):
                print("Inicio de sesión exitoso.")
                return True
            else:
                # Si no existe se incremente la variable intentos y se notifica
                Intentos += 1
                print(f"Intento fallido. Te quedan {Max_Intentos - Intentos} intentos.")
        # Si dichos intentos son mas de los permitidos, te devuelve a la interfaz principal
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
    #Aca vamos a verificar que dicho nombre no se encuentre dentro de las listas de Usuarios
    while not(Verificar_Existencia_Usuario(Lista_Usuarios,Nombre_Usuario)):
        print("=================================================================================================")
        print("|                                 INGRESAR NUEVAMENTE SU NOMBRE                                 |")
        print("=================================================================================================")
        print("=================================================================================================")
        Nombre_Usuario = input("INGRESAR SU NOMBRE DE USUARIO = ")
        print("=================================================================================================")
    #Si no exite el Nombre puede crearse la cuenta y podemos pedir ahora la Contraseña
    print("=================================================================================================")
    Contraseña_Usuario = input("INGRESAR SU CONTRASEÑA DE USUARIO = ")
    print("=================================================================================================")
    # Dicho Usuario y Contraseña van a ser agregadas a las listas
    Agregar_Usuario(Lista_Usuarios,Lista_Contraseñas,Nombre_Usuario,Contraseña_Usuario)
    return
#=================================== OPCION 3 IMPRIMIR LISTAS DE USUARIOS =========================================
def Imprimir_Listas_Usuarios(Lista_Usuarios, Lista_Contraseñas):
    print("=================================================================================================")
    print("|                                         IMPRIMIR LISTAS                                        |")
    print("=================================================================================================")
    # Vamos a recorrer ambas listas hasta el final de ellas y vamos a imprimir el contenido.
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
    #Inicializamos una varible indice en 0 para posicionarnos en el comienzo de la lista
    i = 0
    # mientras i no llegue a el fin de la lista y El Usuario sea distinto a el Usuario ingresado 
    while((i < len(Lista_Usuarios)) and (Lista_Usuarios[i] != Nombre_Usuario)):
        #Incrementamos el indice para seguir buscando se existe el Usario ingresado
        i = i + 1
    # Aca verificamos si Salimos porque llegamos al final de la lista o porque encontramos que existe
    if(i < len(Lista_Usuarios)):
        print("EL NOMBRE YA SE ENCUENTRA UTILIZANDOSE, POR FAVOR INTENTE CON OTRO NUEVO")
        return False
    print("EL NOMBRE SE ENCUENTA DISPONIBLE :) ")
    return True

def Agregar_Usuario(Lista_Usuarios,Lista_Contraseñas,Nombre_Usuario,Contraseña_Usuario):
    #Aca agregamos al final de las listas el nuevo Usuario y Contraseña 
    Lista_Usuarios.append(Nombre_Usuario)
    Lista_Contraseñas.append(Contraseña_Usuario) 
    return Lista_Usuarios,Lista_Contraseñas

def Verificacion_Menu(Valor_Mini_Interfaz):
    #Aca creamos una funcion para que si el usuario elige mal las opciones que intente nuevamente
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
    #Aca creamos una funcion para que si el usuario elige mal las opciones que intente nuevamente
    while((Menu != 1) and (Menu != 2) and (Menu != 3) and (Menu != 4) and (Menu != 5) and (Menu != Fin)):
        print("=================================================================================================")
        print("|                        INGRESASTE MAL EL VALOR DE LAS OPCIONES                                |")
        print("|                             INTENTAR NUEVAMENTE POR FAVOR                                     |")
        print("=================================================================================================")
        Menu = int (input("Ingrese la Opcion elegida: "))
    return

def Buscar_Usuario(Lista_Usuarios, Lista_Contraseñas, Nombre_Usuario, Contraseña_Usuario):
    #Inicializamos una varible indice en 0 para posicionarnos en el comienzo de la lista
    i = 0
    # mientras i no llegue a el fin de la lista y El Usuario sea distinto a el Usuario ingresado
    while ((i < len(Lista_Usuarios)) and (Lista_Usuarios[i] != Nombre_Usuario)):
        #Incrementamos el indice para seguir buscando se existe el Usario ingresado
        i = i + 1
    # Aca verificamos si Salimos porque llegamos al final de la lista o porque encontramos que existe
    if(i < len(Lista_Usuarios)):
        #Creamos una variable para guardar la posicion del Usuario para luego buscarla en la misma posicion en Contraseña
        Pos = i
        # Si es igual el valor ingresado por teclado con el valor guardado en esa posicion significa que el ingreso a sido realizado correctamente
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
    #Ingresamos por teclado en nombre del nuevo producto a agregar a las listas
    New_producto = input("Ingrese el producto: ")
    print("=================================================================================================")
    #Mientras no exista ya dicho nuevo producto va poder ingresar las veces que quiera un nuevo nombre
    while chequear_si_exsiste_producto(New_producto, Productos):
        print("=================================================================================================")
        print("|                       EL PRODUCTO YA EXISTE, INGRESE UNO NUEVO                                |")
        print("=================================================================================================")
        New_producto = input("Ingrese el producto: ")
        print("=================================================================================================")
    #Ingresamos por teclado la cantidad que va haber de este nuevo producto
    print("=================================================================================================")    
    New_cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
    print("=================================================================================================")
    #Si se ingresa una cantidad negativa no va a ser valida y tendra que ingresarlo nuevamente
    while New_cantidad <= 0:
        print("=================================================================================================")
        print("|                      CANTIDAD NO VALIDA, INGRESE UNA CANTIDAD MAYOR A 0                       |")
        print("=================================================================================================")
        New_cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
        print("=================================================================================================")
    #Ingresamos por teclado el precio de este nuevo producto
    print("=================================================================================================")
    New_precio = int(input("Ingrese el precio del producto: "))
    print("=================================================================================================")
    #Si se ingresa un precio negativo no va a de ser posible y tedra que ingresarlo nuevamente
    while New_precio < 0:
        print("=================================================================================================")
        print("|                    PRECIO NO VALIDO, INGRESE UN PRECIO MAYOR O IGUAL A 0                      |")
        print("=================================================================================================")
        New_precio = int(input("Ingrese el precio del producto: "))
        print("=================================================================================================")

    #Aca vamos a estar llamando la funcion de agregar_Producto y tambien actualizando el Stock_Total
    Stock_total = agregar_producto(New_producto, New_cantidad, New_precio, Productos, Stocks, Precios, Stock_total)
    #Aca llammos a esta funcion para ordenar dicho nuevo producto y que sea mas eficiente las busquedas despues
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
    #Ingresamos por teclado el valor, si quiere eliminar si o no un producto
    print("=================================================================================================")
    Verificar_Eliminar = int (input("Quiere eliminar un Producto 1= Si , -1 = No: "))
    print("=================================================================================================")
    #Mientras sea distinto al corte seguimos
    while(Verificar_Eliminar != Fin):
        #Ingresamos por teclado el producto que se desea eliminar
        print("=================================================================================================")
        Producto_Eliminar = (input("Ingrese el nombre del producto que desea eliminar: "))
        print("=================================================================================================")
        #Llamamos a la funcion para relizar la busqueda y si se encuntra dicho producto eliminarlo
        Borrar_Producto(Productos, Precios, Stocks, Producto_Eliminar)
        #Preguntamos si quiere eliminar otro producto o quiere volver al menu interfaz
        print("=================================================================================================")
        Verificar_Eliminar = int (input("Quiere eliminar un Producto 1= Si , -1 = No: "))
        print("=================================================================================================")
    #llamamos a imprimir stock para mostrar como a quedado luego de dicha eliminacion
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
    #Aca ingresamos por teclado el valor para elegir dentro de las opciones
    opcion = int(input("Ingrese la opción deseada: "))
    print("=================================================================================================")
    #Aca verificamos que el valor ingresado cumpla con las opciones correctas
    while opcion != 1 and opcion != 2:
        print("=================================================================================================")
        print("|                      OPCION NO VALIDA, INGRESE UNA OPCION VALIDA                              |")
        print("=================================================================================================")
        opcion = int(input("Ingrese la opción deseada: "))
        print("=================================================================================================")
    #Si ingresa 1 entra a la parte de actualizar Stock
    if (opcion == 1):
        print("=================================================================================================")
        print("|                                   ACTUALIZAR STOCK                                            |")
        print("=================================================================================================")
        #Ingresamos por teclado el producto el cual queremos actualizar el stock
        producto = input("Ingrese el producto a actualizar stock: ")
        print("=================================================================================================")
        #Verificamos que el producto ingresado exista para actualizarlo
        while not chequear_si_exsiste_producto(producto, Productos):
            print("=================================================================================================")
            print("|                  EL PRODUCTO NO EXISTE, INGRESE UN PRODUCTO VALIDO                            |")
            print("=================================================================================================")
            #Ingresa nuevamente hasta que se ingrese correctamente
            producto = input("Ingrese el producto a actualizar stock: ")
            print("=================================================================================================")
        #Ingresamos la cantidad de unidades a agregar de ese producto
        print("=================================================================================================")    
        cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
        print("=================================================================================================")
        #Verificamos que el valor ingresado no sea negativo o cero
        while cantidad <= 0:
            print("=================================================================================================")
            print("|                  CANTIDAD NO VALIDA, INGRESE UNA CANTIDAD MAYOR A 0                           |")
            print("=================================================================================================")
            #Ingresa nuevamente hasta que se ingrese correctamente
            cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
            print("=================================================================================================")
        #Llamamos la funcion actualizar para que la nueva cantidad sea ingresada
        actualizar_stock(producto, cantidad, Productos, Stocks, Stock_total)
        print("=================================================================================================")
        print("|                             STOCK ACTUALIZADO CON EXITO                                       |")
        print("=================================================================================================")
        #Llamamos a la funcion de ordenar por si lo actulizado a modicado el orden de las listas
        Ordenamiento_ListasParaleas_Burbuja(Productos, Precios,Stocks)
    #Si ingresa 2 entra a la parte de actualizar Precio
    if (opcion == 2):
        print("=================================================================================================")
        print("|                                   ACTUALIZAR PRECIO                                           |")
        print("=================================================================================================")
        #Ingresamos por teclado el producto a actualizar el precio
        producto = input("Ingrese el producto a actualizar precio: ")
        print("=================================================================================================")
        #Verificamos que dicho pruducto exista dentro de las listas
        while not chequear_si_exsiste_producto(producto, Productos):
            print("=================================================================================================")
            print("|                     EL PRODUCTO NO EXISTE, INGRESE UN PRODUCTO VALIDO                         |")
            print("=================================================================================================")
            # Ingresa nuevamente hasta que el producto sea el correcto
            producto = input("Ingrese el producto a actualizar precio: ")
            print("=================================================================================================")
        #Ingresamos por teclado el nuevo precio que va a tener el producto
        print("=================================================================================================")
        precio = int(input("Ingrese el precio del producto: "))
        print("=================================================================================================")
        #Verificamos que el precio ingresado no sea negativo ni cero
        while precio < 0:
            print("=================================================================================================")
            print("|                     PRECIO NO VALIDO, INGRESE UN PRECIO MAYOR O IGUAL A 0                     |")
            print("=================================================================================================")
            # Ingresa nuevamente hasta que el precio sea correcto
            precio = int(input("Ingrese el precio del producto: "))
            print("=================================================================================================")
        #Llamamos a la funcion actualizar_precio para genera el cambio del precio del producto
        actualizar_precio(producto, precio, Productos, Precios)
        print("=================================================================================================")
        print("|                                  PRECIO ACTUALIZADO CON EXITO                                 |")
        print("=================================================================================================")
    return
#================================================ OPCION 4 SALIDA_STOCK =============================================
def retirar_stock():
    #Declaro una variable para que el bucle comienze y lo inicializo en 1
    continuar = 1
    #Mientras continuar sea 1 el while va a seguir
    while continuar == 1:
        #Llamamos a la funcion Imprimir para ver antes cuales son los productos disponible de las listas
        IMPRIMIR_STOCK()
        #Llamamos a la funcion solicitar producto para buscar si existe dicho producto a realizar la salida
        indice_producto = solicitar_producto()
        #Llamamos a la funcion de solicitar cantidad para pedir la cantidad que se desea extraer y que cumpla con los rangos permitidos
        cantidad_extraer = solicitar_cantidad(Stocks[indice_producto])
        # Actualizamos el Stock 
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
    #Creamos una variable para tener el largo de la lista de stock
    n = len(Stocks)
    #Recorremos la lista con un indice hasta el final 
    for i in range(n):
        #Recocrremos la lista con el valor mas grande para ir llevandolo al final de la lista
        for j in range(0, n - i - 1):
            #Si el stock que vamos moviendo hacia atras es mas grande generamos el cambio
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
    #Retornamos las listas ordenadas por el Stock de menor a mayor
    return Productos, Precios, Stocks

def IMPRIMIR_STOCK():
    print("=================================================================================================")
    print("|                                   PRODUCTOS DISPONIBLES                                       |")
    print("=================================================================================================")
    print("| Producto     | Stock disponible | Precio por unidad                                           |")
    print("=================================================================================================")
    #Recorremos la listas y con la posicion de productos lo utilizamos para imprimir en las posiciones de las otras listas
    for i in range(len(Productos)):
        print(f"| {Productos[i]:<12} | {Stocks[i]:<15}  | ${Precios[i]:<20}                                       |")
    print("=================================================================================================")
    print(f"Stock total: {Stock_total} unidades ")
    return

################################### FUNCIONES DE LAS OPCIONES DEL CONTROL DE STOCK ####################################

########################################## FUNCIONES DE CONTROL DE STOCK #####################################################
################################## AGREGAR Y ACTUALIZAR PRODUCTO  ##############################################
def chequear_si_exsiste_producto(producto, productos):
    #Recorremos con un for hasta el final de la lista
    for i in range(len(productos)):
        #SI el producto en busqueda se encuentra en la lista retornamos true porque se encontro
        if producto == productos[i]:
            return True
    #Si no se encontro devolvera false
    return False

def actualizar_stock(producto, cantidad, productos, stocks, Stock_total):
    #Recorremos con un for hasta el final de la lista Productos
    for i in range(len(productos)):
        #Si el producto se encuentra en la lista: Incrementamos con la cantidad nueva al stock y stock_Total
        if producto == productos[i]:
            stocks[i] += cantidad
            Stock_total += cantidad
            print("El stock del producto: "+ productos[i] + " ha sido actualizado")

def actualizar_precio(producto, precio, productos, precios):
    #Recorremos la lista hasta el final de la lista de Productos
    for i in range(len(productos)):
        #Si se encuentra el producto en la lista se Actualiza el precio en la posicion sacada de la lista de productos en el lugar 
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

    # Se agrefa el incremento del Stock a la lista de Stock_Total
    Stock_total += New_cantidad

    print(f"El producto {New_producto} ha sido agregado al sistema")
    return Stock_total
################################## AGREGAR O ACTUALIZAR PRODUCTO  ##############################################

######################################## ELIMINAR PRODUCTOS ####################################################
def Borrar_Producto(productos, precios, stock, nombre_producto):
    #Recorre la lista de Productos hasta el final
    for i in range(len(productos)):
        #Si encuentra el producto a eliminar realiza el pop del producto con la posicion en cada una de las listas en esa posicion
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
    #Recorre la lista de Productos hasta el fianl
    for i in range(len(Productos)):
        #Si encuentra el producto a busar devuelve la posicion donde se a encontra dentro de la lista sino devuelve -1 como corte
        if Productos[i] == Producto_Buscar:
            return i
    return -1

def solicitar_producto():
    #Creamos una variable para poder entrar en el mientras, y cuando no se cumpla corta con la iteracion
    producto_valido = -1
    while producto_valido == -1:
        #Preguntamos que producto es el que desea entraer
        print("=================================================================================================")
        producto_buscado = input("| ¿Qué producto desea extraer?: ")
        print("=================================================================================================")
        #Llamamos a la variable de Buscar y verificamos que dentro
        producto_valido = Buscar_Producto(Productos, producto_buscado)
        #Si la funcion de buscar_Producto devuelve -1 significa que no se a encontra dicho producto, ingrese nuevamente
        if producto_valido == -1:
            print("=================================================================================================")
            print("| El producto ingresado es incorrecto. Intente nuevamente.                                      |")
            print("=================================================================================================")
        else:
            #la funcion duvuelve el indice y lo informa
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
