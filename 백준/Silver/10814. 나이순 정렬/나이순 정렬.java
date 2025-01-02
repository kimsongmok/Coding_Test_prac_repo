import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

class Member {
  int age;
  String name;
  int order;

  public Member(int age, String name, int order) {
    this.age = age;
    this.name = name;
    this.order = order;
  }
}


public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(bf.readLine());

    List<Member> members = new ArrayList<>();

    for(int i=0; i<n; i++){
      String[] input = bf.readLine().split(" ");
      int age = Integer.parseInt(input[0]);
      String name = input[1];
      members.add(new Member(age, name, i));
    }

    members.sort((m1, m2) -> {
      if (m1.age != m2.age) {
        return Integer.compare(m1.age, m2.age);
      } else {
        return Integer.compare(m1.order, m2.order);
      }
    });
    StringBuilder sb = new StringBuilder();
    for (Member member : members) {
      sb.append(member.age).append(" ").append(member.name).append("\n");
    }
    System.out.print(sb);

  }
}
