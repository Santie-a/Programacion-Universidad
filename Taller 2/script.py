def get_input():
    # Estructura 'While True' con 'try - except' para no continuar el programa hasta que los valores introducidos sean válidos
    while True:
        try:
            annual_salary = float(input("Introduzca su salario anual: "))
            sem_annual_raise = float(input("Introduzca el porcentaje de aumento semestral en su salario, en decimal: "))
            total_cost = float(input("Introduzca el valor de su casa soñada: "))
            months_to_save = int(input("Introduzca el número de meses que tiene como objetivo para comprar la casa: "))
            if annual_salary > 0 and sem_annual_raise > 0 and total_cost > 0 and months_to_save > 0:
                break
            print("Los datos introducidos no son válidos!")
        except Exception as e:
            print("Introduce un valor válido!", e)

    return annual_salary, sem_annual_raise, total_cost, months_to_save

def get_months_for_part_payment(annual_salary, sem_annual_raise, portion_saved, total_cost):    
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
    lower = 0
    high = 1
    while True:
        portion_saved = (high - lower) / 2
        months = get_months_for_part_payment(annual_salary, sem_annual_raise, portion_saved, total_cost)
        if months > months_to_save:
            high /= 2
        
        break # Falta añadir la logica para encontrar la mejor taza de ahorro
    
if __name__ == "__main__":
    annual_salary, sem_annual_raise, total_cost, months_to_save = get_input()
    best_portion_saved = get_best_portion_saved(annual_salary, sem_annual_raise, total_cost, months_to_save)