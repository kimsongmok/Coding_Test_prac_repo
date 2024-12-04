import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    String[] colors = {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};
    int[] multipliers = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000};

    String color1 = bf.readLine();
    String color2 = bf.readLine();
    String color3 = bf.readLine();
    int value1 = 0;
    int value2 = 0;
    long mul = 0;

    for (int i = 0; i < colors.length; i++) {
      if (colors[i].equals(color1)) {
        value1 = i;
      }
      if (colors[i].equals(color2)) {
        value2 = i;
      }
      if (colors[i].equals(color3)) {
        mul = multipliers[i];
      }
    }
    long res = (value1*10L+value2)*mul;

    System.out.println(res);

  }
}
