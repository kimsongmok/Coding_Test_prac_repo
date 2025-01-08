import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
  static class Jewels{
    int weight, value;
    Jewels(int weight, int value){
      this.weight = weight;
      this.value = value;
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(bf.readLine());


    int N = Integer.parseInt(st.nextToken());
    int K = Integer.parseInt(st.nextToken());

    Jewels[] jewels = new Jewels[N];
    int[] bags = new int[K];

    for(int i=0; i<N; i++){
      st = new StringTokenizer(bf.readLine());
      int weight = Integer.parseInt(st.nextToken());
      int value = Integer.parseInt(st.nextToken());
      jewels[i] = new Jewels(weight, value);
    }

    for(int j=0; j < K; j++){
      bags[j] = Integer.parseInt(bf.readLine());
    }

    Arrays.sort(jewels, (a, b) -> a.weight - b.weight);
    Arrays.sort(bags);

    PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

    long maxValue = 0;
    int jewelIndex = 0;

    for (int bag : bags) {
      while (jewelIndex < N && jewels[jewelIndex].weight <= bag) {
        pq.add(jewels[jewelIndex].value);
        jewelIndex++;
      }
      if (!pq.isEmpty()) {
        maxValue += pq.poll();
      }
    }
    System.out.println(maxValue);
  }
}
