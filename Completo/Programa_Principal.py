Lista_Usuarios = ["juan"]
Lista_Contraseñas = [123]

def Verificar_Existencia_Usuario(Lista_Usuarios,Nombre_Usuario):
    if (Nombre_Usuario in Lista_Usuarios):
        print("EL NOMBRE YA SE ENCUENTRA UTILIZANDOSE, POR FAVOR INTENTE CON OTRO NUEVO")
        return False
    else:
        print("EL NOMBRE SE ENCUENTA DISPONIBLE :) ")
        return True
    
def Imprimir_Listas_Usuarios(Lista_Usuarios, Lista_Contraseñas):
    print("=================================================================================================")
    print("|                                         IMPRIMIR LISTAS                                        |")
    print("=================================================================================================")
    print("Lista de Usuarios Registrados:")
    for usuario in Lista_Usuarios:
        print(usuario)
    print("---------------------------------------")
    print("Lista de Contraseñas Registradas:")
    for contraseña in Lista_Contraseñas:
        print(contraseña)
    print("=================================================================================================")
    return

def Agregar_Usuario(Lista_Usuarios,Lista_Contraseñas,Nombre_Usuario,Contraseña_Usuario):
    Lista_Usuarios.append(Nombre_Usuario)
    Lista_Contraseñas.append(Contraseña_Usuario) 
    return Lista_Usuarios,Lista_Contraseñas


def Verificar_Credenciales(Lista_Usuarios, Lista_Contraseñas, Nombre_Usuario, Contraseña_Usuario):
    if Nombre_Usuario in Lista_Usuarios:
        indice = Lista_Usuarios.index(Nombre_Usuario)
        return Lista_Contraseñas[indice] == Contraseña_Usuario
    return False

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

def INICIAR_SESION():
    print("=================================================================================================")
    print("|                                         INICIAR SESION                                        |")
    print("=================================================================================================")
    Intentos = 0
    Max_Intentos = 3

    Inicio = int (input("Si quiere iniciar sesion ponga 1, si quiere salir ponga -1:  "))
    while(Inicio != Fin):
        while((Inicio != 1) and (Inicio != Fin)):
            print("Ingresaste mal las opciones a elegir")
            Inicio = int (input("Si quiere iniciar sesion ponga 1, si quiere salir ponga -1"))

        print("=================================================================================================")
        Nombre_Usuario = str (input("INGRESAR SU NOMBRE DE USUARIO = "))
        print("=================================================================================================")
        print("=================================================================================================")
        Contraseña_Usuario = int (input("INGRESAR SU CONTRASEÑA DE USUARIO = "))
        print("=================================================================================================")

        while Intentos < Max_Intentos and not Verificar_Credenciales(Lista_Usuarios, Lista_Contraseñas, Nombre_Usuario, Contraseña_Usuario):
            Intentos = Intentos + 1
            if Intentos < Max_Intentos:
                print("=================================================================================================")
                print("|                   INCORRECTO, INGRESE NUEVAMENTE SU NOMBRE Y CONTRASEÑA                       |")
                print("=================================================================================================")
                Nombre_Usuario = input("INGRESAR SU NOMBRE DE USUARIO = ")
                Contraseña_Usuario = input("INGRESAR SU CONTRASEÑA DE USUARIO = ")
        if Verificar_Credenciales(Lista_Usuarios, Lista_Contraseñas, Nombre_Usuario, Contraseña_Usuario):
            print("Inicio de sesión exitoso.")
            return True
        else:
            print("=================================================================================================")
            print("|       HAS SUPERADO EL LÍMITE DE INTENTOS. ACCESO DENEGADO.                                    |")
            print("=================================================================================================")
        return False


def CREAR_SESSION():
    print("=================================================================================================")
    print("|                                         CREAR SESION                                          |")
    print("=================================================================================================")
    print("=================================================================================================")
    Nombre_Usuario = str (input("INGRESAR SU NOMBRE DE USUARIO = "))
    print("=================================================================================================")
    while not(Verificar_Existencia_Usuario(Lista_Usuarios,Nombre_Usuario)):
        print("=================================================================================================")
        print("|                                 INGRESAR NUEVAMENTE SU NOMBRE                                 |")
        print("=================================================================================================")
        print("=================================================================================================")
        Nombre_Usuario = str (input("INGRESAR SU NOMBRE DE USUARIO = "))
        print("=================================================================================================")
    print("=================================================================================================")
    Contraseña_Usuario = int (input("INGRESAR SU CONTRASEÑA DE USUARIO = "))
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

def Menu_Interactivo_ControlStock():
    print("=================================================================================================")
    print("|                                      CONTROL DE STOCKS                                        |")
    print("=================================================================================================")
    print("=================================================================================================")
    print("|                             CREAR PRODUCTO, INGRESE EL VALOR 1                                |")
    print("=================================================================================================")
    print("=================================================================================================")
    print("|                             ELIMINAR PRODUCTO, INGRESE EL VALOR 2                             |")
    print("=================================================================================================")
    print("=================================================================================================")
    print("|                             ENTRADA DE STOCK, INGRESE EL VALOR 3                              |")
    print("=================================================================================================")
    print("=================================================================================================")
    print("|                             SALIDA DE STOCK, INGRESE EL VALOR 4                               |")
    print("=================================================================================================")
    print("=================================================================================================")
    print("|                             STOCK A IMPRIMIR, INGRESE EL VALOR 5                              |")
    print("=================================================================================================")
    print("=================================================================================================")
    print("|                     SI USTED QUIERE TERMINAR EL PROGRAMA, INGRESE EL VALOR -1                 |")
    print("=================================================================================================")
    return
################################## AGREGAR O ACTUALIZAR PRODUCTO  ##############################################
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
    pns.append(list(zip([producto], [cantidad])))
    # Se imprime un mensaje de que el producto ha sido agregado al sistema
    print(f"El producto {producto} ha sido agregado al sistema")

# Se recorre la lista de productos
def opcion_1(producto, productos, stocks, pns):
    if chequear_si_exsiste_producto(producto, productos):
        actualizar_stock(producto, cantidad, productos, stocks, pns)
    else:   
        agregar_producto(producto, productos, stocks, pns)    
    print(pns)
################################## AGREGAR O ACTUALIZAR PRODUCTO  ##############################################






######################################################             PROGRAMA PRINCIPAL             #####################################################################################
Fin = -1

# listas
remeras = ["Remera A", "Remera B", "Remera C", "Remera D"]
sremeras = [1, 22, 3, 4]
pantalones = ["Pantalon A", "Pantalon B", "Pantalon C", "Pantalon D"]
spantalones = [4, 2, 5, 7]

# pnd se encarga de juntar ambas listas, se juntará los items en base a sus respectivas posiciones
pnsrem = list(zip(remeras, sremeras))
pnspan = list(zip(pantalones, spantalones))

Menu_Interactivo_GestionUsuario()
print("=================================================================================================")
Valor_Mini_Interfaz = int (input("INGRESAR SU VALOR POR FAVOR = "))
print("=================================================================================================")

while(Valor_Mini_Interfaz != Fin):
    Verificacion_Menu(Valor_Mini_Interfaz)


    if(Valor_Mini_Interfaz == 1):   
        while(INICIAR_SESION()):
            Menu_Interactivo_ControlStock()
            Menu = int (input("Ingrese la Opcion elegida: "))
            while(Menu != Fin):
                while((Menu != 1) and (Menu != 2) and (Menu != 3) and (Menu != 4) and (Menu != 5) and (Menu != Fin)):
                    print("Ingresaste mal el valor de las Opciones del Menu: ")
                    Menu = int (input("Ingrese la Opcion elegida: "))

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
                    existe = False
                    # Se crea una variable para saber la posición del producto en la lista
                    pos = 0
                    opcion_1(producto, productos, stocks, pns)
                
                if(Menu == 2):
                    print("ESTA ES LA PARTE 2")
                
                if(Menu == 3):
                    print("ESTA ES LA PARTE 3")

                if(Menu == 4):
                    print("ESTA ES LA PARTE 4")

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
