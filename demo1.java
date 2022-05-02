class A
{
      		A()
		{
			System.out.println("A class");
		}
}
class B
{
		B()
		{
			System.out.println("B class");
		}
}
class Demo1
{
	public static void main(String args[])
	  { 
		System.out.println(" Say Hello to Java");
		A a= new A();
		B b= new B();
	}		
}