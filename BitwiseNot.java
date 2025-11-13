import java.util.Scanner;

public class BitwiseNot {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Showcasing Bitwise NOT operator\n");
        System.out.print("Please Enter the first number: ");
        int first = input.nextInt();
        System.out.print("Now, Enter the other number: ");
        int second = input.nextInt();

        int result = first ^ second;
        System.out.println("The result is: " + result);

    }
}
