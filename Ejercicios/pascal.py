from math import factorial as fact

while True:
	try:
		n = int(input("Introduzca un número entero para mostrar las n primeras filas del triángulo de pascal: "))
		if n >= 0: break
	except Exception as e:
		print("Introduzca un número válido!")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ")

	for j in range(i+1):
		c = (fact(i)) // ((fact(j) * fact(i-j)))
		print(c, end=" ")
	print()