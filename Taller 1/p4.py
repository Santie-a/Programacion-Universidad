from datetime import datetime

def saludo():
    print(
        """
Bienvenido al calculador de estadía en la zona cafetera de Colombia!
Hay 2 tipos de alojamiento:
    - Casa: 120.000 COP por noche.
    - Apartamento: 100.000 COP por noche.
Tenga en cuenta que:
    - Si es temporada alta (15 DIC - 15 ENE, 22 MAR - 31 MAR, 15 JUN - 15 JUL) se le hace un incremento del 30%.
    - Si se reserva para estancias de más de 7 noches se le hace un descuento del 15%.
    - Si se hace la reserva con 6 Meses de antelación se le hace un descuento del 10%.
        """
    )

def get_type():
    while True:
        tipo_de_estadia = input("Ingrese C para casa o A para Apartamento: ").lower()
        if tipo_de_estadia == "c" or tipo_de_estadia == "a":
            return tipo_de_estadia
        print("Introduzca una opción válida!")

def get_dates():
    while True:
        try:
            llegada = datetime.strptime(input("Introduzca la fecha de llegada al hospedaje (dd-mm-aaaa): "), "%d-%m-%Y")
            salida = datetime.strptime(input("Introduzca la fecha de salida del hospedaje (dd-mm-aaaa): "), "%d-%m-%Y")
            print(f"Usted se quedará {(salida - llegada).days} dias.")
            return (llegada, salida)
        except Exception as e:
            print(e)

def get_base_cost(tipo_de_estadia, dates):
    days = (dates[1] - dates[0]).days
    if tipo_de_estadia == "c":
        return 120000 * days
    if tipo_de_estadia == "a":
        return 100000 * days

def domingo_de_pascua(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    L = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * L) // 451
    mes = (h + L - 7 * m + 114) // 31
    dia = ((h + L - 7 * m + 114) % 31) + 1
    return dia, mes

def is_easter_day(dates):
    easter_day, easter_month = domingo_de_pascua(dates[1].year)
    easter = datetime.strptime(f"{easter_day}-{easter_month}-{dates[1].year}", "%d-%m-%Y")
    if (easter >= dates[0] and easter <= dates[1]):
        return True
    return False

def is_high_season(dates):
    if is_easter_day(dates):
        return True
    return False

def is_six_months_further(arrival_date):
    if (arrival_date - datetime.now()).days > 182:
        return True
    return False

def is_seven_days_longer(dates):
    if (dates[1] - dates[0]).days > 7:
        return True

def get_final_cost(base_cost, dates, ):
    final_cost = base_cost
    if is_high_season(dates):
        final_cost *= 1.3
    if is_seven_days_longer(dates):
        final_cost = final_cost - (final_cost * 0.15)
    if is_six_months_further(dates[0]):
        final_cost = final_cost - (final_cost * 0.1)

    return final_cost

def main():
    saludo()
    tipo_de_estadia = get_type()
    dates = get_dates()
    base_cost = get_base_cost(tipo_de_estadia, dates)
    final_cost = get_final_cost(base_cost, dates)
    if is_high_season(dates):
        print("Su viaje está en temporada alta.")
        final_cost *= 1.3
    
    print(final_cost)

main()

# Falta comprobar si se le aplican descuentos y verificar si está en temporada alta 
