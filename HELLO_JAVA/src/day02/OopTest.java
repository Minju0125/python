package day02;

public class OopTest {
	public static void main(String[] args) {
		Human hum = new Human();
		Animal ani = new Animal();
		System.out.println("flagLife:" + ani.flagLife);
		hum.die();
		System.out.println("flagLife:" + ani.flagLife);
	}
}
