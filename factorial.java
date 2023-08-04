import java.util.*;

public class App {
	public static void main(String[] args) {
		int num = 5;
		System.out.println("Factorial of " + num + " is equal " + factorialOf(num));
	}

	public static int factorialOf(int number) {
		if (number == 0) return 1;
		if (number > 0) return number * factorialOf(number - 1);
	}
}
