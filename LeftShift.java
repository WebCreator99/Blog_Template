import java.util.Scanner;

public class LeftShift {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Welcome to showcase of LeftShift operator\n");
        System.out.print("please enter your number:");
        int num = input.nextInt();

        int result = num << 1;
        System.out.print("your result is: " + result);


    }
}
