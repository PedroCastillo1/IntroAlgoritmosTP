"""Opción 1: Agregar o actualizar productos 

El usuario podrá agregar nuevos productos al sistema indicando su nombre, precio por unidad y cantidad de unidades ingresadas. 

Si el producto ya existe, solo se actualizará el número de unidades ingresadas, sumándolas a las ya existentes. 

El sistema recalculará el stock total como la diferencia entre las entradas y las salidas de cada producto."""

# listas
productos = ["Remeras","Pantalon","Buzos","Gorras","Zapatillas"]
stocks = [10,20,15,23,25]
precios = [10,22,32,14,99]


# Se pide al usuario que ingrese el producto, su precio y la cantidad de unidades ingresadas
producto = input("Ingrese el producto: ")
cantidad = int(input("Ingrese la cantidad de unidades ingresadas: "))
precio = int(input("Ingrese el precio del producto: "))


def chequear_si_exsiste_producto(producto, productos):
    for i in range(len(productos)):
        if producto == productos[i]:
            return True
    return False

def actualizar_stock(producto, cantidad, productos, stocks):
    for i in range(len(productos)):
        if producto == productos[i]:
            stocks[i] += cantidad
            print("El stock del producto: "+ productos[i] + " ha sido actualizado")

def actualizar_precio(producto, precio, productos, precios):
    for i in range(len(productos)):
        if producto == productos[i]:
            precios[i] = precio
            print("El precio del producto: "+ productos[i] + " ha sido actualizado")

def agregar_producto(producto, productos, stocks, precios, precio, cantidad):
    # Se agrega el producto a la lista de productos
    productos.append(producto)
    # Se agrega el stock a la lista de stocks
    stocks.append(cantidad)
    # Se agrega el precio a la lista de precios
    precios.append(precio)

    print(f"El producto {producto} ha sido agregado al sistema")


# Hace todo lo que se pide en la opción 1
def opcion_1(producto, productos, stocks, precios, precio, cantidad):
    if chequear_si_exsiste_producto(producto, productos):
        actualizar_stock(producto, cantidad, productos, stocks)
        actualizar_precio(producto, precio, productos, precios)
    else:   
        agregar_producto(producto, productos, stocks, precios, precio, cantidad)   
    print(productos)
    print(stocks)
    print(precios)
    
opcion_1(producto, productos, stocks, precios, precio, cantidad)
