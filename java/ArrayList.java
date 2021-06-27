// java 자료형에는 ArrayList와 List라는 별개의 자료형이 존재한다.
// 둘의 가장 큰 차이점은 '크기를 유동적으로 조절할 수 있는가'이다.
// ArrayList는 10개로 정한 후 그 이상을 담을 수 없지만, List는 유동적인 조절이 가능하다.

import java.util.ArrayList;

ArrayList<Integer> integers1 = new ArrayList<Integer>(); // 타입 지정
ArrayList<Integer> integers2 = new ArrayList<>(); // 타입 생략 가능
ArrayList<Integer> integers3 = new ArrayList<>(10); // 초기 용량(Capacity) 설정
ArrayList<Integer> integers4 = new ArrayList<>(integers1); // 다른 Collection값으로 초기화
ArrayList<Integer> integers5 = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5)); // Arrays.asList()

// add() 메소드로 값 추가 가능
public class ArrayListTest {
    public static void main(String[] args) {
        ArrayList<String> colors = new ArrayList<>();
        // add() method
        colors.add("Black");
        colors.add("White");
        colors.add(0, "Green"); // 인덱스 지정도 가능
        colors.add("Red");

        // set() method
        colors.set(0, "Blue");

        System.out.println(colors);
    }
}