# Santiago Díaz Obando, TI 1028481987

print("Bienvenido al ascensor del edificio.")

# Entrada y su verificación en el rango del edificio (Bucle hasta que se cumpla)
while True:
    floor = int(input("Introduzca en qué piso está: "))
    if floor >= 1 and floor <= 25:
        break
    else:
        print("El piso no es válido.")

# Añadir posibilidad de interacción mediante un bucle
while True:
    print(f"El ascensor está en el piso {floor}")

    # Lectura de posible acción
    action = input("Escriba subir, bajar o salir para realizar acciones: ").lower()

    # Verificar si es una acción válida y mover el ascensor
    if action == "subir":
        if floor < 25:
            print("Subiendo un piso...")
            floor += 1
        else:
            print("Este es el último piso!")
    elif action == "bajar":
        if floor > 1:
            print("Bajando un piso...")
            floor -= 1
        else:
            print("Este es el primer piso!")

    # Acción para romper el bucle
    elif action == "salir":
        print(f"Usted ha salido en el piso {floor} del edificio.")
        break

    # Caso por defecto
    else:
        print("Introduzca una acción válida.")
    
    print(" ")