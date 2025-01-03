import java.util.*;
import java.io.*;

public class Main {

  static Queue<Node> q = new LinkedList<>();

  static int dx[] = {0,0,-1,1};
  static int dy[] = {-1,1,0,0};
  static int map[][];
  static boolean visit[][];

  static int now_x, now_y;
  static int N,M,K;
  static int cnt;

  static class Node{
    int x;
    int y;

    public Node(int x, int y){
      this.x = x;
      this.y = y;
    }
  }
  static void BFS(int x, int y){
    q.offer(new Node(x,y));
    visit[y][x] = true;

    while (!q.isEmpty()){
      Node node = q.poll();

      for(int i=0; i<4; i++){
        now_x = node.x + dx[i];
        now_y = node.y + dy[i];

        if((now_x >= 0 && now_x < M && now_y >=0 && now_y < N) && !visit[now_y][now_x] && map[now_y][now_x]==1){
          q.offer(new Node(now_x, now_y));
          visit[now_y][now_x] = true;
        }
      }

    }
  }

  public static void main(String[] args) throws IOException{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    StringBuilder sb = new StringBuilder();

    int T = Integer.parseInt(bf.readLine());

    for(int i = 0; i < T; i++){
      st = new StringTokenizer(bf.readLine());

      M = Integer.parseInt(st.nextToken());
      N = Integer.parseInt(st.nextToken());
      K = Integer.parseInt(st.nextToken());

      map = new int[N][M];
      visit = new boolean[N][M];

      for(int j = 0; j < K; j++){
        st = new StringTokenizer(bf.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        map[y][x] = 1;
      }

      cnt = 0;
      for(int j = 0; j < N; j++){
        for(int k = 0; k < M; k++){
          if(visit[j][k]==false && map[j][k] == 1){
            cnt++;
            BFS(k,j);
          }
        }
      }
      sb.append(cnt).append('\n');
    }
    System.out.println(sb);
  }
}
