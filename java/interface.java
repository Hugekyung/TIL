// 자바 Interface
// 인터페이스는 상속받을 클래스에서 구체적으로 구현할 메소드에 대한 정의를 한다. 즉, 메소드의 이름과 입출력에 대한 정의만 있고 그 내용 부분은 없다. 인터페이스를 쓰는 이유는

// 1. 동일한 기능, 동일한 코드의 반복을 줄이고 구현할 메소드의 수에 대한 의존성을 줄여 효율성 향상
// 2. 자식클래스에서 필수적으로 구현해야할 기능들을 정하는 역할

// 변경 전
public class ZooKeeper {
    public void feed(Tiger tiger) {
        System.out.println("feed apple");
    }

    public void feed(Lion lion) {
        System.out.println("feed banana");
    }

		... // 새로운 동물이 추가될 때마다 feed 메소드를 새롭게 만들어야 한다.

		public void feed(Crocodile crocodile) {
		    System.out.println("feed strawberry");
		}
		
		public void feed(Leopard leopard) {
		    System.out.println("feed orange");
		}
		
		...
	
    public static void main(String[] args) {
        ZooKeeper zooKeeper = new ZooKeeper();
        Tiger tiger = new Tiger();
        Lion lion = new Lion();
        zooKeeper.feed(tiger);
        zooKeeper.feed(lion);
    }
}


// 변경 후(interface 추가)
public interface Predator {
    public String getFood(); // 메소드 이름과 입출력에 대한 정의만 있다.
}

// 아래와 같이 각각의 동물클래스는 Predator라는 interface를 implements받는다.
public class Tiger extends Animal implements Predator {
    public String getFood() {
        return "apple";
    }
}

public class Lion extends Animal implements Predator {
    public String getFood() {
        return "banana";
    }
}

// ZooKeeper클래스는 동물 수의 변경에 따라 feed메소드를 새롭게 구현해야하는 번거로움을
// 피할 수 있고, 어떤 동물인지 상관하지 않아도 된다(독립적인 클래스가 될 수 있다), 
// 이는 코드의 유지보수 효율성을 높여준다.
public class ZooKeeper {    
    public void feed(Predator predator) {
        System.out.println("feed "+predator.getFood());
    }
}