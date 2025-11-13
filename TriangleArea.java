import java.util.Scanner;

public class TriangleArea {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to Area Calculator\n ");
        System.out.print("Please enter your base in cms: ");
        double base = input.nextDouble();
        System.out.print("Now, Please enter your perpendicular height in cms: ");
        double height = input.nextDouble();

        double perpendicularArea = (base * height) / 2;
        double area = 0.5 * base * height;

        System.out.println("The area of the triangle is " + area + "cms2");
    }
}
