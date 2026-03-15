import math

def calcular_area():
    print("--- Calculadora de Áreas ---")
    print("1. Cuadrado")
    print("2. Triángulo")
    print("3. Círculo")
    
    opcion = input("\nSelecciona una opción (1-3): ")

    if opcion == "1":
        # Área del cuadrado: lado * lado
        lado = float(input("Ingresa la medida del lado: "))
        area = lado ** 2
        print(f"El área del cuadrado es: {area:.2f}")

    elif opcion == "2":
        # Área del triángulo: (base * altura) / 2
        base = float(input("Ingresa la base: "))
        altura = float(input("Ingresa la altura: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area:.2f}")

    elif opcion == "3":
        # Área del círculo: pi * radio^2
        radio = float(input("Ingresa el radio: "))
        area = math.pi * (radio ** 2)
        print(f"El área del círculo es: {area:.2f}")

    else:
        print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    calcular_area()