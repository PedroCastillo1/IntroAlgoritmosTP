productos = ["remeras", "zapatillas", "buzos", "gorras", "pantalones"]
cantidad = [30, 50, 40, 20, 10]
stock_total = 150
 
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