package PAO.Lab3;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        //arrays au dim fixa
        int [] arr = new int[0];
        int [] arr2 = {3, 2, 7, 4};
        int [] arr3 = new int[]{1, 2, 3, 4};
        int [][] arr4 = {
            {1, 2, 3, 4},
            {2, 3},
            {5, 6, 7}
        };

        // for(int i = 0; i < arr2.length; i++) {
        //     System.out.println(arr2[i]);
        // }

        // for(int i : arr2) {
        //     System.out.println(i);
        // }

        // Arrays.stream(arr2)
        //         .forEach(e -> System.out.println(e));

        // System.out.println(Arrays.deepToString(arr4));

        // Arrays.sort(arr2);
        // System.out.println(Arrays.toString(arr2));

        arr = addElementToArray(arr, 8);
        arr = addElementToArray(arr, 6);
        arr = addElementToArray(arr, 3);
        
        arr = deleteFromArray(arr, 3);

        System.out.println(Arrays.toString(arr));


        var singletonService = Singleton.getInstance();
        System.out.println(singletonService.hashCode());
    }


    private static int[] deleteFromArray(int[] arr, int value) {
        return Arrays.stream(arr).filter(e -> e != value).toArray();
    }

    private static int[] addElementToArray(int[] arr, int value) {
        int [] newArr = new int[arr.length + 1];

        // System.arraycopy(arr, 0, newArr, 0, arr.length);
        for(int i = 0; i < arr.length; i++) {
            newArr[i] = arr[i];
        }

        newArr[newArr.length - 1] = value;
        return newArr;
    }
}