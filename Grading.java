import java.util.Scanner;

 class Grading {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Welcome to Grade Calculator\n");
        System.out.print("Please Enter Your Percentage: ");
        float percentage = input.nextFloat();

        if (percentage >= 90) {
            System.out.println("You have got A");
        } else if (percentage >= 75) {
            System.out.println("You have got B");
        } else if (percentage >=60) {
            System.out.println("You have got C, work hard next time");
        } else if (percentage>=30) {
            System.out.println("You have got D, You seriously work harder");
        }else{
            System.out.println("Sorry you have got failed test and got the F");
        }


    }
}
