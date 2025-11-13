import java.util.Scanner;

public class ReverseTheDigits {
    public static void main(String[] args) {
            Scanner input = new Scanner(System.in);
            System.out.println("Welcome to Reverse the Digits");
            System.out.print(" please enter your Number: ");
            int num = input.nextInt();
            int reverse = reverse(num);
            System.out.println("Reverse of Your number  is " + reverse);
    }

    public static int reverse(int num) {
        int newNum = 0;
        while (num > 0) {
            int digit = num % 10;
            newNum = newNum * 10 + digit;
            num /= 10;
        }
        return newNum;
    }
}
