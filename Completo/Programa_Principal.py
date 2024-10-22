Fin = -1

Lista_Usuarios = ["Martin","luca","Pedro","Lucia","Lautaro"]
Lista_Contraseñas = ["123","1234","12345","123456","1234567"]

# listas
productos = ["remeras", "zapatillas", "buzos", "gorras", "pantalones"]
cantidad = [30, 50, 40, 20, 10]
stock_total = 150

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
########################################## FUNCIONES DE USUARIOS #####################################################

########################################## FUNCION DE MENU INTERACTIVO ###############################################
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
    print("|                             ENTRADA DE STOCK, INGRESE EL VALOR 3                              |")
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
########################################## FUNCION DE MENU INTERACTIVO ###############################################

################################## AGREGAR O ACTUALIZAR PRODUCTO  ##############################################
# pnd se encarga de juntar ambas listas, se juntará los items en base a sus respectivas posiciones
def combine_lists(list1, list2):
    combined = []
    for i in range(len(list1)):
        combined.append((list1[i], list2[i]))
    return combined

# pnd se encarga de juntar ambas listas, se juntará los items en base a sus respectivas posiciones
pnspan = combine_lists(pantalones, spantalones)
pnsrem = combine_lists(remeras, sremeras)

def chequear_si_exsiste_producto(producto, productos):
    for i in range(len(productos)):
        # Se recorre la lista de productos en la posición i
        for j in range(len(productos[i])):
            # Si el producto ingresado es igual a un producto existente
            if producto == productos[i][j]:
                return True

def actualizar_stock(producto, cantidad, productos, stocks, pns):
    for i in range(len(productos)):
        # Se recorre la lista de productos en la posición i
        for j in range(len(productos[i])):
            # Si el producto ingresado es igual a un producto existente
            if producto == productos[i][j]:
                # Se suma la cantidad ingresada al stock existente
                stocks[i][j] += cantidad
                # Se actualiza la lista pns
                pns[i][j] = (producto, stocks[i][j])
                # Se imprime un mensaje de que el stock ha sido actualizado
                print(f"El stock de {producto} ha sido actualizado a {stocks[i][j]}")
                
def agregar_producto(producto, productos, stocks, pns):
    # Se agrega el producto a la lista de productos
    productos.append([producto])
    # Se agrega el stock a la lista de stocks
    stocks.append([cantidad])
    # Se agrega el producto y su stock a la lista pns
    pns.append(combine_lists([producto], [cantidad]))
    # Se imprime un mensaje de que el producto ha sido agregado al sistema
    print(f"El producto {producto} ha sido agregado al sistema")

# Hace todo lo que se pide en la opción 1
def opcion_1(producto, productos, stocks, pns):
    if chequear_si_exsiste_producto(producto, productos):
        actualizar_stock(producto, cantidad, productos, stocks, pns)
    else:   
        agregar_producto(producto, productos, stocks, pns)    
    print(pns)
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
    while cantidad_a_extraer > cantidad[producto] or cantidad_a_extraer < 0:
        if cantidad_a_extraer > cantidad[producto]:
            print(f"Stock insuficiente. Solo hay {cantidad[producto]} unidades de {productos[producto]}.")
        elif cantidad_a_extraer < 0:
            print("Cantidad negativa no permitida.")
        cantidad_a_extraer = int(input(f"Cantidad de {productos[producto]} a extraer (o -1 para cancelar): "))
    return cantidad_a_extraer

def mostrar_stock():
    print(f"El stock final quedó en {stock_total}.")
    for i, producto in enumerate(productos):
        print(f"La cantidad de {producto} es de {cantidad[i]}.")
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
                    # Se pide al usuario que ingrese el producto, su precio y la cantidad de unidades ingresadas
                    producto = input("Ingrese el producto: ")
                    cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
                    # Se crea una lista con los datos ingresados
                    nuevo_producto = [producto, cantidad]

                    # Se crea una lista con los productos existentes
                    productos = [remeras, pantalones]
                    # Se crea una lista con los stocks existentes
                    stocks = [sremeras, spantalones]
                    # Se crea una lista con los productos y sus stocks
                    pns = [pnsrem, pnspan]
                    # Se crea una variable para saber si el producto ya existe
                
                    opcion_1(producto, productos, stocks, pns)
                
                if(Menu == 2):
                    print("ESTA ES LA PARTE 2")
                
                if(Menu == 3):
                    print("ESTA ES LA PARTE 3")

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
                                    
                                        cantidad[producto_seleccionado] -= cantidad_a_extraer
                                        stock_total -= cantidad_a_extraer
                                        print(f"Operación confirmada. Quedan {cantidad[producto_seleccionado]} {productos[producto_seleccionado]}.")
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
