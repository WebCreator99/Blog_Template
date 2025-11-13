import java.util.Scanner;

public class SimpleInterest {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Welcome to simple interest Calculator\n ");
        System.out.print("Please enter your principal amount Rs ");
        int principal = input.nextInt();
        System.out.print("Now, Tell me your rate of interest ");
        float rate = input.nextFloat();
        System.out.print("Now, tell me for how many years are you borrowing this money: ");
        float years = input.nextFloat();

        float interest = (principal * rate * years) / 100;
        System.out.println("\n\n Your interest is Rs: " + interest);
    }
}
