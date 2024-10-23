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
    producto=remeras
    stock=stock_remeras
    print("Ordenaremos la lista Remeras")
elif lista_elegida==2:
    producto=pantalones
    stock=stock_pantalones
    print("Ordenaremos la lista Pantalones")

#listas para los productos ordenados
producto_ordenado=[]
stock_ordenado=[]


#ordenar lista elegida

index_menor_stock=0
while stock:
    for i in range(len(stock)):
        if stock[i]< stock[index_menor_stock]:
            index_menor_stock=i

#agregar a la lista ordenada 
producto_ordenado.append(producto[index_menor_stock])
stock_ordenado.append(stock[index_menor_stock])


print("Productos ordenados en base al stock: ")
for a in range(len(producto_ordenado)):
    print(f"{producto_ordenado[a]}:{stock_ordenado[a]} en stock")


