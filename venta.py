def es_venta_grande(venta):
    return venta > 20000

def analizar_ventas():
    total = 0
    cantidad_grandes = 0

    while True:
        venta = int(input("Ingrese el valor de la venta (-1 para terminar): "))

        if venta == -1:
            break

        total += venta

        if es_venta_grande(venta):
            cantidad_grandes += 1

    print("Total de ventas: $", total)
    print("Cantidad de ventas grandes:", cantidad_grandes)

# Ejecutar el programa
analizar_ventas()   
