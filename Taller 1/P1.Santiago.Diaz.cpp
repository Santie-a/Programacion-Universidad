// Santiago Díaz Obando, TI 1028481987

#include <iostream>
#include <string>

using namespace std;

int main()
{
    // Declaración de Variables
    string letter;
    int grade;

    cout<<"Conversor de nota a letra." << endl;

    // Entrada de datos
    cout<<"Por favor introduzca la nota (0 - 100): ";
    cin >> grade;

    // Asegurarse que la nota esté entre 0 y 100
    if (grade >= 0 && grade <= 100) {

        // Asignación de letra según la nota
        if (grade >= 90) {
            letter = "A";
        }
        else if (grade >= 80) {
            letter = "B";
        }
        else if (grade >= 70) {
            letter = "C";
        }
        else if (grade >= 69) {
            letter = "D";
        }
        else {
            letter = "F";
        }
        
        // Impresión de la letra
        cout << "La letra para la nota de " << grade << " es " << letter << endl;
    
    // Caso por defecto
    } else {
        cout << "La nota no es un valor válido" << endl;
    }
    

    return 0;
}