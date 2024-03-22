#include <iostream>
#include <cmath>
#include <string>

using namespace std;

string to_binary(int base_10) {
    string binary;
    if (base_10 == 0) {
        return "0";
    }
    while (base_10 > 0) {
        binary = to_string(base_10 % 2) + binary;
        base_10 = base_10 / 2;
    }
    return binary;
}

int to_decimal(string base_2) {
    int base_10 = 0;
    int length = base_2.size();
    for (int i; i < length - 1; i++) {
        if (base_2[length - i - 1] == '1') {
            base_10 += pow(2, i);
        }
    }
    return base_10;
}

int main() {
    int decimal;
    string binary;
    cout <<  "Ingrese el numero para convertir a binario";
    cin >> decimal;
    binary = to_binary(decimal);
    cout << binary << endl;
    decimal = to_decimal(binary);
    cout << decimal << endl;
}