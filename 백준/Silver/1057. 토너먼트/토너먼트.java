import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(bf.readLine());

    int n = Integer.parseInt(st.nextToken());
    int k = Integer.parseInt(st.nextToken());
    int l = Integer.parseInt(st.nextToken());
    int cnt = 0;

    while (k!=l){
      k = (k+1)/2;
      l = (l+1)/2;

      cnt ++;
    }
    System.out.println(cnt);
  }
}
