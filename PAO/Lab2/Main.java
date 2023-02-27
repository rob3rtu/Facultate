import java.util.Scanner;

//Compile and run
//javac Main.java
//java Main

public class Main {
    public static void main(String[] args) {
        // System.out.println("Salutare!!");

        // int intValue = 3;
        // System.out.println(intValue);

        // short shortValue = 5;
        // System.out.println(shortValue);

        // long longValue = 5;
        // System.out.println(longValue);

        // byte byteValue = 4;
        // System.out.println(byteValue);

        // float floatValue = 5.5f;
        // System.out.println(floatValue);

        // boolean booleanValue = false;
        // System.out.println(booleanValue);

        // char charValue = 'A';
        // System.out.println(charValue);

        // Integer integerValue = 5;
        // Short shortValue = 3;
        // Long lonValue = 3l;

        // primitiva -> wrapper == BOXING
        // wrapper -> primitiva == UNBOXING

        // char c = 'a';

        // while (c <= 'z') {
        // System.out.println(c);
        // c++;
        // }

        Scanner scanner = new Scanner(System.in);
        // System.out.println("Input: ");
        // int value = scanner.nextInt();
        // System.out.println("Ai scris: " + value);

        // scanner.close();

        System.out.print("Primu numar: ");
        int a = scanner.nextInt();

        System.out.print("Al doilea numar: ");
        int b = scanner.nextInt();

        System.out.print("Operatie: ");
        String op = scanner.next();

        switch (op) {
            case "+":
                System.out.println("Suma: " + (a + b));
                break;
            case "-":
                System.out.println("Diferenta: " + (a - b));
                break;
            case "*":
                System.out.println("Inmultire: " + (a * b));
                break;
            case "/":
                System.out.println("Impartire: " + (a / b));
                break;
            default:
                break;
        }
    }
}