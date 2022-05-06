class Emp:
    def __init__(self):
        self.uid=input("Enter your ID : ")
        self.name=input("Enter your name : ")
        self.age=input("Enter your age : ")

    def display(self):
        print("\nEmployee Details")
        records=[str(self.uid),self.name,str(self.age),str(self.salary),self.desig]
        f=open("prj2insert.txt","a")
        for line in records:
            f.write(line)
            f.write("\t")
        f.write("\n")
        f=open("prj2insert.txt","r")
        print(f.read())
        f.close()

    def salaryrise(self):
        records=[str(self.uid),self.name,str(self.age),str(self.salary+200),self.desig]
        f=open("prj2salary.txt","a")
        for line in records:
            f.write(line)
            f.write("\t")
        f.write("\n")
        f.close()

class Clerk(Emp):
    salary=15000
    desig="CLERK"    

class Developer(Emp):
    salary=20000
    desig="DEVELOPER"

class Manager(Emp):
    salary=25000
    desig="MANAGER"

class Tester(Emp):
    salary=30000
    desig="TESTER"

while(True):
    print("\n1.Create\n2.Display\n3.Salary rise\n4.Exit\n")
    opt1=int(input("Enter Your choice : "))
    if(opt1==1):
            print("1)Clerk\n2)Developer\n3)Manager\n4)Tester\n5)Exit\n")
            opt2=int(input("Enter the Job Role : "))
            if(opt2==1):
                print("Clerk")
                c=Clerk()
                c.display()
                c.salaryrise()
            elif(opt2==2):
                print("Developer")
                d=Developer()
                d.display()
                d.salaryrise()
            elif(opt2==3):
                print("Manager")
                m=Manager()
                m.display()
                m.salaryrise()
            elif(opt2==4):
                print("Tester")
                t=Tester()
                t.display()
                t.salaryrise()
            else:
                break
            
    elif(opt1==2):
        f=open("prj2insert.txt","r")
        print(f.read())
        f.close()
        
    elif(opt1==3):
        f=open("prj2salary.txt","r")
        print(f.read())
        f.close()
        
    else:
        break
