"""
Aca vamos a crear un menu interectivo donde el Usuario va a poder elegir la accion requerida en el momento.
    Las Opciones que podra elegir son las siguientes:
        - 1 = Crear Productos: (Seria crear un nuevo producto con sus demas cosas (Precio,Cantidad))
        - 2 = Eliminar Productos: (Seria Eliminar un producto con sus demas cosas (Precio,Cantidad))
        - 3 = ENTRADA DE STOCK: (Seria Actualizar/Aumentar la Cantidad de stock de los Productos (Dependiendo cual fue ingresado))
        - 4 = SALIDA DE STOCK: (Seria Actualizar/Disminuir la Cantidad de stock de los Productos (Dependidendo cuak fue ingresado))
        - 5 = STOCK_Imprirmir: (Seria Un Imprimir ENORME de todas las listas para ver los Productos,Precio,Stocks_Totales)
        - 6 = Cerrar Session: (Seria salir de este Menu Interactivo, y volver al Menu del Usuario).
"""
Fin = -1

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


Menu_Interactivo_ControlStock()
Menu = int (input("Ingrese la Opcion elegida: "))
while(Menu != Fin):
    while((Menu != 1) and (Menu != 2) and (Menu != 3) and (Menu != 4) and (Menu != 5) and (Menu != Fin)):
        print("Ingresaste mal el valor de las Opciones del Menu: ")
        Menu = int (input("Ingrese la Opcion elegida: "))



    print("Estas dentro del while y elegiste una de las opciones")
    """
        Aca van a estar los if de cada opcion que se puede elegir
        y dependiendo de la opcion elegida, se van a aplicar
        y realizaran las acciones pedidas
        
    """

    Menu_Interactivo_ControlStock()
    Menu = int (input("Ingrese la Opcion elegida: "))

print("USTED A CERRADO SESSION.")