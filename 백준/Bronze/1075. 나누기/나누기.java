import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(bf.readLine());
    int F = Integer.parseInt(bf.readLine());
    int S = N;

    S /= 100;
    S *= 100;
    while((S % F) != 0){
      S++;
    }
    String ans = Integer.toString(S);
    System.out.println(ans.substring(ans.length()-2, ans.length()));
  }
}