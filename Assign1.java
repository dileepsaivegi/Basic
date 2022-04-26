import java.util.Scanner;
class Clerk
{
 	static int Salary=15000;
 	static String designation="Clerk";
 	String id,Name;
 	int Age;
 	
	Clerk()
 		{
 			 Scanner sc=new Scanner(System.in);
 			 System.out.print("ID:");
 			 id=sc.next();
  			System.out.print("Name:");
  			Name=sc.next();
  			System.out.print("Age:");
 			 Age=sc.nextInt();
 		}	 
 void display()
 {
  System.out.println("ID: "+id+" ,Name: "+Name+"  Age: "+Age+" ,Salary: "+Salary+" ,Designation:"+designation);
 }
}
class Dev
{
 	static int salary=25000;
 	static String designation="Dev";
 	String ID,name;
	int age;
	Dev()
 	{
 		 Scanner sc=new Scanner(System.in);
 		 System.out.print("ID:");
 		 ID=sc.next();
 		 System.out.print("Name:");
 		 name=sc.next();
		 System.out.print("Age:");
		 age=sc.nextInt();
	 } 
 	void display()
 	{
 		 System.out.println("ID:"+ID+" ,Name:"+name+" ,Age:"+age+" ,Salary:"+salary+" ,Designation:"+designation);
 	}
}
class Tester
{
	 static int salary=20000;
	 static String designation="Tester";
	 String ID,name;
	 int age;
	 Tester()
	 {
		  Scanner sc=new Scanner(System.in);
		  System.out.print("ID:");
		  ID=sc.next();
		  System.out.print("Name:");
		  name=sc.next();
		  System.out.print("Age:");
		  age=sc.nextInt();
	 } 
 	void display()
 	{
  		System.out.println("ID:"+ID+" ,Name:"+name+" ,Age:"+age+" ,Salary:"+salary+" ,Designation:"+designation);
 	}
}
class Manager
{
	 static int salary=50000;
	 static String designation="Manager";
	 String ID,name;
	 int age;
	 Manager()
	 {
		  Scanner sc=new Scanner(System.in);
		  System.out.print("ID:");
		  ID=sc.next();
 		 System.out.print("Name:");
 		 name=sc.next();
 		 System.out.print("Age:");
 		 age=sc.nextInt();
 	} 
 	void display()
 	{
 		 System.out.println("ID:"+ID+" ,Name:"+name+" ,Age:"+age+" ,Salary:"+salary+" ,Designation:"+designation);
 	}
}

class Assign1
{
	 public static void main(String args[])
	 {
		  Scanner sc=new Scanner(System.in);
		  System.out.println("Enter the option");
	           int option=sc.nextInt();
 	 switch (option)
 	 {
 		  case 1:   Clerk c=new Clerk();
 			       c.display();
 				   break;
 		  case 2:   Dev d=new Dev();
    				d.display();
   				 break;
   		  case 3:   Tester t=new Tester();
    				t.display();
   				 break;
  		 case 4:  Manager m=new Manager();
   				 m.display();
   				 break;
   		default: System.out.println("Invalid option");
  	}
 }
}
