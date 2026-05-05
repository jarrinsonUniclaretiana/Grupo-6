sexo = input("Sexo (H/M): ")
hemo = float(input("Hemoglobina: "))
glucosa = float(input("Glucosa: "))
colesterol = float(input("Colesterol: "))

# Hemoglobina
if sexo == "H":
    if hemo < 12:
        estado_hemo = "Patológico"
    elif hemo >= 13.5 and hemo <= 17.5:
        estado_hemo = "Normal"
    else:
        estado_hemo = "Alerta"
else:
    if hemo < 11:
        estado_hemo = "Patológico"
    elif hemo >= 12 and hemo <= 15.5:
        estado_hemo = "Normal"
    else:
        estado_hemo = "Alerta"

# Glucosa
if glucosa < 100:
    estado_glucosa = "Normal"
elif glucosa <= 125:
    estado_glucosa = "Alerta"
else:
    estado_glucosa = "Patológico"

# Colesterol
if colesterol < 200:
    estado_col = "Normal"
elif colesterol <= 239:
    estado_col = "Alerta"
else:
    estado_col = "Patológico"

# Mostrar resultados
print("\nResultados:")
print("Hemoglobina:", estado_hemo)
print("Glucosa:", estado_glucosa)
print("Colesterol:", estado_col)

# Alerta combinada
if sexo == "H" and hemo < 12 and glucosa > 126:
    print("Alerta combinada")
elif sexo == "M" and hemo < 11 and glucosa > 126:
    print("Alerta combinada")

# Recomendaciones específicas
print("\nRecomendaciones:")

if estado_hemo == "Patológico":
    print("- Revisar hemoglobina (posible anemia)")
elif estado_hemo == "Alerta":
    print("- Hemoglobina en rango de alerta, se recomienda control")

if estado_glucosa == "Patológico":
    print("- Glucosa elevada (posible diabetes), consultar médico")
elif estado_glucosa == "Alerta":
    print("- Glucosa en rango de prediabetes, mejorar hábitos alimenticios")

if estado_col == "Patológico":
    print("- Colesterol alto, reducir consumo de grasas saturadas")
elif estado_col == "Alerta":
    print("- Colesterol en límite alto, vigilar dieta")

print("\nNota: Estos son rangos de referencia del Laboratorio Clínico Quibdó.")

input("\nPresiona ENTER para salir...")