package PAO.Lab3.exercise;

public class Service {
    private Car[] cars = new Car[0];
    private Service() {}

    private static class ServiceHolder {
        private static final Service INSTANCE = new Service();
    }

    public static Service getInstance() {
        return ServiceHolder.INSTANCE;
    }

    public void addCar(Car c) {
        Car [] newArr = new Car[cars.length + 1];

         System.arraycopy(cars, 0, newArr, 0, cars.length);

         newArr[newArr.length - 1] = c;
        cars = newArr;
    }

    public void listAllCars() {
        for(Car c : cars) {
            System.out.println(c.getName() + " " + c.getColor());
        }
    }
}
