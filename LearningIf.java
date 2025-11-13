public class LearningIf {
    public static void main(String[] args) {
        boolean isMale = true;
        String name = "Bob\n";

        System.out.print("Before if\n ");
        if (isMale) {
            System.out.print("Mr." + name);
        } else {
            System.out.print("Mr." + name);
        }
        System.out.print("After if\n ");

        boolean isSeniorCitizen = true;
        boolean isAnAdult = true;

        if (isSeniorCitizen) {
            System.out.print("Hello Senior Citizen");
        } else if (isAnAdult) {
                System.out.print("Hello Anadult");
        } else {
                System.out.print("Hello Anadult");
        }
    }
}
