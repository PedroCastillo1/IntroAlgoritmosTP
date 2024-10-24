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

Productos = ["manzana", "banana", "pera", "naranja"]
Precios = [1.0, 0.5, 1.2, 0.8] 
Stocks = [100, 150, 80, 120] 

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
        
    print(f"El producto '{nombre_producto}' no fue encontrado en la lista.")
    return

def Imprimir_Listas_Stock(Productos, Precios, Stock):
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
    return



###################################### Programa Principal #######################################################
Fin = -1
Verificar_Eliminar = int (input("Quiere eliminar un Producto 1= Si , -1 = No: "))
while(Verificar_Eliminar != Fin):
    Producto_Eliminar = (input("Ingrese el nombre del producto que desea eliminar: "))
    Borrar_Producto(Productos, Precios, Stocks, Producto_Eliminar)
    Verificar_Eliminar = int (input("Quiere eliminar un Producto 1= Si , -1 = No: "))
Imprimir_Listas_Stock(Productos, Precios, Stocks)
