// Santiago Díaz Obando, TI 1028481987

#include <iostream>
#include <string>

using namespace std;

int main()
{
    // Declarar variables
    int f;
    string action;

    cout << "Bienvenido al ascensor del edificio." << endl;

    // Entrada del piso inicial
    cout << "Introduzca el piso en el que esta: ";
    cin >> f;

    // Verificar que sea un piso valido (1 - 25)
    if (f < 1 || f > 25) {
        cout << "No es un piso valido." << endl;
        return 0;
    }

    // Añadir posibilidad de interacción mediante un bucle
    while (true) {
        cout << "El ascensor está en el piso " << f << endl;

        // Entrada de una posible acciión del usuario
        cout << "Escriba subir, bajar o salir para realizar acciones: ";
        cin >> action;

        // Condicionales y acciones según entrada
        if (action == "subir") {
            if (f < 25) {
                cout << "Subiendo un piso..." << endl;
                f += 1;
            } else {
                cout << "Este es el último piso!" << endl;
            }
        }
        else if (action == "bajar") {
            if (f > 1) {
                cout << "Bajando un piso..." << endl;
                f -= 1;
            } else {
                cout << "Este es el primer piso!" << endl;
            }
        }
        // Si la acción es salir se rompe el ciclo
        else if (action == "salir") {
            cout << "Usted ha salido en el piso " << f << " del edificio." << endl;
            break;
        }
        // Caso por defecto
        else {
            cout << "No es una acción valida";
        }
        
    }
    
    return 0;
}