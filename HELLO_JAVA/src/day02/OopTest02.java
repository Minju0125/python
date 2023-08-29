package day02;

public class OopTest02 {
	public static void main(String[] args) {
		Human hum = new Human();
		System.out.println("flagLife:" + hum.flagLife);
		System.out.println("job:" + hum.job);
		hum.die();
		hum.chippo("프로그래머");
		System.out.println("flagLife:" + hum.flagLife);
		System.out.println("job:" + hum.job);
	}
}
