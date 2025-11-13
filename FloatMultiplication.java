import java.util.Scanner;

public class FloatMultiplication {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("We are doing FloatMultiplication\n ");
        System.out.print("Please enter first decimal number: ");
        double first = input.nextDouble();
        System.out.print("Now, please enter second number: ");
        double second = input.nextDouble();


        System.out.print("\n Result is: " + first + second );
        System.out.print("\n Result is: " + (first + second ));


    }
}
