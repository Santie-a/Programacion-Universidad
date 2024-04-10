def generar_primos(n: int) -> list:
    """
    Función que genera los n primeros primos y los devuelve en forma de lista.
    """
    # Inicialización de una lista vacía y un número de prueba
    primes = list()
    test = 2

    # Bucle para encontrar los n primeros numeros primos
    while len(primes) < n:
        is_prime = True

        # Va por cada número en el rango del número. Si encuentra un divisor que sea distinto a el mismo, ya no es primo
        for i in range(2, test + 1):
            if test % i == 0 and i != test:
                is_prime = False
                break
        
        # Si la condición de primo no cambia, es primo y se agraga a la lista
        if is_prime:
            primes.append(test)
        
        # Se incrementa el número de prueba
        test += 1
        
    return primes

print(generar_primos(5))