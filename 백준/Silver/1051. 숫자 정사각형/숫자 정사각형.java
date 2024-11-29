import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(bf.readLine());
    
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    int max_size = 1;

    char[][] grid = new char[n][m];
    for(int i=0;i<n;i++){
      grid[i] = bf.readLine().toCharArray();
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        for (int size = 1; size < Math.min(n, m); size++){
          if (i + size < n && j + size < m) {
            if (grid[i][j] == grid[i][j + size] && grid[i][j] == grid[i + size][j] && grid[i][j] == grid[i + size][j + size]) {
              max_size = Math.max(max_size, (size + 1) * (size + 1));
            }
          }
        }
      }
    }
    System.out.println(max_size);


  }
}
