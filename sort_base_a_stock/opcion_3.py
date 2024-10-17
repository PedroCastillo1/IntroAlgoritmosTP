
productos = [
    {"nombre": "Producto A", "stock": 20},
    {"nombre": "Producto B", "stock": 5},
    {"nombre": "Producto C", "stock": 15},
    {"nombre": "Producto D", "stock": 0},
    {"nombre": "Producto E", "stock": 3},
]

P_ordenados= sorted(productos, key=lambda x: x['stock'])

print('Lista de productos ordenados: ')
for producto in P_ordenados:
    print(f"'nombre: '{producto['nombre']}, 'Stock: '{producto['stock']}")
