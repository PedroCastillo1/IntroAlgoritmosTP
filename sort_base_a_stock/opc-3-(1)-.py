"""
Tengo que hacer:
    Dos listas
        Una de producto y otra de stock
Conectarlas por la posición de producto (no me gusta la idea, siento que puede fallar)
el sort y sorted se queda
"""
"""
Remeras= 4 Pantalones= 4 Buzos= 4

"""
#listas
"""
productos =[  
    'remeras'[ "Producto A", "Producto B", "Producto C", "Producto D", "Producto E",],
    'pantalones'["Producto A,""Producto B,""Producto C,""Producto D,""Producto E,"]
]
stock=["remeras"[1,22,3,4],"pantalones"[4,2,5,7], "buzos"[33, 1 , 5, 8]]
"""
remeras=[ "Producto A", "Producto B", "Producto C", "Producto D", "Producto E",]
sremeras=[1,22,3,4]
pantalones=["Producto A","Producto B","Producto C","Producto D","Producto E",]
spantalones=[4,2,5,7]

#pnd se encarga de juntar ambas listas, se juntará los items en base a sus respectivas posiciones
pnsrem=list(zip(remeras, sremeras))
pnspan=list(zip(pantalones, spantalones))
'''
este se ecarga de ordenar los productos, serán ordenados en base al stock, e imprimidos ordenados de forma descendente 
pns= la lista zipped que junta la lista de producto y la de stocks
pnspan= zipped de pantalones y sus stock
pnrem= zipped de remeras y su stock
lamba es para no tener q escribir otro def. "x:x[1]" es para que el sort sea en base al stock, la cual es la segunda variable en las tuplas (los zip). 
'''
def ordenar(pns):
    ordenar=sorted(pns, key=lambda x: x[1]);
    for prod, stoc in pns:
        print(f"Producto: {prod}, Stock: {stoc}")
ordenar(pnsrem)
ordenar(pnspan)
