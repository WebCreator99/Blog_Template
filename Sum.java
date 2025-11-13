import java.util.Scanner;

public class Sum {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print(" Welcome to Java World ");
        System.out.print( " Please enter  first number: ");
        int firstNum = input.nextInt();
        System.out.print(" Now, Please enter  second number: ");
        int secondNum = input.nextInt();
        int sum = firstNum + secondNum;
        System.out.println("Your number is: " + sum);
    }
}
