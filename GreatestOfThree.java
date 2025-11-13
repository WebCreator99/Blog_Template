import java.util.Scanner;

public class GreatestOfThree {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Welcome to the World Of Three\n ");
        System.out.print("Please Enter Your first Number: ");
        int first = input.nextInt();
        System.out.print("Please Enter Your second Number: ");
        int second = input.nextInt();
        System.out.print("Please Enter Your third Number: ");
        int third = input.nextInt();

        if(first >= second && first >= third){
            System.out.println(first + " is the greater number");
        }else if (second >= first && second >= third){
            System.out.println(second + " is the greater number");
        }else {
            System.out.println(first + " is the less number");
        }
    }
}
