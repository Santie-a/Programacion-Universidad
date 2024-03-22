// Santiago Díaz Obando, TI 1028481987

#include <iostream>
#include <string>

using namespace std;

int main() {
	 // Declarar variables
    int piso, destino;

    cout << "Bienvenido al ascensor del edificio." << endl;

    // Entrada del piso inicial
    cout << "Introduzca el piso en el que esta: ";
    cin >> piso;

	// Verificar si el piso es valido
	if (piso >= 1 && piso <= 25) {
		// Verificar si es el primer piso
		if (piso == 1) {
			cout << "Usted puede únicamente SUBIR." << endl;
			cout << "Indique a que piso desea subir: ";
			cin >> destino;
			// Verificar si el destino es valido
			if (destino > 1 && destino <= 25) {
				cout << "Usted ha llegado al piso " << destino << ". Subio " << destino - 1 << " piso(s)." << endl;
			} else if (destino == 1) {
				cout << "Usted ha seleccionado el mismo piso." << endl;
			} else {
				cout << "No existe el piso " << destino;
			}
		// Verificar si es ultimo piso
		} else if (piso == 25) {
			cout << "Usted puede únicamente BAJAR." << endl;
			cout << "Indique a que piso desea subir: ";
			cin >> destino;
			// Verificar si el destino es valido
			if (destino >= 1 && destino < 25) {
				cout << "Usted ha llegado al piso " << destino << ". Bajo " << 25 - destino << " piso(s)." << endl;
			} else if (destino == 25) {
				cout << "Usted ha seleccionado el mismo piso." << endl;
			} else {
				cout << "No existe el piso " << destino;
			}
		} else {
			cout << "Usted puede SUBIR o BAJAR." << endl;
			cout << "Indique a que piso desea ir: ";
			cin >> destino;
			// Verificar si el destino es valido
			if (destino >= 1 && destino <= 25) {
				if (destino > piso) {
					cout << "Usted ha llegado al piso " << destino << ". Subio " << destino - piso << " piso(s)." << endl;
				} else if (destino < piso) {
					cout << "Usted ha llegado al piso " << destino << ". Bajo " << piso - destino << " piso(s)." << endl;
				} else {
					cout << "Usted ha seleccionado el mismo piso." << endl;
				}
			} else {
				cout << "No existe el piso " << destino;
			}
		}
	} else {
		cout << "El piso " << piso << " no es valido!" << endl;
	}
}