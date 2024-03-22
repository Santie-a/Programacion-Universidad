# Santiago Díaz Obando, TI 1028481987 

print("Bienvenido al ascensor del edificio.")
piso = int(input("Introduzca el piso ne el que se encuentra: "))

if piso >= 1 and piso <= 25:
	if piso == 1:
		print("Usted puede únicamente SUBIR.")
		destino = int(input("Indique a qué piso desea subir: "))
		if destino > 1 and destino <= 25:
			print(f"Usted ha llegado al piso {destino}. Subió {destino - 1} piso(s).")
		elif destino == 1:
			print("Usted ha seleccionado el mismo piso.")
		else:
			print(f"No existe el piso {destino}!")
	elif piso == 25:
		print("Usted puede únicamente BAJAR.")
		destino = int(input("Indique a qué piso desea bajar: "))
		if destino >= 1 and destino < 25:
			print(f"Usted ha llegado al piso {destino}. Bajó {25 - destino} piso(s).")
		elif destino == 25:
			print("Usted ha seleccionado el mismo piso.")
		else:
			print(f"No existe el piso {destino}!")
	else:
		print("Usted puede SUBIR o BAJAR.")
		destino = int(input("Indique a qué piso desea ir: "))
		if destino >= 1 and destino <= 25:
			if destino > piso:
				print(f"Usted ha llegado al piso {destino}. Subió {destino - piso} piso(s).")
			elif destino < piso:
				print(f"Usted ha llegado al piso {destino}. Bajó {piso - destino} piso(s).")
			else:
				print("Usted ha seleccionado el mismo piso.")
		else:
			print(f"No existe el piso {destino}!")
else:
	print(f"El piso {piso} no es válido!")