// Santiago Díaz Obando, TI 1028481987

#include <iostream>
#include <string>

using namespace std;

int main() {
	 // Declarar variables
    int piso;
	string action;

    cout << "Bienvenido al ascensor del edificio." << endl;

    // Entrada del piso inicial
    cout << "Introduzca el piso en el que esta: ";
    cin >> piso;

	// Verificar si el piso es valido
	if (piso >= 1 && piso <= 25) {
		// Verificar si es el primer piso
		if (piso == 1) {
			cout << "Usted puede únicamente SUBIR." << endl;
			cout << "Escriba su accion (SUBIR): ";
			cin >> action;
			// Verificar si la accion es valida
			if (action == "SUBIR") {
				cout << "Usted ha llegado al piso " << piso + 1 << " . Subio 1 piso." << endl;
			} else {
				cout << action << " no es valida!";
			}
		// Verificar si es ultimo piso
		} else if (piso == 25) {
			cout << "Usted puede únicamente BAJAR." << endl;
			cout << "Escriba su accion (BAJAR): ";
			cin >> action;
			// Verificar si la accion es valida
			if (action == "BAJAR") {
				cout << "Usted ha llegado al piso " << piso - 1 << " . Bajo 1 piso." << endl;
			} else {
				cout << action << " no es valida!";
			}
		} else {
			cout << "Usted puede SUBIR o BAJAR." << endl;
			cout << "Escriba su accion (SUBIR, BAJAR):";
			cin >> action;
			// Verificar si la accion es valida
			if (action == "SUBIR") {
				cout << "Usted ha llegado al piso " << piso + 1 << " . Subio 1 piso." << endl;
			} else if (action == "BAJAR") {
				cout << "Usted ha llegado al piso " << piso - 1 << " . Bajo 1 piso." << endl;
			} else {
				cout << action << " no es valida!";
			}
		}
	} else {
		cout << "El piso " << piso << " no es valido!" << endl;
	}
}