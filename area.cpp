#include <iostream>
using namespace std;

int main() {
    int opcion;
    
    cout << "1. Cuadrado, 2. Triangulo, 3. Circulo" << endl;
    cin >> opcion;

    if (opcion == 1) {
        double lado;
        cout << "Lado: ";
        cin >> lado;
        cout << "El area es: " << lado * lado;
    }
    else if (opcion == 2) {
        double base, altura;
        cout << "Base: "; cin >> base;
        cout << "Altura: "; cin >> altura;
        cout << "El area es: " << (base * altura) / 2;
    }
    else if (opcion == 3) {
        double radio;
        cout << "Radio: "; cin >> radio;
        cout << "El area es: " << 3.1416 * radio * radio;
    }

    return 0;
}