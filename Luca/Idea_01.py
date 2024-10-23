"""
Desarrollar un programa en Python que permita la gestión de un sistema de stock para una tienda,
donde los usuarios puedan agregar productos,
registrar entradas y salidas de stock,
y visualizar el stock total de cada producto de manera ordenada. 

"""
# Lo que podemos hacer es que el sistema de control de stock sea de un local de ropa

"""
Inicialización del sistema: 

Se deberán crear cinco listas que almacenarán los siguientes datos: 

1- productos: nombres de los productos que se manejarán en el sistema. 

2- precios: precios por unidad de cada producto. 

3- entradas: cantidad de unidades ingresadas para cada producto. 

4- salidas: cantidad de unidades vendidas o retiradas para cada producto. 

5- stock_total: cantidad total de unidades disponibles de cada producto (calculada como la diferencia entre entradas y salidas). 

"""
#Para la lista de Productos podemos tener Productos = ["Remeras", "Pantalones", "camperas", "buzos", "zapatos"] .etc

#Para la lista de Precios supongo que se pondra asi? Precios = [12.99 , 22.99 , 31.99 , 40 , 100]. etc
#Supongo que podemos buscar el precio del producto comparando las posiciones de las listas. (Despues lo vemos)

#Para la lista de Entrada supomgo que es algo que nosotros pedimos como una variable
#O capaz que haya la opcion de sacar varios productos distintos y ahi necesitemos de las listas (DEBATE)

#Para la lista de Salida supongo que lo mismo que entrada (DEBATE)

#Para la lista de Stock_TOTAL supongo que seria asi Stock_Total = [12, 32, 23, 79]. etc

#Que el programa tenga una section donde puedas comunicarte con el provedor y si hay productos para ingresar o no.

#Que el programa tenga una section donde puedas eliminar del stock los productos vendidos y actualizar las listas.

#Hay que mantener actualizado las cantidades de cada producto. y que tenga verificaciones de cuantos hay por hay una compra grande y si cumple con el stock almacenado

"""
Funcionalidades principales del sistema: El programa deberá ofrecer las siguientes opciones: 

Opción 1: Agregar o actualizar productos 

    El usuario podrá agregar nuevos productos al sistema indicando su nombre, precio por unidad y cantidad de unidades ingresadas. 

    Si el producto ya existe, solo se actualizará el número de unidades ingresadas, sumándolas a las ya existentes. 

    El sistema recalculará el stock total como la diferencia entre las entradas y las salidas de cada producto. 

Opción 2: Registrar salida de productos 

    El usuario podrá registrar la salida de unidades de un producto (por ejemplo, ventas o retiros de stock). 

    El sistema validará que la cantidad a retirar no exceda el stock disponible, mostrando un mensaje de error si esto ocurre. 


"""

#El AGREGAR O ACTUALIZAR PRODUCTOS
    #Requiere de las listas de Productos,Precio,Entrada y Stock_Total
    #Productos porque si agregamos un nuevo producto necesitamos el nombre dentro de la lista
    #Precio porque si agregamos un nuevo producto nevcesita un precio para poderle cobrar al cliente
    #Entrada porque en ese mismo momento le estamos ingresando la cantidad de productos que hay
    #Stock_total porque hay que tener actualizado el stock que tenemos de todos los productos

#El REGISTRAR SALIDA DE PRODUCTOS
    #Requiere de las listas Productos,Salida y Stock_Total
    #Prodcuto porque necesitamos el nombre del producto a sacar y de ahi buscarlo en la lista
    #Salida porque nosotros vamos a pedirle una cantidad especifica de productos a sacar
    #Stock_Total porque vamos a verificar que lo pedido esta para sacar y en caso contrario que lo vuelva a intentar o otra cosa

"""
Opción 3: Mostrar stock total y ordenado 

    El sistema mostrará el listado de productos con su stock total disponible, ordenado de menor a mayor cantidad de unidades. 

Opción 4: Salir 

    El usuario podrá salir del programa cuando lo desee. 

"""

#MOSTRAR STOCK TOTAL
    #Hay que siempre mantener el orden de la lista
    #Si se ingresa nuevos productos o es modificada las cantidades por entrada o salida. todo tiene que mantener su orden
    #Necesitaremos una funcion que actualice el orden cada vez que se haga algun cambio.
    #Tiene que haber una funcion que sea Mostrar Stock y que solo la recorra y imprima en pantalla los datos
    #Hay que pensarlo bien eso asi muestra el nombre de cada producto con su correspondiente stock

#SALIDA DEL PROGRAMA DEL USUARIO
    #Podemos recrear un menu donde por medio de que numero ponga dentro del rango de opciones
    #pueda hacer determinada accion
    #supongamos que quiere agrergar buen que aprete el 1. y una vez finalizado lo devuelva al menu
    #Y que si quiere salir del menu (Salir del programa o mandarlo a ingreso de usuario) sea otro numero

"""
Requerimientos específicos: 

    Se debe implementar una función de búsqueda que permita encontrar si un producto ya existe en la lista. 

    Se debe implementar un algoritmo de ordenamiento por selección para mostrar el stock total de cada producto de menor a mayor. 

    Se deberán manejar entradas inválidas, como intentar registrar una salida mayor a la cantidad de stock disponible. 
"""

#BUSQUEDA
    #Es una funcion que recorra la lista verificando si encuentra el producto
    #Si lo encuentra retorna true
    #No lo encuentra retorna false
    #Fuera de la funcion notifica que el producto no fue encontrado

#ORDEN STOCK
    #Se va a tener que recorrer la lista de manera eficiente (existen varias formas)
    #SE va a tener que ir ubicando a medida que se encuentre un mayor stock de un producto adelante hasta el final de la lista

#SALIDAS O ENTRADAS INVALIDAD
    #Vamos a crear una funcion que verifique si la cantidad de productos a ingresar es la correcta por el espacio o no
    #Vamos a crear una funcion que verifique si la cantidad de productos es la correcta pedida para sacar del stock


"""
Formato del programa: 

El programa se ejecutará mediante un menú interactivo que permitirá al usuario seleccionar las opciones mediante números. 

El programa deberá funcionar de forma continua hasta que el usuario elija la opción de salida. 
"""

#El usuario a usar el programa sea el que trabaja en el lugar
#que haya antes de todo el programa una parte de seguridad al programa, (Usuario y contrasenia)

#MENU INTERACTIVO
    #Que luego del ingreso al programa exita un menu donde eliga dentro de una rango (ej = 1-5)
    #Las opciones que quiera realizar (1= Agrear 2= Ordenar 3=Salida_Productos).etc

    #Tiene que haber una de las opcione donde pueda cerrar sesion y que pueda tambien despues de eso terminar el programa

"""
Ejemplo de funcionamiento: 

    1- El usuario selecciona la opción "1. Agregar o actualizar producto":

        Se ingresa el nombre del producto, el precio por unidad y la cantidad de unidades ingresadas. 

        Si el producto ya existe, se actualiza la cantidad de unidades.  


    2- El usuario selecciona la opción "2. Registrar salida de producto": 

        Se ingresa el nombre del producto y la cantidad de unidades que se desea registrar como salidas. 

        Si no hay suficiente stock, el programa debe notificar al usuario. 



    3- El usuario selecciona la opción "3. Mostrar stock total y ordenado": 

        Se muestra un listado de todos los productos, con su cantidad de stock disponible, ordenado de menor a mayor. 

    4- El usuario selecciona la opción "4. Salir": 

        El programa finaliza. 

"""



"""
Pautas de evaluación 

    El trabajo se evaluará en base a los siguientes criterios: 

    Correcta implementación de las funciones requeridas. 

    Organización y legibilidad del código. 

    Manejo adecuado de los datos (listas y condiciones). 

    Aplicación correcta de los datos solicitados. 

    Funcionalidad completa según las especificaciones. 
"""