def Ordenamiento_ListasParaleas_Burbuja(products, prices,stocks):
    n = len(prices)
    for i in range(n):
        for j in range(0, n - i - 1):
            if prices[j] > prices[j + 1]:
                # Intercambiar precios
                AUX = prices[j]
                prices[j] = prices[j + 1]
                prices[j + 1] = AUX
                # Intercambiar productos para mantener la correspondencia
                AUX = products[j]
                products[j] = products[j + 1]
                products[j + 1] = AUX
                # Intercambiar Stocks para mantener la correspondencia
                AUX = stocks[j]
                stocks[j] = stocks[j + 1]
                stocks[j + 1] = AUX

    return products, prices, stocks

# Ejemplo de uso
productos = ["Producto A", "Producto B", "Producto C"]
precios = [30, 10, 20]
stocks = [10,20,15]


print(productos)
print(precios)
print(stocks)

productos_ordenados, precios_ordenados , stocks_ordenados = Ordenamiento_ListasParaleas_Burbuja(productos, precios,stocks)

print("Productos ordenados:", productos_ordenados)
print("Precios ordenados:", precios_ordenados)
print("Stocks ordenados:", stocks_ordenados)
