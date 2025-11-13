public class Function {
    public static void main(String[] args) {
//        System.out.println("In main method");
//        greetUser();
//        System.out.println("method calling complete");
//        greetUser();
//        printFirstPattern();
//        printSecondPattern();
        printThirdPattern();

    }

    public static void greetUser() {
        System.out.println("Hello World");
    }

    public static void printThirdPattern() {
        System.out.println("        *");
        System.out.println("      * *");
        System.out.println("    * * *");
        System.out.println("  * * * *");
        System.out.println("* * * * *");
    }

    public static void printSecondPattern() {
        System.out.println("* * * * *");
        System.out.println("* * * *");
        System.out.println("* * *");
        System.out.println("* * ");
        System.out.println("* ");

    }

    public static void printFirstPattern() {
        System.out.println("*");
        System.out.println("* * ");
        System.out.println("* * *");
        System.out.println("* * * * * ");
        System.out.println("* * * * * * ");

//        int rows = 0;
//        while (rows < 5) {
//            System.out.print("*");
//            int i = 0;
//            while (i < rows) {
//                System.out.print(" * ");
//                i++;
//
//            }
//            System.out.println();
//            rows++;

//            int rows = 0;
//            while (rows < 5) {
//                System.out.print("*");
//                int i = 0;
//                while (i < rows) {
//                    System.out.print(" * ");
//                    i--;
//
//                }
//                System.out.println();
//                rows++;

                int row = 0;
                while (row < 5) {
                    System.out.print("*");
                    int l = 0;
                    while (l < row) {
                        System.out.print(" * ");
                        l++;

                    }
                    System.out.println();
                    row--;
                }

            }

        }

