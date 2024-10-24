#stock de productos
remeras=[ "Producto A", "Producto B", "Producto C", "Producto D", "Producto E",]
stock_remeras=[1,22,3,4]

pantalones=["Producto A","Producto B","Producto C","Producto D","Producto E",]
stock_pantalones=[4,2,5,7]


#El usuario debe elegir que lista desea ver.  Se debe agregar un print nuevo si se crean listas nuevas
print("1 para ver Remeras")
print("2 para ver pantalones")

lista_elegida=int(input("Elija que lista ver: "))

#Elección
# mismo caso que con los print, se agrega un nuevo elif si se crean nuevas listas
if lista_elegida==1:
    prod=remeras
    stock=stock_remeras
    print("Ordenaremos la lista Remeras")
elif lista_elegida==2:
    prod=pantalones
    stock=stock_pantalones
    print("Ordenaremos la lista Pantalones")
else:
    print("La opción que eligió es inexistente, porfavor elija una que sea válida")
    lista_elegida=int(input("Elija que lista ver: "))

#crea la lista de tupla de forma manual
tupla=[]
def crear_tupla(tuplax, producto, stonck):
    for i in range(len(stonck)):
        tuplax.append((producto[i], stonck[i]))

#ordena la lista elegida
def ordenar(arr): 
    c=len(arr)
    for a in range(c):
        for j in range(0, c-a-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]

ordenado=[]
crear_tupla(tupla, prod, stock)
ordenar(tupla)
#muestra la lista ordenada
for i in range(len(tupla)):
    ordenado.append(tupla[i])
ordenar(ordenado)
print("\nlista ordenada")
print(ordenado)
