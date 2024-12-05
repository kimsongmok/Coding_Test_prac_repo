import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    int k = Integer.parseInt(bf.readLine());

    int limit = 7000000;
    boolean[] isPrime = new boolean[limit + 1];
    List<Integer> primes = new ArrayList<>();

    for (int i = 2; i <= limit; i++) {
      isPrime[i] = true;
    }

    for (int i = 2; i * i <= limit; i++) {
      if (isPrime[i]) {
        for (int j = i * i; j <= limit; j += i) {
          isPrime[j] = false;
        }
      }
    }

    for (int i = 2; i <= limit; i++) {
      if (isPrime[i]) {
        primes.add(i);
      }
    }

    System.out.println(primes.get(k-1));
  }
}
