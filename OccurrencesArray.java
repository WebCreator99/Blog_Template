import java.util.Scanner;

public class OccurrencesArray {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to Array Occurrences");
        int[] numArr = ArrayUtility.inputArray();
        System.out.print("Please enter the number you want to find: ");
        int num = input.nextInt();
        int occurrence = noOfOccurrences(numArr, num);
        System.out.println("Your element was found  " + occurrence + " times in the array");
    }

    public static int noOfOccurrences(int[] numArray, int num) {
        int occ = 0;
        int i = 0;
        while (i < numArray.length) {
            if (numArray[i] == num) {
                occ++;
            }
            i++;
        }
        return occ;

    }
}
