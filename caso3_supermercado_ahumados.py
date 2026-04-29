# =====================================================
# CASO 3 - EJERCICIO 2: SUPERMERCADO AHUMADOS
# Ahumados del Chocó - Sistema de facturación
# =====================================================

# =====================================================
# PRECIOS BASE (constantes)
# =====================================================
PRECIO_NORMAL  = 45000   # $/kg - Carnes normales
PRECIO_AHUMADO = 65000   # $/kg - Ahumadas especiales

# =====================================================
# BIENVENIDA
# =====================================================
print("=" * 52)
print("       BIENVENIDO A AHUMADOS DEL CHOCÓ")
print("=" * 52)

# =====================================================
# ENTRADA DE DATOS - CLIENTE
# =====================================================
nombre_cliente = input("Nombre del cliente: ")
num_compras    = int(input("Número de compras anteriores: "))

# =====================================================
# ENTRADA DE DATOS - DÍA Y HORA
# =====================================================
print("\nDía de la semana:")
print("1-Lun  2-Mar  3-Mié  4-Jue  5-Vie  6-Sáb  7-Dom")
dia  = int(input("Selecciona el día (1-7): "))
hora = int(input("Hora de la compra (0-23): "))

# =====================================================
# ENTRADA DE DATOS - PRODUCTOS
# =====================================================
print("\n--- PRODUCTOS ---")
kg_normal = float(input("Kilos de carne normal   ($45.000/kg): "))

print()
num_variedades = int(input("¿Cuántas variedades de ahumado especial compra? (0 si ninguna): "))

variedades      = []   # lista de tuplas (nombre, kilos)
kg_ahumado_total = 0.0

for i in range(num_variedades):
    nombre_var = input(f"  Nombre variedad {i + 1}: ")
    kg_var     = float(input(f"  Kilos de '{nombre_var}': "))
    variedades.append((nombre_var, kg_var))
    kg_ahumado_total += kg_var

# =====================================================
# CÁLCULO DE SUBTOTALES
# =====================================================
subtotal_normal  = kg_normal        * PRECIO_NORMAL
subtotal_ahumado = kg_ahumado_total * PRECIO_AHUMADO
kg_total         = kg_normal + kg_ahumado_total
subtotal_bruto   = subtotal_normal + subtotal_ahumado

# =====================================================
# REGALO: 2+ variedades ahumadas → 0.5 kg gratis
# =====================================================
if num_variedades >= 2:
    kg_regalo    = 0.5
    valor_regalo = kg_regalo * PRECIO_AHUMADO
else:
    kg_regalo    = 0.0
    valor_regalo = 0.0

# =====================================================
# DESCUENTOS (se aplican sobre el subtotal bruto)
# =====================================================

# 1. Paquete familiar: 5+ kg → 15%
es_paquete_familiar = kg_total >= 5
if es_paquete_familiar:
    descuento_paquete = subtotal_bruto * 0.15
else:
    descuento_paquete = 0.0

# 2. Compra total > $300.000 → 20% adicional
supera_trescientos = subtotal_bruto > 300000
if supera_trescientos:
    descuento_monto = subtotal_bruto * 0.20
else:
    descuento_monto = 0.0

# 3. Matutino: lunes–viernes (días 1–5), 10:00–14:00 → 10%
es_dia_habil    = dia >= 1 and dia <= 5
es_hora_matutina = hora >= 10 and hora < 14
es_matutino     = es_dia_habil and es_hora_matutina
if es_matutino:
    descuento_matutino = subtotal_bruto * 0.10
else:
    descuento_matutino = 0.0

# 4. Sábado: combo (3+ kg normal + ahumado) → 25%
es_sabado      = dia == 6
es_combo_sabado = es_sabado and kg_normal >= 3 and kg_ahumado_total > 0
if es_combo_sabado:
    descuento_sabado = subtotal_bruto * 0.25
else:
    descuento_sabado = 0.0

# 5. Cliente frecuente: 10+ compras → 5% permanente
es_frecuente = num_compras >= 10
if es_frecuente:
    descuento_frecuente = subtotal_bruto * 0.05
else:
    descuento_frecuente = 0.0

# =====================================================
# TOTAL FINAL
# =====================================================
total_descuentos = (descuento_paquete + descuento_monto +
                    descuento_matutino + descuento_sabado +
                    descuento_frecuente)

total_final = subtotal_bruto - total_descuentos - valor_regalo

# =====================================================
# IMPRESIÓN DE FACTURA
# =====================================================
print()
print("=" * 52)
print("          FACTURA - AHUMADOS DEL CHOCÓ")
print("=" * 52)
print(f"  Cliente           : {nombre_cliente}")
print(f"  Compras anteriores: {num_compras}")
print("-" * 52)

# --- Productos ---
print("  PRODUCTOS:")
print(f"  Carne normal  : {kg_normal:.2f} kg × $45.000 = ${subtotal_normal:>11,.0f}")

if num_variedades > 0:
    for nombre_v, kg_v in variedades:
        valor_v = kg_v * PRECIO_AHUMADO
        print(f"  {nombre_v:<14}: {kg_v:.2f} kg × $65.000 = ${valor_v:>11,.0f}")

print(f"  {'Total kilos':<30}: {kg_total:.2f} kg")
print(f"  {'SUBTOTAL BRUTO':<30}: ${subtotal_bruto:>11,.0f}")

# --- Descuentos ---
print("-" * 52)
print("  DESCUENTOS:")
hay_descuento = False

if es_paquete_familiar:
    print(f"  Paquete familiar (5+ kg)     -15%: -${descuento_paquete:>9,.0f}")
    hay_descuento = True
if supera_trescientos:
    print(f"  Compra > $300.000            -20%: -${descuento_monto:>9,.0f}")
    hay_descuento = True
if es_matutino:
    print(f"  Descuento matutino (10-14h)  -10%: -${descuento_matutino:>9,.0f}")
    hay_descuento = True
if es_combo_sabado:
    print(f"  Combo sábado (3kg+ahumado)   -25%: -${descuento_sabado:>9,.0f}")
    hay_descuento = True
if es_frecuente:
    print(f"  Cliente frecuente (10+ comp.)  -5%: -${descuento_frecuente:>9,.0f}")
    hay_descuento = True
if not hay_descuento:
    print("  Sin descuentos aplicables")

# --- Regalos ---
print("-" * 52)
print("  REGALOS:")
if kg_regalo > 0:
    print(f"  2+ variedades → 0.5 kg gratis: -${valor_regalo:>9,.0f}")
else:
    print("  Sin regalos")

# --- Total ---
print("=" * 52)
print(f"  TOTAL DESCUENTOS              : -${total_descuentos:>9,.0f}")
print(f"  TOTAL A PAGAR                 :  ${total_final:>9,.0f}")
print("=" * 52)
print("  ¡Gracias por comprar en Ahumados del Chocó!")
print("=" * 52)
