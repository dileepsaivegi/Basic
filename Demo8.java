import java.util.Scanner;
class Demo8{
  public static void main(String args[]){
    System.out.println("Enter your choice ");
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    System.out.println("Enter the id");
    int id=sc.nextInt();
    System.out.println("Enter the Name");
    String Name=sc.nextLine();
    System.out.println("Enter the age");
    int Age= sc.nextInt();
    System.out.println("Id of the employee is: "+ id);
    System.out.println("Id of the employee is: "+ Name);
    System.out.println("Id of the employee is: "+ Age);
    switch(n){
      case 1: System.out.println("Designation is Clerk");
      System.out.println("Salary is 1500");
      break;

      case 2: System.out.println("Designation is Developer");
      System.out.println("Salary is 25000");
      break;

      case 3: System.out.println("Designation is Tester");
     System.out.println("Salary is 20000");
     break;

     case 4: System.out.println("Designation is Manager");
    System.out.println("Salary is 50000");
    break;

    default: System.out.println("Invalid number");
    }
  }
}
