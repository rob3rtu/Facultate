package PAO.Lab4.colections;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);

        System.out.println("My list: " + list);

        Set<Integer> set = new HashSet<>();
        // Set<Integer> set2 = new TreeSet<>();

        set.add(1);
        set.add(1);

        System.out.println(set);
    }
}
