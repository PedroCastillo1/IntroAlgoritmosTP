#Listas 
Productos = ["Remeras","Pantalon","Buzos","Gorras","Zapatillas"]
Stocks = [30,25,15,60,25]
Precios = [10,22,32,14,99]
Stock_total = 93

def Buscar_Usuario(Lista_Usuarios, Lista_Contraseñas, Nombre_Usuario, Contraseña_Usuario):
    i = 0
    while ((i < len(Lista_Usuarios)) and (Lista_Usuarios[i] != Nombre_Usuario)):
        i = i + 1
    if(i < len(Lista_Usuarios)):
        Pos = i
        if Lista_Contraseñas[Pos] == Contraseña_Usuario:
            return True
    return False

def Buscar_Producto(Productos,Producto_Buscar):
    i = 0
    while ((i < len(Productos)) and (Productos[i] != Producto_Buscar)):
        i = i + 1
    if(i < len(Productos)):
        print("Se ha encontrado el Producto")
        return True
    print("No se ha encontrado el Producto")
    return False

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


#================================================ OPCION 4 SALIDA_STOCK =============================================
def SALIDA_STOCK():
    pregunta = int(input("¿Quiere retirar un producto? Pulse 1 para iniciar y -1 para finalizar: "))

    while pregunta != -1:
        print("Opción no válida.")
        pregunta = int(input("¿Quiere retirar un producto? Pulse 1 para iniciar y -1 para finalizar: "))

    Producto_Buscar = (input("¿Qué producto desea extraer?: "))
    if(Buscar_Producto(Productos,Producto_Buscar)):
        seleccionar_cantidad(Productos)
    else:
        print("El producto que ingresaste es incorrecto")
    




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
                stock_total -= cantidad_a_extraer
                print(f"Operación confirmada. Quedan {Stocks[producto_seleccionado]} {Productos[producto_seleccionado]}.")
                pregunta = int(input("¿Quiere retirar otro producto? Pulse 1 para continuar y -1 para finalizar: "))
    mostrar_stock()
    return
#================================================ OPCION 5 STOCK A IMPRIMIR =============================================


SALIDA_STOCK()