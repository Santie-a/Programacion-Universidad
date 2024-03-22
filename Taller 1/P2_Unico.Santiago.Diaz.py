# Santiago Díaz Obando, TI 1028481987 

print("Bienvenido al ascensor del edificio.")
piso = int(input("Introduzca el piso ne el que se encuentra: "))

if piso >= 1 and piso <= 25:
	if piso == 1:
		print("Usted puede únicamente SUBIR.")
		acción = input("Escriba su acción (SUBIR): ")
		if acción == "SUBIR":
			print(f"Usted ha llegado al piso {piso + 1}. Subió 1 piso.")
		else:
			print(f"{acción} no es válido!")
	elif piso == 25:
		print("Usted puede únicamente BAJAR.")
		acción = input("Escriba su acción (BAJAR): ")
		if acción == "BAJAR":
			print(f"Usted ha llegado al piso {piso - 1}. Bajó 1 piso.")
		else:
			print(f"{acción} no es válido!")
	else:
		print("Usted puede SUBIR o BAJAR.")
		acción = input("Escriba su acción (SUBIR, BAJAR): ")
		if acción == "SUBIR":
			print(f"Usted ha llegado al piso {piso + 1}. Subió 1 piso.")
		elif acción == "BAJAR":
			print(f"Usted ha llegado al piso {piso - 1}. Bajó 1 piso.")
		else:
			print(f"{acción} no es válido!")
else:
	print(f"El piso {piso} no es válido!")