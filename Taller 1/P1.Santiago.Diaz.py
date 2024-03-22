# Santiago Díaz Obando, TI 1028481987

print("Conversor de nota a letra.")

# Lectura de datos
grade = int(input("Por favor introduzca la nota (0 - 100): "))

# Asegurar que la nota este en el rango (0 - 100)
if grade >= 0 and grade <= 100:
    # Comparar para signar una letra
    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    elif grade >= 69:
        letter = "D"
    else:
        letter = "F"
    
    # Impresión de letra
    print(f"La letra para la nota de {grade} es {letter}")
else:
    print("La nota no es un valor válido")