import java.util.Scanner;

public class Relational {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Welcome to Driving License Portal ");
        System.out.print("Please Enter Your age: ");
        int age = input.nextInt();

        if(age>=18){
            System.out.print("You are eligible to drive");
        }else{
            System.out.print("You are not eligible to drive");
        }
    }
}
