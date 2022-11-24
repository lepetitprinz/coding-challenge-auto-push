import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] arr = new int[5];
        for (int i=0; i < arr.length; i++) {
            arr[i] = scanner.nextInt();
        }
        Arrays.sort(arr);
        int arrAvg = Arrays.stream(arr).sum() / 5;
        int median = arr[2];

        System.out.println(arrAvg);
        System.out.println(median);
    }
}