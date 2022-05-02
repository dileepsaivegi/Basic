import java.util.Scanner;
class A
	{
	A()
		{
			Scanner sc=new Scanner(System.in);
			System.out.println("Enter ID:");
			int id=sc.nextInt();
			System.out.println("Enter name:");
			String name=sc.next();
			System.out.println("Enter Age:");
			int age=sc.nextInt();
			System.out.println("Enter Salary:");
			int salary=sc.nextInt();
			System.out.println("Enter Desgination:");
			String Desgination=sc.next();

			System.out.println("ID is "+id);
			System.out.println("Name is "+name);
			System.out.println("Age is "+age);
			System.out.println("Salary is "+salary);
			System.out.println("Designation is "+Desgination);
		}
	}
class Demo2
{
	public static void main(String args[])
	{
		A a=new A();
	}

}