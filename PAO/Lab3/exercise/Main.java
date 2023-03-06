package PAO.Lab3.exercise;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //class Car(name, color, String[] reviews)
        //orice masina noua adaugata are 0 reviews
        //0. Exit aplication
        //1. List all system cars
        //2. Add new car in the system
        //3.* Adaugam new review to a car
        //all of the above operation will be stored in a singleton service
        
        var service = Service.getInstance();

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a command: ");
        String comand = scanner.nextLine();

        while(!comand.equals("0")) {
            if(comand.equals("1")) {
                service.listAllCars();
            } else if(comand.equals("2")) {
                service.addCar(new Car("Tesla", "Rosu"));
            }

            System.out.print("Enter a command: ");
            comand = scanner.next();
        }

        scanner.close();
        
    }
}
