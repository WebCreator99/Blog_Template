import java.util.Scanner;

public class PositiveNegativeZero {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Welcome to number checker\n");
        System.out.print("Please enter your number: ");
        int num = input.nextInt();

        if(num >0){
            System.out.print("Your number is positive ");
        }else if(num == 0){
            System.out.print("Your number is zero ");
        }else{
            System.out.print("Your number is negative ");
        }
    }
}
