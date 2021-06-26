// StringBuffer: 문자열을 추가하거나 변경할 때 주로 사용하는 자료형이다.
// append 메소드를 통해 문자열을 추가한다.

// StringBuffer 사용한 코드
public class Test {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer();
        sb.append("hello");
        sb.append(" ");
        sb.append("jump to java");

        System.out.println(sb.toString()); // toString()메소드로 String 자료형으로 변환
    }
}

// String 사용한 코드
public class Test {
    public static void main(String[] args) {
        String temp = "";
        temp += "hello";
        temp += " ";
        temp += "jump to java";
        System.out.println(temp);
    }
}


// insert: 특정 위치에 문자 삽입
public class Test {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer();
        sb.append("jump to java");
        sb.insert(0, "hello ");
        System.out.println(sb.toString());
    }
}

// substring: 문자 추출
public class Test {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer();
        sb.append("Hello jump to java");
        System.out.println(sb.substring(0, 4));
    }
}