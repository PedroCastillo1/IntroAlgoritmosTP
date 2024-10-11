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





Fin = -1




Lista_Usuarios = []
Lista_Contraseñas = []


def Crear_Usuario()
    
    return

def Ingreso_Usuario():
    Usuario = str (input("Ingresar el Nombre del Usuario: "))
    Contraseña = int (input("Ingresar la Contraseña del Usuario: "))
    #Busqueda del Usuario si Exite
    if():
        
    return 

Programa = int (input("Bienvenido, Para iniciar el programa ingrese el Valor =  1, Para Apagar el programa ingrese el valor = -1"))

while(Programa != Fin):
    print("Ingrese el Valor = 1 (Si usted ya tiene creada una cuenta).")
    print("Ingrese el valor = 2 (Si usted quiere crearse una cuenta)")
    Valor_Cuenta = int (input("INGRESE SU RESPUESTA")) 

    while((Valor_Cuenta != 1) or (Valor_Cuenta != 2))
        print("Ingresaste mal el valor de las opciones: ERROR INGRESE NUEVAMENTE EL VALOR")
        Valor_Cuenta = int (input("INGRESE SU RESPUESTA")) 

    if(Valor_Cuenta == 1):
        Ingreso_Usuario(Lista_Usuarios,Lista_Contraseñas)
    elif(Valor_Cuenta == 2):
        Crear_Usuario(Lista_Usuarios,Lista_Contraseñas)



print("Hasta luego!!, (Usted apago el programa)")