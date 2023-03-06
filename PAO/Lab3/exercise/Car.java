package PAO.Lab3.exercise;

public class Car {
    private String name;
    private String color;
    private String[] reviews = new String[0];

    public Car(String _name, String _color) {
        // super();
        name = _name;
        color = _color;   
    }

    public String getName() {
        return name;
    }

    public String getColor() {
        return color;
    }

    public void setName(String _name) {
        name = _name;
    }
}
