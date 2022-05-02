class A
{
	private String name;
	private int id;
	void setName(String 2name)
	{
		this.name=name;
	}
	String getname()
	{
		return name;
	}
}
class OR
{
	public static void main(String[] args)
	{
		A a=new A();
		a.setName("Dileep");
		System.out.println(a.getName());
	}
}