import java.util.*;

public class Main {
    static int n;
    static int result;
    public static void main(String[] args) throws NullPointerException {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i=0; i < n; i++) {
            pq.add(scanner.nextInt());
        }

        for (int i=0; i < n-1; i++) {
            int a = pq.poll();
            int b = pq.poll();
            int sum = a + b;
            result += sum;
            pq.add(sum);
        }
        System.out.println(result);
    }
}
