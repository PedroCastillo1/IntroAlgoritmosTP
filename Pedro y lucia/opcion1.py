"""Opción 1: Agregar o actualizar productos 

El usuario podrá agregar nuevos productos al sistema indicando su nombre, precio por unidad y cantidad de unidades ingresadas. 

Si el producto ya existe, solo se actualizará el número de unidades ingresadas, sumándolas a las ya existentes. 

El sistema recalculará el stock total como la diferencia entre las entradas y las salidas de cada producto."""

# listas
remeras = ["Remera A", "Remera B", "Remera C", "Remera D"]
sremeras = [1, 22, 3, 4]
pantalones = ["Pantalon A", "Pantalon B", "Pantalon C", "Pantalon D"]
spantalones = [4, 2, 5, 7]

# pnd se encarga de juntar ambas listas, se juntará los items en base a sus respectivas posiciones
def combine_lists(list1, list2):
    combined = []
    for i in range(len(list1)):
        combined.append((list1[i], list2[i]))
    return combined

pnspan = combine_lists(pantalones, spantalones)
pnsrem = combine_lists(remeras, sremeras)

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
    
opcion_1(producto, productos, stocks, pns)
