package day10;

public class RefTest {
	
	public static void changeVal(int a) {
		a = 3;
	}
	
	public static void changeRef(int[] arr) {
		arr[0] = 4;
	}
	
	public static void main(String[] args) {
		int a = 1;
		int[] b = {2}; 
		System.out.println("a: " + a);
		System.out.println("b: " + b[0]);
		changeVal(a);
		changeRef(b); //배열은 주소값
		System.out.println("a: " + a);
		System.out.println("b: " + b[0]);
	}
}
