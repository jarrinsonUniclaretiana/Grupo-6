def calcular_factura():
    print("SUPERMERCADO AHUMADOS")

    normales = float(input("Kilos de carne normal: "))
    especiales = float(input("Kilos de carne ahumada especial: "))
    variedades = int(input("Cantidad de variedades ahumadas: "))
    compras_cliente = int(input("Cantidad de compras del cliente: "))
    dia = input("Dia de la compra (lunes, martes, miercoles, jueves, viernes, sabado): ").lower()
    hora = int(input("Hora de la compra (0-23): "))

    precio_normal = 45000
    precio_especial = 65000

    subtotal_normal = normales * precio_normal
    subtotal_especial = especiales * precio_especial
    subtotal = subtotal_normal + subtotal_especial

    descuento = 0

    total_kilos = normales + especiales
    if total_kilos >= 5:
        descuento += subtotal * 0.15

    if subtotal > 300000:
        descuento += subtotal * 0.20

    if dia in ["lunes", "martes", "miercoles", "jueves", "viernes"] and 10 <= hora < 14:
        descuento += subtotal * 0.10

    if dia == "sabado":
        descuento += subtotal * 0.25

    if compras_cliente >= 10:
        descuento += subtotal * 0.05

    total = subtotal - descuento

    regalo = 0
    if variedades >= 2:
        regalo = 0.5

    print("\nFACTURA")
    print("Kilos normales:", normales, "Subtotal:", subtotal_normal)
    print("Kilos especiales:", especiales, "Subtotal:", subtotal_especial)
    print("Subtotal total:", subtotal)
    print("Descuentos aplicados:", descuento)
    print("Regalo (kg):", regalo)
    print("TOTAL A PAGAR:", total)

calcular_factura()