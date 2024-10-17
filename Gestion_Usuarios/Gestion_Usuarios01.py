"""
Aca lo que vamos a programar es el interfaz de Gestion de Usuarios
    -Se necesitan las listas de Usuarios y Contraseñas
        -De estas listas van a tener que existir las Funciones (Agregar_Usuario,Eliminar_Usuario,Buscar_Usuario,Ordenar_Usuario)
        -De estas listas van a tener que existir las Funciones (Agregar_Contraseña,Eliminar_Contraseña,Buscar_Contraseña,Ordenar_Contraseña)

    1- Como primera parte Vamos a preguntar a el Usuario que ingrese su cuenta o sino tiene, que se cree una.

    -Dentro de ese mini interfaz, Vamos a crear 3 opciones (Ingresar_Session  -  Crear_Cuenta  -  Borrar_Cuenta)
    (Verificamos que dentro del interfaz de Usuario que no halla ingresado mal el valor de opciones,en caso contrario que los ingrese nuevamente)

        -Ingresar_Session: 1 Opcion
            -Le vamos a pedir al Usuario que ingrese su nombre
            -Le vamos a pedir al Usuario que ingrese su Contraseña
            -Verificamos que dicho Usuario con su Contraseña Exista 
                * Funcion de Verificar_Usuario
                    - Va a recorrer en busqueda del Nombre del Usuario en la lista de Nombres_Usuarios y Va a devolver la Posicion del Nombre
                        -Si no encuentra el nombre va a retornar en la posicion -1  (Generando un corte y Comunicando un ERROR)
                -Si la verificacion da CORRECTO ingresas a la siguiente interfaz que ya es el programa de CONTROL DE STOCKS
                -Si la verificacion de INCORRECTO while(Tenes 3 intentos para volver a Ingresar_Session) sino se termina el programa.
        
        -Crear_Cuenta: 2 Opcion
            -Le vamos a pedir al Usuario que ingrese su NUEVO nombre
            -Le vamos a pedir al Usuario que ingrese su NUEVA Contraseña
            -Verificamos que dicho Usuario nuevo no este duplicado
                * Funcion de Verificar_Duplicado
                    -Va a recorrer la lista de Nombres_Usuarios y va a ir comparando uno por uno si el Nuevo nombre es igual a alguno ya de la lista
                    -si existe un nombre ya dentro de la lista de Nombres_Usuarios (Tendra que ingresar un Distinto Nombre ya que ese ya existe, que lo intente las veces que quiera)
                    -NO existe ese nombre dentro de la lista de Nombres_Usuarios tendra que hacer las siguientes cosas:
            -Llamar a la Funcion de Agregar_Usuario:
                * Funcion de Agregar_Usuario:
                    -Va a agregar dentro de la lista de Nombres_Usuarios el nuevo dato (ej =  Nombres_Usuarios.append (Nombre_Nuevo)  )
                    -Va a agregar dentro de la lista de Contraseña_Usuarios el nuevo dato (ej =  Contraseñas_Usuarios.append (Contraseña_Nueva)  )
            -Llamar a la Funcion de Ordenar_Usuarios
                *  Funcion de Ordenar_Usuarios:
                    - Va a recorrer la lista de Nombres y va a ir comparando en Orden alfabetico si es mayor o no al nuevo nombre
                    - Cuando encuentre en lugar a insertar, Generar un corrimiento de los demas elementos y Se guardara en una variable la Posicion donde fue guardado dicho nombre
                    - Va a recorrer la lista de Contraseñas y va a ir a la Posicion guardada de la lista de nombres y va generar un corrimiento de los demas elementos
                     (Significa que incrementaria la Dimencion_Logica de la lista y incrementaria la posicion de los elementos desde la Posicion del nuevo dato)
            -Damos como finalizado la creacion de la Nueva_Cuenta y nos dirigimos a la mini interfaz nuevamente.

        - Borrar_Cuenta: 3 Opcion
            -Verificamos con una Contraseña si tiene permisos para poder borrar una cuenta.
                -Si no es correcta (Tiene 3 intentos y sino lo devuelve a la Mini interfaz)
                -Si es correcto procede a pedirle los datos para realizar la eliminacion de la cuenta
            -Le vamos a pedir al Usuario que ingrese el Nombre a Borrar
            -Le vamos a pedir al Usuario que ingrese la Contraseña a Borrar
            -Verificamos que dicho Usuario Exista 
                * Funcion de Verificar_Usuario
                    - Va a recorrer en busqueda del Nombre del Usuario en la lista de Nombres_Usuarios y Va a devolver la Posicion del Nombre
                        -Si no encuentra el nombre va a retornar en la posicion -1  (Generando un corte y Comunicando un ERROR) - (Significa que no existe dicho Usuario y no puede ser borrado)
            -Llamar a la Funcion de Borrar_Cuenta
                -Si lo encuentra procede a borrarlo:
                * Funcion de Eliminar_Usuario
                     -Va a Eliminar dentro de la lista de Nombres_Usuarios el Nombre ingresado (ej =  Nombres_Usuarios.remove(Nombre_a_Borrar)  )
                * Funcion de Eliminar_Contraseña
                     -Va a Eliminar dentro de la lista de Contraseñas_Usuarios la Contraseña ingresada (ej =  Contraseñas_Usuarios.remove(Contraseña_a_Borrar)  )
            -Damos como finalizado la Eliminacion de la  Cuenta de Usuario y nos dirigimos a la mini interfaz nuevamente.                                                                       
"""

Lista_Usuarios = ["juan"]
Lista_Contraseñas = [123]

def Verificar_Existencia_Usuario(Lista_Usuarios,Nombre_Usuario):
    if (Nombre_Usuario in Lista_Usuarios):
        print("EL NOMBRE YA SE ENCUENTRA UTILIZANDOSE, POR FAVOR INTENTE CON OTRO NUEVO")
        return False
    else:
        print("EL NOMBRE SE ENCUENTA DISPONIBLE :) ")
        return True
    
def Imprimir_Listas(Lista_Usuarios, Lista_Contraseñas):
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
    else:
        print("=================================================================================================")
        print("|       HAS SUPERADO EL LÍMITE DE INTENTOS. ACCESO DENEGADO.                                    |")
        print("=================================================================================================")
    return 


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

######################################################             PROGRAMA PRINCIPAL             #####################################################################################
Fin = -1

Menu_Interactivo_GestionUsuario()

print("=================================================================================================")
Valor_Mini_Interfaz = int (input("INGRESAR SU VALOR POR VAFOR = "))
print("=================================================================================================")

while(Valor_Mini_Interfaz != Fin):
    Verificacion_Menu(Valor_Mini_Interfaz)

    if(Valor_Mini_Interfaz == 1):   
        INICIAR_SESION()

    if(Valor_Mini_Interfaz == 2):
        CREAR_SESSION()
      
    if(Valor_Mini_Interfaz == 3):
        Imprimir_Listas(Lista_Usuarios, Lista_Contraseñas)  

    Menu_Interactivo_GestionUsuario()
    
    print("=================================================================================================")
    Valor_Mini_Interfaz = int (input("INGRESAR SU VALOR POR VAFOR = "))
    print("=================================================================================================")
        

print("USTED A FINALIZADO EL PROGRAMA, HASTA LUEGOO")
######################################################             PROGRAMA PRINCIPAL             #####################################################################################












































