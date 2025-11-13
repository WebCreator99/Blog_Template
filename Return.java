import java.util.Scanner;

public class Return {
    public static void main(String[] args) {
//        Scanner input = new Scanner(System.in);
//        System.out.print("Welcome to calculator\n");
//        System.out.print("Please enter the number: ");
//        int first = input.nextInt();
//        System.out.print("Please enter the number: ");
//        int second = input.nextInt();
        greet();
        int first = readNumber();
        int second = readNumber();

        int sum = first + second;
        System.out.print("Sum of the number is: " + sum);
    }

    public static int readNumber() {
        Scanner input = new Scanner(System.in);
        System.out.print("Please enter the number: ");
        int number = input.nextInt();
        return number;
    }

    public static void greet() {
        System.out.println("Welcome to calculator\n");
    }
}
