"""ELIMINAR Productos 
Pasos a REALIZAR:
Paso_1: 
    ingresar por teclado El Nombre del Producto que desea eliminar
Paso_2:
    Buscar en la lista de Productos el nombre ingresado por teclado (Recorrer la lista)
Paso_3:
    Si se encuentra, comunicar que se encontro y que se realizara la eliminacion del Producto
        - Utilizar el remove o el pop del elemento
    No se encuentra, Comunicar que no se encontro y que no se realizara la eliminacion del Producto
Paso_4:
    Imprimir la lista de Productos en caso de que se haya realizado la eliminacion
Paso_5:
    Retornar al menu del Control de Stock
"""

# listas
Productos = ["Remera", "Pantalon", "Buzo", "zapatilla"]
Precios = [10.99, 22, 30, 40]
Cant_Stock = [10, 20, 30, 40]


def Buscar_Producto(Productos,Producto_Eliminar):
    i = 0
    while ((i < len(Productos)) and (Productos[i] != Producto_Eliminar)):
        i = i + 1
    if(i < len(Productos)):
        return True
    return False

def Imprimir_Listas_Stock(Productos, Precios, Cant_Stock):
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
    for i in range(len(Cant_Stock)):
        print(Cant_Stock[i], end=" ")
    print()
    print("=================================================================================================")
    return

Imprimir_Listas_Stock(Productos, Precios, Cant_Stock)


###################################### Programa Principal #######################################################
Fin = -1
Verificar_Eliminar = int (input("Esta seguro de querer eliminar un Prducto 1= Si , -1 = No"))
while(Verificar_Eliminar != Fin):
    Producto_Eliminar = (input("Ingresar el Nombre del Producto a querer ELIMINAR"))
    if(Buscar_Producto(Productos,Producto_Eliminar)):
        print(f"Se ha encontrado dicho Producto, Vamos a ELIMNAR {Producto_Eliminar}")

