class Emp:

 '''def __init__(self,uid,name,age,salary,design):
        self.uid=uid;
        self.name=name;
        self.age= age;
        self.salary = salary;
        self.design=design; '''
    def __init__(self):

        self.uid=input("Enter id: ");
        self.name=input("Enter name: ");
        self.age=input("Enter age: ");
        self.salary =input("Enter salary: ");
        self.design=input("Enter design: ");
        




    def display(self):
        print("Name : ",self.name);
        print("Id : ",self.uid);
        print("age : ",self.age);
        print("salary: ",self.salary);
        print("Design: ",self.design);

#e=Emp(108,'Dileep',21,40000,'Clerk');
e=Emp();
e.display();
