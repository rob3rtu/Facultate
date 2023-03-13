package PAO.Lab4.equalsAndHashCodes;

import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Book b1 = new Book("b1");
        Book b2 = new Book("b1");

        // Doua obiecte egale au acelasi hashCode,
        // Dar doua obiecte cuacelasi hashcode nu sunt neaprat egale

        // System.out.println(b1.equals(b2));

        Set<Book> bookSet = new HashSet<>();

        bookSet.add(b1);
        bookSet.add(b2);

        System.out.println(bookSet);

    }

}
