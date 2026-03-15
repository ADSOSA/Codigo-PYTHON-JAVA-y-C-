import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        
        System.out.println("1. Cuadrado, 2. Triangulo, 3. Circulo");
        int opcion = teclado.nextInt();

        if (opcion == 1) {
            System.out.print("Lado: ");
            double lado = teclado.nextDouble();
            double area = lado * lado;
            System.out.println("El area es: " + area);
        }
        else if (opcion == 2) {
            System.out.print("Base: ");
            double base = teclado.nextDouble();
            System.out.print("Altura: ");
            double altura = teclado.nextDouble();
            double area = (base * altura) / 2;
            System.out.println("El area es: " + area);
        }
        else if (opcion == 3) {
            System.out.print("Radio: ");
            double radio = teclado.nextDouble();
            double area = 3.1416 * radio * radio;
            System.out.println("El area es: " + area);
        }
    }
}