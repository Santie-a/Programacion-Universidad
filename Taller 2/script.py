def get_input():
    """
    Función para obtener valores de usuario.
    Usa una estructura 'While True' con 'try - except' para no continuar el programa hasta que los valores introducidos sean válidos.
    """
    while True:
        try:
            annual_salary = float(input("Introduzca su salario inicial: "))
            if annual_salary > 0:
                break
            print("Los datos introducidos no son válidos!")
        except Exception as e:
            print("Introduce un valor válido!", e)

    return annual_salary

def get_months_for_part_payment(annual_salary, sem_annual_raise, portion_saved, total_cost):
    """
    Función para determinar los meses necesarios para pagar una cuota inicial del 25% del costo total, teniendo en cuenta que se tiene un incremento semestral del salario.
    """  
    # Declaración de variables y cálculos iniciales
    portion_down_payment = total_cost * 0.25
    current_savings = 0
    month_salary = annual_salary / 12
    months_before_portion = 0
    
    # Bucle para determinar la cantidad de meses que se tiene que ahorrar para pagar la cuota inicial, teniendo en cuenta un incremento semestral
    while current_savings < portion_down_payment:
        if months_before_portion % 6 == 0 and months_before_portion != 0:
            month_salary *= 1 + sem_annual_raise
        inversion_return = current_savings * 0.04/12
        current_savings += inversion_return + month_salary * portion_saved
        months_before_portion += 1

    return months_before_portion
        
def get_best_portion_saved(annual_salary, sem_annual_raise, total_cost, months_to_save):
    """
    Función que retorna la mejor taza de ahorro para pagar la una cuota del 25% del costo total, basado en el salario, incremento mensual y los meses presupuestados para el ahorro. 
    """
    # Inicialización de variables para el bucle 
    low = 0
    high = 1

    # Variable para contablizar el número de iteraciones necesarias para encontrar la taza
    steps = 0

    # Bucle para determinar la mejor taza de ahorro
    while True:
        # Taza de prueba basado en los 2 límites (inicia en 0.5 - 50%)
        portion_saved = round((high + low) / 2, 4)

        # Meses para el pago inicial basado en la taza de prueba
        months = get_months_for_part_payment(annual_salary, sem_annual_raise, portion_saved, total_cost)
        # Si los meses necesarios son menores que los pesupuestados, se puede encontrar una taza más baja
        if months < months_to_save:
            high = portion_saved
            steps += 1
        
        # Si los meses necesarios son mayores que los presupuestados, se nececita una taza más alta
        elif months > months_to_save:
            low = portion_saved
            steps += 1

        # Se rompe el bucle cuando los meses necesarios con la taza encontrada son los mismos que los meses presupuestados
        elif months == months_to_save:
            break

        if months == 1:
            return 0, 0

        # Caso especial donde los meses necesarios son siempre mayores a los presupuestados, con lo cual se retorna None para condición el el programa principal
        if low == 1.0:
            return None, None
    
    return portion_saved, steps

# Programa principal    
if __name__ == "__main__":
    # Asignación de variables, asumiendo 7% de incremento semestral, 1M de costo de la casa y 36 meses para ahorrar
    annual_salary, sem_annual_raise, total_cost, months_to_save = get_input(), 0.07, 1000000, 36

    # Encontrar la mejor taza de ahorros basada en los datos asignados
    best_portion_saved, steps = get_best_portion_saved(annual_salary, sem_annual_raise, total_cost, months_to_save)

    # Verificar si existe una taza de ahorro
    if best_portion_saved:
        print(f"Se encontró la mejor taza de ahorro mensual para {int(months_to_save / 12)} años: {best_portion_saved}, en {steps} pasos.")
    
    # Es posible pagar en un solo mes
    elif best_portion_saved == 0:
        print("La cuota inicial se puede pagar en un solo mes")

    # De lo contrario indicar que no se encontró
    else:
        print(f"No es posible pagar la cuota inicial en {int(months_to_save / 12)} años.")
