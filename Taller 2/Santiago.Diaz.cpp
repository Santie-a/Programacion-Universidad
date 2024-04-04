// Santiago Díaz Obando, TI 1028481987

// Programa para calcular la mejor taza de ahorro para 36 meses para para pagar la una cuota inicial de 25% de una casa de 1M, teniendo en cuenta inversiones de 4% anual y un incremento del 7% semestral

#include <iostream>
#include <limits>
#include <cmath>
#include <string>
using namespace std;


// Función para obtener entrada correcta del usuario sin terminar el programa (La entrada tiene que ser mayor que 11, ya que entre 1 y 11  no avanza el programa).
long int get_input()
{
  	string input;
 	while (true)
	{
	    	cout << "Introduzca su salario inicial: ";
	    	getline(cin, input);
	
	    	// Validar la entrada
	    	bool valid = true;
	    	for (char c : input)
		{
			if (!isdigit(c))
			{
	        		valid = false;
	        		break;
			}
	    	}	
	
	    	if (valid)
			{
	      		long int annual_salary = stol(input, nullptr, 0);
	      		if (annual_salary > 11)
			{
	        		return annual_salary;
	      		}
	    	}
	
	    	std::cout << "Entrada no válida. Inténtalo de nuevo." << std::endl;
	}
}


// Función para determinar los meses necesarios para pagar una cuota inicial del 25% del costo total, teniendo en cuenta que se tiene un incremento semestral del salario.
int get_months_for_part_payment(long int annual_salary, float sem_annual_raise, float portion_saved, long int total_cost)
{
	// Declaración de variables y cálculos iniciales
	double portion_down_payment = total_cost * 0.25;
	double current_savings = 0;
	double month_salary = annual_salary / 12;
	double inversion_return;
	int months_before_portion = 0;

	// Bucle para determinar la cantidad de meses que se tiene que ahorrar para pagar la cuota inicial, teniendo en cuenta un incremento semestral
	while (current_savings < portion_down_payment)
	{
		if ((months_before_portion % 6 == 0) && (months_before_portion != 0))
		{
			month_salary *= 1 + sem_annual_raise;
		}
		inversion_return = current_savings * 0.04/12;
		current_savings += inversion_return + month_salary * portion_saved;
		months_before_portion++;		
	}
	return months_before_portion;
}


// Función que retorna la mejor taza de ahorro para pagar la una cuota del 25% del costo total, basado en el salario, incremento mensual y los meses presupuestados para el ahorro.
pair<double, int> get_best_portion_saved(long int annual_salary, float sem_annual_raise, long int total_cost, int months_to_save)
{
	// Inicialización de variables para el bucle
	int months;
	double portion_saved;
	double low = 0;
	double high = 1;

	// Variable para contablizar el número de iteraciones necesarias para encontrar la taza
	int steps = 0;

	// Bucle para determinar la mejor taza de ahorro
	while (true)
	{
		// Taza de prueba basado en los 2 límites (inicia en 0.5 - 50%)
		portion_saved = round(((high + low) / 2) * 10000) / 10000.0;

		// Meses para el pago inicial basado en la taza de prueba
		months = get_months_for_part_payment(annual_salary, sem_annual_raise, portion_saved, total_cost);

		// Si los meses necesarios son menores que los pesupuestados, se puede encontrar una taza más baja
		if (months < months_to_save)
		{
			high = portion_saved;
			steps++;
		}

		// Si los meses necesarios son mayores que los presupuestados, se nececita una taza más alta
		else if (months > months_to_save)
		{
			low = portion_saved;
			steps++;
		}

		// Se rompe el bucle cuando los meses necesarios con la taza encontrada son los mismos que los meses presupuestados
		else if (months == months_to_save)
		{
			break;
		}
		
		// Caso especial
		if (months == 1)
		{
			return make_pair(0, 0);
		}

		// Caso especial donde los meses necesarios son siempre mayores a los presupuestados, con lo cual se retorna -1 para condición el el programa principal
		if (low == 1.0)
		{
			return make_pair(-1, 0);
		}
		
	}
	
	return make_pair(portion_saved, steps);
}


// Programa principal
int main()
{
	// Entrada del usuario
	long int annual_salary = get_input();

	// Encontrar la mejor taza de ahorros, asumiendo 7% de incremento semestral, 1M de costo de la casa y 36 meses para ahorrar
	pair<double, int> data = get_best_portion_saved(annual_salary, 0.07, 1000000, 36);
	double best_portion_saved = data.first;
	int steps = data.second;

	// Verificar si existe una taza de ahorro
	if (best_portion_saved > 0)
	{
		cout << "Se encontró la mejor taza de ahorro mensual para 3 anios: " << best_portion_saved << " en " << steps << " pasos.";
	}

	// El salario es demasiado alto para el calculo
	else if (best_portion_saved == 0)
	{
		cout << "El salario es demasiado alto! Seguramente se puede pagar la cuota inicial en un mes.";
	}

	// De lo contrario indicar que no se encontró
	else
	{
		cout << "No es posible pagar la cuota inicial en 3 anios.";
	}
	return 0;
}
